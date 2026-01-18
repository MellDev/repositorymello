# 🛠️ Comandos Úteis - Portfolio

## 🚀 Início Rápido

### Iniciar Tudo de Uma Vez
```bash
./start.sh
```

---

## 🔧 Backend (API FastAPI)

### Setup Inicial
```bash
cd api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### Desenvolvimento
```bash
# Iniciar servidor com hot-reload
uvicorn app.main:app --reload

# Iniciar em porta específica
uvicorn app.main:app --reload --port 8080

# Iniciar com host público
uvicorn app.main:app --reload --host 0.0.0.0
```

### Testes
```bash
# Rodar testes
pytest

# Testes com coverage
pytest --cov=app --cov-report=html

# Testes verbosos
pytest -v
```

### Dependências
```bash
# Instalar nova dependência
pip install nome-pacote

# Atualizar requirements.txt
pip freeze > requirements.txt

# Instalar dependências de desenvolvimento
pip install pytest pytest-cov black flake8
```

### Formatação
```bash
# Formatar código com black
black app/

# Verificar estilo com flake8
flake8 app/
```

### Database (MongoDB)
```bash
# Iniciar MongoDB local
mongod --dbpath ~/data/db

# Conectar via CLI
mongosh mongodb://localhost:27017/portfolio
```

---

## 🎨 Frontend (Angular)

### Setup Inicial
```bash
cd frontend
npm install
```

### Desenvolvimento
```bash
# Iniciar servidor de desenvolvimento
npm start
# ou
ng serve

# Iniciar em porta específica
ng serve --port 4300

# Abrir browser automaticamente
ng serve --open
```

### Build
```bash
# Build de desenvolvimento
ng build

# Build de produção
ng build --configuration production

# Build com análise de bundle
ng build --stats-json
npm install -g webpack-bundle-analyzer
webpack-bundle-analyzer dist/portfolio-frontend/stats.json
```

### Testes
```bash
# Testes unitários
ng test

# Testes E2E
ng e2e

# Testes com coverage
ng test --code-coverage
```

### Linting
```bash
# Verificar código
ng lint

# Corrigir automaticamente
ng lint --fix
```

### Criar Novos Componentes
```bash
# Criar componente
ng generate component components/nome-componente

# Criar service
ng generate service services/nome-service

# Criar módulo
ng generate module nome-modulo
```

---

## 🗄️ Git

### Commits
```bash
# Stage e commit
git add .
git commit -m "feat: adiciona nova funcionalidade"

# Commit types (Conventional Commits)
# feat: nova funcionalidade
# fix: correção de bug
# docs: documentação
# style: formatação
# refactor: refatoração
# test: testes
# chore: tarefas gerais
```

### Branches
```bash
# Criar e mudar para nova branch
git checkout -b feature/nome-feature

# Listar branches
git branch

# Mudar de branch
git checkout main

# Deletar branch
git branch -d feature/nome-feature
```

### Sincronização
```bash
# Push
git push origin main

# Pull
git pull origin main

# Fetch
git fetch origin
```

---

## 🐛 Debugging

### Backend
```bash
# Logs detalhados
uvicorn app.main:app --reload --log-level debug

# Python debugger (pdb)
# Adicione no código: import pdb; pdb.set_trace()

# Verificar variáveis de ambiente
python -c "from app.config import settings; print(settings.dict())"
```

### Frontend
```bash
# Build em modo debug
ng build --configuration development

# Verificar erros TypeScript
tsc --noEmit

# Análise de performance
ng build --configuration production --source-map
```

---

## 📊 Monitoramento

### Verificar Saúde da API
```bash
curl http://localhost:8000/health

# Com formatação JSON
curl http://localhost:8000/health | jq
```

### Verificar Endpoints
```bash
# Listar repositórios GitHub
curl http://localhost:8000/api/github/repos

# Listar horários disponíveis
curl "http://localhost:8000/api/calendar/available-slots?date=2024-01-15"

# Criar agendamento (POST)
curl -X POST http://localhost:8000/api/calendar/appointments \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Teste",
    "email": "teste@exemplo.com",
    "phone": "11999999999",
    "service": "consulting",
    "date": "2024-01-15",
    "time": "10:00",
    "message": "Teste"
  }'
```

---

## 🔒 Segurança

### Gerar Secret Key
```bash
# Python
python -c "import secrets; print(secrets.token_urlsafe(32))"

# OpenSSL
openssl rand -base64 32
```

### Verificar Vulnerabilidades
```bash
# Backend
pip install safety
safety check

# Frontend
npm audit
npm audit fix
```

---

## 📦 Deploy

### Build para Produção

**Backend:**
```bash
cd api
pip install -r requirements.txt
# Configure variáveis de ambiente no servidor
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
ng build --configuration production
# Arquivos em: dist/portfolio-frontend/
```

### Docker (Opcional)

**Backend Dockerfile:**
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Build e Run:**
```bash
docker build -t portfolio-api .
docker run -p 8000:8000 --env-file .env portfolio-api
```

---

## 🧹 Limpeza

### Backend
```bash
cd api

# Limpar cache Python
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# Remover ambiente virtual
rm -rf venv
```

### Frontend
```bash
cd frontend

# Limpar cache e dependências
rm -rf node_modules package-lock.json
rm -rf dist .angular

# Reinstalar tudo
npm install
```

---

## 📝 Logs

### Acessar Logs
```bash
# Backend logs
tail -f api.log

# Frontend logs (servidor de dev)
# Logs aparecem no terminal onde rodou `ng serve`

# Logs do sistema (macOS)
log show --predicate 'process == "uvicorn"' --last 1h
```

---

## 🔄 Atualizar Dependências

### Backend
```bash
pip list --outdated
pip install --upgrade nome-pacote
pip freeze > requirements.txt
```

### Frontend
```bash
npm outdated
npm update
# ou para atualizar Angular
ng update @angular/cli @angular/core
```

---

## 💡 Dicas Úteis

### Verificar Portas em Uso
```bash
# macOS/Linux
lsof -i :8000
lsof -i :4200

# Matar processo na porta
kill -9 $(lsof -t -i:8000)
```

### Limpar Terminal
```bash
clear
# ou
Cmd+K (macOS)
```

### Variáveis de Ambiente
```bash
# Ver variável
echo $PYTHONPATH

# Exportar temporariamente
export API_URL=http://localhost:8000

# Ver todas
env | grep API
```

---

## 🆘 Troubleshooting

### Backend não inicia
```bash
# Verificar Python
python3 --version

# Verificar pip
pip --version

# Reinstalar dependências
pip install --force-reinstall -r requirements.txt
```

### Frontend não inicia
```bash
# Verificar Node
node --version
npm --version

# Limpar e reinstalar
rm -rf node_modules package-lock.json
npm cache clean --force
npm install

# Instalar Angular CLI globalmente
npm install -g @angular/cli
```

### Erro de CORS
- Verifique se a API está rodando
- Verifique URL em `api-config.service.ts`
- Verifique configuração CORS em `main.py`

### Banco de dados não conecta
- Verifique se MongoDB está rodando
- Verifique URL no `.env`
- Tente modo sem banco (opcional no código)

---

## 🔗 Links Úteis

- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **Angular Docs**: https://angular.io/docs
- **TypeScript**: https://www.typescriptlang.org/docs/
- **Pydantic**: https://docs.pydantic.dev/
- **RxJS**: https://rxjs.dev/guide/overview

---

## 📞 Comandos de Produção

### Monitoramento
```bash
# Status do servidor
systemctl status portfolio-api

# Logs em tempo real
journalctl -u portfolio-api -f

# Restart serviço
systemctl restart portfolio-api
```

### Backup
```bash
# Backup do banco
mongodump --db portfolio --out backup/

# Restore
mongorestore --db portfolio backup/portfolio/
```

---

✨ **Mantenha este arquivo como referência rápida!**
