# ✅ Checklist de Setup - Portfolio

Use este checklist para garantir que tudo está configurado corretamente.

## 📋 Antes de Começar

- [ ] Node.js 18+ instalado (`node --version`)
- [ ] Python 3.10+ instalado (`python3 --version`)
- [ ] Git instalado (`git --version`)
- [ ] Editor de código (VS Code recomendado)

---

## 🔧 Setup do Backend

### 1. Dependências Python
- [ ] Navegou para pasta `api/`: `cd api`
- [ ] Criou ambiente virtual: `python3 -m venv venv`
- [ ] Ativou ambiente virtual: `source venv/bin/activate`
- [ ] Instalou dependências: `pip install -r requirements.txt`

### 2. Variáveis de Ambiente
- [ ] Copiou `.env.example` para `.env`: `cp .env.example .env`
- [ ] Abriu arquivo `.env` para edição
- [ ] Configurou variáveis básicas (mínimo necessário):
  - [ ] `API_TITLE` (opcional - já tem valor padrão)
  - [ ] `DEBUG=true` (para desenvolvimento)
  - [ ] `SECRET_KEY` (gere um: `python -c "import secrets; print(secrets.token_urlsafe(32))"`)

### 3. Configurações Opcionais

#### Google Calendar (pode deixar em modo mock inicialmente)
- [ ] Criou projeto no Google Cloud Console
- [ ] Ativou Google Calendar API
- [ ] Criou Service Account
- [ ] Baixou credenciais JSON
- [ ] Salvou em `api/credentials/service-account.json`
- [ ] Configurou no `.env`:
  ```
  GOOGLE_CALENDAR_CREDENTIALS_FILE=credentials/service-account.json
  GOOGLE_CALENDAR_ID=seu-email@gmail.com
  ```

#### GitHub (opcional - funciona sem token)
- [ ] Gerou Personal Access Token no GitHub
- [ ] Configurou no `.env`:
  ```
  GITHUB_USERNAME=seu-usuario
  GITHUB_TOKEN=ghp_seu_token
  ```

#### Email (opcional - para formulário de contato)
- [ ] Configurou conta Gmail com senha de app
- [ ] Configurou no `.env`:
  ```
  SMTP_HOST=smtp.gmail.com
  SMTP_PORT=587
  SMTP_USERNAME=seu-email@gmail.com
  SMTP_PASSWORD=sua-senha-app
  EMAIL_FROM=seu-email@gmail.com
  EMAIL_TO=destino@exemplo.com
  ```

#### MongoDB (opcional - não necessário para início)
- [ ] MongoDB instalado e rodando
- [ ] Configurou no `.env`:
  ```
  MONGODB_URL=mongodb://localhost:27017
  MONGODB_DB_NAME=portfolio
  ```

### 4. Teste do Backend
- [ ] Iniciou servidor: `uvicorn app.main:app --reload`
- [ ] Backend rodando em: http://localhost:8000
- [ ] Acessou documentação: http://localhost:8000/docs
- [ ] Testou endpoint de saúde: http://localhost:8000/health

---

## 🎨 Setup do Frontend

### 1. Dependências Node
- [ ] Navegou para pasta `frontend/`: `cd frontend`
- [ ] Instalou dependências: `npm install`
- [ ] Aguardou instalação completa (pode demorar alguns minutos)

### 2. Configuração da API
- [ ] Abriu `src/app/services/api-config.service.ts`
- [ ] Verificou que `baseUrl` está correto: `http://localhost:8000`
- [ ] (Opcional) Alterou se a API estiver em outra porta

### 3. Teste do Frontend
- [ ] Iniciou servidor: `npm start` ou `ng serve`
- [ ] Frontend rodando em: http://localhost:4200
- [ ] Abriu no navegador: http://localhost:4200
- [ ] Página carregou corretamente
- [ ] Não há erros no console do navegador (F12)

---

## 🚀 Teste Completo da Integração

### Navegação
- [ ] Navbar visível no topo
- [ ] Menu responsivo funciona (teste redimensionar janela)
- [ ] Links de navegação funcionam (scroll suave)

### Hero Section
- [ ] Seção de apresentação carregou
- [ ] Animações funcionando
- [ ] Botões clicáveis

### Projects
- [ ] Seção de projetos carregou
- [ ] Se configurou GitHub, projetos aparecem
- [ ] Cards com hover effect funcionam

### Tools
- [ ] Cards de ferramentas visíveis
- [ ] Modal do Gallery Downloader abre
- [ ] Formulário de download aparece

### Schedule (Agendamento)
- [ ] Formulário de agendamento visível
- [ ] Selecionou uma data
- [ ] Horários disponíveis carregaram (ou mensagem de mock)
- [ ] Formulário pode ser preenchido
- [ ] Botão de enviar funciona

### Contact
- [ ] Formulário de contato visível
- [ ] Campos com validação (email obrigatório)
- [ ] Cards de contato (email, WhatsApp, etc) visíveis

### Footer
- [ ] Footer visível no fim da página
- [ ] Ano atual aparece corretamente

---

## 🐛 Troubleshooting

### Backend

#### ❌ Erro: `ModuleNotFoundError`
```bash
# Reinstalar dependências
pip install --force-reinstall -r requirements.txt
```

#### ❌ Erro: `Port already in use`
```bash
# Encontrar processo na porta 8000
lsof -i :8000

# Matar processo
kill -9 <PID>
```

#### ❌ Google Calendar não funciona
- ✅ É normal! Modo mock está ativo
- Para usar real, complete setup do Google Calendar acima

### Frontend

#### ❌ Erro: `npm ERR! code ENOENT`
```bash
# Reinstalar node_modules
rm -rf node_modules package-lock.json
npm install
```

#### ❌ Erro: `Port 4200 is already in use`
```bash
# Usar porta diferente
ng serve --port 4300
```

#### ❌ Erro CORS no navegador
- [ ] Verificar se backend está rodando em http://localhost:8000
- [ ] Verificar se frontend está rodando em http://localhost:4200
- [ ] Verificar CORS em `api/app/main.py`

#### ❌ API requests falham (404)
- [ ] Verificar se backend está rodando
- [ ] Verificar URL em `api-config.service.ts`
- [ ] Abrir DevTools (F12) e ver erros na aba Network

---

## ✅ Setup Completo!

Se todos os itens acima estão marcados, seu portfolio está pronto! 🎉

### Próximos Passos Sugeridos:

1. **Personalizar Conteúdo:**
   - [ ] Editar informações em `hero.component.html`
   - [ ] Atualizar links de contato em `contact.component.html`
   - [ ] Adicionar foto/avatar em `assets/`

2. **Customizar Aparência:**
   - [ ] Alterar cores em `styles.scss` (variáveis CSS)
   - [ ] Modificar estilos dos componentes

3. **Adicionar Dados:**
   - [ ] Adicionar projetos reais via API ou banco
   - [ ] Configurar Google Calendar real
   - [ ] Configurar email SMTP

4. **Deploy:**
   - [ ] Frontend: Vercel, Netlify, ou GitHub Pages
   - [ ] Backend: Railway, Heroku, ou AWS
   - [ ] Database: MongoDB Atlas (gratuito)

---

## 🆘 Precisa de Ajuda?

### Logs para Debug:

**Backend:**
```bash
# Ver logs detalhados
uvicorn app.main:app --reload --log-level debug
```

**Frontend:**
```bash
# Console do navegador (F12)
# Aba Console: erros JavaScript
# Aba Network: requisições HTTP
```

### Comandos Úteis:

```bash
# Ver processo rodando
ps aux | grep uvicorn
ps aux | grep node

# Verificar portas
lsof -i :8000
lsof -i :4200

# Limpar tudo e recomeçar
cd api && rm -rf venv
cd frontend && rm -rf node_modules
```

---

## 📚 Documentação Adicional

- `README.md` - Visão geral do projeto
- `INICIO_RAPIDO.md` - Guia detalhado passo a passo
- `COMANDOS.md` - Lista de comandos úteis
- `STATUS_PROJETO.md` - Status completo da implementação

---

**🎊 Parabéns por configurar seu portfolio!**

Agora é só personalizar e impressionar! 🚀
