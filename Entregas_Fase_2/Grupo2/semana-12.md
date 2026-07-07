# Semana 12

> **Status:** Concluída
> **Período:** 23/06/2026 a 29/06/2026
> **Semana do ciclo:** 12 / 14
> **Fase atual:** Fase 2, Desenvolvimento
> **Responsável pelo preenchimento:** Diogo

---

## Objetivo da Semana

Estabelecer a base da camada de auditoria, ou seja, a entidade, o service e o módulo global, de modo que o interceptor a ser criado na Semana 13 tenha um alvo de persistência estável. Em paralelo, avançar a tela de upload de arquivos (pendência arrastada da Semana 11) e entregar a estrutura da navbar global do frontend, unificando a navegação entre os fluxos de paciente e médico.

---

## Entregas Realizadas

### Backend

Hugo entregou a base da auditoria em duas frentes coordenadas. Na frente de modelagem (#50), a entidade `AuditLog` foi criada com TypeORM contendo `id` (uuid), `userId`, `tipoEvento` (enum `TipoEventoAuditoria`), `recursoId`, `status` (`SUCCESS`/`FAILURE`), `ipOrigem`, `userAgent` e `timestamp` (`CreateDateColumn`). O par `status` + `tipoEvento` foi escolhido deliberadamente sobre a alternativa de eventos separados para sucesso e falha, porque permite consultas simétricas e reduz a explosão de valores do enum.

Na frente de serviço (#51), o `AuditLogService` foi implementado dentro de um módulo global (`@Global()`), expondo o método `registrar()` que persiste o log no banco e, em paralelo, emite via `Logger` do NestJS para stdout, garantindo que, mesmo em uma eventual falha de persistência, o evento permaneça rastreável nos logs do Cloud Run. Falhas do próprio `registrar()` são absorvidas silenciosamente para nunca derrubar a requisição de negócio original, decisão que mantém a auditoria como camada não intrusiva.

Diogo executou a migração de `synchronize: true` para migrations explícitas, trabalho preparatório crítico para deploy seguro em produção, e corrigiu o `docker-compose.yml` que estava impedindo o subimento correto de todos os serviços no ambiente local, destravando o restante do time.

**Commits relacionados:**

| Hash                                                                  | Data  | Autor     | Descrição                                                               |
| :-------------------------------------------------------------------- | :---- | :-------- | :---------------------------------------------------------------------- |
| [`f9a8873`](https://github.com/Diogo-Olivv/HealthTech/commit/f9a8873) | 22/06 | Diogo     | refactor(db): migra synchronize para migrations                         |
| [`b8c0f20`](https://github.com/Diogo-Olivv/HealthTech/commit/b8c0f20) | 22/06 | Diogo     | refactor(db): Adiciona migrations restantes + refatoração do teste e2e  |
| [`36ff8c9`](https://github.com/Diogo-Olivv/HealthTech/commit/36ff8c9) | 24/06 | Hugo Rosa | (feat) Entidade audit-log criado (#50)                                  |
| [`11c7ea6`](https://github.com/Diogo-Olivv/HealthTech/commit/11c7ea6) | 24/06 | Hugo Rosa | (feat) Audit-log migrations criado (#50)                                |
| [`8962630`](https://github.com/Diogo-Olivv/HealthTech/commit/8962630) | 24/06 | Hugo Rosa | (feat) Audit Module Adicionado (#51)                                    |
| [`dcede63`](https://github.com/Diogo-Olivv/HealthTech/commit/dcede63) | 24/06 | Hugo Rosa | (feat) Service adicionado (#51)                                         |
| [`42506f8`](https://github.com/Diogo-Olivv/HealthTech/commit/42506f8) | 24/06 | Hugo Rosa | (test) Testes adicionados (#50, #51)                                    |
| [`56631ec`](https://github.com/Diogo-Olivv/HealthTech/commit/56631ec) | 24/06 | Hugo Rosa | (test) Testes adicionados (#50, #51)                                    |
| [`6300f7a`](https://github.com/Diogo-Olivv/HealthTech/commit/6300f7a) | 24/06 | Hugo Rosa | (feat) App module alterado (#50, #51)                                   |
| [`60e1c3e`](https://github.com/Diogo-Olivv/HealthTech/commit/60e1c3e) | 27/06 | Diogo     | fix: Ajusta setup-inicial do projeto (docker compose) inicia tudo agora |

**Branch:** `feat/auditoria`
**Issue(s):** #50, #51, #52 (em andamento)
**PRs:** -

---

### Frontend

Luíza iniciou a navbar global (#62) com estrutura do componente `Navbar.tsx`, estilização, layout de dashboard e correções sucessivas de HTML/CSS. A decisão de tratar a navbar como componente reutilizável, em vez de embutir em cada layout, só foi consolidada no fim da semana, quando Lucas fez a extração final. Até lá, o componente conviveu com implementações paralelas, o que explica alguns dos vaivéns de HTML/CSS visíveis nos commits.

Lucas conduziu a evolução da tela de upload de arquivos em conjunto com uma passagem larga pela padronização do CSS: adição do CSS de dashboard, mensagens de erro específicas por perfil, ajuste do layout de login/registro, min widths defensivos e limpeza de linhas comentadas. A troca de `<body>` por `<div>` no wrapper (`9a3f032`) foi uma correção sutil que evitava conflito de estilos em rotas com layouts aninhados no Next.js.

Do lado organizacional, a tela de upload (#30) permaneceu em andamento no encerramento da semana, arrastando para a Semana 13 uma pendência que já vinha da Semana 11, sinal de que a complexidade do drag and drop e da integração com o backend foi subestimada no planejamento original.

**Commits relacionados:**

| Hash                                                                  | Data  | Autor | Descrição                                                                         |
| :-------------------------------------------------------------------- | :---- | :---- | :-------------------------------------------------------------------------------- |
| [`f20a545`](https://github.com/Diogo-Olivv/HealthTech/commit/f20a545) | 21/06 | Luíza | feat: adiciona estrutura do navbar (#62)                                          |
| [`21dc8f8`](https://github.com/Diogo-Olivv/HealthTech/commit/21dc8f8) | 21/06 | Luíza | style: estiliza navbar (#62)                                                      |
| [`1619d3d`](https://github.com/Diogo-Olivv/HealthTech/commit/1619d3d) | 23/06 | Lucas | feat: adiciona css dashboard, atualiza mensagem de erro para cada usuário (#30)   |
| [`802f9c6`](https://github.com/Diogo-Olivv/HealthTech/commit/802f9c6) | 23/06 | Lucas | fix: ajuste html de layout e padroniza css do layout de login e register (#30)    |
| [`18520d1`](https://github.com/Diogo-Olivv/HealthTech/commit/18520d1) | 23/06 | Lucas | refactor: exclui linhas comentadas desnecessárias (#30)                           |
| [`2e91348`](https://github.com/Diogo-Olivv/HealthTech/commit/2e91348) | 23/06 | Luíza | feat: adiciona pasta dashboard e move arquivos (#62)                              |
| [`cb49b90`](https://github.com/Diogo-Olivv/HealthTech/commit/cb49b90) | 23/06 | Luíza | fix: html navbar (#62)                                                            |
| [`076f958`](https://github.com/Diogo-Olivv/HealthTech/commit/076f958) | 25/06 | Lucas | add(css): add min-width no login e register (#30)                                 |
| [`16ac241`](https://github.com/Diogo-Olivv/HealthTech/commit/16ac241) | 25/06 | Lucas | fix(frontend): css das de login, registro e global.css; exclusão de linhas vazias |
| [`16c0d93`](https://github.com/Diogo-Olivv/HealthTech/commit/16c0d93) | 26/06 | Luíza | fix: css navbar (#62)                                                             |
| [`de62926`](https://github.com/Diogo-Olivv/HealthTech/commit/de62926) | 26/06 | Luíza | fix: navbar corrige html (#62)                                                    |
| [`9a3f032`](https://github.com/Diogo-Olivv/HealthTech/commit/9a3f032) | 27/06 | Lucas | fix: troca body por div, para evitar uso duplicado (#30)                          |
| [`e4f8969`](https://github.com/Diogo-Olivv/HealthTech/commit/e4f8969) | 27/06 | Lucas | fix: ajuste organização do codigo (#30)                                           |
| [`a40b483`](https://github.com/Diogo-Olivv/HealthTech/commit/a40b483) | 29/06 | Lucas | feat: transformei NavBar em component (#62)                                       |
| [`d4f1461`](https://github.com/Diogo-Olivv/HealthTech/commit/d4f1461) | 29/06 | Lucas | fix: ajuste na tela de registro e login (#30)                                     |
| [`3dee3f1`](https://github.com/Diogo-Olivv/HealthTech/commit/3dee3f1) | 29/06 | Lucas | fix: padroniza a identação de todos os arquivos tsx e css                         |

**Branch:** `feat/navbar`, `30-frontend-tela-de-upload-de-arquivos`
**Issue(s):** #30 (em andamento), #62 (em andamento)
**PRs:** -

---

### Documentação

README reorganizado com Code of Conduct e CONTRIBUTING separados em arquivos próprios, alinhando o repositório ao padrão OSS que a documentação em GitHub Pages já seguia. Ata da reunião de 23/06 registrada.

**Commits relacionados:**

| Hash                                                                  | Data  | Autor | Descrição                                                   |
| :-------------------------------------------------------------------- | :---- | :---- | :---------------------------------------------------------- |
| [`dda9fa1`](https://github.com/Diogo-Olivv/HealthTech/commit/dda9fa1) | 22/06 | Diogo | docs: Atualiza README + separa CodeOfConduct e Contributing |
| [`8f30f7d`](https://github.com/Diogo-Olivv/HealthTech/commit/8f30f7d) | 23/06 | Lucas | feat: ata reunião 2026-06-23                                |

**Branch:** `docs`
**Issue(s):** -

---

## Participação por Integrante

| Integrante | Commits | Issues principais         | Status       |
| :--------- | :-----: | :------------------------ | :----------- |
| Diogo      |    3    | db migrations, docker fix | Concluída    |
| Hugo       |    7    | #50, #51 (auditoria base) | Concluída    |
| Martin     |    -    | -                         | -            |
| Lucas      |   11    | #30, #62 (upload, navbar) | Em andamento |
| Luíza      |    6    | #62 (navbar)              | Em andamento |
| Gabriel    |    -    | -                         | -            |

---

## Bloqueios e Riscos

| Bloqueio / Risco                        | Impacto                                     | Responsável           | Prazo |
| :-------------------------------------- | :------------------------------------------ | :-------------------- | :---- |
| #52 (interceptor) ainda não iniciado    | Médio, bloqueia issues #53 a #55            | Hugo, Martin          | 29/06 |
| Tela de upload (#30) pendente desde s11 | Alto, fluxo completo de arquivo bloqueado   | Lucas, Luíza, Gabriel | 29/06 |

---

## Pendências para a Próxima Semana

> Semana 13 / 14, foco em interceptor de auditoria e aplicação da auditoria nas rotas.

| Tarefa                                        | Responsável    | Issue | Prioridade |
| :-------------------------------------------- | :------------- | :---- | :--------- |
| AuditInterceptor e decorator @Audit           | Hugo, Martin   | #52   | Alta       |
| Auditoria em rotas de autenticação e cadastro | Hugo, Martin   | #53   | Alta       |
| Auditoria em rotas de arquivos                | Hugo, Martin   | #54   | Alta       |
| Auditoria em rotas de vínculo médico paciente | Hugo, Martin   | #55   | Alta       |
| Criar UserType ADMIN e seed                   | Hugo, Martin   | #56   | Alta       |
| Concluir tela de upload de arquivos           | Lucas, Luíza   | #30   | Alta       |
| Concluir navbar global                        | Lucas, Luíza   | #62   | Alta       |
| Endpoint de consulta de logs (admin)          | Hugo, Martin   | #57   | Média      |
| Tela de consulta de logs (admin)              | Gabriel, Lucas | #58   | Média      |

---

_Documento preenchido por: Diogo_
