# Resumo das Atividades

## Semana 10 – Sprint 4: Módulo de Arquivos, Vínculo Médico-Paciente e Integração Frontend-Backend

Esta semana representou a primeira entrega de integração sistêmica completa do projeto, com a implementação da funcionalidade central de negócio (gerenciamento de arquivos médicos), a camada de autorização por tipo de usuário e a unificação da identidade visual do frontend:

**Backend (Autenticação e Guards por Tipo):**
Implementamos a identificação do tipo de usuário diretamente no payload do JWT no momento do login (#19). O `RolesGuard` foi criado para verificar o campo `tipo` do token e proteger rotas restritas por perfil: rotas de médico retornam `403` para pacientes e vice-versa, sem necessidade de consulta adicional ao banco. Luíza implementou o guard e escreveu testes de integração via Supertest validando o comportamento de acesso negado para cada tipo.

**Backend (Módulo de Arquivos):**
Martin criou a entidade `Arquivo` com TypeORM (#26), incluindo os campos `nomeOriginal`, `nomeUnico` (UUID gerado pelo backend, nunca o nome fornecido pelo usuário), `tipo`, `tamanho`, `caminhoStorage`, além das FKs para o paciente dono e para o médico que realizou o upload. Um DTO de resposta estrito foi implementado garantindo que `caminhoStorage` nunca apareça nas respostas da API. Testes de segurança verificam automaticamente essa omissão. Hugo implementou o `StorageService` (#27) com geração de nome único por UUID e integração com o Google Cloud Storage, além de testes unitários cobrindo o gerador de nomes.

**Backend (Módulo MedicoPaciente):**
Hugo criou o módulo `MedicoPaciente` completo (#29): entity com chave primária composta `(medicoId, pacienteId)` — garantindo que o mesmo par não seja vinculado duas vezes — DTO, controller e service com os quatro endpoints (`POST /vincular`, `DELETE /desvincular`, `GET /meus-pacientes`, `GET /meus-medicos`). Martin adicionou testes unitários do service cobrindo criação, remoção e listagens.

**Backend (Correções e Alinhamento):**
Diogo atuou na fase de integração: removeu o prefixo global `/api` das rotas, alinhou as estruturas de DTOs, adicionou validação de CPF no frontend e backend, corrigiu o `cloudbuild.yaml` e ajustou as URLs de comunicação entre frontend e backend. Ao total, 9 commits de correção e configuração foram necessários para estabilizar o ambiente integrado.

**Frontend (Identidade Visual e Cadastro Unificado):**
Lucas liderou a refatoração visual completa das páginas de login e cadastro (#18) em 13 commits ao longo da semana. As variáveis CSS foram centralizadas em `globals.css` com a paleta de cores definida na identidade visual do projeto (`--color-primary: #1e4969`, `--color-secondary: #368ca0`). A fonte Inter foi integrada, logos vetorizadas e favicon foram substituídos. O formulário de cadastro foi unificado: um único formulário com radio buttons para seleção do tipo de usuário (Paciente ou Médico) exibe dinamicamente os campos específicos de cada perfil (CPF e data de nascimento para paciente; CRM e especialidade para médico). O redirecionamento pós-login direciona automaticamente para `/paciente` ou `/medico` conforme o tipo retornado no token.

**Gestão:**
Semana de maior volume de commits do ciclo até então: 38 commits distribuídos entre Lucas (13), Diogo (9), Hugo (8), Martin (5) e Luíza (2). Três branches foram mergeadas via PRs revisados: `feat/medico-paciente` (#40), `feat/arquivo-migration` (#42) e `feat/integracao-banco` (#45).
