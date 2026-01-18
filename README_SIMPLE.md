# Portfolio - Gabriel Orellana

Este repositório contém um portfolio interativo completo com backend FastAPI e frontend Angular.

## ✨ Funcionalidades

- 🗓️ **Sistema de Agendamento** com Google Calendar API
- 📥 **Gallery Downloader** para download de mídia
- 📊 **Integração com GitHub** para exibir repositórios
- 📧 **Formulário de Contato** com envio de email
- 🎨 **Interface Moderna** e totalmente responsiva

## 🚀 Início Rápido

### Opção 1: Script Automatizado (Recomendado)

```bash
./start.sh
```

Este script irá:
- ✅ Criar ambiente virtual Python
- ✅ Instalar todas as dependências
- ✅ Iniciar o backend em http://localhost:8000
- ✅ Iniciar o frontend em http://localhost:4200

### Opção 2: Manual

**Backend:**
```bash
cd api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

## 📚 Documentação Completa

- 📖 **[Guia de Início Rápido](INICIO_RAPIDO.md)** - Setup detalhado e troubleshooting
- 📖 **[README Backend](api/README.md)** - Documentação da API
- 📖 **[README Frontend](frontend/README.md)** - Documentação do Angular

## 🛠️ Tecnologias

### Backend
- FastAPI (Python 3.10+)
- Google Calendar API
- GitHub API
- gallery-dl
- MongoDB (opcional)

### Frontend
- Angular 17
- TypeScript
- SCSS
- RxJS

## 🔗 Links Úteis

Após iniciar o projeto:
- 🌐 Frontend: http://localhost:4200
- 🔌 API: http://localhost:8000
- 📄 Swagger Docs: http://localhost:8000/docs
- 📘 ReDoc: http://localhost:8000/redoc

## ⚙️ Configuração

### Google Calendar (Opcional)
Para usar agendamento real ao invés do modo mock:
1. Veja o [guia detalhado](INICIO_RAPIDO.md#configuração-do-google-calendar)
2. Obtenha credenciais do Google Cloud
3. Configure `api/credentials/service-account.json`
4. Atualize `api/.env`

### Email (Opcional)
Para envio de emails real:
1. Configure SMTP no `api/.env`
2. Use senha de app do Gmail

## 📁 Estrutura

```
repositorymello/
├── api/                 # Backend FastAPI
│   ├── app/
│   │   ├── api/routes/  # Endpoints
│   │   ├── services/    # Lógica de negócios
│   │   ├── schemas/     # Modelos Pydantic
│   │   └── main.py
│   ├── credentials/     # Credenciais Google
│   └── .env
│
├── frontend/            # Frontend Angular
│   ├── src/app/
│   │   ├── components/  # Componentes UI
│   │   └── services/    # Serviços HTTP
│   └── package.json
│
├── start.sh            # Script de início
└── INICIO_RAPIDO.md    # Guia detalhado
```

## 🎯 Próximos Passos

1. ✅ Clone o repositório
2. ✅ Execute `./start.sh`
3. ⚙️ (Opcional) Configure Google Calendar
4. ⚙️ (Opcional) Configure Email SMTP
5. 🎨 Customize cores e conteúdo
6. 🚀 Deploy para produção

## 📝 Licença

MIT

---

⭐ **Desenvolvido por Gabriel Orellana**
