# Relatório da Semana 12 - Onboarding Digital

## Visão geral

Durante a semana 12, o foco do projeto foi avançar na análise de documentos pelo RH, substituir dados mockados por informações reais da API e implementar logs de auditoria para as principais ações do sistema.

Foram criadas issues específicas para alteração de status, integração das telas do RH, auditoria, atualização do dashboard e revisão da documentação.

Também foi realizada uma revisão geral dos Pull Requests abertos para identificar conflitos, duplicações, ausência de testes e incompatibilidades entre as implementações.

## Issues criadas

### Backend

- [Issue #23 - Implementar análise e decisão de documentos no backend](https://github.com/daisha19/Onboarding-Digital/issues/48)

  Objetivo: permitir que usuários RH alterem o status dos documentos enviados pelos colaboradores.

  A funcionalidade deve permitir aprovação, rejeição e indicação de documento em análise, garantindo que apenas usuários RH possam executar essas ações.

- [Issue #25 - Implementar logs de auditoria reais para ações críticas](https://github.com/daisha19/Onboarding-Digital/issues/50)

  Objetivo: registrar as principais ações realizadas no sistema.

  Eventos esperados:
  - Login realizado com sucesso.
  - Tentativa de login inválida.
  - Logout.
  - Upload de documento.
  - Download de documento.
  - Exclusão de documento.
  - Aprovação ou rejeição.
  - Tentativa de acesso não autorizado.

### Frontend

- [Issue #24 - Integrar tela de documentos do RH com ações reais de análise](https://github.com/daisha19/Onboarding-Digital/issues/49)

  Objetivo: conectar a tela do RH aos endpoints reais do backend.

  A tela deve permitir visualizar documentos, aprovar, rejeitar e acompanhar os status sem depender de dados mockados.

- [Issue #26 - Trocar mocks do dashboard RH por dados reais da API](https://github.com/daisha19/Onboarding-Digital/issues/51)

  Objetivo: substituir colaboradores, documentos e registros de auditoria fictícios por dados obtidos da API.

  A issue também prevê estados de carregamento, erro e ausência de dados.

### Documentação e DevOps

- [Issue #27 - Revisar documentação e validação final da semana 12](https://github.com/daisha19/Onboarding-Digital/issues/52)

  Objetivo: revisar o README, registrar as entregas da semana, atualizar a documentação e reunir evidências dos testes realizados.

## Pull Requests relacionados

### PR #53 - Integração com Google Cloud Storage

Autor: guin409  
Link: [PR #53](https://github.com/daisha19/Onboarding-Digital/pull/53)

Esse PR continua a entrega pendente da semana 11 relacionada ao armazenamento em nuvem.

Os testes do backend passaram, mas ainda foram solicitados ajustes relacionados ao download e à exclusão no GCS, testes do modo cloud e centralização das validações de upload.

Status: Ainda não foi mergeado, pois aguarda correções.

### PR #54 - Trocar mocks do dashboard

Autor: Mateiki  
Link: [PR #54](https://github.com/daisha19/Onboarding-Digital/pull/54)

Esse PR substitui dados mockados do dashboard RH por dados reais da API e adiciona uma rota para consulta dos logs de auditoria.

Durante a revisão, foi identificado que o PR está apontando para `main`, enquanto o fluxo de integração do projeto ocorre em `dev`.

Também foi observado que o endpoint de auditoria apenas consulta registros existentes, mas não implementa a criação dos logs.

Status: Ainda não foi mergeado. Foi solicitada a troca da base para `dev`, atualização da branch e resolução dos conflitos.

### PR #55 - Integrar tela RH

Autor: Edupizzol  
Link: [PR #55](https://github.com/daisha19/Onboarding-Digital/pull/55)

Esse PR conecta as telas do RH e do colaborador à API real, adicionando endpoints para listagem, download e alteração de status.

O build e o lint do frontend passaram, mas foram identificadas sobreposições com alterações já existentes na branch `dev`.

Também foram encontrados pontos que precisam ser corrigidos, como duplicação da rota de alteração de status, incompatibilidade do download com o Google Cloud Storage e ausência de testes para os novos endpoints.

Status: Ainda não foi mergeado, pois possui conflitos e ajustes pendentes.

### PR #56 - Análise e decisão de documentos

Autor: ninaalves14  
Link: [PR #56](https://github.com/daisha19/Onboarding-Digital/pull/56)

Esse PR implementa o endpoint para atualização do status dos documentos pelo RH.

O check automatizado e os testes existentes passaram. Entretanto, os testes adicionados verificam apenas o registro da rota e a exigência de autenticação.

Foram solicitados testes adicionais para aprovação, rejeição, permissão de RH, documento inexistente e status inválido. Também foi solicitada a padronização dos nomes dos status.

Status: Ainda não foi mergeado, pois aguarda pequenos ajustes e nova revisão.

### PR #57 - Logs de auditoria reais

Autor: marrathomaz  
Link: [PR #57](https://github.com/daisha19/Onboarding-Digital/pull/57)

Esse PR foi aberto para implementar os logs de auditoria da semana 12.

Durante a revisão, foram identificados conflitos com a branch `dev`, utilização de arquivos antigos, imports inexistentes e incompatibilidade entre os parâmetros do serviço de auditoria e as chamadas realizadas pelas rotas.

Os testes não conseguem ser iniciados devido a um erro de importação do modelo de auditoria. A estrutura atual também não permite representar corretamente eventos sem documento ou usuário identificado, como logout e tentativa inválida de login.

Status: Não deve ser mergeado no estado atual. Foi recomendado refazer a implementação sobre a estrutura atual da branch `dev`.

## Ajustes realizados diretamente na branch dev

Foi revisado o commit responsável por alinhar as telas do frontend ao fluxo real da aplicação.

As seguintes correções foram realizadas:

- Remoção de documentos e registros de auditoria fictícios.
- Correção do dashboard RH para não listar usuários RH como colaboradores.
- Padronização da variável `NEXT_PUBLIC_API_BASE_URL`.
- Proteção das telas por perfil de usuário.
- Remoção da exibição dos caminhos internos dos arquivos.
- Utilização dos documentos reais no resumo do colaborador.
- Correção dos avisos de lint.
- Validação do build de produção do frontend.
- Execução dos testes existentes do backend.

O commit corrigido foi enviado para a branch `dev` com o identificador `27a0091`.

## Resultado da semana

A semana 12 avançou na organização das funcionalidades de análise de documentos, integração das telas e auditoria.

As issues foram distribuídas e todos os principais PRs foram revisados. Os comentários com os ajustes necessários foram publicados diretamente nos respectivos Pull Requests.

Apesar do avanço, a semana 12 ainda não pode ser considerada concluída. A alteração de status precisa de testes adicionais, as telas do RH precisam ser atualizadas com a `dev` e a implementação de auditoria precisa ser refeita.

