# Relatório da Semana 10 - Onboarding Digital

## Visão geral

Durante a semana 10, o foco do projeto foi avançar na funcionalidade de gerenciamento de documentos dentro da plataforma de onboarding digital. As atividades concentraram-se principalmente na criação das issues relacionadas ao fluxo de documentos, upload, listagem por perfil de usuário, integração com telas do frontend e ajustes necessários nos fluxos de autenticação e cadastro.


## Issues criadas

### Backend

- [Issue #14 - Criar estrutura de gerenciamento de documentos no backend](https://github.com/daisha19/Onboarding-Digital/issues/29)

  Objetivo: criar a base inicial para gerenciamento de documentos no backend, incluindo rotas, schemas, serviços e persistência dos metadados no banco.

  Essa issue serviu como fundação para o fluxo de documentos, permitindo que o sistema começasse a tratar documentos enviados por colaboradores e acessados pelo RH.

- [Issue #15 - Implementar upload e armazenamento de documentos](https://github.com/daisha19/Onboarding-Digital/issues/30)

  Objetivo: implementar o envio de arquivos de documentos, com armazenamento físico e registro dos dados no banco.

  A issue envolve validações como tipo de arquivo, tamanho máximo, usuário autenticado e associação do documento ao colaborador correto.

- [Issue #16 - Criar listagem filtrada de documentos](https://github.com/daisha19/Onboarding-Digital/issues/31)

  Objetivo: criar uma listagem de documentos respeitando o perfil do usuário autenticado.

  Regras esperadas:
  - Colaborador deve visualizar apenas os próprios documentos.
  - RH deve visualizar os documentos dos colaboradores.
  - Usuários sem autenticação não devem acessar a listagem.

- [Issue #22 - Criar bootstrap do primeiro RH/admin](https://github.com/daisha19/Onboarding-Digital/issues/44)

  Objetivo: resolver a necessidade de criação inicial de um usuário RH ou administrador no sistema.

  Essa issue é importante porque algumas funcionalidades dependem de autenticação e permissões de RH, então o sistema precisa ter uma forma segura de criar o primeiro usuário com esse perfil.

## Frontend

- [Issue #17 - Criar tela de upload](https://github.com/daisha19/Onboarding-Digital/issues/32)

  Objetivo: criar uma tela para que o colaborador consiga enviar documentos pelo painel.

  A tela deve se conectar ao backend, carregar os tipos de documento disponíveis, permitir seleção de arquivo, enviar o documento e exibir mensagens de sucesso ou erro.

- [Issue #18 - Criar tela "Meus Documentos" para colaborador](https://github.com/daisha19/Onboarding-Digital/issues/33)

  Objetivo: permitir que o colaborador visualize os documentos que já enviou.

  Essa tela deve consumir a listagem filtrada do backend, exibindo apenas os documentos do usuário autenticado.

- [Issue #19 - Ajustar dashboard RH para documentos reais](https://github.com/daisha19/Onboarding-Digital/issues/34)

  Objetivo: conectar o dashboard do RH aos dados reais de documentos.

  Essa issue prepara a interface do RH para deixar de usar dados mockados e passar a consumir informações persistidas no backend.

- [Issue #20 - Corrigir fluxo de autenticação e rota de login](https://github.com/daisha19/Onboarding-Digital/issues/36)

  Objetivo: corrigir inconsistências no fluxo de login, principalmente relacionadas às rotas usadas no frontend.

  Essa correção é importante porque algumas telas protegidas redirecionam usuários não autenticados para a tela de login.

- [Issue #21 - Corrigir e padronizar fluxos de cadastro de usuários](https://github.com/daisha19/Onboarding-Digital/issues/37)

  Objetivo: padronizar os fluxos de cadastro e corrigir inconsistências entre frontend e backend.

  Essa issue apoia o funcionamento correto dos perfis de usuário, especialmente RH e colaborador.

## Pull Requests relacionados

### PR #39 - issue #16 - Listagem documentos

Autor: marrathomaz  
Link: [PR #39](https://github.com/daisha19/Onboarding-Digital/pull/39)

Esse PR foi aberto para implementar a listagem filtrada de documentos. Durante a revisão, foram identificados problemas estruturais, como imports que não existem no projeto, uso de `FastAPI()` diretamente no arquivo de rota e campos incompatíveis com o modelo real de `Documento`.

Status: Ainda não dei o merge pois pedi correções necessarias.

### PR #40 - Issue 17 criar tela de upload

Autor: Mateiki  
Link: [PR #40](https://github.com/daisha19/Onboarding-Digital/pull/40)

Esse PR implementa a tela de upload de documentos no frontend. A tela inclui formulário, seleção de tipo de documento, envio de arquivo e mensagens de retorno.

Durante a revisão, foi identificado que o PR estava apontando para `main`, enquanto o fluxo de integração do projeto está acontecendo em `dev`. Também foi apontado o uso de rota de login incorreta.

Status: Ainda não dei o merge pois pedi correções necessarias.
### PR #41 - issue #14: adiciona rotas de documentos

Autor: ninaalves14  
Link: [PR #41](https://github.com/daisha19/Onboarding-Digital/pull/41)

Esse PR implementa a estrutura de documentos no backend, incluindo rotas, schemas, serviços e integração com o modelo existente.

Após comentários de revisão, foram adicionados commits corrigindo pontos importantes, como filtragem por perfil na listagem e uso de status inicial adequado.

Status: Já foi mergeado pois pedi correções e a Nina já corrigiu.
### PR #42 - Upload armazenamento

Autor: marrathomaz  
Link: [PR #42](https://github.com/daisha19/Onboarding-Digital/pull/42)

Esse PR foi identificado como duplicado do PR #43, usando a mesma branch de funcionalidade, mas apontando para `main`.

Status: Vou fechar ele pois é redundante.

### PR #43 - issue #15 - Upload armazenamento

Autor: marrathomaz  
Link: [PR #43](https://github.com/daisha19/Onboarding-Digital/pull/43)

Esse PR trata do upload e armazenamento de documentos. Durante a revisão, foram identificados problemas como criação de modelo duplicado, imports fora do padrão do projeto e ausência de registro correto da rota no `main.py`.

Status: Ainda não dei o merge pois pedi correções necessarias.


## Resultado da semana

A semana 10 avançou bastante na organização da funcionalidade de documentos. Foram criadas as principais issues para dividir o trabalho entre backend e frontend, e os primeiros PRs começaram a implementar upload, listagem e telas relacionadas.
Ela está um pouco atrasada, mas já ta qiase finalizada, só falta uns ajustes. Atrasei a entrega deste relatório por motivos de que eu queria que as issues já estivessem completas e mergeadas. Porém, não deu tempo, peço desculpas pelo atraso.
