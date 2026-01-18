# Portfolio Frontend - Angular

Frontend em Angular integrado com API FastAPI.

## 🚀 Funcionalidades

- ✅ Interface moderna e responsiva
- ✅ Integração completa com API FastAPI
- ✅ Sistema de agendamento com Google Calendar
- ✅ Integração com GitHub
- ✅ Download de mídia com gallery-dl
- ✅ Formulário de contato
- ✅ Galeria de projetos

## 📋 Pré-requisitos

- Node.js 18+
- Angular CLI 17
- API FastAPI rodando em http://localhost:8000

## 🔧 Instalação

1. **Instalar dependências:**
```bash
cd frontend
npm install
```

2. **Configurar API URL:**
   - Edite `src/app/services/api-config.service.ts`
   - Configure a URL da API (padrão: http://localhost:8000)

3. **Iniciar servidor de desenvolvimento:**
```bash
npm start
# ou
ng serve
```

4. **Acessar:**
   - Frontend: http://localhost:4200
   - API: http://localhost:8000

## 🏗️ Estrutura

```
frontend/
├── src/
│   ├── app/
│   │   ├── components/     # Componentes da UI
│   │   │   ├── navbar/
│   │   │   ├── hero/
│   │   │   ├── projects/
│   │   │   ├── tools/
│   │   │   ├── schedule/
│   │   │   ├── contact/
│   │   │   └── footer/
│   │   ├── services/       # Serviços HTTP
│   │   │   ├── api-config.service.ts
│   │   │   ├── calendar.service.ts
│   │   │   ├── github.service.ts
│   │   │   ├── scraper.service.ts
│   │   │   ├── project.service.ts
│   │   │   └── contact.service.ts
│   │   ├── app.module.ts
│   │   └── app.component.ts
│   ├── styles.scss         # Estilos globais
│   └── index.html
├── angular.json
├── package.json
└── tsconfig.json
```

## 🎨 Componentes

### Navbar
- Navegação fixa no topo
- Menu responsivo para mobile
- Scroll suave entre seções

### Hero
- Seção de apresentação
- Animações CSS
- CTAs para ações principais

### Projects
- Listagem de projetos da API
- Cards interativos
- Links para GitHub e demos

### Tools
- Demonstrações de ferramentas
- Modal de Gallery Downloader
- Integração com API de scraping

### Schedule
- Formulário de agendamento
- Integração com Google Calendar
- Verificação de horários disponíveis em tempo real

### Contact
- Formulário de contato
- Validação de campos
- Envio via API

## 📦 Build para Produção

```bash
ng build --configuration production
```

Os arquivos estarão em `dist/portfolio-frontend/`

## 🔧 Configuração da API

Por padrão, a API é acessada em `http://localhost:8000`.

Para mudar:
1. Edite `src/app/services/api-config.service.ts`
2. Ou use variáveis de ambiente

## 🛠️ Tecnologias

- Angular 17
- TypeScript
- SCSS
- RxJS
- HttpClient
- Reactive Forms
- Font Awesome

## 📄 Licença

MIT
