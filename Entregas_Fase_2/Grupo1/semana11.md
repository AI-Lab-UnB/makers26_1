## Semana 11 – Sprint 5: Uploads, Autenticação Avançada e Integração com Nuvem

Esta semana marcou a superação de desafios cruciais de segurança e arquitetura do MVP, garantindo que as operações do produto ocorram em um ambiente validado e persistente:

**Backend (Infraestrutura, Cloud e Segurança Rigorosa):**
Finalizamos a migração completa do controle de versionamento do banco de dados para o Flyway (substituindo o DDL-Auto), etapa fundamental para habilitar futuros deploys em nuvem sem risco de perda de dados. Entregamos a funcionalidade crítica da aplicação: Upload de Arquivos validado e diretamente integrado ao armazenamento em nuvem do Google Cloud Storage (GCS). Refinamos pesadamente as barreiras de segurança habilitando a política `SameSite=Lax` nas sessões e tornando o envio de um token de mitigação de risco (`X-XSRF-TOKEN`) um requisito absoluto para todas as chamadas HTTP restritas.

**Frontend (Gestão de Documentos e Resolução de Tokens):**
No lado cliente, entregamos a tela inteligente `Documentos.jsx`, equipada com visualizações interativas em grid e listas e mecanismos de pesquisa funcional baseada em títulos e projetos. Refatoramos todo o arcabouço de requisições web no React para interceptar e embutir com sucesso as credenciais `XSRF`, pareando e validando perfeitamente a comunicação imposta pelo backend.

**Contratos de Comunicação (Docs-as-Code):**
A fim de garantir consistência técnica entre os desenvolvedores de front e back, formalizamos documentações sólidas no padrão de contratos de API. Deixamos as expectativas de entrada (Requests) e saída (Responses) estritamente especificadas, equalizando e travando os DTOs em ambas as pontas.

**Gestão da Equipe e Reconhecimentos:**
O grande nível técnico alcançado com as implementações de segurança e a finalização madura dos uploads rendeu à equipe um reconhecimento formal por parte da nossa tutoria, utilizando nosso projeto como referência prática para os demais grupos. Decidimos suspender temporariamente a dinâmica semanal de rotação de papéis para que um membro da equipe (Arthur) pudesse se focar totalmente na implantação da área de documentação sistêmica técnica e da arquitetura de logs, estabilizando as bases operacionais para a nossa próxima entrega do MVP.
