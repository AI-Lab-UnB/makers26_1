# Semanas 7 e 8 – Planejamento e Estrutura Inicial do FIFA Team Hub

## Objetivo das Semanas

As Semanas 7 e 8 foram dedicadas à organização inicial do projeto **FIFA Team Hub**, envolvendo a definição da proposta da aplicação, alinhamento da equipa e planejamento da arquitectura que será utilizada ao longo do desenvolvimento de 8 sprints.

O foco principal foi estruturar as bases do projeto antes do início da implementação técnica, garantindo que todos os integrantes compartilhassem a mesma visão sobre os objetivos, tecnologias, responsabilidades e cronograma de entrega.

---

## Semana 7 – Planejamento do Projeto

### Objetivo da Semana 7

Estabelecer os fundamentos do projeto através do planejamento estratégico, definição de escopo, alinhamento da equipa e estruturação das tecnologias a serem utilizadas.

### Atividades Realizadas na Semana 7

#### Formação da Equipa

Inicialmente foi realizada a organização do grupo de trabalho, definindo os integrantes responsáveis pelo desenvolvimento do projeto e estabelecendo uma divisão inicial de responsabilidades por frente técnica.

A equipa foi organizada em **rotação semanal de sprints**, garantindo que cada membro adquira experiência em múltiplas áreas (Backend, Frontend, DevOps, Documentação) ao longo do desenvolvimento. Essa abordagem promove aprendizado distribuído e reduz riscos de dependência de conhecimento único.

#### Divisão de Responsabilidades da Equipa

| Membro | Papel | GitHub |
|--------|-------|--------|
| **Júlia Campos** | Tech Lead / Backend | [@camposs04](https://github.com/camposs04) |
| **Josef Woljtyla** | Backend | [@JosefWojtyla](https://github.com/JosefWojtyla) |
| **João Sauma** | Backend / Frontend / Integração | [@jvsauma](https://github.com/jvsauma) |
| **Caio Felipe** | Frontend / UI/UX | [@caio-nascime](https://github.com/caio-nascime) |
| **Arthur Miguel** | Backend / Cloud / Deploy | [@arthurmgl99](https://github.com/arthurmgl99) |

**Total: 5 pessoas | 1 Tech Lead | 4 Engenheiros Full-Stack com especialização**

#### Definição do Tema e Escopo

Foi escolhido o tema **FIFA Team Hub**, com a proposta de desenvolver um **portal seguro de gestão de recursos para seleções nacionais de futebol**.

**Proposta de Valor:**
- Centralizar convocações, documentação de viagem, laudos médicos e relatórios táticos num portal único
- Garantir isolamento absoluto entre seleções (tecnicamente impossível acessar dados de outra seleção)
- Criar trilha de auditoria completa para conformidade regulatória (LGPD)
- Apoiar autonomia de comissões técnicas com interface self-service
- Substituir processos manuais (e-mails, drives compartilhadas) por sistema estruturado

**Funcionalidades Principais do MVP:**
1. Autenticação segura com JWT e controle de acesso por perfil (RBAC)
2. Upload de documentos com validações rigorosas no servidor
3. Listagem filtrada por seleção (isolamento garantido)
4. Armazenamento no Google Cloud Storage
5. Logs imutáveis de auditoria para conformidade
6. Aprovação estruturada de laudos médicos
7. Dashboard diferenciado por perfil (Technical Staff, Organizer, Auditor)

#### Planejamento da Arquitectura

Foram realizadas discussões sobre a estrutura geral do sistema, definindo:

- **Isolamento Multi-Tenant:** Row-level filtering em todas as queries; impossibilidade de cross-selection access
- **Segurança em Camadas:** Autenticação JWT, autorização RBAC, validação no servidor, criptografia em trânsito
- **Auditoria Completa:** AuditLog imutável registando LOGIN, UPLOAD, DOWNLOAD, DELETE, APPROVE, REJECT, ACCESS_DENIED
- **Escalabilidade:** Arquitectura preparada para migração de storage local (S10) → GCS (S11)
- **Testabilidade:** Testes de isolamento bloqueadores em CI/CD; nenhum PR sem testes de segurança passa

#### Escolha da Stack Tecnológica

A equipa definiu as tecnologias que serão utilizadas durante o desenvolvimento do projeto, alinhadas com modernidade, segurança e facilidade de manutenção.

| Camada | Tecnologia | Justificativa |
|--------|-----------|---------------|
| **Frontend** | Vue 3 + TypeScript | Reatividade nativa, type-safety, componentes reutilizáveis |
| **Backend** | Flask + Python | Leve, seguro, autenticação JWT nativa, ORM robusto |
| **ORM/Migrations** | SQLAlchemy + Alembic | Queries tipadas, migrações versionadas, segurança |
| **Banco de Dados** | PostgreSQL 15 | UUID nativo, Enums, Full-text search, row-level filtering |
| **Autenticação** | python-jose + bcrypt | JWT stateless, hash de senha seguro (bcrypt ≥10) |
| **Storage (Dev)** | Filesystem local | Desenvolvimento simples, pronto para migrar a GCS |
| **Storage (Prod)** | Google Cloud Storage | Redundância, criptografia nativa, links temporários assinados |
| **Containerização** | Docker + Docker Compose | Ambientes reproduzíveis, escalabilidade |
| **CI/CD** | GitHub Actions | Testes automatizados, build bloqueador em falhas |
| **Cloud** | Google Cloud Platform | Cloud Run, Cloud SQL, Cloud Storage, escalabilidade automática |
| **Documentação** | Astro Starlight + GitHub Pages | Documentação técnica versionada, deploy automático |

#### Organização do Repositório

Foi criado e configurado o repositório do projeto no GitHub:

**Repositório Principal:** [FIFATeamHub/fifa_team_hub](https://github.com/FIFATeamHub/fifa_team_hub)

**Estrutura de Pastas Definida:**
```
fifa_team_hub/
├── backend/                    # Flask API
│   ├── app/
│   │   ├── models/            # SQLAlchemy models
│   │   ├── routes/            # Blueprints e endpoints
│   │   ├── services/          # Lógica de negócio
│   │   ├── middlewares/       # Auth decorators, error handlers
│   │   └── config.py          # Configurações centralizadas
│   ├── tests/                 # Testes unitários e integração
│   ├── migrations/            # Alembic migrations
│   ├── requirements.txt       # Dependências Python
│   └── Dockerfile
├── frontend/                   # Vue 3 + TypeScript
│   ├── src/
│   │   ├── components/        # Componentes reutilizáveis
│   │   ├── pages/             # Rotas (Vue Router)
│   │   ├── stores/            # Pinia state management
│   │   ├── composables/       # Lógica reutilizável
│   │   └── services/          # Chamadas à API
│   ├── tests/                 # Testes Vitest
│   └── package.json
├── docs/                       # Documentação Astro Starlight
│   └── src/content/docs/
├── .github/
│   ├── workflows/             # GitHub Actions CI/CD
│   └── ISSUE_TEMPLATE/
├── docker-compose.yml
├── .gitignore
└── README.md
```

**Padrões Definidos:**
- **Commits:** Conventional Commits (feat:, fix:, docs:, chore:)
- **Branches:** `main` (produção), `develop` (integração), `feature/*` (desenvolvimento)
- **PR Policy:** Obrigatório 1 revisor; CI/CD deve passar; sem conflitos de merge
- **Code Review:** Foco em segurança (isolamento), testes e performance

#### Cronograma de Sprints (S9–S14)

| Sprint | Semana | Foco | Entregas |
|--------|--------|------|----------|
| **S9** | Semana 9 | Autenticação | Login, JWT, hash de senha, middleware de rota |
| **S10** | Semana 10 | Upload e Listagem | Upload de documentos, validações, listagem filtrada |
| **S11** | Semana 11 | Cloud Storage | Integração GCS, links temporários, soft-delete |
| **S12** | Semana 12 | Logs e Auditoria | AuditLog completo, painel de logs, aprovação de laudos |
| **S13** | Semana 13 | Deploy | GCP deployment, hardening, testes de produção |
| **S14** | Semana 14 | Demonstração | Demo final, ajustes, apresentação ao avaliador |

---

## Semana 8 – Estrutura Inicial do Projeto

### Objetivo da Semana 8

Realizar a configuração inicial da infraestrutura do projeto, preparando o ambiente de desenvolvimento e implementando a base técnica das camadas Backend, Frontend e DevOps.

### Atividades Realizadas na Semana 8

#### Backend – Estrutura Inicial

**Responsáveis:** Júlia (Âncora) + Josef

Nesta semana foi organizada a estrutura base da aplicação Flask:

1. **Setup do Projecto:**
   - Criação da estrutura de pastas (`app/`, `tests/`, `migrations/`)
   - Configuração de `requirements.txt` com dependências iniciais
   - Setup do `Dockerfile` com Python 3.11 e hot-reload para desenvolvimento

2. **Configuração da Base de Dados:**
   - Instalação e configuração do PostgreSQL via Docker Compose
   - Criação de `app/config.py` centralizando variáveis de ambiente
   - Setup inicial do SQLAlchemy ORM
   - Inicialização do Alembic para versionamento de migrações

3. **Estrutura de Camadas:**
   - Definição de padrão Factory Pattern para aplicação Flask
   - Organização de Blueprints por domínio (auth, documents, logs)
   - Setup inicial de tratamento de erros e validação

4. **Testes Iniciais:**
   - Configuração do pytest
   - Criação de test fixtures para banco de dados
   - Primeiro teste de health check (`GET /health` → 200)

**Status Final:** Estrutura pronta, Docker rodando, primeira rota funcional

#### Frontend – Estrutura Inicial

**Responsáveis:** Caio (Âncora) + Arthur

Nesta semana foi realizado o setup inicial do Vue 3 com TypeScript:

1. **Setup do Projecto:**
   - Inicialização com Vite (moderna, rápida)
   - Configuração de TypeScript com strict mode
   - Setup do Tailwind CSS para estilização

2. **Router e State Management:**
   - Vue Router configurado com rotas base (`/login`, `/dashboard`, `/404`)
   - Pinia store inicializada para gerenciamento de estado
   - Estrutura de tipos TypeScript para estado reactivo

3. **Componentes Base:**
   - Layout principal (header, sidebar, main content)
   - Componente de formulário com validação client-side
   - Componente de tabela reutilizável
   - Componentes de feedback (toast, modal, spinner)

4. **Integração com Backend:**
   - Axios configurado com baseURL do backend
   - Interceptors para injetar JWT automaticamente
   - Error handling centralizado para 401/403

5. **Testes Iniciais:**
   - Setup do Vitest + `@vue/test-utils`
   - Primeiro teste de componente (renderização)
   - Configuração de jsdom para testes DOM

**Status Final:** Interface estruturada, componentes base prontos, Axios integrado

#### DevOps – Ambiente Local

**Responsáveis:** Júlia (Âncora) + João

Nesta semana foi configurado o ambiente completo para desenvolvimento local:

1. **Docker Compose:**
   - Serviço PostgreSQL com healthcheck
   - Serviço Backend Flask com volume para hot-reload
   - Serviço Frontend Vite com volume para live-reload
   - Network compartilhada para comunicação entre serviços
   - Variáveis de ambiente via `.env.example`

2. **Configuração de Ambiente:**
   - `.env.example` preenchido com todas as variáveis necessárias
   - `.gitignore` atualizado (não versionar `.env`, `node_modules`, `__pycache__`)
   - README com passos para rodar o ambiente (`docker compose up`)

3. **Validação:**
   - Teste: `docker compose up` sobe todos os serviços sem erros
   - Teste: `GET /health` retorna 200 em 30 segundos
   - Teste: Frontend acessível em `localhost:5173`
   - Teste: Todos os membros conseguem rodar localmente

**Status Final:** Ambiente reproduzível, todos operacional

#### Documentação – Base do Projeto

**Responsáveis:** Josef (Âncora) + Arthur

Nesta semana foi inicializada a documentação:

1. **GitHub Pages com Astro Starlight:**
   - Criação de repositório separado para documentação ou pasta `/docs`
   - Configuração inicial do Astro com tema Starlight
   - Estrutura de documentação: `docs/`, `visao/`, `requisitos/`, `api/`

2. **Documentação Inicial:**
   - `README.md` do repositório com overview do projeto
   - Documentação de arquitetura (diagramas, decisões técnicas)
   - Guia de setup do ambiente local
   - Template de PR com checklist

3. **Configuração do CI:**
   - GitHub Actions workflow para deploy automático de Pages
   - Validação de Markdown em PRs

**Status Final:** Documentação estruturada, GitHub Pages pronto para S9

---

## Conclusão Geral

### Semana 7 – Planejamento Consolidado

A Semana 7 foi fundamental para estabelecer os alicerces do projeto. A equipa alignou-se em torno de:

✅ **Proposta de Valor Clara:** Portal seguro de gestão de documentos de seleções nacionais

✅ **Escopo Bem Definido:** 18 User Stories, 6 Características, 18 Requisitos Funcionais

✅ **Stack Moderno:** Vue 3, Flask, PostgreSQL, GCS, Docker, GitHub Actions

✅ **Cronograma Realista:** 6 sprints de 1 semana cada + 1 sprint de demonstração

✅ **Foco em Segurança:** Isolamento multi-tenant, auditoria completa, LGPD compliance

### Semana 8 – Estrutura Técnica Pronta

A Semana 8 transformou o planejamento em realidade técnica:

✅ **Backend:** Flask estruturado, PostgreSQL rodando, primeira rota funcional

✅ **Frontend:** Vue 3 + TypeScript pronto, componentes base implementados, Axios integrado

✅ **DevOps:** Docker Compose reproduzível, ambiente funcional em qualquer máquina

✅ **Documentação:** Estrutura de Pages pronta, guias iniciais documentados

✅ **CI/CD:** GitHub Actions configurado, primeira validação de código

### Próximas Etapas

A equipa está pronta para **Semana 9 (Sprint 9)**, focado em **Autenticação e Controle de Acesso:**

- Endpoints de login e cadastro de usuários
- Middleware de rota protegida (JWT guard)
- Telas de login e dashboard no frontend
- Testes de isolamento e segurança
- Documentação de endpoints

---

## Repositório do Projeto

**Repositório Principal:** [FIFATeamHub/fifa_team_hub](https://github.com/FIFATeamHub/fifa_team_hub)

**Documentação:** [GitHub Pages - FIFA Team Hub](https://fifateamhub.github.io/fifa_team_hub/) (irá ser ativado após S9)

**Status Atual:**
- ✅ Estrutura Backend rodando
- ✅ Estrutura Frontend funcional
- ✅ Docker Compose operacional
- ✅ Documentação inicial estruturada
- ⏳ Aguardando Semana 9 para implementação de features

---

## Próxima Semana

**Semana 9 – Autenticação e Controle de Acesso**

Foco: Implementar fluxo de autenticação completo com JWT, registro de usuários e redireccionamento por perfil. Primeira entrega com funcionalidade real ao utilizador.

**Sprint Goals:**
- Endpoint de login e cadastro
- Middleware de autenticação
- Telas de login e dashboard
- Testes de isolamento
- Documentação de endpoints