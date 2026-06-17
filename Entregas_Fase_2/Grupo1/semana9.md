# Resumo das Atividades

## Semana 9 – Sprint 3: Inicialização Técnica

Com o planejamento concluído nas semanas anteriores, a Semana 9 marcou o início do desenvolvimento efetivo da aplicação:

**Backend:**
Configuramos o projeto Spring Boot com todas as dependências da sprint, criamos a entidade `User` com JPA e implementamos o primeiro endpoint real de negócio: `POST /api/auth/register`. O endpoint valida que o e-mail pertence ao domínio `@unb.br`, rejeita duplicatas e armazena a senha com BCrypt. A separação de responsabilidades entre Controller, Service e Repository foi aplicada desde o início para suportar a testabilidade do código.

**Frontend:**
Inicializamos o projeto com Vite, React e Bootstrap, configuramos o roteamento com `react-router-dom` e entregamos as três telas que cobrem o fluxo inicial do usuário: Login, Cadastro e Dashboard. A estrutura de componentes foi organizada em módulos desde o começo para facilitar a escalabilidade.

**Testes:**
Configuramos JUnit 5 com Mockito e integramos o JaCoCo ao build do Maven. Os testes cobrem os principais cenários da camada de serviço: registro com e-mail inválido, e-mail duplicado e registro bem-sucedido, resultando em 92% de cobertura inicial.

**Auditoria:**
A entidade `AuditLog` e o repositório correspondente foram criados e estruturados. A integração com os demais módulos (registro de eventos de autenticação, por exemplo) está planejada para as próximas sprints.
