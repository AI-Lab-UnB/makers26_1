# Semana 9 – Autenticação e Controle de Acesso

## Objetivo da Semana

A Semana 9 foi dedicada à implementação do **sistema de autenticação e controle de acesso** do FIFA Team Hub. Este é o pilar de segurança do projeto: sem autenticação robusta, o isolamento entre seleções não é possível. O foco foi implementar JWT stateless, hash de senhas com bcrypt, middleware de rota protegida e fluxo de autenticação completo no frontend.

Esta semana também marcou o início da **engenharia de requisitos formal**, com documentação de requisitos funcionais, não-funcionais e externos seguindo o padrão IEEE 830.

---

## Divisão da Equipa (Rotação Sprint 9)

| Frente | Responsáveis | Foco |
|--------|--------------|------|
| **Backend** | Josef (Âncora) + Arthur (1ª vez BE real) | Endpoints auth, hash bcrypt, JWT, middleware |
| **Frontend** | Caio (Âncora) + João (1ª vez FE real) | Telas login/cadastro, store Pinia, interceptors |
| **DevOps** | Júlia (Âncora, 1ª vez DO) + Arthur (2ª frente) | JWT_SECRET_KEY, GitHub Pages, variáveis env |
| **Documentação** | Arthur (Responsável) | Endpoints auth, payloads JWT, Postman collection |

---

## Issues Geradas (S9-01 a S9-13)

### Backend (4 Issues)

**[S9-01] Criar modelo User com SQLAlchemy + migration Alembic**
- Responsáveis: Josef + Arthur
- Campos: id (UUID), email (unique), password_hash, role (Enum), selection_id (FK, nullable), is_active, created_at
- Migration versionada com Alembic
- Script de seed com 2 seleções (BRA/ARG) e usuários de teste
- **Status:** ✅ Concluída
- **Entrega:** Tabelas `users` e `selections` no banco

**[S9-02] Implementar hash de senha com bcrypt e AuthService**
- Responsáveis: Josef + Arthur
- Dependências: `passlib[bcrypt]`, `python-jose`
- Funções: `hash_password()`, `verify_password()`, `create_access_token()`, `decode_token()`
- JWT_SECRET_KEY e JWT_EXPIRE lidos do `.env`
- Testes unitários de hash e JWT
- **Status:** ✅ Concluída
- **Entrega:** AuthService pronto para endpoints

**[S9-03] Endpoints POST /auth/register e POST /auth/login**
- Responsáveis: Josef + Arthur
- `POST /auth/register`: cria usuário com validação de e-mail duplicado, retorna 201
- `POST /auth/login`: valida credenciais, retorna JWT com user_id, role, selection_id, exp
- `GET /auth/me`: endpoint protegido que retorna dados do usuário autenticado
- Tratamento de erros: 400, 401, 409, 422
- Testado no Postman com múltiplos cenários
- **Status:** ✅ Concluída
- **Entrega:** Endpoints funcionais com curl/Postman

**[S9-04] Criar decorator @require_auth (JWT guard) no Flask**
- Responsáveis: Júlia (lidera) + Arthur (implementa)
- Decorator extrai token do header `Authorization: Bearer <token>`
- Decodifica JWT, injeta `g.current_user_id`, `g.current_user_role`, `g.current_selection_id`
- Retorna 401 se token ausente/expirado/inválido
- Decorator `@require_role("TECHNICAL_STAFF")` para restrições adicionais
- Teste que sem token retorna 401, com token válido retorna 200
- **Status:** ✅ Concluída
- **Entrega:** Decorator pronto para proteger rotas futuras

### Frontend (2 Issues)

**[S9-05] Telas de cadastro e login + fluxo de sessão JWT**
- Responsáveis: Caio (Âncora) + João (Par)
- Telas: LoginPage, RegisterPage com validação client-side
- Armazenamento de token em `localStorage`
- `GET /auth/me` após login para confirmar autenticação
- Redirect para dashboard ou volta ao login se falhar
- Mensagens de erro amigáveis (401, 403, etc.)
- **Status:** ✅ Concluída
- **Entrega:** Fluxo login → dashboard funcional

**[S9-06] Controle de acesso por role no frontend (RBAC)**
- Responsáveis: Caio + João
- Composable `usePermissions` com mapa de permissões
- Componente `<PermissionGate>` que renderiza apenas se autorizado
- Navigation guard RBAC: redireciona rota /audit apenas para AUDITOR
- Página 403 para tentativas de acesso não autorizado
- **Status:** ✅ Concluída
- **Entrega:** RBAC completo no frontend

### DevOps / Infra (2 Issues)

**[S9-07] Configurar variáveis de auth + GitHub Pages**
- Responsáveis: Júlia (Âncora) + Arthur (Apoio)
- `.env.example`: JWT_SECRET_KEY, JWT_ALGORITHM, JWT_EXPIRE_MINUTES
- `docker-compose.yml`: passar variáveis ao backend
- GitHub Pages configurado em Settings → Pages (source: GitHub Actions)
- `docs/index.md` com links para documentação
- **Status:** ✅ Concluída
- **Entrega:** Variáveis configuradas, Pages pronto para S9

**[S9-08] Workflow GitHub Actions — CI básico (lint + testes)**
- Responsáveis: Júlia + Arthur
- `.github/workflows/ci.yml`: trigger em PRs para `develop` e `main`
- Job backend: `pytest + PostgreSQL service container`
- Job frontend: `ESLint + vue-tsc + Vitest`
- CI bloqueia PR com testes/lint falhando
- Badge de status no README
- **Status:** ✅ Concluída
- **Entrega:** Pipeline CI/CD operacional

### Documentação (1 Issue)

**[S9-09] Documentar endpoints de auth + collection Postman**
- Responsável: Arthur
- `docs/api-auth.md`: endpoints com método, path, auth, body, respostas
- Payload JWT documentado: `{user_id, role, selection_id, exp}`
- Fluxo de sessão e expiração explicado
- Collection Postman em `docs/postman/s9_auth.json`
- **Status:** ✅ Concluída
- **Entrega:** Documentação completa acessível via GitHub Pages

### Produto / Requisitos (4 Issues)

**[S9-10] Levantar e documentar requisitos: RF, RNF, externos**
- Responsáveis: Júlia (Lidera) + Josef (Revisão técnica)
- 18 RFs documentados com critério de aceitação
- 10 RNFs com métricas mensuráveis
- 6 REs (requisitos externos)
- Priorização MoSCoW integrada
- **Status:** ✅ Concluída
- **Entrega:** `docs/requisitos.md` no GitHub Pages

**[S9-11] Escrever User Stories com critérios de aceitação (BDD)**
- Responsáveis: Júlia + Caio (Revisão UX)
- 18 User Stories no formato: "Como [persona], quero [ação] para que [benefício]"
- Critérios BDD: Given/When/Then
- Cobertura dos 3 perfis (TECHNICAL_STAFF, ORGANIZER, AUDITOR)
- **Status:** ✅ Concluída
- **Entrega:** `docs/user-stories.md`

**[S9-12] Criar diagrama UML — casos de uso + diagrama de classes**
- Responsáveis: Arthur (Lidera) + João
- Diagrama de casos de uso com 3 atores e interações principais
- Diagrama de classes com 4 entidades (User, Selection, Document, AuditLog)
- Exportados como PNG em `docs/diagrams/`
- **Status:** ✅ Concluída
- **Entrega:** `docs/uml.md` com diagramas

**[S9-13] Criar backlog completo + MVP definido + walkthrough + protótipo**
- Responsáveis: Júlia (Backlog + MVP) + Caio (Prototipo) + João (Apoio)
- Backlog com 18 items, priorização MoSCoW completa
- MVP definido com critério claro de conclusão (S13)
- Walkthrough do fluxo principal (login → upload → auditoria)
- Wireframes de baixa fidelidade em `docs/wireframes/`
- **Status:** ✅ Concluída
- **Entrega:** `docs/backlog.md` + `docs/prototipo.md`

---

## Tarefas por Frente Técnica

### Backend — Tarefas Concluídas

- ✅ Modelo User com campos corretos (id, email, password_hash, role, selection_id)
- ✅ Modelo Selection com código FIFA único
- ✅ Migration Alembic aplicada (`alembic upgrade head`)
- ✅ Script de seed criado com 2 seleções e usuários de teste
- ✅ AuthService com `hash_password()`, `verify_password()`, `create_access_token()`, `decode_token()`
- ✅ Endpoints POST /auth/register, POST /auth/login, GET /auth/me funcionais
- ✅ Validações de e-mail duplicado, senha mínima 8 caracteres
- ✅ JWT contém user_id, role, selection_id, exp (60 min)
- ✅ Decorator @require_auth extrai token e injeta dados em `g.`
- ✅ Decorator @require_role restringe por perfil
- ✅ AuditLog registado para eventos LOGIN, LOGOUT, REGISTER
- ✅ Testes unitários de AuthService passando
- ✅ PR aprovado, merge na main

### Frontend — Tarefas Concluídas

- ✅ Tela LoginPage com e-mail + senha, submit chamando POST /auth/login
- ✅ Tela RegisterPage com e-mail + senha + seleção
- ✅ Validação client-side (e-mail válido, senha ≥ 8)
- ✅ Token JWT armazenado em localStorage após login bem-sucedido
- ✅ GET /auth/me chamado automaticamente após login
- ✅ Redirect para /dashboard se autenticado, para /login se não
- ✅ Mensagens de erro amigáveis (401, 403, 422)
- ✅ Logout limpa token e localStorage
- ✅ Interceptor Axios injeta `Authorization: Bearer <token>` automaticamente
- ✅ Composable usePermissions mapeando ações → roles
- ✅ Componente <PermissionGate> renderizando condicionalmente
- ✅ Navigation guard bloqueando rotas não autorizadas
- ✅ Página 403 para acesso negado
- ✅ Testes Vitest de componentes e store
- ✅ PR aprovado, merge na main

### DevOps — Tarefas Concluídas

- ✅ `.env.example` atualizado com JWT_SECRET_KEY, JWT_ALGORITHM, JWT_EXPIRE_MINUTES
- ✅ `docker-compose.yml` passando variáveis JWT ao backend
- ✅ `.gitignore` incluindo `.env` (não versionar credenciais)
- ✅ GitHub Pages Settings configurado (source: GitHub Actions)
- ✅ `docs/index.md` criado com links para documentação
- ✅ `.github/workflows/ci.yml` criado com jobs backend e frontend
- ✅ CI trigger em PRs para develop e main
- ✅ Backend job: pytest + PostgreSQL service container
- ✅ Frontend job: ESLint + vue-tsc + Vitest
- ✅ PR com CI falhando é bloqueado automaticamente
- ✅ Badge de status do CI adicionado ao README
- ✅ Todos os membros conseguem rodar `docker compose up` e acessar localhost:3000/5173

### Documentação — Tarefas Concluídas

- ✅ `docs/api-auth.md` documentando POST /auth/register, POST /auth/login, GET /auth/me
- ✅ Payload JWT documentado com todos os campos
- ✅ Fluxo de sessão explicado (60 min, redirect no 401)
- ✅ Collection Postman exportada e testada (`docs/postman/s9_auth.json`)
- ✅ Exemplos de request/response para cada endpoint
- ✅ Regras de validação documentadas
- ✅ `docs/requisitos.md` com 18 RFs, 10 RNFs, 6 REs
- ✅ `docs/user-stories.md` com 18 User Stories formato BDD
- ✅ `docs/uml.md` com diagramas de casos de uso e classes
- ✅ GitHub Pages publicando documentação automaticamente

---

## Testes de Isolamento e Segurança

### Testes Implementados

✅ `test_document_isolation.py`:
- Upload cria documento com selection_id correto (do token, não do body)
- TECHNICAL_STAFF da BRA não vê documentos da ARG em listagem
- Acesso direto a documento de outra seleção retorna 403
- Eliminação de documento de outra seleção é bloqueada
- ORGANIZER não acessa RELATORIO_TATICO

✅ Testes de Autenticação:
- Login com credenciais válidas retorna JWT com claims corretos
- Login com credenciais inválidas retorna 401 sem indicar qual campo errou
- Senha provisória obriga troca no primeiro acesso
- Token expirado retorna 401 e redireciona ao login

✅ CI/CD:
- PR com testes falhando é bloqueado
- Linting e type-check são obrigatórios
- Badge de status no README

---

## Métricas de Conclusão

| Métrica | Meta | Alcançado |
|---------|------|-----------|
| Issues S9 | 13 | ✅ 13 |
| User Stories | 18 | ✅ 18 |
| Requisitos | 34 (18 RF + 10 RNF + 6 RE) | ✅ 34 |
| Testes de isolamento | 5+ | ✅ 5+ |
| Endpoints funcionais | 3 (register, login, me) | ✅ 3 |
| Telas FE | 2 (login, register) | ✅ 2 |
| CI/CD pipeline | 2 jobs (BE + FE) | ✅ 2 |
| Documentação | GitHub Pages pronto | ✅ Pronto |

---

## Status Final da Semana 9

### ✅ Concluído

- ✅ Autenticação JWT completa (registro, login, me)
- ✅ Hash de senha com bcrypt
- ✅ Middleware de rota protegida
- ✅ RBAC (Role-Based Access Control) no frontend
- ✅ Fluxo de login → dashboard completo
- ✅ Testes de isolamento e segurança
- ✅ CI/CD pipeline operacional
- ✅ Documentação de requisitos, user stories, UML, backlog
- ✅ GitHub Pages publicando documentação
- ✅ Collection Postman para testes manuais

### ⏳ Pronto para S10

- ✅ Backend pronto para receber endpoints de upload
- ✅ Frontend pronto para componente de upload
- ✅ DevOps com variáveis de ambiente configuradas
- ✅ Documentação estruturada para expansão

---

## Aprendizados e Desafios

### Desafios Enfrentados

1. **Primeiro contato com BE (Arthur) e FE (João):** 
   - Resolvido com pair programming intenso com âncoras (Josef/Caio)
   - Arthur aprendeu arquitetura Flask, SQLAlchemy, Alembic
   - João aprendeu Vue 3, Pinia, TypeScript, interceptors

2. **Isolamento de dados:**
   - Decisão crítica: row-level filtering obrigatório
   - Implementado testes que bloqueiam PRs em violações
   - Nenhum cenário de cross-selection access

3. **Engenharia de requisitos:**
   - Padrão IEEE 830 com métrica em cada RNF
   - 18 User Stories em formato BDD
   - Priorização MoSCoW com Planning Poker

### Sucessos

1. **Equipa alinhada:** Todos entendem segurança, isolamento, auditoria
2. **CI/CD desde o início:** Testes bloqueadores evitam débitos técnicos
3. **Documentação formal:** Requisitos + User Stories + UML claros
4. **MVP bem definido:** 18 User Stories com priorização clara

---

## Próxima Sprint: Semana 10

**Semana 10 – Upload e Listagem**

Foco: Implementar o core do produto — upload de documentos e listagem filtrada por seleção.

**Divisão Equipa (Rotação):**
- Backend: Arthur (Âncora) + Caio (1ª vez BE)
- Frontend: João (Âncora) + Josef (1ª vez FE)
- DevOps: Júlia + João
- Docs: Caio

**Issues S10:**
- [S10-BE-01] Endpoint de upload multipart/form-data
- [S10-BE-02] Endpoint de listagem com filtro por seleção
- [S10-BE-03] Endpoint de eliminação (soft delete)
- [S10-FE-01] Componente de upload com progresso
- [S10-FE-02] Listagem com paginação e filtros
- [S10-DO-01] Configuração de storage local
- [S10-DC-01] Documentação de endpoints
- [S10-QA-01] Testes de isolamento + segurança

**Métrica de Sucesso:** Upload de PDF ≤ 10 MB funciona end-to-end, documentos isolados por seleção, AuditLog registado.