# 🚀 Deploy para Google Cloud Run

## Pré-requisitos

1. **Google Cloud SDK instalado**
   ```bash
   gcloud --version
   ```

2. **Autenticar no GCP**
   ```bash
   gcloud auth login
   gcloud config set project SEU-PROJECT-ID
   ```

3. **Habilitar APIs necessárias**
   ```bash
   gcloud services enable cloudbuild.googleapis.com
   gcloud services enable run.googleapis.com
   gcloud services enable containerregistry.googleapis.com
   ```

## Deploy via Cloud Build

### Opção 1: Deploy Completo (Backend + Frontend)
```bash
gcloud builds submit --config cloudbuild.yaml
```

### Opção 2: Deploy apenas Backend
```bash
cd api
gcloud builds submit --tag gcr.io/SEU-PROJECT-ID/portfolio-api
gcloud run deploy portfolio-api \
  --image gcr.io/SEU-PROJECT-ID/portfolio-api \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated
```

### Opção 3: Deploy apenas Frontend
```bash
cd frontend
gcloud builds submit --tag gcr.io/SEU-PROJECT-ID/portfolio-frontend
gcloud run deploy portfolio-frontend \
  --image gcr.io/SEU-PROJECT-ID/portfolio-frontend \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated
```

## Configurar Variáveis de Ambiente

### Backend
```bash
gcloud run services update portfolio-api \
  --region us-central1 \
  --set-env-vars="NODE_ENV=production,SECRET_KEY=sua-chave-secreta" \
  --set-secrets="GOOGLE_SERVICE_ACCOUNT_FILE=google-credentials:latest"
```

### Criar Secrets
```bash
# Google Calendar credentials
gcloud secrets create google-credentials \
  --data-file=api/credentials/service-account.json

# GitHub token
echo "seu-github-token" | gcloud secrets create github-token --data-file=-

# Email SMTP
echo "seu-app-password" | gcloud secrets create smtp-password --data-file=-
```

## Atualizar CORS no Backend

Após deploy do frontend, pegue a URL e atualize o CORS:

```bash
FRONTEND_URL=$(gcloud run services describe portfolio-frontend --region us-central1 --format 'value(status.url)')

gcloud run services update portfolio-api \
  --region us-central1 \
  --update-env-vars="CORS_ORIGINS=[\"${FRONTEND_URL}\",\"http://localhost:4200\"]"
```

## Conectar Frontend ao Backend

Atualizar `frontend/src/environments/environment.prod.ts`:
```typescript
export const environment = {
  production: true,
  apiUrl: 'https://portfolio-api-xxx.run.app'
};
```

Rebuild e redeploy:
```bash
cd frontend
gcloud builds submit --tag gcr.io/SEU-PROJECT-ID/portfolio-frontend
```

## Verificar Logs

```bash
# Backend logs
gcloud run services logs read portfolio-api --region us-central1

# Frontend logs
gcloud run services logs read portfolio-frontend --region us-central1
```

## Custom Domain (Opcional)

```bash
gcloud run domain-mappings create \
  --service portfolio-frontend \
  --domain seu-dominio.com \
  --region us-central1
```

## Custos Estimados

Cloud Run cobra por:
- Requests: $0.40 por milhão
- CPU: $0.00002400 por vCPU-segundo
- Memória: $0.00000250 por GiB-segundo

**Free tier**: 2 milhões de requests/mês grátis! 🎉

## Troubleshooting

### Container não inicia
```bash
# Testar localmente
docker build -t portfolio-api ./api
docker run -p 8080:8080 portfolio-api
```

### Erro de permissões
```bash
# Dar permissão ao Cloud Build
gcloud projects add-iam-policy-binding SEU-PROJECT-ID \
  --member=serviceAccount:PROJECT_NUMBER@cloudbuild.gserviceaccount.com \
  --role=roles/run.admin
```
