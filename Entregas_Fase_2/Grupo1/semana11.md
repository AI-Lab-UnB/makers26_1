# Resumo das Atividades

## Semana 11 – Sprint 5: Migração de Arquivos, Segurança Rigorosa e Contratos
Esta semana solucionou limitações críticas na nossa engenharia local de dados, garantindo que as operações do produto transitem em um ambiente validado, imutável e estruturalmente preparado para a nuvem.

**Backend (Cloud Storage, Infraestrutura e Flyway):**
Concluímos um pilar arquitetural inegociável migrando o controle do banco de dados do antigo DDL-Auto (inadequado para produção) para a solidez e rastreabilidade transacional das migrações do **Flyway**. No viés de negócio, unificamos o serviço validado de Uploads redirecionando-o para um armazenamento real na nuvem através de integração primária com o Google Cloud Storage (GCS). A segurança atingiu grau máximo, com o backend bloqueando duramente todas e quaisquer mutações de estado (`POST`, `PUT`, `DELETE`) sem o fornecimento perfeito do escudo de `X-XSRF-TOKEN`.

**Frontend (Interface Inteligente de Documentos):**
Aprimoramos o ecossistema React ao entregar a tela definitiva de documentos (`Documentos.jsx`), totalmente baseada em reatividade de estado para alternar a experiência do usuário perfeitamente entre mosaico (Grid) e Linhas detalhadas (Listas), unificado a um potente motor indexador para pesquisas locais. Reparamos massivamente os interceptores no framework front-end para que embutissem em tempo real o cabeçalho XSRF em harmonia irrestrita com os impedimentos restritos da API no Spring Boot.

**Documentação (Docs-as-Code e Contratos):**
Solidificamos o elo de desenvolvimento isolado introduzindo os Contratos Estritos de API diretamente na documentação em MkDocs. Mapeamos com exatidão as expectativas algorítmicas de Entrada (Requests) e Saída (Responses) cobrindo todos os Data Transfer Objects (DTOs), eliminando suposições e instabilidades durante o consumo de endpoints. Em decorrência do modelo robusto e seguro estipulado, o repositório passou a ser endossado pela tutoria como referencial técnico positivo da disciplina.
