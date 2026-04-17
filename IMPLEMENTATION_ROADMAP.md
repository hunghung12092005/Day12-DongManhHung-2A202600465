# Day 12 - Implementation Roadmap

Tai lieu nay tom tat tung phan cua project theo kieu "lam gi, xem gi, xong thi duoc gi" de ban bat dau nhanh.

## Muc tieu cuoi cung

Ban can hoan thanh 3 nhom viec:

1. Hieu tung concept qua `01` den `05`
2. Hoan thien san pham cuoi o `06-lab-complete`
3. Nop bai day du voi:
   - `MISSION_ANSWERS.md`
   - `DEPLOYMENT.md`
   - `screenshots/`
   - repo GitHub co public URL hoac instructor access

## Thu tu nen lam

1. Chay nhanh `01` de thay su khac nhau giua dev va production
2. Chay `02` de dong goi bang Docker
3. Xem `03` de chon cach deploy
4. Chay `04` de them auth va bao ve API
5. Xem `05` de hieu health check, stateless, scale
6. Dung `06-lab-complete` lam ban final
7. Deploy that su va hoan thien tai lieu nop bai

## Part 1 - Localhost vs Production

Folder: `01-localhost-vs-production`

Muc tieu:
- Hieu vi sao code "chay tren may em" chua du de deploy
- Phan biet config dev va production

Can xem:
- `01-localhost-vs-production/README.md`
- `01-localhost-vs-production/develop/app.py`
- `01-localhost-vs-production/production/app.py`
- `01-localhost-vs-production/production/config.py`

Can lam:
- Chay ban `develop/`
- So sanh voi ban `production/`
- Ghi lai anti-patterns va diem khac nhau

Ban se rut ra:
- Khong hardcode secrets
- Dung environment variables
- Tach config khoi code

Output nen co:
- Cau tra loi cho Part 1 trong `MISSION_ANSWERS.md`

## Part 2 - Docker

Folder: `02-docker`

Muc tieu:
- Dong goi app thanh image
- Hieu su khac nhau giua Dockerfile co ban va production

Can xem:
- `02-docker/README.md`
- `02-docker/develop/Dockerfile`
- `02-docker/production/Dockerfile`
- `02-docker/production/docker-compose.yml`

Can lam:
- Build ban `develop/`
- Chay container
- So sanh Dockerfile `develop` va `production`
- Ghi lai image size, base image, workdir, startup command

Ban se rut ra:
- Docker giai quyet "works on my machine"
- Multi-stage giup image gon hon
- Compose giup ghep nhieu service

Output nen co:
- Cau tra loi cho Part 2 trong `MISSION_ANSWERS.md`

## Part 3 - Cloud Deployment

Folder: `03-cloud-deployment`

Muc tieu:
- Dua app len cloud va lay URL public

Can xem:
- `03-cloud-deployment/README.md`
- `03-cloud-deployment/railway/`
- `03-cloud-deployment/render/`
- `03-cloud-deployment/production-cloud-run/`

Can lam:
- Chon 1 nen tang: Railway, Render hoac Cloud Run
- Deploy app
- Test lai endpoint bang `curl`
- Chup man hinh dashboard va service dang chay

Ban se rut ra:
- App local can them config deploy moi len cloud duoc
- Public URL la mot deliverable bat buoc cua bai

Output nen co:
- URL that trong `DEPLOYMENT.md`
- Anh trong `screenshots/`
- Cau tra loi deployment trong `MISSION_ANSWERS.md`

## Part 4 - API Gateway

Folder: `04-api-gateway`

Muc tieu:
- Bao ve API khong cho ai cung goi duoc
- Han che lam dung va ton chi phi

Can xem:
- `04-api-gateway/README.md`
- `04-api-gateway/develop/app.py`
- `04-api-gateway/production/app.py`
- `04-api-gateway/production/auth.py`
- `04-api-gateway/production/rate_limiter.py`
- `04-api-gateway/production/cost_guard.py`

Can lam:
- Chay ban `develop`
- Test co key va khong co key
- Doc ban `production` de hieu auth + rate limit + cost guard

Ban se rut ra:
- API key la lop bao ve toi thieu
- Rate limit chan spam
- Cost guard tranh vuot ngan sach

Output nen co:
- Test result cho Part 4 trong `MISSION_ANSWERS.md`

## Part 5 - Scaling & Reliability

Folder: `05-scaling-reliability`

Muc tieu:
- Lam app san sang cho van hanh that
- Hieu health, ready, graceful shutdown, stateless design

Can xem:
- `05-scaling-reliability/develop/app.py`
- `05-scaling-reliability/production/app.py`
- `05-scaling-reliability/production/docker-compose.yml`
- `05-scaling-reliability/production/nginx.conf`
- `05-scaling-reliability/production/test_stateless.py`

Can lam:
- Doc va chay health check
- Xem readiness va graceful shutdown
- Xem vi du Redis + Nginx load balancing

Ban se rut ra:
- Scale ngang thi app nen stateless
- Health va readiness la bat buoc khi deploy
- Shutdown dung cach giup deploy an toan hon

Output nen co:
- Giai thich Part 5 trong `MISSION_ANSWERS.md`

## Part 6 - Final Project

Folder: `06-lab-complete`

Muc tieu:
- Day la ban final de nop
- Ghep tat ca nhung gi da hoc vao 1 project production-ready

Can xem:
- `06-lab-complete/README.md`
- `06-lab-complete/app/main.py`
- `06-lab-complete/app/config.py`
- `06-lab-complete/Dockerfile`
- `06-lab-complete/docker-compose.yml`
- `06-lab-complete/.env.example`
- `06-lab-complete/check_production_ready.py`

Can lam:
- Copy `.env.example` thanh `.env`
- Chay local bang Docker Compose
- Test `/health`, `/ready`, `/ask`
- Chay `python3 check_production_ready.py`
- Deploy len cloud

Trang thai hien tai:
- Production checker dang pass 100%
- Ban final co san de dung lam nen nop bai

Luu y:
- README co nhac `auth.py`, `rate_limiter.py`, `cost_guard.py`
- Hien tai logic do dang nam trong `app/main.py`
- Neu muon dep va dung checklist hon, ban co the tach module sau

## Nhung file nop bai can co

1. `MISSION_ANSWERS.md`
- Tra loi tung exercise cua Part 1 den Part 5

2. `DEPLOYMENT.md`
- Ghi public URL, platform, lenh test, env vars, screenshots

3. `screenshots/`
- Chua anh dashboard deploy
- Chua anh app dang chay
- Chua anh test API thanh cong

## Cach lam nhanh nhat de nop bai

1. Dung `06-lab-complete` lam ban final
2. Deploy len Railway hoac Render
3. Dien `MISSION_ANSWERS.md`
4. Dien `DEPLOYMENT.md`
5. Them screenshots
6. Push GitHub

## Goi y check truoc khi nop

- App local chay duoc
- Docker build duoc
- Public URL goi duoc
- `/health` tra `200`
- `/ask` khong co key thi `401`
- `/ask` co key thi `200`
- Repo khong commit `.env`
- Khong co hardcoded secrets
