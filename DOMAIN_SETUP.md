# Configuração de Domínio Personalizado

## Domínio: projetosmello.com.br

### 1. Mapear domínio no Cloud Run

```bash
# Frontend (www ou raiz)
gcloud run domain-mappings create \
  --service portfolio-frontend \
  --domain projetosmello.com.br \
  --region us-central1

# Ou com www
gcloud run domain-mappings create \
  --service portfolio-frontend \
  --domain www.projetosmello.com.br \
  --region us-central1

# API (subdomínio)
gcloud run domain-mappings create \
  --service portfolio-api \
  --domain api.projetosmello.com.br \
  --region us-central1
```

### 2. Configurar DNS (no seu provedor de domínio)

Após executar os comandos acima, o Cloud Run fornecerá registros DNS. Adicione no seu provedor:

**Para o domínio principal (frontend):**
```
Tipo: A
Nome: @ (ou projetosmello.com.br)
Valor: [IP fornecido pelo Cloud Run]

Tipo: AAAA
Nome: @ (ou projetosmello.com.br)
Valor: [IPv6 fornecido pelo Cloud Run]
```

**Para o www:**
```
Tipo: CNAME
Nome: www
Valor: ghs.googlehosted.com
```

**Para a API:**
```
Tipo: CNAME
Nome: api
Valor: ghs.googlehosted.com
```

### 3. Atualizar CORS no Backend

```bash
gcloud run services update portfolio-api \
  --region us-central1 \
  --update-env-vars "CORS_ORIGINS=[\"https://projetosmello.com.br\",\"https://www.projetosmello.com.br\",\"http://localhost:4200\"]"
```

### 4. Atualizar API URL no Frontend

Edite `frontend/src/environments/environment.prod.ts`:
```typescript
export const environment = {
  production: true,
  apiUrl: 'https://api.projetosmello.com.br'
};
```

Depois faça rebuild e redeploy do frontend.

### 5. Verificar configuração SSL

O Cloud Run automaticamente provisiona certificados SSL (HTTPS). Aguarde alguns minutos após configurar o DNS.

### 6. Verificar status

```bash
# Listar mapeamentos
gcloud run domain-mappings list --region us-central1

# Ver detalhes
gcloud run domain-mappings describe projetosmello.com.br \
  --region us-central1
```

## Troubleshooting

### DNS não propagou
- Pode levar até 48h, mas geralmente é rápido (5-30 min)
- Verifique com: `dig projetosmello.com.br` ou `nslookup projetosmello.com.br`

### Certificado SSL pendente
- Aguarde propagação DNS completa
- Pode levar até 24h após DNS estar correto

### CORS errors
- Certifique-se que o backend tem o domínio correto no CORS_ORIGINS
- Inclua https:// e não http://

## URLs Finais

- **Frontend**: https://projetosmello.com.br
- **API**: https://api.projetosmello.com.br
- **Docs da API**: https://api.projetosmello.com.br/docs
