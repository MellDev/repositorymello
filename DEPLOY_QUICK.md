# 🚀 Deploy Rápido - Google Cloud Run

## ✅ Arquivos Criados

### Backend (api/)
- ✅ `Dockerfile` - Container otimizado multi-stage
- ✅ `.dockerignore` - Ignora arquivos desnecessários
- ✅ Health check endpoint `/health`

### Frontend (frontend/)
- ✅ `Dockerfile` - Build Angular + Nginx
- ✅ `nginx.conf` - Configuração otimizada
- ✅ `.dockerignore` - Ignora node_modules
- ✅ `environments/` - Configuração dev/prod

### Deploy
- ✅ `cloudbuild.yaml` - Build automático pelo Cloud Build
- ✅ `deploy.sh` - Script simplificado de deploy
- ✅ `DEPLOY.md` - Documentação completa

---

## 🎯 Como Fazer Deploy

### Opção 1: Script Automático (Recomendado)
```bash
# Configurar projeto
gcloud config set project SEU-PROJECT-ID

# Deploy completo
./deploy.sh all

# Ou separado
./deploy.sh backend
./deploy.sh frontend
```

### Opção 2: Cloud Build Manual
```bash
# Deploy via Cloud Build
gcloud builds submit --config cloudbuild.yaml

# Após deploy, pegar as URLs
gcloud run services list --platform managed
```

### Opção 3: Docker Manual
```bash
# Backend
cd api
gcloud builds submit --tag gcr.io/SEU-PROJECT-ID/portfolio-api
gcloud run deploy portfolio-api --image gcr.io/SEU-PROJECT-ID/portfolio-api

# Frontend
cd frontend
gcloud builds submit --tag gcr.io/SEU-PROJECT-ID/portfolio-frontend
gcloud run deploy portfolio-frontend --image gcr.io/SEU-PROJECT-ID/portfolio-frontend
```

---

## ⚙️ Antes do Deploy

### 1. Instalar gcloud CLI
```bash
# macOS
brew install google-cloud-sdk

# Ou baixe de: https://cloud.google.com/sdk/docs/install
```

### 2. Autenticar
```bash
gcloud auth login
gcloud config set project SEU-PROJECT-ID
```

### 3. Habilitar APIs
```bash
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com
```

### 4. Atualizar Frontend com URL do Backend
Após deploy do backend, atualizar em:
- `frontend/src/environments/environment.prod.ts`
```typescript
apiUrl: 'https://sua-url-backend.run.app'
```

---

## 🔐 Configurar Secrets (Opcional)

### Google Calendar
```bash
gcloud secrets create google-credentials \
  --data-file=api/credentials/service-account.json

gcloud run services update portfolio-api \
  --set-secrets="GOOGLE_SERVICE_ACCOUNT_FILE=google-credentials:latest"
```

### GitHub Token
```bash
echo "seu-token" | gcloud secrets create github-token --data-file=-

gcloud run services update portfolio-api \
  --update-env-vars="GITHUB_TOKEN=projects/SEU-PROJECT-ID/secrets/github-token"
```

### Email SMTP
```bash
echo "senha-app-gmail" | gcloud secrets create smtp-password --data-file=-

gcloud run services update portfolio-api \
  --update-env-vars="SMTP_PASSWORD=projects/SEU-PROJECT-ID/secrets/smtp-password"
```

---

## 📊 Verificar Deploy

```bash
# Listar serviços
gcloud run services list

# Ver logs do backend
gcloud run services logs read portfolio-api --tail=100

# Ver logs do frontend
gcloud run services logs read portfolio-frontend --tail=100

# Testar endpoints
curl https://sua-url-backend.run.app/health
curl https://sua-url-frontend.run.app/health
```

---

## 💰 Custos

**Cloud Run Free Tier:**
- 2 milhões de requests/mês GRÁTIS
- 360.000 vCPU-segundos/mês GRÁTIS
- 180.000 GiB-segundos/mês GRÁTIS

Seu portfólio provavelmente ficará **100% gratuito** 🎉

---

## 🔧 Troubleshooting

### Erro: "Container failed to start"
```bash
# Testar localmente
docker build -t test-api ./api
docker run -p 8080:8080 test-api
```

### Erro: "Permission denied"
```bash
# Dar permissões ao Cloud Build
PROJECT_NUMBER=$(gcloud projects describe SEU-PROJECT-ID --format="value(projectNumber)")
gcloud projects add-iam-policy-binding SEU-PROJECT-ID \
  --member=serviceAccount:${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com \
  --role=roles/run.admin
```

### Frontend não conecta ao Backend
1. Verificar `environment.prod.ts` tem URL correta
2. Atualizar CORS no backend:
```bash
FRONTEND_URL="https://sua-url-frontend.run.app"
gcloud run services update portfolio-api \
  --update-env-vars="CORS_ORIGINS=[\"$FRONTEND_URL\"]"
```

---

## 📚 Próximos Passos

1. ✅ Deploy básico funcionando
2. ⬜ Configurar domínio customizado
3. ⬜ Configurar secrets (Calendar, GitHub, Email)
4. ⬜ Configurar CI/CD automático via GitHub Actions
5. ⬜ Adicionar monitoramento com Cloud Monitoring

Para mais detalhes, veja `DEPLOY.md`
