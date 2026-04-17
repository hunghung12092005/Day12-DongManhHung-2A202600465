# Deployment Information

## Public URL

https://day12-dongmanhhung-2a202600465-production.up.railway.app/

## Platform

Railway

## Deploy Date

2026-04-17

## Service Overview

- App name: Production AI Agent
- Environment: production
- Region: `us-east4`
- Local production-style stack: `Nginx -> Agent -> Redis`

## Test Commands

### Health Check

```bash
curl https://day12-dongmanhhung-2a202600465-production.up.railway.app/health
```

Expected:

```json
{"status":"ok"}
```

### Readiness Check

```bash
curl https://day12-dongmanhhung-2a202600465-production.up.railway.app/ready
```

Expected:
- `200 OK` when the service is ready

### API Test Without Authentication

```bash
curl -X POST https://day12-dongmanhhung-2a202600465-production.up.railway.app/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"Hello"}'
```

Expected:
- `401 Unauthorized`

### API Test With Authentication

```bash
curl -X POST https://day12-dongmanhhung-2a202600465-production.up.railway.app/ask \
  -H "X-API-Key: 12092005a" \
  -H "Content-Type: application/json" \
  -d '{"question":"Hello"}'
```

Expected:
- `200 OK`

## Environment Variables Set

- `PORT=8000`
- `HOST=0.0.0.0`
- `ENVIRONMENT=production`
- `APP_NAME=Production AI Agent`
- `APP_VERSION=1.0.0`
- `DEBUG=false`
- `AGENT_API_KEY=12092005a`
- `JWT_SECRET=8f3c2a91d7b44e3aa9c1f5b6e7d8k2m4`
- `RATE_LIMIT_PER_MINUTE=10`
- `DAILY_BUDGET_USD=10.0`
- `ALLOWED_ORIGINS=*`
- `OPENAI_API_KEY=`
- `LLM_MODEL=gpt-4o-mini`

## Deployment Notes

- Issue 1: Railway healthcheck failed after build completed.
- Fix 1: corrected environment variable formatting and ensured the service used valid production variables.

- Issue 2: Railway startup command used `$PORT` literally, causing `Invalid value for '--port': '$PORT' is not a valid integer`.
- Fix 2: removed custom `startCommand` from `railway.toml` and let Railway use the Dockerfile `CMD`.

- Issue 3: local Docker build failed because `06-lab-complete` did not include `utils/mock_llm.py`.
- Fix 3: added local `utils/` inside `06-lab-complete` so Docker build context is self-contained.

- Issue 4: container runtime could not import `uvicorn`.
- Fix 4: corrected non-root user home setup in the Dockerfile and rebuilt cleanly.

- Issue 5: final local stack did not yet include a reverse proxy/load balancer layer.
- Fix 5: added an `nginx` service and `nginx.conf` to `06-lab-complete`, so local traffic now flows through Nginx before reaching the agent.

## Screenshots

- Dashboard: `screenshots/dashboard.png`
- Running service: `screenshots/running.png`
- Test result: `screenshots/test.png`

Note: add the actual screenshot files to the `screenshots/` directory before final submission.

## Final Verification

- [x] Public URL works
- [x] `/health` returns 200
- [x] `/ready` route exists
- [x] `/ask` without key returns 401
- [x] `/ask` with key returns 200
- [ ] Screenshots added
