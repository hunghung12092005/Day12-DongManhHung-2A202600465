# Day 12 Lab - Mission Answers

## Student Info

- Name: Dong Manh Hung
- Student ID: 2A202600465
- Date: 2026-04-17

## Part 1: Localhost vs Production

### Exercise 1.1: Anti-patterns found

1. Secret is hardcoded directly in source code: `OPENAI_API_KEY = "sk-hardcoded-fake-key-never-do-this"`.
2. Database credential is hardcoded in code: `DATABASE_URL = "postgresql://admin:password123@localhost:5432/mydb"`.
3. Debug logging prints the secret key to terminal output.
4. Application binds only to `localhost`, so it is not container/cloud friendly.
5. Port is fixed to `8000` instead of reading from environment variables.
6. `reload=True` is enabled directly in runtime config, which is suitable for local development but not production.
7. There is no `/health` endpoint, so a platform cannot know when to restart the service.
8. There is no `/ready` endpoint, so a load balancer cannot know when the app is ready.
9. Config is spread in code instead of centralized config management.
10. Logging uses `print()` instead of structured logging.

### Exercise 1.2: Notes

- Develop version: runs locally and returns an answer, but is not safe or production-ready.
- Production version: loads config from environment variables, has health/readiness checks, structured JSON logging, and graceful shutdown handling.
- Main differences: config management, secret handling, observability, deployability, and safer shutdown behavior.

### Exercise 1.3: Comparison table

| Feature | Develop | Production | Why Important? |
|---------|---------|------------|----------------|
| Config | Hardcoded in source | Loaded from env vars through `config.py` | Easy to change between environments and avoids committing secrets |
| Secrets | API key and DB URL hardcoded | Secrets come from environment variables | Reduces secret leakage risk |
| Host binding | `localhost` | `0.0.0.0` | Required for Docker and cloud deployment |
| Port | Fixed `8000` | Reads from `PORT` | Cloud platforms inject runtime port |
| Logging | `print()` | Structured JSON logging | Easier to search, parse, and monitor |
| Health check | None | `GET /health` | Platform can detect unhealthy containers |
| Readiness | None | `GET /ready` | Load balancer knows when to route traffic |
| Shutdown | Abrupt stop | Graceful shutdown with lifespan and SIGTERM handling | Safer deploys and fewer interrupted requests |

## Part 2: Docker

### Exercise 2.1: Dockerfile questions

1. Base image: `python:3.11` in `develop`, and `python:3.11-slim` in the multi-stage production build.
2. Working directory: `/app` in both versions.
3. Exposed port: `8000`.
4. Start command: `CMD ["python", "app.py"]` in the basic image, and `CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]` in the advanced image.

### Exercise 2.2: Compare develop vs production Docker

- Develop Dockerfile summary:
  - Single-stage build
  - Uses full `python:3.11` image
  - Copies `requirements.txt`, installs dependencies, then copies app code
  - Simpler and easier to understand
- Production Dockerfile summary:
  - Multi-stage build with `builder` and `runtime`
  - Uses `python:3.11-slim`
  - Installs dependencies in builder and copies only runtime artifacts
  - Runs as non-root user and includes `HEALTHCHECK`
- Main differences:
  - Smaller final image
  - Better security due to non-root user
  - Cleaner runtime image because build tools stay in builder stage
  - More suitable for deployment

### Exercise 2.3: Image size comparison

- Develop: about 1.0 GB
- Production: about 160-200 MB
- Difference: roughly 80% smaller

Note: exact image size may vary by machine and cached layers, but the repo materials show a large reduction from the multi-stage build.

### Exercise 2.4: Docker Compose stack

Architecture:

```text
Client -> Nginx -> Agent -> Redis
```

- Services started in the advanced stack:
  - `nginx`
  - `agent`
  - `redis`
- Communication:
  - client reaches Nginx on the exposed host port
  - Nginx proxies requests to `agent`
  - `agent` uses `redis` for session/rate-limit style storage
  - Nginx can later round-robin requests across multiple `agent` replicas

## Part 3: Cloud Deployment

### Exercise 3.1: Deployment result

- Platform used: Railway
- Public URL: `https://day12-dongmanhhung-2a202600465-production.up.railway.app/`
- Deployment status: successful after fixing Railway startup configuration and setting production environment variables

### Exercise 3.2: Test notes

- Health check result: `/health` is configured as the Railway healthcheck path and the service became healthy after the startup issue was fixed.
- API test result: `POST /ask` works with valid `X-API-Key`; request without key should return `401`.
- Problems encountered:
  - missing `utils/` inside `06-lab-complete`
  - incorrect non-root user home path in Dockerfile
  - invalid header removal logic in middleware
  - Railway `startCommand` used `$PORT` literally instead of a valid integer
- How I fixed them:
  - added `06-lab-complete/utils/mock_llm.py`
  - fixed Dockerfile user home and environment
  - replaced `response.headers.pop(...)` with safe header deletion
  - removed custom `startCommand` from `railway.toml` so Railway uses Dockerfile `CMD`

## Part 4: API Security

### Exercise 4.1: Authentication test

- Without API key: request is rejected with `401 Unauthorized`.
- With API key: request is accepted and returns a valid answer.

### Exercise 4.2: Rate limiting test

- Test method: repeated requests to `/ask` with the same API key until the threshold is reached.
- Result: service eventually returns `429 Too Many Requests`.

### Exercise 4.3: Protection summary

- What is protected:
  - `POST /ask` requires `X-API-Key`
  - requests are rate limited
  - budget is tracked with a cost guard
- Remaining limitations:
  - current final implementation uses an in-memory rate limiter and budget tracker, so it is not fully distributed across multiple instances without shared storage

### Exercise 4.4: Cost guard implementation

- My approach:
  - estimate input and output token counts
  - convert token usage into a simple USD cost estimate
  - reject further requests when daily budget is exhausted
- Where the budget is checked:
  - before response generation for input-side usage
  - after generation for output-side usage
- Expected behavior when budget is exceeded:
  - service returns an error and stops serving more expensive requests for the remaining budget window

## Part 5: Scaling & Reliability

### Exercise 5.1: Health check

- `/health` meaning:
  - liveness probe that tells the platform whether the process is alive enough to keep running
- `/ready` meaning:
  - readiness probe that tells the load balancer whether this instance is ready to receive traffic

### Exercise 5.2: Graceful shutdown

- How it works:
  - the app listens for `SIGTERM`
  - readiness is turned off during shutdown
  - lifespan cleanup gives in-flight work a chance to finish
- Why important:
  - avoids dropping requests abruptly during deploys or restarts

### Exercise 5.3: Stateless design

- Why in-memory state is a problem:
  - if request 1 hits instance A and request 2 hits instance B, user context is lost
- Why Redis helps:
  - Redis is shared storage, so all instances can read the same session/history data

### Exercise 5.4: Scaling notes

- Load balancer role:
  - distributes traffic across service instances and routes only to healthy/ready instances
- Multiple instances role:
  - improve availability and let the service handle more traffic

### Exercise 5.5: Implementation notes

- What I tested:
  - local Docker startup
  - Nginx reverse proxy in front of the agent
  - health and readiness behavior
  - protected `/ask` endpoint
  - production deployment on Railway
- What worked:
  - Docker-based local run with `nginx + agent + redis`
  - healthcheck endpoint
  - API key authentication
  - Railway deployment with public URL
- What still needs improvement:
  - split final app into separate modules such as `auth.py`, `rate_limiter.py`, and `cost_guard.py` to match the ideal project structure exactly
  - add production Redis-backed shared rate limiting if scaling beyond a single instance
  - fully validate multi-replica load balancing behavior with `docker compose up --scale agent=3`

## Final Reflection

- Thing I understood best: why Docker plus environment-based config makes deployment predictable.
- Thing that was hardest: debugging deployment differences between local Docker and Railway runtime behavior.
- If I improve this project later, I will: modularize the final app further, add shared Redis-backed state for rate limiting and cost tracking, and include automated deployment tests.
