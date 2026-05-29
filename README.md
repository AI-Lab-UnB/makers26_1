# makers26_1

Repositório oficial de entregas das demandas do **Programa AILAB Makers 2026.1**.

O AILAB Makers é uma iniciativa de formação prática em Inteligência Artificial e desenvolvimento de software, com foco em desenvolvimento colaborativo, resolução de problemas reais, disciplina técnica, versionamento profissional e entrega funcional. Neste ciclo, o foco está na consolidação de fundamentos em programação, engenharia de software e implantação de sistemas em nuvem.

---

## Objetivo deste repositório

Este repositório foi criado para concentrar as entregas técnicas dos participantes do programa ao longo do ciclo 2026.1.

Aqui deverão ser registradas as atividades, evoluções, entregas parciais e contribuições dos alunos e dos grupos, seguindo a política de Git e entregas definida para o ciclo.

---

## Fases do ciclo (visão integrada)

O ciclo está organizado em duas etapas complementares:

- **Fase 1 (formação estruturada):** fortalecimento de fundamentos técnicos, cultura de engenharia, organização profissional via Git e preparação para desenvolvimento aplicado.
- **Fase 2 (projeto aplicado em nuvem):** desenvolvimento em grupo de uma aplicação web real, com autenticação, controle de acesso, upload/listagem de documentos, logs auditáveis e deploy em nuvem.

Essa organização mantém continuidade entre aprendizado e execução prática, com foco em rotina profissional de desenvolvimento.

---

## Regras obrigatórias (oficiais da Fase 2)

Todos os participantes devem seguir obrigatoriamente:

- **Branch individual por aluno na Fase 1 e branch por grupo na Fase 2**
- **Padrão de branch: `[nome]_[matricula]` (Fase 1) ou `grupo[numero]` (Fase 2)**
- **Pull Request obrigatório**
- **Code review obrigatório**
- **Atenção aos PRs: as avaliações serão feitas por eles; cada grupo deve manter PRs atualizados e sem conflitos**

### Regras de entregas e acompanhamento

- O não cumprimento das 4 horas presenciais, sem justificativa, resulta em advertência de faltas.
- 3 advertências de faltas levam ao desligamento.
- 2 semanas sem commits geram advertência de produtividade.
- 2 advertências de produtividade levam ao desligamento.
- Plágio leva ao desligamento imediato.
- Não conclusão da formação impede a participação nas fases posteriores.
- Entregas com atraso não justificado terão desconto na nota.
- Entregas de baixíssima qualidade terão desconto na nota.
- O não cumprimento dos padrões das atividades e das regras do laboratório pode levar a advertência ou desligamento.

### Regras do projeto e do laboratório

- Não trazer pessoas de fora do projeto para o laboratório.
- Manter o laboratório organizado.
- Se for o último a sair, desligar tudo e fechar.
- Evitar uso do laboratório às quartas-feiras, de 14h30 às 15h.
- Manter um ambiente agradável e silencioso.
- Todos os padrões passados devem ser seguidos.

---

## Organização esperada

Cada participante deve:

1. Trabalhar na branch correta da fase (individual na Fase 1, grupo na Fase 2)
2. Registrar evolução com frequência
3. Abrir Pull Requests das entregas e atualizações realizadas
4. Participar do processo de code review
5. Manter os materiais organizados e rastreáveis no repositório

O uso correto do Git faz parte da formação do programa e compõe a avaliação dos participantes.

---

## Desafio técnico do ciclo

Após a formação técnica inicial, os estudantes desenvolvem em equipe uma aplicação web autenticada implantada na Google Cloud.

O desafio envolve:

- autenticação e controle de acesso
- persistência de dados
- armazenamento de documentos
- registro de eventos e auditoria
- implantação em ambiente cloud

A aplicação deve contemplar funcionalidades como:

- cadastro
- login
- upload
- listagem
- download
- exclusão

---

## Cronograma resumido da Fase 2 (Semanas 7 a 14)

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

---

## Temas sugeridos para projetos

- Repositório Acadêmico de Artigos e Pesquisas (EdTech)
- Portal de Gestão de Seleções ("FIFA Team Hub")
- Sistema de Gestão de Prontuários e Exames (HealthTech)
- Sistema de Admissão de Funcionários (Onboarding Digital)

Se o grupo quiser propor outro tema, a proposta deve ser validada por Marina ou Rafael antes do início do desenvolvimento. Não pode haver tema repetido entre os grupos.

---

## Grupos e integrantes

| Grupo 1 | Grupo 2 | Grupo 3 | Grupo 4 |
| --- | --- | --- | --- |
| Alana Cristyna Feitosa Dias | Hugo Sousa Rosa | Guilherme Negreiros Pereira | Arthur Miguel Silva Rocha |
| Arthur Carvalho Leite | Martin Quadros De Melo | Matheus Eiki Kimura Rezede | João Vítor Sauma de Faria |
| Mariana Souza Farias Andrade | Gabriel Robson Nunes Neiva da Silva | Eduardo Jesus Dal Pizzol | Júlia Santana Campos |
| Pedro Henrique Pereira Santos | Luiza Carneiro Carvalho | Nina Rosa Alves Amorim | Caio Felipe Alcantara Nascimento |
| Luis Gustavo Ferreira Nunes | Diogo Oliveira Ferreira | Raissa Silva de Oliveira | Josef Wojtyla Barros de Souza |
| Mateus Alves Araújo | Lucas De Paula Leal | Thomaz Marra Martins |  |

---

## Papéis sugeridos nos grupos

- Líder técnico: acompanha decisões técnicas, integra entregas e ajuda o grupo a manter o escopo.
- Backend: organiza API, autenticação, regras de acesso, banco e logs.
- Frontend: organiza telas, fluxos de autenticação, upload, listagem e experiência do usuário.
- DevOps: acompanha deploy, variáveis de ambiente, storage, banco em nuvem e documentação de execução.
- Documentação e Logs: garante README, evidências, diagramas, logs auditáveis e organização da entrega.

---

## Checklist semanal de acompanhamento

- [ ] Todos os integrantes cumpriram as 4 horas presenciais?
- [ ] Cada integrante realizou commits na semana?
- [ ] Existe PR aberto, atualizado e sem conflitos?
- [ ] O grupo registrou o que foi feito na semana?
- [ ] A entrega da semana está funcionando minimamente?
- [ ] O README ou documentação foi atualizado?
- [ ] Há evidência de teste, print, vídeo ou URL quando necessário?
- [ ] Há pendências ou bloqueios para informar aos tutores?

---

## Boas práticas para participação

Para um bom acompanhamento da participação no programa, recomenda-se:

- fazer commits frequentes e com mensagens claras
- manter a branch organizada
- abrir PRs bem descritos
- revisar o código dos colegas com responsabilidade
- documentar aprendizados, decisões e entregas sempre que necessário

---

## Estrutura

A estrutura interna pode variar no decorrer do projeto, mas a organização atual é:

```bash
makers26_1/
├── README.md
├── Entregas_Fase_1/
│   ├── Semana1/
│   ├── Semana2a4/
│   └── Semana5e6/
└── Entregas_Fase_2/
    ├── Grupo1/
    ├── Grupo2/
    ├── Grupo3/
    └── Grupo4/
```

---

## Modelo de Pull Request

### Contexto

Exemplo:
Este PR introduz a entrega da **Semana XX**, contendo os materiais desenvolvidos conforme as orientações da atividade proposta.

Os arquivos foram organizados na pasta correspondente e nomeados de acordo com o padrão definido no repositório, para facilitar a identificação e a revisão.

### O que foi adicionado

Exemplos:
- Arquivo(s) referente(s) à atividade da semana
- Documento(s), código(s), imagem(ns), relatório(s) ou outro(s) artefato(s) solicitado(s)
- Estrutura organizada de acordo com o modelo de entrega individual ou em grupo
- Conteúdo revisado antes do envio

### Tipo de Mudança

- [ ] Correção de Bug
- [ ] Nova Funcionalidade
- [ ] Documentação
- [ ] Refatoração
- [ ] Configuração
- [ ] Entrega acadêmica

### Checklist

- [ ] Arquivo/pasta nomeado conforme o padrão do projeto
- [ ] Entrega colocada na pasta correta
- [ ] Branch identificada corretamente para a fase (individual ou grupo)
- [ ] Conteúdo revisado
- [ ] Nenhuma informação sensível exposta
- [ ] Arquivos organizados corretamente
- [ ] Markdown renderiza corretamente, quando aplicável

### Notas para o Revisor

Exemplos:
- A entrega foi feita individualmente.
- A entrega contém mais de um arquivo, por isso foi organizada em uma pasta própria.
- O conteúdo segue exatamente o que foi solicitado na atividade.
- Em caso de entrega em grupo, os arquivos foram organizados com a identificação do grupo.

---

## Instruções completas da Fase 2 por grupo

O conteúdo integral da apresentação da Fase 2 foi adicionado em Markdown nas pastas de cada grupo:

- `Entregas_Fase_2/Grupo1/instrucoes_fase_2.md`
- `Entregas_Fase_2/Grupo2/instrucoes_fase_2.md`
- `Entregas_Fase_2/Grupo3/instrucoes_fase_2.md`
- `Entregas_Fase_2/Grupo4/instrucoes_fase_2.md`
