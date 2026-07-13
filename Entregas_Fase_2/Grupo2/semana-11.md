# Semana 11

> **Status:** Concluída
> **Período:** 16/06/2026 a 22/06/2026
> **Semana do ciclo:** 11 / 14
> **Fase atual:** Fase 2, Desenvolvimento
> **Responsável pelo preenchimento:** Diogo

---

## Objetivo da Semana

Fechar o ciclo de gerenciamento de arquivos, entregando o endpoint de upload com integração ao Google Cloud Storage, o endpoint de listagem com isolamento por perfil e as telas de listagem no frontend para paciente e médico. Em paralelo, iniciar o planejamento da camada de auditoria, requisito obrigatório da Fase 2, para destravar o desenvolvimento nas semanas seguintes.

---

## Entregas Realizadas

### Backend

Semana focada em consolidar o módulo de arquivos como funcionalidade central de negócio. Martin entregou o endpoint `POST /arquivos/upload` (#28) com validação de formato, tamanho e verificação obrigatória de vínculo médico paciente antes de persistir o metadado. A integração com o `StorageService` foi conectada de ponta a ponta, e o commit do metadado só ocorre depois do upload físico confirmado, evitando registros órfãos. A cobertura de testes acompanhou a entrega: testes E2E validando o fluxo HTTP completo e testes unitários cobrindo controller e service.

Hugo entregou o endpoint `GET /arquivos` (#32) aplicando o mesmo princípio de isolamento por tipo já introduzido na Semana 10: paciente recebe apenas os próprios arquivos; médico recebe apenas os arquivos de pacientes vinculados, filtrando via a tabela `MedicoPaciente`. Um DTO estrito de saída foi mantido para garantir que `caminhoStorage` continue omitido nas respostas, com teste automatizado verificando essa omissão.

Diogo adicionou um driver local de armazenamento como fallback do `StorageService`, permitindo desenvolvimento sem credenciais GCS ativas e reduzindo o custo dos ciclos locais. No mesmo eixo de integração, removeu a página `/dashboard` remanescente e ajustou o redirect pós login para direcionar direto para `/paciente` ou `/medico` conforme o campo `tipo` do JWT, alinhando com a decisão arquitetural da Semana 10.

**Commits relacionados:**

| Hash                                                                  | Data  | Autor     | Descrição                                                                       |
| :-------------------------------------------------------------------- | :---- | :-------- | :------------------------------------------------------------------------------ |
| [`e06a2ee`](https://github.com/Diogo-Olivv/HealthTech/commit/e06a2ee) | 16/06 | martinnho | feat(arquivos): implementa endpoint POST /arquivos/upload (#28)                 |
| [`874fabd`](https://github.com/Diogo-Olivv/HealthTech/commit/874fabd) | 16/06 | martinnho | test(arquivos): adiciona testes E2E do endpoint de upload (#28)                 |
| [`e566471`](https://github.com/Diogo-Olivv/HealthTech/commit/e566471) | 16/06 | martinnho | test(arquivos): adiciona testes unitários do service e controller               |
| [`b26f4de`](https://github.com/Diogo-Olivv/HealthTech/commit/b26f4de) | 16/06 | Hugo Rosa | (feat) Endpoint GET /arquivos com guards                                        |
| [`2ece66b`](https://github.com/Diogo-Olivv/HealthTech/commit/2ece66b) | 16/06 | Hugo Rosa | (feat) Adicionado testes automatizados                                          |
| [`4eb7153`](https://github.com/Diogo-Olivv/HealthTech/commit/4eb7153) | 16/06 | Hugo Rosa | (feat) DTO estrito de saída                                                     |
| [`0efa708`](https://github.com/Diogo-Olivv/HealthTech/commit/0efa708) | 17/06 | martinnho | fix(arquivos): corrige retorno do serviço e ajusta configuração de testes       |
| [`3281131`](https://github.com/Diogo-Olivv/HealthTech/commit/3281131) | 17/06 | Diogo     | feat(storage): adiciona driver local para upload de arquivos em desenvolvimento |
| [`b613929`](https://github.com/Diogo-Olivv/HealthTech/commit/b613929) | 17/06 | Diogo     | refactor(auth): remove página de dashboard e redireciona login conforme tipo    |
| [`cc7bd5b`](https://github.com/Diogo-Olivv/HealthTech/commit/cc7bd5b) | 17/06 | Diogo     | fix(arquivos): resolve erros de sintaxe que impediam build do backend           |
| [`616455c`](https://github.com/Diogo-Olivv/HealthTech/commit/616455c) | 17/06 | Diogo     | chore: adiciona caso de teste manual de arquivos                                |

**Branch:** `feat/upload-arquivos`, `feat/listagem-arquivos`
**Issue(s):** #28, #32
**PRs:** #47 (listagem-arquivos), #48 (upload-arquivos)

---

### Frontend

Gabriel liderou a criação das telas de listagem de arquivos para paciente (`/paciente/arquivos`) e médico (`/medico/arquivos`) (#33). Cada tela consome o `GET /arquivos` e exibe nome do arquivo, tipo, data de upload e médico responsável. Como o próprio backend cuida do filtro por perfil, o frontend permanece agnóstico ao tipo de usuário no ponto de consumo, o que reduz a superfície de erro de autorização no cliente.

Lucas conduziu a evolução da identidade visual: cores da paleta oficial centralizadas em `globals.css`, logos e favicon substituídos, e ajustes de responsividade no login e no cadastro. Diogo fez uma passagem transversal extraindo componentes e ícones compartilhados para a nova pasta comum e realinhando o contrato entre frontend e backend do módulo de arquivos, prevenindo divergência de nomes de campos que já havia sido custosa na Semana 10.

**Commits relacionados:**

| Hash                                                                  | Data  | Autor          | Descrição                                                        |
| :-------------------------------------------------------------------- | :---- | :------------- | :--------------------------------------------------------------- |
| [`51c4e09`](https://github.com/Diogo-Olivv/HealthTech/commit/51c4e09) | 15/06 | Gabriel Robson | feat(arquivos): criar páginas de listagem para médico e paciente |
| [`d5d4751`](https://github.com/Diogo-Olivv/HealthTech/commit/d5d4751) | 16/06 | Gabriel Robson | Refatora página de arquivos do médico conforme feedback do PR    |
| [`c053065`](https://github.com/Diogo-Olivv/HealthTech/commit/c053065) | 16/06 | lucaspaulaleal | refactor(globals.css): atualiza cores da identidade visual       |
| [`f8b8cb5`](https://github.com/Diogo-Olivv/HealthTech/commit/f8b8cb5) | 16/06 | lucaspaulaleal | refactor(styles): atualiza cores e coloca logo nas páginas       |
| [`62e104b`](https://github.com/Diogo-Olivv/HealthTech/commit/62e104b) | 16/06 | lucaspaulaleal | refactor(public): troca das logos e favicon                      |
| [`9ccb68d`](https://github.com/Diogo-Olivv/HealthTech/commit/9ccb68d) | 17/06 | lucaspaulaleal | feat(layout): adiciona layout no login e registro                |
| [`3ed786e`](https://github.com/Diogo-Olivv/HealthTech/commit/3ed786e) | 17/06 | lucaspaulaleal | refactor(register): atualiza estilos e melhora responsividade    |
| [`b9c9aac`](https://github.com/Diogo-Olivv/HealthTech/commit/b9c9aac) | 17/06 | Diogo          | refactor(frontend): extrai componentes e ícones compartilhados   |
| [`06ae755`](https://github.com/Diogo-Olivv/HealthTech/commit/06ae755) | 17/06 | Diogo          | refactor(arquivos): alinha contrato entre frontend e backend     |

**Branch:** `feat/Tela-de-listagem-de-arquivos`
**Issue(s):** #33
**PRs:** #49 (Tela-de-listagem-de-arquivos)

---

### Documentação

Planejamento completo da camada de auditoria consolidado em `docs/auditoria/`: histórias de usuário, dependências entre issues (#34 a #44) e critérios de teste. Esse trabalho de preparação foi crítico para permitir que a Semana 12 começasse já com a entidade e o service atacáveis em paralelo. Ata da reunião de 17/06 registrada.

**Branch:** `docs`
**Issue(s):** -

---

## Participação por Integrante

| Integrante | Commits | Issues principais                   | Status    |
| :--------- | :-----: | :---------------------------------- | :-------- |
| Diogo      |    6    | #28, #32, #33 (integrações e fixes) | Concluída |
| Hugo       |    5    | #32 (GET /arquivos)                 | Concluída |
| Martin     |    5    | #28 (POST /upload + testes)         | Concluída |
| Lucas      |    5    | #33 (estilos e layout)              | Concluída |
| Luíza      |    -    | -                                   | -         |
| Gabriel    |    2    | #33 (telas de listagem)             | Concluída |

---

## Bloqueios e Riscos

| Bloqueio / Risco                         | Impacto                                   | Responsável           | Prazo     |
| :--------------------------------------- | :---------------------------------------- | :-------------------- | :-------- |
| Tela de upload (#30) ainda não concluída | Médio, bloqueia fluxo completo de arquivo | Luíza, Lucas, Gabriel | 22/06     |
| Auditoria (#34 a #44) não iniciada       | Alto, requisito obrigatório da Fase 2     | Hugo                  | Semana 12 |

---

## Pendências para a Próxima Semana

> Semana 12 / 14, foco em concluir o gerenciamento de arquivos e iniciar auditoria.

| Tarefa                                | Responsável           | Issue | Prioridade |
| :------------------------------------ | :-------------------- | :---- | :--------- |
| Tela de upload de arquivos (frontend) | Luíza, Lucas, Gabriel | #30   | Alta       |
| Criar entidade AuditLog               | Hugo, Martin          | #34   | Alta       |
| Implementar AuditLogService           | Hugo, Martin          | #35   | Alta       |
| Criar UserType ADMIN                  | Hugo, Martin          | #40   | Alta       |
| Download e exclusão de arquivos       | Hugo, Martin          | -     | Média      |

---

_Documento preenchido por: Diogo_
