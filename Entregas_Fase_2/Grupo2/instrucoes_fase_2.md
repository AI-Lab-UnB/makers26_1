AILAB MAKERS

Apresentação da Fase 2

Projeto Aplicado em Nuvem | Semanas 7 a 14

Laboratório de Inteligência Artificial – AILAB FCTE – Universidade de Brasília

# 1. O que é a Fase 2?

A Fase 2 é o momento em que os participantes deixam a formação estruturada e passam a trabalhar em grupo em um projeto aplicado. O objetivo é planejar, desenvolver, documentar e apresentar uma aplicação web real, com autenticação, controle de acesso, upload/listagem de documentos, logs auditáveis e implantação em nuvem.

Nesta etapa, a avaliação considera tanto o resultado técnico quanto a organização do grupo: uso do Git, qualidade dos PRs, participação semanal, presença no laboratório, documentação e capacidade de demonstrar o funcionamento da aplicação.

# 2. Desafio da Fase 2

Cada grupo deverá desenvolver uma aplicação web implantada na Google Cloud que atenda aos requisitos mínimos abaixo:

- Permitir cadastro e autenticação de usuários.

- Permitir upload de documentos.

- Listar documentos vinculados ao usuário autenticado.

- Garantir isolamento entre usuários.

- Registrar logs auditáveis das principais ações.

- Implantar a aplicação em ambiente de nuvem.

# 3. Cronograma resumido

| Semana | Foco | Entrega esperada |
| --- | --- | --- |
| Semana 7 | Planejamento | Formação de grupos, definição de tema, papéis, arquitetura, stack e repositório. |
| Semana 8 | Estrutura inicial | Setup do backend, frontend, banco e autenticação inicial. |
| Semana 9 | Autenticação e controle de acesso | Cadastro, login, hash de senha, sessão/JWT e rota protegida. |
| Semana 10 | Upload e listagem | Upload funcional, associação com usuário e listagem filtrada. |
| Semana 11 | Storage e persistência | Integração com Google Cloud Storage e metadados persistidos. |
| Semana 12 | Logging e auditoria | Logs de login, logout, upload, download, exclusão e tentativas inválidas. |
| Semana 13 | Deploy em Google Cloud | Deploy público, banco em nuvem e storage configurado. |
| Semana 14 | Demonstração final | Apresentação da arquitetura, código, segurança, logs e deploy. |

# 4. Ideias de temas sugeridos

As opções abaixo são apenas sugestões, mas são sugestões bem elaboradas e pensadas para o tempo disponível de desenvolvimento. Por isso, recomendamos que os grupos escolham uma delas sempre que fizer sentido para o interesse do grupo.

Caso o grupo queira escolher outro tema, deve apresentar a proposta para Marina ou Rafael antes de iniciar o desenvolvimento. Não pode haver tema repetido: cada grupo deve trabalhar com um tema diferente.

### Repositório Acadêmico de Artigos e Pesquisas (EdTech)

Sistema voltado para laboratórios universitários, grupos de iniciação científica ou programas de pós-graduação centralizarem publicações, relatórios e datasets.

- Upload de documentos: Artigos em PDF, relatórios de pesquisa, dissertações e datasets.

- Isolamento: Rascunhos de pesquisas não publicadas ficam visíveis apenas para os autores e orientadores do projeto.

- Logs auditáveis: Controle de versões, registro de quem atualizou o rascunho e histórico de acesso a dados de pesquisa.

### Portal de Gestão de Seleções – “FIFA Team Hub”

Software para comissões técnicas de seleções, auditores e organizadores. O objetivo é centralizar a submissão oficial de listas de convocados, documentação de viagem, laudos médicos e relatórios táticos.

- Upload de documentos: Lista oficial de convocação, imagens de passaportes, laudos médicos, relatórios táticos e esquemas de jogadas.

- Isolamento entre usuários: Cada seleção funciona como um ambiente isolado. A comissão técnica do Brasil, por exemplo, não pode acessar documentos da Argentina. Organizadores/admins podem ter visão restrita da documentação burocrática.

- Logs auditáveis: Registro preciso de quem enviou a lista final, quando enviou, submissão/aprovação de laudos médicos e tentativas de acesso negado entre seleções.

### Sistema de Gestão de Prontuários e Exames (HealthTech)

Plataforma para clínicas ou profissionais de saúde independentes onde pacientes e médicos podem gerenciar resultados de exames e documentos médicos.

- Upload de documentos: PDFs de laudos, imagens de raio-x, receitas médicas e exames.

- Isolamento: Um paciente só acessa seus próprios exames; um médico só visualiza documentos dos pacientes vinculados a ele.

- Logs auditáveis: Registro de quem acessou, baixou ou alterou um laudo, simulando necessidades de conformidade como LGPD/HIPAA.

### Sistema de Admissão de Funcionários (Onboarding Digital)

Software para departamentos de RH e novos colaboradores, com foco em automatizar e centralizar o recebimento de documentos admissionais de forma segura.

- Upload de documentos: CNH, comprovante de residência, diplomas, documentos pessoais e formulários admissionais.

- Isolamento: Um candidato ou colaborador não pode acessar documentos de outro.

- Logs auditáveis: Registro de quando o RH validou, aprovou ou solicitou ajustes em cada documento enviado.

Espaço para definição do tema escolhido por grupo:

| Grupo | Tema escolhido | Aprovado por Marina/Rafael? |
| --- | --- | --- |
| Grupo 2 |  |  |

# 5. Grupos e integrantes

| Grupo 2 |
| --- |
| Hugo Sousa Rosa |
| Martin Quadros De Melo |
| Gabriel Robson Nunes Neiva da Silva |
| Luiza Carneiro Carvalho |
| Diogo Oliveira Ferreira |
| Lucas De Paula Leal |

# 6. Papéis sugeridos nos grupos

Os papéis abaixo ajudam a distribuir responsabilidades. Eles não impedem colaboração: todos devem entender o projeto como um todo e participar das entregas.

| Papel | Responsabilidade principal |
| --- | --- |
| Líder técnico | Acompanha decisões técnicas, integra entregas e ajuda o grupo a manter o escopo. |
| Backend | Organiza API, autenticação, regras de acesso, banco e logs. |
| Frontend | Organiza telas, fluxos de autenticação, upload, listagem e experiência do usuário. |
| DevOps | Acompanha deploy, variáveis de ambiente, storage, banco em nuvem e documentação de execução. |
| Documentação & Logs | Garante README, evidências, diagramas, logs auditáveis e organização da entrega. |

# 7. Regras de entregas e acompanhamento

- O não cumprimento das 4 horas presenciais, sem justificativa, resulta em advertência de faltas.

- 3 advertências de faltas levam ao desligamento.

- 2 semanas sem commits geram advertência de produtividade.

- 2 advertências de produtividade levam ao desligamento.

- Plágio leva ao desligamento imediato.

- Não conclusão da formação impede a participação nas fases posteriores.

- Entregas com atraso não justificado terão desconto na nota.

- Entregas de baixíssima qualidade terão desconto na nota.

- O não cumprimento dos padrões das atividades e das regras do laboratório pode levar a advertência ou desligamento.

# 8. Regras do projeto e do laboratório

- Não trazer pessoas de fora do projeto para o laboratório.

- Manter o laboratório organizado.

- Se for o último a sair, desligar tudo e fechar.

- Evitar uso do laboratório às quartas-feiras, de 14h30 às 15h.

- Manter um ambiente agradável e silencioso.

- Atenção aos PRs: é por lá que as avaliações serão feitas. É responsabilidade de cada grupo manter os PRs sem conflitos e atualizados.

- Todos os padrões passados devem ser seguidos.

# 9. Checklist de acompanhamento semanal

| Item | Sim/Não | Observações |
| --- | --- | --- |
| Todos os integrantes cumpriram as 4 horas presenciais? |  |  |
| Cada integrante realizou commits na semana? |  |  |
| Existe PR aberto, atualizado e sem conflitos? |  |  |
| O grupo registrou o que foi feito na semana? |  |  |
| A entrega da semana está funcionando minimamente? |  |  |
| O README ou documentação foi atualizado? |  |  |
| Há evidência de teste, print, vídeo ou URL quando necessário? |  |  |
| Há pendências ou bloqueios para informar aos tutores? |  |  |

# 10. Observações finais

A Fase 2 deve ser tratada como um projeto real: com organização, colaboração, cuidado com qualidade e responsabilidade nas entregas. O objetivo não é apenas entregar uma aplicação, mas praticar uma rotina profissional de desenvolvimento em equipe.
