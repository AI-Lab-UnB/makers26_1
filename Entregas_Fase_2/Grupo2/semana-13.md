# Semana 13

> **Status:** Concluída
> **Período:** 30/06/2026 a 06/07/2026
> **Semana do ciclo:** 13 / 14
> **Fase atual:** Fase 3, Deploy e Demo
> **Responsável pelo preenchimento:** Diogo

---

## Objetivo da Semana

Fechar a camada de auditoria com o interceptor global e o decorator `@Audit` aplicado às rotas de autenticação, entregar os fluxos de upload e listagem de arquivos no frontend, habilitar o vínculo médico paciente ponta a ponta e estabilizar o deploy na Cloud Run na região us central para viabilizar a demo final.

---

## Entregas Realizadas

### Backend

Martin entregou o `AuditInterceptor` global (#52), que lê a metadata configurada no handler através do decorator `@Audit` e registra o resultado da requisição: `SUCCESS` no operador `tap` do RxJS e `FAILURE` no `catchError`, sempre re lançando a exceção original para que o `ExceptionFilter` padrão continue tratando a resposta HTTP. Essa separação garante que a auditoria seja não intrusiva, ou seja, uma falha na persistência do log jamais compromete o comportamento observável da API.

Diogo conduziu o refactor da API do decorator, consolidando a forma de chamada em torno de um único evento por ação de negócio no formato `{ evento, extractRecursoId }`. O campo `status` da própria entidade `AuditLog` passou a ser a fonte única de verdade para o desfecho da operação, o que permitiu remover o valor `LOGIN_FALHA` do enum, inclusive no banco de produção. A consulta equivalente agora é feita via `WHERE tipoEvento = 'LOGIN' AND status = 'FAILURE'`, resultado direto do princípio de simetria adotado na Semana 12 ao modelar a entidade.

Martin também aplicou a auditoria nas rotas de login e cadastro (#53), corrigiu a tipagem do TypeORM para os campos `nullable` da entidade (`userId`, `recursoId`, `ipOrigem`, `userAgent`), tornando explícito o fato de que eventos anônimos como uma tentativa de login com credenciais inexistentes devem persistir mesmo sem `userId` associado.

Lucas criou uma nova rota de listagem de prontuário que retorna os arquivos do paciente vinculado ao médico autenticado, apoiando a nova tela de prontuário do frontend. Além disso, o retorno do CPF foi adicionado ao payload para permitir a exibição correta na tela de upload.

**Commits relacionados:**

| Hash                                                                  | Data  | Autor  | Descrição                                                                            |
| :-------------------------------------------------------------------- | :---- | :----- | :----------------------------------------------------------------------------------- |
| [`52b7ac3`](https://github.com/Diogo-Olivv/HealthTech/commit/52b7ac3) | 01/07 | Diogo  | fix: Ajuste de servidor para US + audit-log uuid                                     |
| [`a5ef58b`](https://github.com/Diogo-Olivv/HealthTech/commit/a5ef58b) | 01/07 | Diogo  | fix: ajuste audit-log uuid                                                           |
| [`bddb0f6`](https://github.com/Diogo-Olivv/HealthTech/commit/bddb0f6) | 04/07 | Martin | fix(audit): corrige tipagem do TypeORM para campos nullable na entidade AuditLog     |
| [`0160041`](https://github.com/Diogo-Olivv/HealthTech/commit/0160041) | 04/07 | Martin | feat(audit): implementa AuditInterceptor global e decorator (Resolve #52)            |
| [`de6b747`](https://github.com/Diogo-Olivv/HealthTech/commit/de6b747) | 04/07 | Martin | feat(users): aplica auditoria nas rotas de login e cadastro (Resolve #53)            |
| [`e7659c5`](https://github.com/Diogo-Olivv/HealthTech/commit/e7659c5) | 06/07 | Lucas  | feat(backend): criar rota para listar prontuário                                     |
| [`9c193b1`](https://github.com/Diogo-Olivv/HealthTech/commit/9c193b1) | 06/07 | Diogo  | refactor(audit): refactor da API + forma de chamar                                   |
| [`0da5e7c`](https://github.com/Diogo-Olivv/HealthTech/commit/0da5e7c) | 06/07 | Diogo  | fix: remove LOGIN_FALHA do enum no banco de produção                                 |
| [`a0ce9aa`](https://github.com/Diogo-Olivv/HealthTech/commit/a0ce9aa) | 06/07 | Diogo  | Merge branch 'develop' into feat/auditoria                                           |
| [`40fbb4a`](https://github.com/Diogo-Olivv/HealthTech/commit/40fbb4a) | 06/07 | Diogo  | Merge pull request #65 from Diogo-Olivv/feat/auditoria                               |

**Branch:** `feat/auditoria`
**Issue(s):** #52, #53
**PRs:** [#65](https://github.com/Diogo-Olivv/HealthTech/pull/65) (merged)

---

### Frontend

Lucas conduziu a maior entrega individual do ciclo, com 25 commits que consolidaram três frentes simultâneas.

Na frente de arquivos (#30, #32), a tela de upload foi finalmente entregue com implementação em CSS Modules, funcionalidade de arrastar e soltar, isolamento total do CSS do componente e separação da rota do dashboard. A tela de listagem de arquivos do médico foi entregue com filtro pelo médico autenticado, e a tela de prontuário passou a consumir a nova rota do backend.

Na frente de vínculo médico paciente (#29), o fluxo ficou funcional ponta a ponta: botão de vincular ajustado, correção da violação das regras de hooks no modal de vínculo e tabela de pacientes vinculados exibindo data de nascimento. O painel de resumo do médico passou a exibir contagens reais, substituindo os placeholders herdados de sprints anteriores.

Na frente de autenticação e navegação, o `AuthContext` foi criado e o `AuthGuard` refatorado para proteger rotas por tipo de usuário. O token deixou de ser parametrizado nas chamadas de API, passando a fluir pelo contexto, e os retornos das chamadas foram tipados explicitamente. A navbar (#62) foi concluída com informações reais do usuário, menu mobile, novos links e substituição de HTML nativo por componentes Next.js para ganho de performance.

Ainda houve uma passagem de qualidade abrangente: `alert` nativo substituído pelo componente `FeedbackMessage`, comentários redundantes e blocos inativos removidos, nomenclatura padronizada para inglês e diversos ajustes de UI.

**Commits relacionados:**

| Hash                                                                  | Data  | Autor | Descrição                                                                                             |
| :-------------------------------------------------------------------- | :---- | :---- | :---------------------------------------------------------------------------------------------------- |
| [`80cfe91`](https://github.com/Diogo-Olivv/HealthTech/commit/80cfe91) | 01/07 | Lucas | fix(Button Modal): botão de vincular Paciente                                                         |
| [`d252699`](https://github.com/Diogo-Olivv/HealthTech/commit/d252699) | 01/07 | Lucas | feat(NavBar): Informações reais do usuário                                                            |
| [`bfaf537`](https://github.com/Diogo-Olivv/HealthTech/commit/bfaf537) | 04/07 | Lucas | feat: ajuste na navbar e apaga o oii                                                                  |
| [`0f0b399`](https://github.com/Diogo-Olivv/HealthTech/commit/0f0b399) | 04/07 | Lucas | feat(backend,frontend): Funcionalidade de vincular médico com paciente                                |
| [`9e1e570`](https://github.com/Diogo-Olivv/HealthTech/commit/9e1e570) | 04/07 | Lucas | feat: Tabela de pacientes vinculados funcionando                                                      |
| [`9b73878`](https://github.com/Diogo-Olivv/HealthTech/commit/9b73878) | 04/07 | Lucas | feat: data de nascimento do paciente na tabela de pacientes                                           |
| [`ad14933`](https://github.com/Diogo-Olivv/HealthTech/commit/ad14933) | 04/07 | Lucas | feat: painel contagem real no painel de resumo do médico                                              |
| [`6997b9e`](https://github.com/Diogo-Olivv/HealthTech/commit/6997b9e) | 04/07 | Lucas | fix: descomentei o leitor de status da página                                                         |
| [`0f88c30`](https://github.com/Diogo-Olivv/HealthTech/commit/0f88c30) | 05/07 | Lucas | fix(medico): resolve erro que escondia botão de vincular pacientes quando a lista estava vazia        |
| [`55e716f`](https://github.com/Diogo-Olivv/HealthTech/commit/55e716f) | 05/07 | Lucas | refactor: melhora nomenclatura de componentes para inglês e remove código não utilizado               |
| [`83b79cb`](https://github.com/Diogo-Olivv/HealthTech/commit/83b79cb) | 05/07 | Lucas | chore: remove comentários redundantes e blocos de código inativos                                     |
| [`3128520`](https://github.com/Diogo-Olivv/HealthTech/commit/3128520) | 05/07 | Lucas | fix(ui): troca html nativo por componentes nextjs para performance; arruma iniciais; corrige link nav |
| [`d533b4f`](https://github.com/Diogo-Olivv/HealthTech/commit/d533b4f) | 05/07 | Lucas | fix(modal): corrige violação das regras de hooks no modal de vínculo                                  |
| [`c2d3c1d`](https://github.com/Diogo-Olivv/HealthTech/commit/c2d3c1d) | 06/07 | Lucas | feat: adiciona AuthGuard para proteger rotas por tipo de usuario                                      |
| [`f4d65f3`](https://github.com/Diogo-Olivv/HealthTech/commit/f4d65f3) | 06/07 | Lucas | refactor: conserta rota raiz do dashboard e separa tela de upload                                     |
| [`065ff00`](https://github.com/Diogo-Olivv/HealthTech/commit/065ff00) | 06/07 | Lucas | feat: cria tela de listagem de arquivos do medico                                                     |
| [`1577e8c`](https://github.com/Diogo-Olivv/HealthTech/commit/1577e8c) | 06/07 | Lucas | refactor: remove token parametrizado e tipa retornos de API                                           |
| [`2c8ee1c`](https://github.com/Diogo-Olivv/HealthTech/commit/2c8ee1c) | 06/07 | Lucas | feat: implementa upload de arquivos, estilos CSS Modules e retorno de CPF no backend                  |
| [`3870b17`](https://github.com/Diogo-Olivv/HealthTech/commit/3870b17) | 06/07 | Lucas | feat: funcionalidade de arrastar e soltar arquivo no upload                                           |
| [`0b26c64`](https://github.com/Diogo-Olivv/HealthTech/commit/0b26c64) | 06/07 | Lucas | feat(auth): implementar AuthContext e refatorar AuthGuard para proteção de rotas                      |
| [`1e9c6ba`](https://github.com/Diogo-Olivv/HealthTech/commit/1e9c6ba) | 06/07 | Lucas | refactor(ui): melhoria na NavBar com menu mobile e novos links para novas páginas                     |
| [`a25ccc5`](https://github.com/Diogo-Olivv/HealthTech/commit/a25ccc5) | 06/07 | Lucas | fix(arquivos): trava listagem de arquivos por médico e isola css do componente de upload              |
| [`c1393ee`](https://github.com/Diogo-Olivv/HealthTech/commit/c1393ee) | 06/07 | Lucas | refactor(ui): remove alert nativo, implementa FeedbackMessage e limpa código redundante               |
| [`9c16e70`](https://github.com/Diogo-Olivv/HealthTech/commit/9c16e70) | 06/07 | Lucas | feat(frontend): implementar tela de prontuário                                                        |
| [`6bdfdaa`](https://github.com/Diogo-Olivv/HealthTech/commit/6bdfdaa) | 06/07 | Lucas | chore: troca de nome de caminho                                                                       |

**Branch:** `develop`, `30-frontend-tela-de-upload-de-arquivos`, `feat/Tela-de-listagem-de-arquivos`
**Issue(s):** #29, #30, #32, #62

---

### Infraestrutura e Cloud

Diogo migrou o deploy da Cloud Run para a região us central com o objetivo de reduzir a latência percebida durante a demo e evitar picos de cold start em regiões menos utilizadas. Os caminhos do `cloudbuild.yaml` foram corrigidos após a reestruturação do repositório, e o schema da tabela `audit-log` recebeu ajustes de uuid para compatibilidade com o banco de produção.

**Commits relacionados:**

| Hash                                                                  | Data  | Autor | Descrição                                        |
| :-------------------------------------------------------------------- | :---- | :---- | :----------------------------------------------- |
| [`52b7ac3`](https://github.com/Diogo-Olivv/HealthTech/commit/52b7ac3) | 01/07 | Diogo | fix: Ajuste de servidor para US + audit-log uuid |
| [`79a70b6`](https://github.com/Diogo-Olivv/HealthTech/commit/79a70b6) | 01/07 | Diogo | fix: Deploy para us-central                      |
| [`ba11b40`](https://github.com/Diogo-Olivv/HealthTech/commit/ba11b40) | 01/07 | Diogo | fix: cloudbuild paths                            |

**Branch:** `develop`, `feat/auditoria`
**Issue(s):** -

---

## Participação por Integrante

| Integrante | Commits | Issues principais                          | Status       |
| :--------- | :-----: | :----------------------------------------- | :----------- |
| Diogo      |    7    | #52 (refactor API), deploy Cloud Run       | Concluída    |
| Hugo       |    -    | -                                          | -            |
| Martin     |    3    | #52, #53 (interceptor + auth)              | Concluída    |
| Lucas      |   25    | #29, #30, #32, #62 (upload, listagem, nav) | Concluída    |
| Luíza      |    -    | -                                          | -            |
| Gabriel    |    -    | -                                          | -            |

---

## Bloqueios e Riscos

| Bloqueio / Risco                                   | Impacto                                          | Responsável           | Prazo |
| :------------------------------------------------- | :----------------------------------------------- | :-------------------- | :---- |
| Auditoria de arquivos e vínculo (#54, #55)         | Médio, cobertura de auditoria incompleta         | Hugo, Martin          | 13/07 |
| UserType ADMIN + endpoint/tela de logs (#56 a #58) | Alto, painel de admin ainda sem visualização     | Hugo, Martin, Gabriel | 13/07 |

---

## Pendências para a Próxima Semana

> Semana 14 / 14, foco em fechamento da auditoria nas rotas restantes, painel admin e preparação da demo final.

| Tarefa                                        | Responsável    | Issue | Prioridade |
| :-------------------------------------------- | :------------- | :---- | :--------- |
| Auditoria em rotas de arquivos                | Hugo, Martin   | #54   | Alta       |
| Auditoria em rotas de vínculo médico paciente | Hugo, Martin   | #55   | Alta       |
| Criar UserType ADMIN e seed                   | Hugo, Martin   | #56   | Alta       |
| Endpoint de consulta de logs (admin)          | Hugo, Martin   | #57   | Média      |
| Tela de consulta de logs (admin)              | Gabriel, Lucas | #58   | Média      |
| Preparação da demo final e revisão docs       | Todos          | -     | Alta       |

---

_Documento preenchido por: Diogo_
