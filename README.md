# Portfolio Website - Gabriel Orellana

Portfólio interativo e funcional com diversas ferramentas úteis, incluindo integração com Google Calendar, scraping de mídia, integração com GitHub e muito mais.

## 🎯 Funcionalidades

### Frontend
- ✅ Site responsivo e moderno
- ✅ Sistema de agendamento integrado
- ✅ Demonstração de ferramentas interativas
- ✅ Galeria de projetos
- ✅ Formulário de contato

### Backend API
- ✅ **Google Calendar**: Agendamento com service account
- ✅ **GitHub**: Integração completa com seus repositórios
- ✅ **Scraping**: Download de mídia com gallery-dl
- ✅ **Email**: Sistema de notificações
- ✅ **Swagger**: Documentação automática da API

## 📁 Estrutura do Projeto

```
repositorymello/
├── backend/              # API Node.js + Express
│   ├── src/
│   │   ├── controllers/  # Lógica de negócio
│   │   ├── routes/       # Definição de rotas
│   │   ├── config/       # Configurações
│   │   ├── middleware/   # Middlewares
│   │   └── utils/        # Utilitários
│   ├── logs/            # Logs da aplicação
│   ├── package.json
│   └── .env
├── js/                  # JavaScript do frontend
├── styles/              # CSS
└── index.html           # Página principal
```

## 🚀 Como Usar

### Backend

1. **Instale as dependências:**
```bash
cd backend
npm install
```

2. **Configure o arquivo `.env`:**
   - MongoDB URI
   - Credenciais do Google Calendar
   - GitHub token (opcional, mas recomendado)
   - Credenciais de email

3. **Inicie o servidor:**
```bash
# Desenvolvimento (com auto-reload)
npm run dev

# Produção
npm start
```

4. **Acesse a documentação:**
   - API: http://localhost:3000
   - Swagger: http://localhost:3000/api-docs
   - Health: http://localhost:3000/health

### Frontend

1. **Abra o arquivo `index.html` em um navegador** ou use um servidor local:

```bash
# Usando Python
python -m http.server 5173

# Usando Node.js (http-server)
npx http-server -p 5173

# Ou abra diretamente no navegador
open index.html
```

## 🔧 Configuração do Google Calendar

1. Acesse o [Google Cloud Console](https://console.cloud.google.com)
2. Crie um novo projeto
3. Ative a **Google Calendar API**
4. Crie uma **Service Account**:
   - IAM & Admin → Service Accounts
   - Create Service Account
   - Baixe o JSON de credenciais
5. Compartilhe seu Google Calendar com o email da service account
6. Configure no `.env`:
   ```
   GOOGLE_CLIENT_EMAIL=sua-service-account@projeto.iam.gserviceaccount.com
   GOOGLE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
   GOOGLE_CALENDAR_ID=seu-calendar-id@group.calendar.google.com
   ```

## 🔐 GitHub Token (Opcional)

Para evitar rate limiting da API do GitHub:

1. Acesse: https://github.com/settings/tokens
2. Generate new token (classic)
3. Selecione scope: `public_repo`
4. Configure no `.env`:
   ```
   GITHUB_USERNAME=MellDev
   GITHUB_TOKEN=ghp_seu_token_aqui
   ```

## 📦 Instalação do gallery-dl

Para usar a funcionalidade de scraping:

```bash
# macOS
brew install gallery-dl

# Linux (pip)
pip install gallery-dl

# Ou via pipx
pipx install gallery-dl
```

## 🌐 Endpoints da API

### Calendar
- `GET /api/calendar/available-slots?date=2026-01-15`
- `POST /api/calendar/appointments`
- `GET /api/calendar/appointments`
- `PUT /api/calendar/appointments/:id`
- `DELETE /api/calendar/appointments/:id`

### GitHub
- `GET /api/github/repos`
- `GET /api/github/repos/:owner/:repo`
- `GET /api/github/stats`
- `GET /api/github/contributions`

### Scraper
- `POST /api/scraper/download`
- `GET /api/scraper/status/:jobId`
- `GET /api/scraper/platforms`

### Projects
- `GET /api/projects`
- `GET /api/projects/:id`

### Contact
- `POST /api/contact`

## 🛠️ Tecnologias Utilizadas

### Backend
- Node.js + Express
- MongoDB + Mongoose
- Google APIs (Calendar)
- GitHub API
- Swagger/OpenAPI
- Nodemailer
- Winston (logs)
- gallery-dl

### Frontend
- HTML5 + CSS3
- JavaScript (Vanilla)
- Font Awesome
- Design responsivo

## 📝 TODO

- [ ] Adicionar autenticação JWT
- [ ] Implementar upload de imagens
- [ ] Criar dashboard admin
- [ ] Adicionar testes automatizados
- [ ] Deploy em produção

## 📄 Licença

MIT

## 👤 Autor

**Gabriel Orellana**
- GitHub: [@MellDev](https://github.com/MellDev)
- Email: gorellana@example.com

---

Feito com ❤️ por Gabriel Orellana
