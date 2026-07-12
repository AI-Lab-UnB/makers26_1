# Semana 14

> **Status:** Concluída
> **Período:** 07/07/2026 a 13/07/2026
> **Semana do ciclo:** 14 / 14
> **Fase atual:** Fase 3, Deploy e Demo
> **Responsável pelo preenchimento:** Diogo

---

## Objetivo da Semana

Fechar o ciclo com a auditoria estendida a todas as rotas sensíveis, entregar o CRUD completo de arquivos com controle de acesso por vínculo aprovado, subir o painel administrativo com consulta de logs, consolidar a arquitetura frontend em torno de hooks e proxy, blindar o pipeline com CI/CD, CodeQL e Dependabot e preparar a base para a demo final com responsividade mobile e um design system coerente via `sweetalert2`.

---

## Entregas Realizadas

### Backend

Hugo conduziu a frente de painel administrativo. Criou o `UserType.ADMIN` com migration correspondente do enum no banco (#56), o seed manual (`npm run seed:admin`) com bloqueio em produção via `ADMIN_SEED_ALLOW_PROD` e o endpoint `GET /audit/logs` protegido por `RolesGuard(ADMIN)` com filtros por `userId`, busca livre de usuário por nome ou email, `tipoEvento`, `dataInicio`, `dataFim` e paginação (#57). Também endereçou dois pontos de segurança de superfície: o `ValidationPipe` agora rejeita campos não declarados no cadastro público (fechando a possibilidade de escalada por payload como `tipo: ADMIN`) e o seed de admin teve o import dinâmico corrigido para operar com `moduleResolution=nodenext`.

Martin fechou a cobertura de auditoria nas rotas restantes. Aplicou o decorator `@Audit()` no `ArquivosController` cobrindo upload, visualização, download e exclusão (#54), na criação de vínculo médico paciente (#55) e centralizou a interface `AuthRequest` removendo casts inseguros que estavam espalhados pelos guards e interceptors.

Diogo consolidou o CRUD completo de arquivos com validação de tipo (PDF, JPEG, PNG) e tamanho (≤10 MB), download por stream, edição de descrição e exclusão. O vínculo médico paciente ganhou fluxo de solicitação, aprovação, rejeição e revogação com campo `status`, e a regra de acesso passou a exigir vínculo `APROVADO` para leitura ou edição de arquivos, com testes cobrindo o bloqueio. As especialidades médicas foram normalizadas em N:N com uma tabela pivot e seed a partir da lista oficial do CFM, acompanhadas de uma migration `ZerarMedicos` para reset controlado do ambiente. O Swagger foi habilitado no `main.ts` fora de produção com Bearer Auth persistido, `PublicUser` foi convertido em classe e o `UsersController` recebeu decorators de documentação.

Ainda em backend, houve um bloco relevante de fixes: `LOGIN_FALHA` foi removido do enum no banco de produção via migration (a consulta equivalente é feita por `tipoEvento = LOGIN AND status = FAILURE`), o `data-source` desatualizado foi corrigido, o download de arquivo passou a usar o endpoint `/raw` via blob no lugar da signed URL do GCS (o Cloud Run não tem a permissão `iam.serviceAccounts.signBlob`), o endpoint `/arquivos/:id/download` junto com o `getSignedUrl` foi removido como código morto e o `@Audit(DOWNLOAD_ARQUIVO)` foi conectado ao endpoint de stream.

Cobertura de testes ampliada para 116 testes passando: cobertura de `400` em `dataFim < dataInicio` e cap silencioso de `limit > 200` no `audit`, bloqueio de leitura e edição quando vínculo não é `APROVADO` em `arquivos`, novos edge cases em `medico-paciente` e ajuste do payload de cadastro em `users` para usar `especialidadeIds`.

**Commits relacionados:**

| Hash                                                                  | Data  | Autor  | Descrição                                                                                        |
| :-------------------------------------------------------------------- | :---- | :----- | :----------------------------------------------------------------------------------------------- |
| [`b450eaa`](https://github.com/Diogo-Olivv/HealthTech/commit/b450eaa) | 08/07 | Diogo  | feat(backend): CRUD completo de arquivos com download, edição e exclusão                         |
| [`40573d5`](https://github.com/Diogo-Olivv/HealthTech/commit/40573d5) | 08/07 | Diogo  | feat(backend): normaliza especialidades em N:N com médico usando lista CFM                       |
| [`6569750`](https://github.com/Diogo-Olivv/HealthTech/commit/6569750) | 08/07 | Diogo  | feat(backend): migration para zerar médicos existentes                                           |
| [`f43ab23`](https://github.com/Diogo-Olivv/HealthTech/commit/f43ab23) | 09/07 | Diogo  | db(medico-paciente): add status/consentimento no schema                                          |
| [`540029d`](https://github.com/Diogo-Olivv/HealthTech/commit/540029d) | 09/07 | Diogo  | db: usa migrationsTransactionMode=each                                                           |
| [`095ac66`](https://github.com/Diogo-Olivv/HealthTech/commit/095ac66) | 09/07 | Diogo  | feat(medico-paciente): fluxo de aprovacao de vinculo                                             |
| [`d647fa5`](https://github.com/Diogo-Olivv/HealthTech/commit/d647fa5) | 09/07 | Diogo  | feat(audit): eventos de solicitacao/aprovacao/rejeicao/revogacao                                 |
| [`222c9d4`](https://github.com/Diogo-Olivv/HealthTech/commit/222c9d4) | 09/07 | Diogo  | feat(arquivos): exige vinculo APROVADO para acesso e edicao                                      |
| [`43abe1e`](https://github.com/Diogo-Olivv/HealthTech/commit/43abe1e) | 09/07 | Martin | feat(medico-paciente): aplica auditoria na criacao                                               |
| [`869c332`](https://github.com/Diogo-Olivv/HealthTech/commit/869c332) | 10/07 | Martin | refactor(auth): centraliza interface AuthRequest e remove casts inseguros (Resolve #54)          |
| [`27f2d93`](https://github.com/Diogo-Olivv/HealthTech/commit/27f2d93) | 10/07 | Martin | feat(arquivos): adiciona auditoria de rotas, testes e refatora tipagem AuthRequest (Resolve #54) |
| [`294be19`](https://github.com/Diogo-Olivv/HealthTech/commit/294be19) | 11/07 | Hugo   | feature: adiciona UserType.ADMIN e migration do enum no banco                                    |
| [`cb4a94d`](https://github.com/Diogo-Olivv/HealthTech/commit/cb4a94d) | 11/07 | Hugo   | fix: rejeita campos não declarados (ex.: tipo) no cadastro público via ValidationPipe            |
| [`9760116`](https://github.com/Diogo-Olivv/HealthTech/commit/9760116) | 11/07 | Hugo   | feature: adiciona seed manual de admin (npm run seed:admin)                                      |
| [`e8ed3e3`](https://github.com/Diogo-Olivv/HealthTech/commit/e8ed3e3) | 11/07 | Hugo   | feature: adiciona GET /audit/logs para admin consultar logs de auditoria com filtros e paginação |
| [`b85d313`](https://github.com/Diogo-Olivv/HealthTech/commit/b85d313) | 11/07 | Hugo   | fix: corrige import dinâmico incompatível com moduleResolution nodenext no seed de admin         |
| [`2be64d6`](https://github.com/Diogo-Olivv/HealthTech/commit/2be64d6) | 11/07 | Diogo  | feat(swagger): setup em main.ts                                                                  |
| [`c613b24`](https://github.com/Diogo-Olivv/HealthTech/commit/c613b24) | 11/07 | Diogo  | feat(swagger): anota DTOs de users                                                               |
| [`bc07fc2`](https://github.com/Diogo-Olivv/HealthTech/commit/bc07fc2) | 11/07 | Diogo  | feat(swagger): decorators em UsersCtrl                                                           |
| [`131fecb`](https://github.com/Diogo-Olivv/HealthTech/commit/131fecb) | 12/07 | Diogo  | test(audit): cobre 400 em dataFim<dataInicio e cap silencioso de limit>200                       |
| [`326f4bd`](https://github.com/Diogo-Olivv/HealthTech/commit/326f4bd) | 12/07 | Diogo  | fix(arquivos): download via /raw                                                                 |
| [`504c8d0`](https://github.com/Diogo-Olivv/HealthTech/commit/504c8d0) | 12/07 | Diogo  | chore(arquivos): remove signed URL                                                               |
| [`e7bf117`](https://github.com/Diogo-Olivv/HealthTech/commit/e7bf117) | 12/07 | Diogo  | feat(audit): filtro por usuário                                                                  |

**Branch:** `feat/crud-arquivos`, `feat/vinculo-aprovacao`, `feat/user-admin`, `feat/audit-arquivos`, `feat/backend-swagger`, `develop`
**Issue(s):** #54, #55, #56, #57
**PRs:** [#67](https://github.com/Diogo-Olivv/HealthTech/pull/67), [#68](https://github.com/Diogo-Olivv/HealthTech/pull/68), [#69](https://github.com/Diogo-Olivv/HealthTech/pull/69), [#71](https://github.com/Diogo-Olivv/HealthTech/pull/71) (todos merged)

---

### Frontend

Diogo conduziu uma refatoração de arquitetura ampla no frontend. O hook genérico `useFetchData` virou a base para hooks por feature (`useAuditLogs`, `useArquivos`, `useMeusMedicos`, `useMeusPacientes`, `usePendingRequests`, `useSolicitacoesEnviadas`, `useProntuarioPaciente` e `useDebouncedValue` para busca com atraso), o que eliminou fetch direto espalhado pelas páginas. Os fluxos de autenticação passaram a viver em Route Handlers `/api/auth/login`, `/api/auth/logout` e `/api/auth/register`, com um proxy catch-all `/api/proxy/[...path]` cobrindo o restante das chamadas ao backend. Os helpers `API_URL`, `authHeaders` e `throwFromResponse` foram centralizados em `src/lib`, e a página "Meus médicos" ganhou SSR com wrapper client para não perder interatividade.

A tela `/admin` foi entregue com layout próprio, index e uma sub rota `/admin/auditoria` que consome o endpoint de logs. A tabela virou componente reutilizável (`audit-table`), com filtros por tipo de evento, intervalo de data e busca livre por usuário (nome ou email), tudo com paginação e debounce. A navbar ganhou o link para o painel administrativo, e o `AuthGuard` foi estendido para proteger a rota `/admin` por papel.

O design system foi consolidado em torno do `sweetalert2` com tema HealthTech e helpers reutilizáveis em `utils/alerts.ts`. Login e cadastro passaram a confirmar sucesso via popup antes do redirect, tabs alternam paciente e médico, validações inline dão feedback antes do submit e a navbar confirma o logout. Os modais viram bottom sheet no mobile, o painel lateral do auth some em telas pequenas, os dashboards e tabelas passam a ser fluidos, o viewport meta foi corrigido, o `lang` foi ajustado para `pt-BR` e o zoom em input do iOS foi bloqueado. Touch targets foram ampliados em navbar, senha e home.

Lucas contribuiu na frente de UX pré refactor, entregando toolbars de pesquisa e ordenação nas tabelas, a página "Meus médicos" para o paciente, ícones nos botões de vínculo e upload, melhorias de acessibilidade por teclado, extração de duplicações para utils e tipagens globais e limpeza de code smells de layout.

Do lado do vínculo, o frontend ganhou as páginas de solicitações enviadas para o médico e pendentes para o paciente, a ação de revogar acesso na `MedicosTable`, DTOs e services de solicitação de vínculo e os textos do `ModalVinculo` foram reescritos para o novo fluxo de solicitação com aprovação. Também houve um passe de qualidade: modais fecham antes do alerta para evitar sobreposição, o CPF foi escondido na listagem de pacientes disponíveis, o download de arquivo migrou para blob via `/raw` e o `FileUpload` ganhou opção "enviar outro".

Cobertura de testes no frontend ampliada para 38 testes passando.

**Commits relacionados:**

| Hash                                                                  | Data  | Autor | Descrição                                                                       |
| :-------------------------------------------------------------------- | :---- | :---- | :------------------------------------------------------------------------------ |
| [`860a5bd`](https://github.com/Diogo-Olivv/HealthTech/commit/860a5bd) | 07/07 | Diogo | feat (frontend): navbar dinamica + modal pesquisavel + DTO de upload de arquivo |
| [`03d7fc0`](https://github.com/Diogo-Olivv/HealthTech/commit/03d7fc0) | 07/07 | Lucas | feat(frontend): cria pagina Meus médicos para o paciente                        |
| [`6efdc27`](https://github.com/Diogo-Olivv/HealthTech/commit/6efdc27) | 07/07 | Lucas | feat(frontend): adicionar toolbars de pesquisa e ordenacao                      |
| [`274e17b`](https://github.com/Diogo-Olivv/HealthTech/commit/274e17b) | 07/07 | Lucas | style(frontend): melhorar acessibilidade de teclado (A11y)                      |
| [`477108f`](https://github.com/Diogo-Olivv/HealthTech/commit/477108f) | 07/07 | Lucas | feat(frontend): adiciona icones nos botões de vinculo e upload                  |
| [`56801e2`](https://github.com/Diogo-Olivv/HealthTech/commit/56801e2) | 07/07 | Lucas | refactor(frontend): extrair duplicacoes para utils e tipagens globais           |
| [`71db6f9`](https://github.com/Diogo-Olivv/HealthTech/commit/71db6f9) | 08/07 | Diogo | feat(frontend): CRUD de arquivos com visualização, edição e exclusão            |
| [`bafca36`](https://github.com/Diogo-Olivv/HealthTech/commit/bafca36) | 08/07 | Diogo | feat(frontend): seletor multi de especialidades e chips no listar médicos       |
| [`8c19437`](https://github.com/Diogo-Olivv/HealthTech/commit/8c19437) | 08/07 | Diogo | refactor(frontend): centraliza helpers HTTP, API_URL e token em src/lib         |
| [`d022e82`](https://github.com/Diogo-Olivv/HealthTech/commit/d022e82) | 08/07 | Diogo | feat(frontend): helpers de alerta usando sweetalert2                            |
| [`312fad4`](https://github.com/Diogo-Olivv/HealthTech/commit/312fad4) | 08/07 | Diogo | style(frontend): tema HealthTech para popups do sweetalert2                     |
| [`2744cb3`](https://github.com/Diogo-Olivv/HealthTech/commit/2744cb3) | 08/07 | Diogo | feat(frontend): validações e feedback de UX no login e cadastros                |
| [`921bb0b`](https://github.com/Diogo-Olivv/HealthTech/commit/921bb0b) | 09/07 | Diogo | feat(frontend): navbar confirma logout com sweetalert2                          |
| [`2616f7d`](https://github.com/Diogo-Olivv/HealthTech/commit/2616f7d) | 09/07 | Diogo | feat(frontend): tabs para trocar entre cadastro paciente/medico                 |
| [`fef685c`](https://github.com/Diogo-Olivv/HealthTech/commit/fef685c) | 09/07 | Diogo | feat(frontend): sucesso confirma com sweetalert antes do redirect               |
| [`7c0a663`](https://github.com/Diogo-Olivv/HealthTech/commit/7c0a663) | 09/07 | Diogo | feat(frontend): DTOs e services de solicitacao de vinculo                       |
| [`59656a2`](https://github.com/Diogo-Olivv/HealthTech/commit/59656a2) | 09/07 | Diogo | feat(frontend/paciente): pagina de solicitacoes pendentes                       |
| [`cf9f57a`](https://github.com/Diogo-Olivv/HealthTech/commit/cf9f57a) | 09/07 | Diogo | feat(frontend/medico): pagina de solicitacoes enviadas                          |
| [`153307d`](https://github.com/Diogo-Olivv/HealthTech/commit/153307d) | 09/07 | Diogo | feat(frontend/paciente): revogar acesso em MedicosTable                         |
| [`79176ae`](https://github.com/Diogo-Olivv/HealthTech/commit/79176ae) | 09/07 | Diogo | feat(frontend): viewport meta, lang pt-BR e evita zoom em input iOS             |
| [`952e0b9`](https://github.com/Diogo-Olivv/HealthTech/commit/952e0b9) | 09/07 | Diogo | style(frontend): modais viram bottom-sheet e botoes empilham no mobile          |
| [`0698924`](https://github.com/Diogo-Olivv/HealthTech/commit/0698924) | 09/07 | Diogo | style(frontend): responsividade mobile em dashboards e tabelas                  |
| [`43e4bae`](https://github.com/Diogo-Olivv/HealthTech/commit/43e4bae) | 09/07 | Diogo | fix(frontend): download de arquivo agora usa endpoint /raw via blob             |
| [`4f6d2ac`](https://github.com/Diogo-Olivv/HealthTech/commit/4f6d2ac) | 12/07 | Diogo | feat(api): route handlers de auth                                               |
| [`5d51040`](https://github.com/Diogo-Olivv/HealthTech/commit/5d51040) | 12/07 | Diogo | feat(api): proxy catch-all + serverFetch                                        |
| [`239199c`](https://github.com/Diogo-Olivv/HealthTech/commit/239199c) | 12/07 | Diogo | refactor(lib): api-config e http                                                |
| [`89dc12c`](https://github.com/Diogo-Olivv/HealthTech/commit/89dc12c) | 12/07 | Diogo | feat(hooks): useFetchData + features                                            |
| [`3861f90`](https://github.com/Diogo-Olivv/HealthTech/commit/3861f90) | 12/07 | Diogo | refactor(pages): consumir hooks                                                 |
| [`8174fc6`](https://github.com/Diogo-Olivv/HealthTech/commit/8174fc6) | 12/07 | Diogo | feat(medicos): SSR + client wrapper                                             |
| [`a6abfe8`](https://github.com/Diogo-Olivv/HealthTech/commit/a6abfe8) | 12/07 | Diogo | feat(user-type): add ADMIN role                                                 |
| [`d25fa80`](https://github.com/Diogo-Olivv/HealthTech/commit/d25fa80) | 12/07 | Diogo | feat(auth-guard): protege rota /admin                                           |
| [`a2fce07`](https://github.com/Diogo-Olivv/HealthTech/commit/a2fce07) | 12/07 | Diogo | feat(navbar): link admin                                                        |
| [`8684d25`](https://github.com/Diogo-Olivv/HealthTech/commit/8684d25) | 12/07 | Diogo | feat(admin): layout e index /admin                                              |
| [`03a9fb4`](https://github.com/Diogo-Olivv/HealthTech/commit/03a9fb4) | 12/07 | Diogo | feat(admin): tela /admin/auditoria                                              |
| [`6646f5e`](https://github.com/Diogo-Olivv/HealthTech/commit/6646f5e) | 12/07 | Diogo | feat(audit-table): componente da tabela                                         |
| [`6aca337`](https://github.com/Diogo-Olivv/HealthTech/commit/6aca337) | 12/07 | Diogo | feat(hook): useAuditLogs                                                        |
| [`fd2f77d`](https://github.com/Diogo-Olivv/HealthTech/commit/fd2f77d) | 12/07 | Diogo | feat(hook): useDebouncedValue                                                   |
| [`f976352`](https://github.com/Diogo-Olivv/HealthTech/commit/f976352) | 12/07 | Diogo | feat(admin): busca por usuário                                                  |

**Branch:** `develop`, `feat/crud-arquivos`, `feat/design-system`, `feat/responsividade-mobile`, `feat/admin-panel`, `feat/frontend-architecture`
**Issue(s):** #58

---

### Infraestrutura e Cloud

Diogo montou a esteira de CI/CD e segurança para o fim do ciclo. O `cloudbuild.yaml` ganhou etapas de lint com auto fix não bloqueante e testes que bloqueiam o deploy em caso de falha. O CodeQL foi configurado em workflow próprio, com varredura semanal e em cada pull request, cobrindo backend e frontend. O Dependabot foi configurado com grupos por ecossistema (`nestjs`, `typeorm`, `react`, `next` e `dev-dependencies`) e regra de ignore para major bumps de npm, o que evita ruído em atualizações que quebrariam compatibilidade sem revisão manual. Husky e lint-staged foram adicionados na raiz do monorepo para garantir formatação e lint mínimos antes do commit.

Ainda em infraestrutura houve três fixes de deploy relevantes: `_BACKEND_URL` foi atualizado para o hostname atual do Cloud Run, o `API_INTERNAL_URL` do frontend passou a apontar diretamente para o serviço backend interno e o `direct VPC egress` foi removido do frontend a cada deploy (não é necessário e estava adicionando latência inicial).

O PR [#93](https://github.com/Diogo-Olivv/HealthTech/pull/93) permanece aberto ao final do ciclo consolidando 11 dos 13 PRs individuais abertos pelo Dependabot num único batch, cobrindo backend (`@nestjs/*`, `typeorm`, `multer`, `@google-cloud/storage`, dev-dependencies), frontend (`next`, `react`, dev-dependencies), raiz (`lint-staged` 15→17) e GitHub Actions (`actions/checkout` v4→v7, `codeql-action` v3→v4). Os dois PRs deixados de fora são os bumps do Docker `node:22-alpine → node:26-alpine`, adiados até a saída do Node 24 LTS (Node 26 será _current_ e não LTS).

**Commits relacionados:**

| Hash                                                                  | Data  | Autor | Descrição                                                            |
| :-------------------------------------------------------------------- | :---- | :---- | :------------------------------------------------------------------- |
| [`59cc7ad`](https://github.com/Diogo-Olivv/HealthTech/commit/59cc7ad) | 08/07 | Diogo | chore: docker compose override para hot reload em dev                |
| [`0c768ce`](https://github.com/Diogo-Olivv/HealthTech/commit/0c768ce) | 09/07 | Diogo | fix: muda "-us" no cloudbuild                                        |
| [`2859cb7`](https://github.com/Diogo-Olivv/HealthTech/commit/2859cb7) | 09/07 | Diogo | fix: data-source desatualizado                                       |
| [`94abd58`](https://github.com/Diogo-Olivv/HealthTech/commit/94abd58) | 11/07 | Diogo | ci: adiciona lint/testes ao cloudbuild                               |
| [`8633cd4`](https://github.com/Diogo-Olivv/HealthTech/commit/8633cd4) | 11/07 | Diogo | ci: adiciona workflow CodeQL                                         |
| [`2d81b80`](https://github.com/Diogo-Olivv/HealthTech/commit/2d81b80) | 11/07 | Diogo | ci: configura Dependabot                                             |
| [`1865b9d`](https://github.com/Diogo-Olivv/HealthTech/commit/1865b9d) | 11/07 | Diogo | chore: adiciona husky + lint-staged                                  |
| [`4a6f7f3`](https://github.com/Diogo-Olivv/HealthTech/commit/4a6f7f3) | 12/07 | Diogo | chore(compose): API_INTERNAL_URL                                     |
| [`f5f3b9d`](https://github.com/Diogo-Olivv/HealthTech/commit/f5f3b9d) | 12/07 | Diogo | fix(deploy): API_INTERNAL_URL no front                               |
| [`8d48013`](https://github.com/Diogo-Olivv/HealthTech/commit/8d48013) | 12/07 | Diogo | fix(deploy): atualiza \_BACKEND_URL para hostname atual do Cloud Run |
| [`02f1dec`](https://github.com/Diogo-Olivv/HealthTech/commit/02f1dec) | 12/07 | Diogo | fix(deploy): remove direct VPC egress do frontend a cada deploy      |

**Branch:** `develop`, `feat/ci-cd-security`, `chore/deps-batch-2026-07`
**Issue(s):** -
**PRs:** [#70](https://github.com/Diogo-Olivv/HealthTech/pull/70) (merged), [#93](https://github.com/Diogo-Olivv/HealthTech/pull/93) (aberto)

---

### Governança e documentação

A documentação MkDocs recebeu uma refatoração completa, com reorganização das seções de arquitetura, tecnologias, modelagem e gestão. Uma nova seção `desenvolvimento/adr/` foi introduzida com índice, template e o **ADR-0001** documentando a decisão de rodar as migrations do TypeORM via Cloud Run Job `healthtech-migrations` em vez de embuti las no start do container. Uma segunda nova seção `desenvolvimento/padroes/` foi criada agrupando o guia de Git, o guia de código, o guia de review, o template de pull request e os templates de issue.

A rota `GET /audit/logs` foi documentada no README do backend, e o seed manual de admin ganhou instruções específicas para ambiente de desenvolvimento.

---

## Participação por Integrante

| Integrante | Commits | Issues principais                                  | Status    |
| :--------- | :-----: | :------------------------------------------------- | :-------- |
| Diogo      |   93    | #58 (admin panel), CI/CD, refactor arquitetura FE  | Concluída |
| Hugo       |    8    | #56, #57 (UserType ADMIN + endpoint audit logs)    | Concluída |
| Martin     |    3    | #54, #55 (auditoria de arquivos e vínculo)         | Concluída |
| Lucas      |    7    | UX de vínculo, tabelas com busca e ordenação, A11y | Concluída |
| Luíza      |    -    | -                                                  | -         |
| Gabriel    |    -    | -                                                  | -         |

---

## Bloqueios e Riscos

| Bloqueio / Risco                                          | Impacto | Responsável | Prazo |
| :-------------------------------------------------------- | :------ | :---------- | :---- |
| Retenção de logs de auditoria                             | Médio   | Diogo, Hugo | -     |
| Cold start do Cloud Run podendo afetar demo final         | Baixo   | Diogo       | Demo  |
| Node 26 (Docker) pendente até saída do Node 24 LTS        | Baixo   | Diogo       | -     |
| Fechar 13 PRs individuais do Dependabot após merge do #93 | Baixo   | Diogo       | -     |

---

## Pendências para a Próxima Semana

> Fim do ciclo Fase 3. Foco agora em demo final, retro e fechamento do repositório.

| Tarefa                                                                 | Responsável | Issue | Prioridade |
| :--------------------------------------------------------------------- | :---------- | :---- | :--------- |
| Implementar retenção de logs de auditoria com scheduler                | Diogo, Hugo | -     | Média      |
| Pré aquecer Cloud Run antes da demo para mitigar cold start            | Diogo       | -     | Alta       |
| Ensaio da demo ponta a ponta (paciente → vínculo → upload → auditoria) | Todos       | -     | Alta       |
| Merge do batch Dependabot (#93) e fechamento dos PRs individuais       | Diogo       | -     | Média      |
| Revisão final da documentação MkDocs e do ADR-0001                     | Diogo       | -     | Média      |

---

## Métricas finais do ciclo

- **Commits na semana (sem merges):** ~110
- **PRs mergeados na semana:** 10 (#64, #65, #66, #67, #68, #69, #70, #71, #72, #79)
- **PRs abertos ao fim do ciclo:** 1 batch consolidado (#93)
- **Testes passando:** 116 no backend, 38 no frontend

---

_Documento preenchido por: Diogo_
