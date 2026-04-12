# Git e GitHub — Resumo Técnico

## Entendendo a diferença

Apesar de serem frequentemente tratados como sinônimos, Git e GitHub são coisas distintas que se complementam.

O **Git** é uma ferramenta instalada localmente no computador. Ela rastreia todas as mudanças feitas nos arquivos de um projeto, permitindo voltar a versões anteriores e trabalhar em equipe sem sobrescrever o trabalho dos outros.

O **GitHub**, por sua vez, é um serviço online. Ele funciona como um repositório remoto onde o código versionado pelo Git pode ser armazenado, compartilhado e colaborado por outras pessoas.

> Em resumo: Git controla as versões, GitHub hospeda o projeto.

---

## Comandos essenciais

Abaixo estão os comandos mais usados no dia a dia com Git:

| Comando | O que faz |
|---|---|
| `git init` | Cria um repositório novo na pasta atual |
| `git clone <url>` | Baixa uma cópia de um repositório remoto |
| `git status` | Exibe quais arquivos foram modificados |
| `git add .` | Marca os arquivos para serem incluídos no próximo commit |
| `git commit -m "mensagem"` | Registra as mudanças com uma descrição |
| `git push` | Envia os commits para o repositório remoto |
| `git pull` | Baixa e aplica as atualizações do repositório remoto |
| `git branch` | Lista as branches existentes no projeto |
| `git checkout <branch>` | Muda para a branch indicada |

---

## Como funciona na prática

O fluxo de trabalho com Git segue uma lógica simples:

1. **Clonar ou iniciar** o repositório
2. **Editar** os arquivos do projeto
3. **Adicionar** as mudanças com `git add`
4. **Confirmar** as alterações com `git commit`
5. **Enviar** para o GitHub com `git push`

Esse ciclo se repete a cada nova alteração, mantendo o histórico do projeto sempre atualizado.

---

## Por que usar?

Além de evitar a perda de código, o Git permite que várias pessoas trabalhem no mesmo projeto ao mesmo tempo, cada uma em sua própria branch, sem interferir no trabalho umas das outras. Isso torna o desenvolvimento mais organizado, seguro e rastreável.
