# Deployment Information

> Dien file nay sau khi ban deploy xong.

## Public URL

TODO

## Platform

TODO

## Deploy Date

TODO

## Service Overview

- App name:
- Environment:
- Region:

## Test Commands

### Health Check

```bash
curl TODO/health
```

Expected:

```json
{"status":"ok"}
```

### Readiness Check

```bash
curl TODO/ready
```

### API Test Without Authentication

```bash
curl -X POST TODO/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"Hello"}'
```

Expected:
- `401 Unauthorized`

### API Test With Authentication

```bash
curl -X POST TODO/ask \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"question":"Hello"}'
```

Expected:
- `200 OK`

## Environment Variables Set

- `PORT`
- `ENVIRONMENT`
- `AGENT_API_KEY`
- `JWT_SECRET`
- `RATE_LIMIT_PER_MINUTE`
- `DAILY_BUDGET_USD`
- `REDIS_URL`
- `LOG_LEVEL`

## Deployment Notes

- Issue 1:
- Fix 1:
- Issue 2:
- Fix 2:

## Screenshots

- Dashboard: `screenshots/dashboard.png`
- Running service: `screenshots/running.png`
- Test result: `screenshots/test.png`

## Final Verification

- [ ] Public URL works
- [ ] `/health` returns 200
- [ ] `/ready` returns 200
- [ ] `/ask` without key returns 401
- [ ] `/ask` with key returns 200
- [ ] Screenshots added
