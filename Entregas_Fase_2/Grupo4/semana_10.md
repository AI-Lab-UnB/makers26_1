# Semana 10 – Upload e Listagem: Associação com Usuário e Filtros

## Objetivo da Semana

A Semana 10 foi dedicada à implementação do **core funcional do FIFA Team Hub** — o sistema de upload e listagem de documentos. Este é o momento em que a aplicação deixa de ser uma "estrutura vazia" e passa a resolver o problema real dos utilizadores: centralizar documentos de seleções de forma segura e rastreável.

O foco foi implementar upload robusto com validações de segurança no servidor, armazenamento seguro em disco local (preparado para GCS na S11), listagem filtrada por seleção, e interface intuitiva de upload com feedback de progresso.

---

## Divisão da Equipa (Rotação Sprint 10)

| Frente | Responsáveis | Foco |
|--------|--------------|------|
| **Backend** | Arthur (Âncora) + Caio (1ª vez BE real) | Endpoints upload/listagem, validações rigorosas, armazenamento |
| **Frontend** | João (Âncora) + Josef (1ª vez FE real) | Componente upload, listagem com paginação, filtros |
| **DevOps** | Júlia (Âncora) + João (Apoio) | Storage local, docker volumes, variáveis de ambiente |
| **Documentação** | Caio (Responsável) | Endpoints upload/listagem, exemplos request/response, Postman |

---

## Issues Geradas (S10-BE-01 a S10-QA-01)

### Backend (3 Issues)

**[S10-BE-01] Endpoint de Upload de Documentos (multipart/form-data)**
- Responsáveis: Arthur (Âncora) + Caio (Par)
- Endpoint: `POST /documents/upload`
- Decorators: `@require_auth`, `@require_role("TECHNICAL_STAFF")`
- Validações rigorosas no servidor:
  - MIME type via `python-magic` (não confiar na extensão)
  - Tamanho máximo 10 MB
  - Tipos aceitos: CONVOCACAO, PASSAPORTE, LAUDO_MEDICO, RELATORIO_TATICO, ESQUEMA_JOGADAS
  - Rejeição HTTP 413 (tamanho), HTTP 415 (tipo), HTTP 422 (doc_type inválido)
- `selection_id` preenchido automaticamente do token (nunca do body)
- Nome único gerado: `{uuid4()}.{extensão}`
- Armazenamento em `backend/storage/uploads/{selection_id}/{stored_name}`
- Metadados persistidos: id, selection_id, uploaded_by, doc_type, original_name, file_size_kb, mime_type, status
- Return 201 com documento criado (sem storage_path exposto)
- AuditLog registado: action=UPLOAD, status=SUCCESS
- **Status:** ✅ Concluída
- **Entrega:** Endpoint funcional, testado no Postman

**[S10-BE-02] Endpoint de Listagem de Documentos com Filtro por Seleção**
- Responsáveis: Arthur + Caio
- Endpoint: `GET /documents`
- Filtro por `selection_id` do utilizador (aplicado no backend, nunca no frontend)
- Lógica diferenciada por perfil:
  - TECHNICAL_STAFF: documentos da própria seleção (todos os tipos)
  - ORGANIZER: CONVOCACAO e PASSAPORTE de todas as seleções
  - AUDITOR: HTTP 403
- Parâmetros opcionais: `?doc_type=CONVOCACAO&page=1&per_page=20`
- Ordenação padrão: `created_at DESC`
- Response com paginação: data, page, per_page, total, pages
- Teste de isolamento: BRA não vê documentos ARG em nenhuma circunstância
- **Status:** ✅ Concluída
- **Entrega:** Listagem funcional com isolamento garantido

**[S10-BE-03] Endpoint de Eliminação de Documento (Soft Delete)**
- Responsáveis: Arthur + Caio
- Endpoint: `DELETE /documents/{document_id}`
- Decorators: `@require_auth`, `@require_role("TECHNICAL_STAFF")`
- Validações: apenas quem fez upload pode eliminar; isolamento verificado
- Soft delete: `deleted_at = datetime.utcnow()` (não apagar do banco)
- Ficheiro físico removido do disco
- AuditLog: action=DELETE, status=SUCCESS
- Return 204 No Content
- Documentos deletados não aparecem em listagens
- **Status:** ✅ Concluída
- **Entrega:** Eliminação com rastreabilidade completa

### Frontend (2 Issues)

**[S10-FE-01] Componente de Upload de Documento com Feedback Visual**
- Responsáveis: João (Âncora) + Josef (Par)
- Componente: `UploadDocumentModal.vue`
- Props: `isOpen`, `onClose`, `onSuccess`
- Campos: input file (accept PDF/JPG/PNG/DOCX), select tipo documento
- Validação client-side:
  - Ficheiro obrigatório (desabilitar botão se vazio)
  - Tamanho máximo 10 MB (exibir erro antes de enviar)
  - Tipo obrigatório (impedir submissão)
- Estado de loading: desabilitar botão/input durante upload
- Barra de progresso via `onUploadProgress` do Axios
- Sucesso: fechar modal, emitir `onSuccess`, toast "Documento enviado com sucesso!"
- Erros:
  - 413: "Ficheiro excede limite permitido"
  - 415: "Formato não suportado"
  - 403: "Não tem permissão"
  - Genérico: "Erro ao enviar. Tente novamente."
- Implementação: FormData com file + doc_type
- Integração dashboard: botão "Enviar Documento" visível apenas TECHNICAL_STAFF
- Ao sucesso, adicionar documento ao topo da lista sem recarregar
- **Status:** ✅ Concluída
- **Entrega:** Upload funcional com feedback visual completo

**[S10-FE-02] Listagem de Documentos com Filtros e Status**
- Responsáveis: João + Josef
- Composable: `useDocuments.ts` com state reativo
- Funções: `fetchDocuments()`, `deleteDocument()`, `addDocument()`
- Componente: `DocumentList.vue` em tabela ou cards
- Colunas: Nome, Tipo, Enviado por, Data/hora, Status, Ações
- Indicação visual de status:
  - PENDING → badge amarela "Pendente"
  - APPROVED → badge verde "Aprovado"
  - REJECTED → badge vermelha "Rejeitado" + tooltip com comentário
- Filtros:
  - Select por tipo de documento (chama fetchDocuments dinamicamente)
  - Botão "Limpar filtros"
- Paginação: botões Anterior/Próxima, "Página X de Y"
- Estado de loading: skeleton loader ou spinner
- Estado vazio: "Nenhum documento encontrado."
- Ação eliminar (TECHNICAL_STAFF apenas): diálogo de confirmação
- Vista ORGANIZER: coluna "Seleção" com código FIFA, sem botão eliminar
- **Status:** ✅ Concluída
- **Entrega:** Listagem completa com paginação e filtros

### DevOps / Infra (1 Issue)

**[S10-DO-01] Configuração do Ambiente Local de Storage e Variáveis**
- Responsáveis: Júlia (Âncora) + João (Apoio)
- Pasta local: `backend/storage/uploads/` (ignorada no .gitignore)
- Variáveis `.env.example`:
  - STORAGE_BACKEND=local
  - LOCAL_STORAGE_PATH=./storage/uploads
  - MAX_FILE_SIZE_MB=10
  - ALLOWED_EXTENSIONS=pdf,jpg,jpeg,png,docx
- `docker-compose.yml`: volume `./backend/storage/uploads:/app/storage/uploads`
- Preparação para GCS (S11): criar `backend/app/services/storage_service.py` com interface abstracta
  - `StorageService` (abstract)
  - `LocalStorageService` (implementação S10)
  - Na S11, apenas `GCSStorageService` será adicionada
- Teste: `docker compose up`, upload cria ficheiro em `backend/storage/uploads/{selection_id}/`
- Teste: `docker compose down` + `docker compose up`, ficheiros persistem
- Todos conseguem rodar o ambiente sem configuração adicional
- **Status:** ✅ Concluída
- **Entrega:** Storage local funcional, preparado para GCS

### Documentação (1 Issue)

**[S10-DC-01] Documentação dos Endpoints de Upload e Listagem**
- Responsável: Caio
- Ficheiro: `docs/api-documents.md`
- Documentar:
  - `POST /documents/upload`: descrição, auth, body, respostas (201, 400, 401, 403, 413, 415, 422)
  - `GET /documents`: descrição, auth, query params, comportamento por perfil, resposta com paginação
  - `GET /documents/{id}`: detalhe, auth, resposta
  - `DELETE /documents/{id}`: método, auth, resposta
- Documentar modelo `Document` com todos os campos e enums
- Documentar regras de validação: tipos, tamanho, MIME types
- Collection Postman atualizada e exportada em `docs/postman/s10_documents.json`
- Adicionar link em `docs/index.md`
- **Status:** ✅ Concluída
- **Entrega:** Documentação completa publicada no GitHub Pages

### QA / Testes de Segurança (1 Issue)

**[S10-QA-01] Testes de Isolamento e Segurança do Upload**
- Responsáveis: Júlia (Lidera) + Arthur (Implementa)
- Ficheiro: `backend/tests/test_document_isolation.py`
- Testes implementados:
  ```
  ✓ Upload cria documento com selection_id correto (do token, não do body)
  ✓ BRA não vê documentos ARG em GET /documents
  ✓ Acesso direto a documento ARG retorna 403 (BRA)
  ✓ Eliminação de documento ARG é bloqueada (BRA)
  ✓ ORGANIZER não acessa RELATORIO_TATICO de nenhuma seleção
  ✓ Tamanho > 10 MB é rejeitado com 413
  ✓ MIME type inválido é rejeitado com 415
  ✓ Tentativa cross-selection gera AuditLog ACCESS_DENIED
  ```
- Testes rodam no CI/CD — falha bloqueia merge
- Coverage mínimo 60% no pytest
- **Status:** Em testes
- **Entrega:** Testes de isolamento passando, CI bloqueando violações

---

## Tarefas por Frente Técnica

### Backend — Tarefas Concluídas

✅ Modelo Document com SQLAlchemy (id, selection_id, uploaded_by, doc_type, original_name, stored_name, file_size_kb, mime_type, status, created_at, deleted_at)

✅ Migration Alembic criada e aplicada

✅ Endpoint POST /documents/upload funcional

✅ Validação de MIME type com python-magic

✅ Validação de tamanho (max 10 MB)

✅ Validação de doc_type contra Enum

✅ Rejeição de e-mail duplicado → HTTP 409

✅ selection_id preenchido do token (nunca do body)

✅ Nome único gerado (uuid + extensão)

✅ Armazenamento em `backend/storage/uploads/{selection_id}/`

✅ Retorno 201 com documento criado

✅ Endpoint GET /documents com filtro por selection_id

✅ Comportamento diferenciado por perfil (TECHNICAL_STAFF/ORGANIZER/AUDITOR)

✅ Paginação funcional (page, per_page, total, pages)

✅ Endpoint DELETE /documents/{id} com soft-delete

✅ Validação: apenas autor pode deletar

✅ Ficheiro físico removido, soft-delete no banco

✅ AuditLog registado para UPLOAD, DELETE, ACCESS_DENIED

✅ Testes de isolamento passando

✅ Testes rodando no CI/CD

✅ Postman collection testada com todos os cenários

### Frontend — Tarefas Concluídas

✅ Componente UploadDocumentModal.vue criado

✅ Input file com accept (PDF, JPG, PNG, DOCX)

✅ Select tipo documento com todas as opções

✅ Validação client-side: ficheiro obrigatório

✅ Validação client-side: tamanho máximo 10 MB (erro amigável)

✅ Validação client-side: tipo obrigatório

✅ Estado de loading: botão/input desabilitados durante upload

✅ Barra de progresso via onUploadProgress

✅ Mensagem de sucesso com toast

✅ Mensagens de erro para 413, 415, 403, genérico

✅ FormData construído com file + doc_type

✅ Token JWT injetado automaticamente via interceptor

✅ Modal fecha após sucesso

✅ onSuccess emitido, documento adicionado ao topo da lista

✅ Composable useDocuments.ts criado

✅ Componente DocumentList.vue com tabela/cards

✅ Colunas: Nome, Tipo, Responsável, Data/hora, Status, Ações

✅ Indicação visual de status (badge cores)

✅ Filtro por tipo (chama fetchDocuments dinamicamente)

✅ Botão "Limpar filtros"

✅ Paginação com botões e indicador

✅ Skeleton loader/spinner durante carregamento

✅ Mensagem "Nenhum documento" quando vazio

✅ Ação eliminar com diálogo de confirmação (TECHNICAL_STAFF)

✅ Vista ORGANIZER sem botão eliminar, coluna "Seleção"

✅ Botão "Enviar Documento" visível apenas TECHNICAL_STAFF

✅ Testes Vitest passando

### DevOps — Tarefas Concluídas

✅ Pasta `backend/storage/uploads/` criada com `.gitkeep`

✅ `.gitignore` cobre `backend/storage/uploads/**`

✅ `.env.example` com STORAGE_BACKEND, LOCAL_STORAGE_PATH, MAX_FILE_SIZE_MB, ALLOWED_EXTENSIONS

✅ `docker-compose.yml` com volume montado

✅ StorageService (abstract) e LocalStorageService (implementação)

✅ Preparação para migração GCS (interface pronta)

✅ Teste: docker compose up sobe sem erros

✅ Teste: upload cria ficheiro em `backend/storage/uploads/{selection_id}/`

✅ Teste: docker compose down + up, ficheiros persistem (volume funciona)

✅ Todos conseguem rodar ambiente localmente

### Documentação — Tarefas Concluídas

✅ `docs/api-documents.md` documentando POST /documents/upload

✅ Documentação de GET /documents com comportamento por perfil

✅ Documentação de GET /documents/{id} e DELETE /documents/{id}

✅ Modelo Document documentado com todos os campos

✅ Regras de validação documentadas (tipos, tamanho, MIME)

✅ Collection Postman atualizada com todos os cenários

✅ Exemplos de request/response para cada endpoint

✅ Fluxo de upload com diagrama explicado

✅ Link adicionado ao `docs/index.md`

---

## Testes de Isolamento e Segurança

### Testes Implementados

✅ `test_document_isolation.py`:
- Upload com BRA cria documento com selection_id=BRA (do token)
- GET /documents com token BRA retorna apenas documentos BRA
- GET /documents/{id} com documento ARG retorna 403 para BRA
- DELETE /documents/{id} com documento ARG retorna 403 para BRA
- ORGANIZER não vê RELATORIO_TATICO em nenhuma seleção
- Upload > 10 MB retorna 413
- MIME type inválido retorna 415
- Tentativa cross-selection gera AuditLog ACCESS_DENIED

✅ Testes de Validação:
- E-mail inválido rejeitado
- doc_type inválido rejeitado
- Ficheiro ausente retorna 400
- Credentials inválidas retornam 401

✅ CI/CD:
- Testes bloqueiam PR em falha
- Coverage mínimo 60% verificado
- Linting + type-check obrigatórios

---

## Métricas de Conclusão

| Métrica | Meta | Alcançado |
|---------|------|-----------|
| Issues S10 | 8 | ✅ 8 |
| Endpoints BE | 3 (upload, listagem, delete) | ✅ 3 |
| Telas FE | 2 (upload modal, listagem) | ✅ 2 |
| Testes isolamento | 8+ | ✅ 8+ |
| Storage local | Funcional | ✅ Funcional |
| Documentação | Endpoints + Postman | ✅ Completa |
| Todos rodando localmente | 100% | ✅ 100% |

---

## Status Final da Semana 10

### ✅ Concluído

- ✅ Upload de documentos (multipart/form-data) com validações rigorosas
- ✅ Armazenamento seguro em disco local (prep para GCS)
- ✅ Listagem filtrada por seleção (isolamento garantido)
- ✅ Soft-delete com rastreabilidade completa
- ✅ Interface de upload com progresso e feedback
- ✅ Listagem com paginação, filtros, status visual
- ✅ Testes de isolamento bloqueadores
- ✅ CI/CD com coverage checking
- ✅ Documentação completa (endpoints + Postman)
- ✅ StorageService preparado para GCS

### ⏳ Pronto para S11

- ✅ Backend pronto para integração GCS
- ✅ Frontend pronto para novas features (aprovação laudos)
- ✅ DevOps com volume Docker funcional
- ✅ Isolamento verificado em cada PR

---

## Aprendizados e Desafios

### Desafios Enfrentados

1. **Primeiro contato com BE (Caio) e FE (Josef):**
   - Caio aprendeu endpoint design, validações, armazenamento
   - Josef aprendeu Vue composables, Axios, paginação
   - Pair programming com âncoras (Arthur/João) intensivo

2. **Validações de segurança no servidor:**
   - Decisão: nunca confiar no cliente
   - python-magic para MIME type real (não extensão)
   - Validação de tamanho, tipo, formatos

3. **Isolamento em upload:**
   - Garantir selection_id vem do token
   - Testes que bloqueiam violações
   - Nenhum cenário permite cross-selection

4. **Storage abstraction:**
   - Design para migração local → GCS
   - Interface StorageService pronta
   - Transição S10 → S11 será transparente

### Sucessos

1. **Isolamento comprovado:** Testes passando, CI bloqueador funcionando
2. **Core funcional entregue:** Usuários podem fazer upload e ver documentos
3. **Interface intuitiva:** Upload com progresso, listagem com filtros
4. **Rastreabilidade completa:** AuditLog registando todas as ações
5. **Preparação para produção:** StorageService abstract, pronto para GCS

---

## Próxima Sprint: Semana 11

**Semana 11 – Cloud Storage: Migração para Google Cloud Storage**

Foco: Migrar storage de local para GCS mantendo abstração, implementar links temporários assinados, preparar para produção.

**Divisão Equipa (Rotação):**
- Backend: Caio (Âncora) + Júlia
- Frontend: José (Âncora) + Arthur
- DevOps: Arthur (Protagonista) + João (Âncora)
- Docs: João

**Issues S11:**
- [S11-BE-01] Implementar GCSStorageService
- [S11-BE-02] Integrar links temporários assinados
- [S11-DO-01] Configurar credenciais GCP e buckets
- [S11-DO-02] Preparar deploy em Google Cloud Run
- [S11-FE-01] Ajustar componentes para GCS URLs
- [S11-QA-01] Testes de integração com GCS

**Métrica de Sucesso:** Upload persiste em GCS, links temporários expiram em 15 min, isolamento mantido, nenhuma URL GCS exposta diretamente.

---

## Comparação: S9 vs S10

| Aspecto | S9 (Autenticação) | S10 (Upload/Listagem) |
|---------|---|---|
| Issues | 13 | 8 |
| Endpoints | 3 (auth) | 3 (document CRUD) |
| Novos membros BE | 1 (Arthur) | 1 (Caio) |
| Novos membros FE | 1 (João) | 1 (Josef) |
| Core funcional | Segurança | Produto |
| Teste bloqueador | Autenticação | Isolamento |
| Tecnologia nova | JWT, bcrypt | python-magic, FormData |
| Preparação futura | GitHub Pages | StorageService abstract |

**Conclusão:** S9 foi preparatória (segurança), S10 entregou o core do produto (upload/listagem). Equipa cresceu em capacidade, novos membros em BE/FE tiveram experiência real em features críticas.