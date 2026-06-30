# Relatório da Semana 11 - Onboarding Digital

## Visão geral

Durante a semana 11, o foco do projeto foi consolidar o fluxo de upload e listagem de documentos iniciado na semana anterior, organizar os Pull Requests que ainda apresentavam conflitos ou duplicações e preparar a integração com o Google Cloud Storage.

Também foram realizadas correções nas telas do frontend, ajustes no isolamento dos documentos por usuário e melhorias na estrutura do backend para garantir a persistência dos metadados dos arquivos.

## Issues trabalhadas

### Backend

- [Issue #15 - Implementar upload e armazenamento de documentos](https://github.com/daisha19/Onboarding-Digital/issues/30)

  Objetivo: implementar o envio de arquivos, o armazenamento dos documentos e o registro dos metadados no banco de dados.

  Durante a semana, foram revisadas diferentes implementações relacionadas ao upload. Algumas estavam duplicadas ou utilizavam estruturas incompatíveis com o restante do projeto.

- [Issue #16 - Criar listagem filtrada de documentos](https://github.com/daisha19/Onboarding-Digital/issues/31)

  Objetivo: garantir que colaboradores visualizem apenas os próprios documentos, enquanto usuários RH possam consultar os documentos enviados pelos colaboradores.

  A funcionalidade foi consolidada nas rotas oficiais de documentos, evitando a manutenção de implementações duplicadas.

- [Issue #22 - Criar bootstrap do primeiro RH/admin](https://github.com/daisha19/Onboarding-Digital/issues/44)

  Objetivo: permitir a criação segura do primeiro usuário RH do sistema.

  Essa funcionalidade é necessária para que o ambiente possa ser configurado inicialmente sem depender da existência prévia de outro usuário RH.

### Frontend

- [Issue #17 - Criar tela de upload](https://github.com/daisha19/Onboarding-Digital/issues/32)

  Objetivo: disponibilizar uma tela para o colaborador selecionar o tipo de documento, escolher um arquivo e realizar o envio para o backend.

  A tela foi revisada e integrada à branch `dev` após a correção de conflitos e ajustes nas rotas utilizadas.

- [Issue #18 - Criar tela "Meus Documentos" para colaborador](https://github.com/daisha19/Onboarding-Digital/issues/33)

  Objetivo: permitir que o colaborador acompanhe os documentos enviados e os respectivos status.

  A tela foi integrada ao fluxo real da aplicação e passou a consumir a listagem protegida do backend.

## Pull Requests relacionados

### PR #39 - issue #16 - Listagem documentos

Autor: marrathomaz  
Link: [PR #39](https://github.com/daisha19/Onboarding-Digital/pull/39)

Esse PR implementava uma listagem de documentos, mas utilizava arquivos e estruturas diferentes das rotas oficiais já integradas ao projeto.

Após a revisão, a implementação duplicada foi removida e a funcionalidade válida foi mantida na estrutura principal do backend.

Status: Fechado sem merge, pois a implementação ficou obsoleta após a consolidação das rotas oficiais.

### PR #40 - Issue 17 criar tela de upload

Autor: Mateiki  
Link: [PR #40](https://github.com/daisha19/Onboarding-Digital/pull/40)

Esse PR implementou a tela de envio de documentos pelo colaborador.

Inicialmente, o PR apresentava conflitos com a branch `dev` e inconsistências nas rotas utilizadas. Após a atualização da branch e a resolução dos conflitos, a tela foi integrada ao projeto.

Status: Mergeado na branch `dev` após as correções solicitadas.

### PR #41 - issue #14: adiciona rotas de documentos

Autor: ninaalves14  
Link: [PR #41](https://github.com/daisha19/Onboarding-Digital/pull/41)

Esse PR implementou schemas, serviços, rotas protegidas, upload e listagem de documentos no backend.

Durante a revisão, foram solicitados ajustes relacionados às permissões e à filtragem dos documentos por usuário.

Status: Mergeado após as correções solicitadas.

### PR #42 - Upload armazenamento

Autor: marrathomaz  
Link: [PR #42](https://github.com/daisha19/Onboarding-Digital/pull/42)

Esse PR utilizava a mesma branch do PR #43, mas estava apontado para `main`.

Status: Fechado sem merge por ser redundante e estar com a base incorreta.

### PR #43 - issue #15 - Upload armazenamento

Autor: marrathomaz  
Link: [PR #43](https://github.com/daisha19/Onboarding-Digital/pull/43)

Esse PR apresentava uma implementação alternativa de upload, incluindo modelos e arquivos duplicados em relação ao backend já integrado.

Após a revisão, a parte redundante foi removida e o fluxo oficial de documentos foi mantido.

Status: Fechado sem merge, pois a funcionalidade já estava consolidada em outra implementação.

### PR #46 - Feature/18 tela documentos

Autor: Edupizzol  
Link: [PR #46](https://github.com/daisha19/Onboarding-Digital/pull/46)

Esse PR implementou as telas relacionadas ao envio e à visualização dos documentos pelo colaborador e pelo RH.

Durante a integração, foi necessário remover uma cópia duplicada do backend que havia sido incluída na branch.

Status: Mergeado na branch `dev` após a remoção dos arquivos duplicados.

### PR #53 - Integração com Google Cloud Storage

Autor: guin409  
Link: [PR #53](https://github.com/daisha19/Onboarding-Digital/pull/53)

Esse PR prepara o sistema para trabalhar com armazenamento local e Google Cloud Storage.

Foram adicionados um serviço centralizado de armazenamento, variáveis de ambiente para configuração do bucket e testes para o modo de armazenamento local.

Durante a revisão, foram solicitados ajustes para completar o download e a exclusão de arquivos no GCS, adicionar testes específicos para o modo cloud e centralizar as validações das rotas de upload.

Status: Ainda não foi mergeado, pois foram solicitadas correções antes da integração.

## Resultado da semana

A semana 11 avançou na consolidação do fluxo de documentos. As principais telas de upload e listagem foram integradas, as rotas do backend foram organizadas e diferentes implementações duplicadas foram removidas.

O upload local e a persistência dos metadados ficaram funcionalmente encaminhados. A preparação para o Google Cloud Storage foi iniciada, mas ainda depende de ajustes antes do merge.

A semana pode ser considerada parcialmente concluída. O fluxo local está funcionando, porém a integração completa com o armazenamento em nuvem permanece pendente.