# 🚀 Guia Rápido de Início

Este guia mostra como rodar o projeto portfolio completo (API + Frontend).

## ⚡ Início Rápido

### 1. Backend (API FastAPI)

```bash
# 1. Entrar na pasta da API
cd api

# 2. Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Iniciar servidor
uvicorn app.main:app --reload
```

✅ **API rodando em:** http://localhost:8000  
📚 **Documentação:** http://localhost:8000/docs

### 2. Frontend (Angular)

Em outro terminal:

```bash
# 1. Entrar na pasta frontend
cd frontend

# 2. Instalar dependências
npm install

# 3. Iniciar servidor de desenvolvimento
npm start
# ou
ng serve
```

✅ **Frontend rodando em:** http://localhost:4200

## 🎯 Testando as Funcionalidades

### 1. Google Calendar (Sistema de Agendamento)
- Acesse http://localhost:4200
- Role até a seção "Agende uma Reunião"
- Selecione uma data
- Escolha um horário disponível
- Preencha o formulário e envie

**Nota:** Por padrão, roda em **modo mock** (dados simulados). Para usar o Google Calendar real, veja [Configuração do Google Calendar](#configuração-do-google-calendar).

### 2. Gallery Downloader (Scraping)
- Na seção "Ferramentas Interativas"
- Clique em "Experimentar" no card "Gallery Downloader"
- Insira uma URL de mídia
- Clique em "Iniciar Download"
- Acompanhe o status

### 3. Projetos do GitHub
- Role até a seção "Projetos"
- Veja seus repositórios listados automaticamente
- Clique nos links para visitar o GitHub

### 4. Formulário de Contato
- Role até "Entre em Contato"
- Preencha o formulário
- Clique em "Enviar Mensagem"

## ⚙️ Configuração do Google Calendar

Para usar o Google Calendar real (não mock):

1. **Criar projeto no Google Cloud:**
   - Acesse: https://console.cloud.google.com/
   - Crie um novo projeto

2. **Ativar API:**
   - No menu, vá em "APIs e Serviços" → "Biblioteca"
   - Procure "Google Calendar API"
   - Clique em "Ativar"

3. **Criar Service Account:**
   - Vá em "APIs e Serviços" → "Credenciais"
   - Clique em "Criar credenciais" → "Conta de serviço"
   - Preencha o nome e clique em "Criar"
   - Pule as permissões opcionais
   - Clique em "Concluir"

4. **Baixar credenciais:**
   - Na lista de contas de serviço, clique na que você criou
   - Vá na aba "Chaves"
   - Clique em "Adicionar chave" → "Criar nova chave"
   - Escolha "JSON"
   - Salve o arquivo baixado

5. **Configurar no projeto:**
   ```bash
   # Mover o arquivo JSON para a pasta credentials
   mv ~/Downloads/seu-arquivo.json api/credentials/service-account.json
   ```

6. **Editar o .env:**
   ```env
   GOOGLE_CALENDAR_CREDENTIALS_FILE=credentials/service-account.json
   GOOGLE_CALENDAR_ID=seu-email@gmail.com
   GOOGLE_CALENDAR_TIMEZONE=America/Sao_Paulo
   ```

7. **Compartilhar calendário:**
   - Abra Google Calendar
   - Nas configurações do calendário, compartilhe com o email da service account
   - Dê permissão de "Fazer alterações em eventos"

8. **Reiniciar API:**
   ```bash
   # Ctrl+C para parar
   uvicorn app.main:app --reload
   ```

## 📧 Configuração de Email (Opcional)

Para o formulário de contato enviar emails reais:

1. **Gerar senha de app do Gmail:**
   - Acesse: https://myaccount.google.com/security
   - Ative "Verificação em duas etapas"
   - Vá em "Senhas de app"
   - Gere uma senha para "Mail"

2. **Editar .env:**
   ```env
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USERNAME=seu-email@gmail.com
   SMTP_PASSWORD=sua-senha-de-app
   EMAIL_FROM=seu-email@gmail.com
   EMAIL_TO=destino@exemplo.com
   ```

## 🐛 Problemas Comuns

### Backend não inicia

```bash
# Verificar se o Python está instalado
python3 --version

# Recriar ambiente virtual
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Frontend não inicia

```bash
# Limpar cache e reinstalar
rm -rf node_modules package-lock.json
npm install

# Se persistir, instalar Angular CLI globalmente
npm install -g @angular/cli
ng serve
```

### CORS Error no navegador

- Verifique se a API está rodando em http://localhost:8000
- Verifique se o frontend está rodando em http://localhost:4200
- O CORS já está configurado para essas portas

### Gallery-dl não funciona

```bash
# Instalar gallery-dl
pip install gallery-dl

# Verificar se está no PATH
which gallery-dl
```

## 📚 Próximos Passos

- [ ] Customizar estilos em `frontend/src/styles.scss`
- [ ] Adicionar seus projetos no banco de dados
- [ ] Configurar Google Calendar real
- [ ] Configurar email real
- [ ] Adicionar seu GitHub token para mais requisições
- [ ] Deploy em produção (Vercel + Railway/Heroku)

## 🎨 Customização

### Cores e Tema
Edite `frontend/src/styles.scss` e altere as variáveis CSS:
```scss
:root {
  --primary-color: #6366f1;      // Sua cor primária
  --secondary-color: #8b5cf6;    // Sua cor secundária
  // ...
}
```

### Informações Pessoais
- Edite `frontend/src/app/components/hero/hero.component.html`
- Altere nome, descrição, links
- Atualize imagens em `frontend/src/assets/`

### Dados do Footer
- Edite `frontend/src/app/components/contact/contact.component.html`
- Atualize email, telefone, redes sociais

## 💡 Dicas

1. **Desenvolvimento:** Use `--reload` no uvicorn para auto-reload
2. **Debug:** Verifique o console do navegador (F12)
3. **API:** Use http://localhost:8000/docs para testar endpoints
4. **Git:** Lembre-se de adicionar `.env` ao `.gitignore`

## 🆘 Ajuda

Se encontrar problemas:
1. Verifique os logs do terminal (backend e frontend)
2. Teste os endpoints na documentação Swagger
3. Verifique se todas as dependências foram instaladas
4. Confirme que as portas 8000 e 4200 estão livres

---

✨ **Pronto para impressionar!** Seu portfolio está configurado e rodando.
