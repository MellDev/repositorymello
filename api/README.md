# Portfolio API - Python FastAPI

API REST completa para portfólio com integração Google Calendar, GitHub, scraping e mais.

## 🚀 Funcionalidades

- ✅ **Google Calendar**: Agendamento com service account
- ✅ **GitHub**: Integração completa com repositórios
- ✅ **Scraping**: Download de mídia com gallery-dl
- ✅ **Email**: Sistema de contato
- ✅ **FastAPI**: Documentação automática Swagger/ReDoc

## 📋 Pré-requisitos

- Python 3.10+
- MongoDB (opcional)
- Google Cloud Service Account
- gallery-dl

## 🔧 Instalação

1. **Criar ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

2. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

3. **Instalar gallery-dl:**
```bash
pip install gallery-dl
# ou
brew install gallery-dl  # macOS
```

4. **Configurar `.env`:**
```bash
cp .env.example .env
# Edite o .env com suas credenciais
```

5. **Adicionar credenciais do Google Calendar:**
   - Coloque o arquivo `service-account.json` em `api/credentials/`

## ▶️ Executar

```bash
# Desenvolvimento (com reload automático)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Produção
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 📚 Documentação

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 🌐 Endpoints

### Calendar
- `GET /api/calendar/available-slots?date=2026-01-15`
- `POST /api/calendar/appointments`
- `GET /api/calendar/appointments`
- `DELETE /api/calendar/appointments/{event_id}`

### GitHub
- `GET /api/github/repos`
- `GET /api/github/repos/{owner}/{repo}`
- `GET /api/github/stats`
- `GET /api/github/contributions`

### Scraper
- `POST /api/scraper/download`
- `GET /api/scraper/status/{job_id}`
- `GET /api/scraper/platforms`

### Projects
- `GET /api/projects`
- `GET /api/projects/{id}`

### Contact
- `POST /api/contact`

## 🔐 Configuração Google Calendar

1. Criar Service Account no Google Cloud Console
2. Baixar arquivo JSON de credenciais
3. Compartilhar Google Calendar com email da service account
4. Configurar no `.env`:
```env
GOOGLE_SERVICE_ACCOUNT_FILE=credentials/service-account.json
GOOGLE_CALENDAR_ID=seu-calendar-id@group.calendar.google.com
```

## 📦 Estrutura

```
api/
├── app/
│   ├── api/
│   │   └── routes/      # Rotas da API
│   ├── services/        # Lógica de negócio
│   ├── schemas/         # Modelos Pydantic
│   ├── config.py        # Configurações
│   └── main.py          # Aplicação principal
├── credentials/         # Credenciais Google
├── requirements.txt
└── .env
```

## 🛠️ Tecnologias

- FastAPI
- Pydantic
- Google APIs
- PyGithub
- gallery-dl
- aiosmtplib

## 📄 Licença

MIT
