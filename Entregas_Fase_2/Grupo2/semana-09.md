# Resumo das Atividades

## Semana 09 – Sprint 3: Módulo de Usuários, Testes Automatizados e Deploy Inicial

Esta semana marcou o início do desenvolvimento efetivo do produto, com a construção das fundações técnicas do backend e o primeiro deploy em produção:

**Backend (Módulo de Usuários):**
Implementamos o módulo completo de usuários com rotas separadas por tipo de perfil. O endpoint `POST /users/pacientes` recebe nome, email, senha, CPF e data de nascimento; o endpoint `POST /users/medicos` recebe nome, email, senha, CRM e especialidade. Criamos `CreatePacienteDto` e `CreateMedicoDto` com herança via `extends CreateUserDto`, garantindo reaproveitamento dos campos comuns e tipagem estrita. O `UsersService` foi refatorado para separar a criação por tipo, aplicar hash bcrypt na senha antes de persistir e retornar uma projeção `PublicUser` que omite `passwordHash` de todas as respostas. O endpoint `POST /users/login` gera um token JWT contendo o `id` e o `tipo` do usuário, permitindo que guards de rota identifiquem o perfil sem consulta adicional ao banco.

**Testes Automatizados:**
Configuramos a suíte de testes com **Jest** e **Supertest**. Escrevemos testes unitários do `UsersService` usando `@nestjs/testing` com mocks de repositório, cobrindo os cenários de cadastro com sucesso, email duplicado e omissão de `passwordHash` na resposta. Os testes E2E sobem o servidor completo e validam os endpoints de cadastro e login via HTTP, incluindo verificação do token retornado. Configuramos timeout e ambiente de testes separado para evitar interferência com o banco de desenvolvimento.

**Infraestrutura:**
Realizamos o primeiro deploy funcional da aplicação no **Google Cloud Run** (#16). O backend containerizado se conecta ao Cloud SQL via Unix socket e lê credenciais do Secret Manager. Adicionamos containers de suporte à integração com o Google Cloud Storage e formalizamos o pipeline de deploy em `cloudbuild.yaml` para torná-lo reproduzível.

**Frontend (Iniciado):**
Gabriel iniciou a camada de identidade visual do frontend, criando os primeiros componentes UI base (`Button`) com testes via React Testing Library. Logos vetorizadas e favicon foram adicionados ao projeto.

**Gestão:**
Martin liderou o desenvolvimento backend com 10 commits ao longo da semana, cobrindo implementação, refatoração e testes. Hugo e Diogo atuaram na infraestrutura GCP. Lucas iniciou as telas de cadastro no frontend (#5, #6, #7), com entrega prevista para a próxima semana.
