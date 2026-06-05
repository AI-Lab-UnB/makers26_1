# Resumo das Atividades (Semanas 7 e 8 do curso)

Link para o repositório: https://github.com/pedrohpsantos/EdTech

As Semanas 7 e 8 do curso correspondem às Sprints 2 e 3 do projeto EdTech. Ou seja, englobam toda a fase de planejamento de arquitetura e requisitos, seguida pelo início da estruturação técnica (desenvolvimento das fundações do backend e frontend).

## O que fizemos na Semana 7 (Sprint 2 do Projeto - Planejamento):

- **Lean Inception:** Definição da Visão do Produto, Personas (Pesquisadora, Orientador, Auditora) e Jornadas de Usuários.
- **Requisitos:** Mapeamento de 22 funcionalidades, Requisitos Funcionais (RFs) e Não Funcionais (RNFs).
- **Arquitetura:** Modelagem C4 (Contexto e Container), Diagramas de Banco de Dados, Segurança e Fluxo JWT, e 9 ADRs (Decision Records) justificando as tecnologias como Spring Boot, Vite, PostgreSQL, e Cloud Run.
- **Gestão:** Organização da equipe (sistema de rotações), definição do Git Flow e critérios de "Done" (DoD).

## O que foi construído na Semana 8 (Sprint 3 do Projeto):

- **Fundação Backend:** Setup do ambiente Spring Boot com as dependências essenciais (JPA, Security, PostgreSQL).
- **Funcionalidades Iniciais:** Criação da primeira entidade (User) e do endpoint de registro (`/api/auth/register`), com validações reais (ex: domínio obrigatório `@unb.br`) e criptografia de senha (BCrypt).
- **Fundação Frontend:** Inicialização do frontend com React, Vite e Bootstrap.
- **Telas Iniciais:** Desenvolvimento das páginas de Login, Cadastro e Dashboard, além da configuração de rotas (`react-router-dom`).
- **Testes e Qualidade:** Configuração da suíte de testes (JUnit, Mockito) integrando o JaCoCo, onde alcançamos 92% de cobertura inicial.
- **Auditoria Base:** Criação e estruturação inicial do Módulo de Auditoria (AuditLog), crucial para os requisitos do projeto.
