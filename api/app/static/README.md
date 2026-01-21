# Instruções para adicionar o currículo

Coloque seu arquivo de currículo (PDF) nesta pasta com o nome:

**Anderson_Mello_Resume.pdf**

Este arquivo será servido através dos endpoints:
- `/api/resume/download` - Para download direto
- `/api/resume/view` - Para visualizar no navegador

## Como adicionar no deployment (Cloud Run)

1. **Opção 1: Build no Docker**
   Adicione no Dockerfile:
   ```dockerfile
   COPY app/static/Anderson_Mello_Resume.pdf /app/app/static/
   ```

2. **Opção 2: Cloud Storage**
   - Upload no Google Cloud Storage
   - Modifique o endpoint para buscar do bucket
   - Mais flexível para atualizações

3. **Opção 3: Environment Variable com URL**
   - Hospede o PDF no Google Drive/Dropbox
   - Configure RESUME_URL no .env
   - O endpoint redireciona para o link
