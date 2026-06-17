# Resumo das Atividades

## Semana 10 – Sprint 4: Gestão de Documentos, Integração e Refinamento de Escopo

Esta semana representou a primeira entrega de comunicação sistêmica do projeto, aliada à implementação da nossa principal funcionalidade de negócio (upload de arquivos) e a ajustes significativos de gestão de produto e usabilidade:

**Backend (Gestão de Documentos, CORS e Segurança):**
Ajustamos as políticas de segurança da API configurando o `CorsConfigurationSource` para mapear e permitir as requisições do ambiente de desenvolvimento frontend. Habilitamos o envio de credenciais e reforçamos a segurança utilizando Cookies JWT estritamente HTTP (`HttpOnly`) com a política `SameSite=Lax`, além de ativar a validação de tokens **CSRF** para proteção contra ataques. No quesito de negócio, implementamos o **upload de documentos**, o salvamento estático dos arquivos, a associação automática do documento ao usuário autenticado (via contexto de segurança) e a listagem filtrada (por título e ID do projeto).

**Frontend (Serviços, Rotas Protegidas e Upload):**
A camada de comunicação foi estruturada no serviço `api.js` contendo requisições com a flag `credentials: 'include'` e o envio automatizado do cabeçalho `X-XSRF-TOKEN`, conectando definitivamente os formulários do React ao banco de dados pelo Spring Boot. Implementamos um componente de rotas privadas (`PrivateRoute`) que blinda o acesso a áreas restritas e criamos a tela de **Documentos**, que permite aos usuários realizarem uploads associados aos seus projetos, buscarem arquivos por filtros e efetuarem o download.

**Frontend (Acessibilidade Visual):**
Aprimoramos o design desenvolvendo a troca nativa entre Modo Claro e Escuro, gerenciada puramente com variáveis de CSS (`data-theme`). Incluímos um componente global de `ThemeToggle` no cabeçalho e utilizamos o `localStorage` para que a preferência do usuário seja memorizada entre suas visitas.

**Gestão e Controle do Escopo (Scope Creep):**
Atuamos taticamente para conter fuga de escopo ("scope creep") proveniente de protótipos de alta fidelidade que inflavam o planejamento inicial da V1. Rejeitamos documentações e issues desnecessárias, recolocando o foco da equipe integralmente no fluxo dos requisitos (F01 a F22) acordados no Canvas MVP. Além disso, oficializamos a nossa primeira rotação de papéis de trabalho, definindo que os ciclos operacionais terão exatamente duas semanas.
