# Resumo das Atividades

## Semana 12 – Sprint 6: Nuvem S3, Relacionamentos e Padronização Corporativa
Esta semana selou a adoção escalável e definitiva da nossa infraestrutura de armazenamento, entregou componentes vitais da operação de relacionamento na plataforma e elevou monumentalmente a maturidade e a estética da nossa documentação corporativa.

**Backend (Storage S3 Centralizado e Associação de Projetos):**
O sistema abandonou permanentemente quaisquer manipulações de arquivos em disco para abraçar a escalabilidade absoluta integrando os documentos ao **Supabase Storage** (conectado de forma universal consumindo a API nativa da AWS S3 SDK), centralizando variáveis sensíveis unicamente no `application.yml`. Na camada de domínio, lançamos o importante endpoint de associação entre pesquisadores e laboratórios (`POST /api/projects/{id}/members`), blindado contra colisões de membros e dados duplicados (evitando inconsistências via tratamentos de 409 Conflict), cujos atos emitem gatilhos instantâneos irremovíveis para o sistema orgânico de logs de Auditoria do sistema.

**Frontend (Associação Nativa e Catálogo de Projetos):**
A tela principal de consumo dos pesquisadores foi finalizada com a interface de Projetos (`/projects`), revelando um amplo catálogo de laboratórios e linhas ativadas na plataforma, empacotadas através de design flexível de cards. Enriquecemos drasticamente a experiência do usuário projetando o laço de "Associação direta", um componente acionável ("Associar-se") que dispara uma comunicação limpa, assíncrona, e de ponta a ponta com a base de dados, devolvendo feedbacks de UI instantâneos, orientando o usuário em caso de duplicidades ou confirmação de pertencimento ao projeto.

**Gestão, Qualidade Documental e DevOps:**
A estrutura MkDocs sofreu a sua mais severa e rigorosa padronização. Abolimos elementos informais (emojis) e trouxemos matrizes iconográficas puras fornecidas nativamente pela tecnologia do Material Design. Todos os requisitos, originalmente quebrados e fracionados, foram formatados, auditados e mapeados para notações unificadas rastreáveis sem ruídos (RF01 a RF22 / RNF01 a RNF25). Inauguramos o abrangente Glossário de Termos no corpo central para sanar a barreira linguística técnica. Como passo de encerramento da Sprint, a frente de infraestrutura sanou passivos históricos e pendências da pipeline bloqueando e resolvendo todos os entraves do GitHub Dependabot, sincronizando todos os branches abertos no Git Flow por force-rebase e firmando uma arquitetura local puramente congruente e zerada de conflitos.
