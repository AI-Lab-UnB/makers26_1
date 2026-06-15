# Resumo das Atividades

## Semana 10 – Sprint 4: Integração, Rotas e Refinamento de Escopo

Esta semana representou a primeira entrega de comunicação sistêmica do projeto, aliada a ajustes significativos de gestão de produto e usabilidade:

**Backend (CORS e Segurança):**
Ajustamos as políticas de segurança da API configurando o `CorsConfigurationSource` para mapear e permitir as requisições do ambiente de desenvolvimento frontend. Também habilitamos o envio e recebimento de credenciais (`allowCredentials = true`), permitindo que a aplicação faça a gestão autêntica por meio de Cookies JWT estritamente HTTP (`HttpOnly`).

**Frontend (Serviços e Rotas Protegidas):**
A camada de comunicação foi estruturada no serviço `api.js` contendo requisições com a flag `credentials: 'include'`, conectando definitivamente os formulários do React (Login e Registro) ao banco de dados pelo Spring Boot. Adicionalmente, implementamos um componente de rotas privadas (`PrivateRoute`) que blinda o acesso à rota `/dashboard` e redireciona usuários não autenticados.

**Frontend (Acessibilidade Visual):**
Aprimoramos o design desenvolvendo a troca nativa entre Modo Claro e Escuro, gerenciada puramente com variáveis de CSS (`data-theme`). Incluímos um componente global de `ThemeToggle` no cabeçalho e utilizamos o `localStorage` para que a preferência do usuário seja memorizada entre suas visitas.

**Gestão e Controle do Escopo (Scope Creep):**
Atuamos taticamente para conter fuga de escopo ("scope creep") provindos de protótipos de alta fidelidade que inflavam o planejamento inicial da V1. Rejeitamos documentações e issues desnecessárias, recolocando o foco da equipe integralmente no fluxo dos requisitos (F01 a F22) acordados no Canvas MVP. Além disso, oficializamos a nossa primeira rotação de papéis de trabalho, definindo que os ciclos operacionais terão exatamente duas semanas.
