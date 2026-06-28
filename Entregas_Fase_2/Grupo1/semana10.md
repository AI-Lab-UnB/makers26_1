# Resumo das Atividades

## Semana 10 – Sprint 4: Gestão de Documentos, Integração e Acessibilidade
Esta semana representou a primeira comunicação real de ponta a ponta entre os microsserviços do projeto, aliada ao refinamento e blindagem do escopo de produto, além de avanços de usabilidade.

**Backend (Uploads, Segurança e CORS):**
Ajustamos as políticas da API configurando a malha do `CorsConfigurationSource` para habilitar comunicações seguras do ambiente de desenvolvimento cliente. Ativamos a aceitação de credenciais entre origens e fortificamos a segurança transacional implantando cookies JWT puramente HTTP (`HttpOnly`) blindados com a flag `SameSite=Lax`. Em paralelo, ativamos a proteção obrigatória contra falsificação implantando a validação sistêmica do token Anti-CSRF (`X-XSRF-TOKEN`). A nível de negócio, entregamos o serviço estático de upload de documentos no disco local associados de maneira indelével ao usuário autenticado (via Spring Security Context).

**Frontend (Conectividade, Upload e Rotas Protegidas):**
No lado cliente, arquitetamos a camada de consumo HTTP de forma centralizada (`api.js`), injetando os cabeçalhos nativos de autorização e permitindo a coleta e o envio automatizado do `X-XSRF-TOKEN` exigido pela API. Construímos e implementamos o componente `PrivateRoute`, travando as rotas sensíveis para visitantes deslogados. Complementamos a entrega conectando a interface avançada de Documentos, permitindo que usuários da base efetuassem envios e buscassem arquivos via filtros consolidados.

**Gestão de Escopo (Produto) e Acessibilidade:**
Do ponto de vista de gestão, atuamos energicamente contra a expansão descontrolada de escopo (*scope creep*) impulsionada por visões futuras, retornando o foco da engenharia integralmente aos requisitos validados no Canvas MVP originais. No quesito usabilidade, entregamos um sistema robusto de suporte a Modo Claro/Escuro nativo, persistido via `localStorage` e gerido de forma otimizada por variáveis de CSS (`data-theme`), alavancando a acessibilidade.
