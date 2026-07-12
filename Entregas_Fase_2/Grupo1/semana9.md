# Resumo das Atividades

## Semana 9 – Sprint 3: Fundações Técnicas e Funcionalidade Inicial
Com todo o planejamento estratégico e arquitetural concluído, a Semana 9 marcou o primeiro mergulho direto no código, entregando a fundação técnica do produto e a nossa primeira rota crítica de registro.

**Backend (API, Persistência e Segurança):**
Realizamos o setup do Spring Boot integrando as dependências vitais da sprint (Spring Data JPA, Spring Security, Driver PostgreSQL e BCrypt). Implementamos a entidade raiz `User` com validações rigorosas e entregamos nosso primeiro endpoint funcional (`POST /api/auth/register`). A lógica de negócio assegura que apenas e-mails corporativos (`@unb.br`) sejam registrados, bloqueia duplicatas no banco e faz o hash imediato das credenciais. A separação de responsabilidades (Controller, Service, Repository) foi adotada desde a base.

**Frontend (Rotas, UI e Integração Base):**
Inicializamos a base da aplicação web utilizando Vite, React e a biblioteca Bootstrap. Desenvolvemos o mapeamento primário do roteamento utilizando `react-router-dom` e entregamos a interface gráfica perfeitamente estruturada para as três telas essenciais de abertura: Login, Cadastro e Dashboard, com foco em componentização modular.

**Testes, Qualidade (QA) e Auditoria:**
Estabelecemos a cultura de qualidade configurando o JUnit 5 em conjunto com Mockito para testes unitários, orquestrados pelo plugin JaCoCo no build do Maven. Os testes cobriram regras estritas de registro, alcançando 92% de cobertura de código inicial na camada de serviço. Simultaneamente, preparamos o terreno para a rastreabilidade da aplicação estruturando a entidade central e o repositório nativo de `AuditLog`.
