# Entrega Semana 1 - Martin - 251026239

## 1. Resumo Técnico: Git & GitHub Crash Course 2025

### Git vs. GitHub
* **Git:** É um Sistema de Controle de Versão (VCS) distribuído. Ele funciona localmente na máquina do desenvolvedor, Que rastreia mudanças no código, permite reverter alterações e facilita o trabalho em diferentes funcionalidades sem quebrar o projeto principal.
* **GitHub:** É uma plataforma web de hospedagem de repositórios remotos. Enquanto o Git faz o gerenciamento do código, o GitHub facilita a colaboração entre equipes, permitindo Pull Requests, revisão de código (Code Review), gerenciamento de issues e integração contínua.

### Principais Comandos Abordados
* `git init`: Inicializa um novo repositório local (cria a pasta oculta `.git`).
* `git clone`: Baixa um repositório remoto para a máquina local.
* `git status`: Verifica o estado atual dos arquivos (rastreados, não rastreados, modificados).
* `git add <arquivo>` ou `git add .`: Move as alterações para a Staging Area.
* `git commit -m "mensagem"`: Salva o estado dos arquivos no repositório local com uma mensagem descritiva.
* `git push`: Envia os commits locais para o repositório remoto.
* `git pull`: Puxa as atualizações mais recentes do repositório remoto para a máquina local.

### Branching e Pull Requests
As **Branches** (ramificações) são cruciais para o trabalho em equipe. Elas criam ambientes isolados (ex: `feature/login`) onde o desenvolvedor pode modificar livremente sem afetar a (`main`). Quando a funcionalidade está pronta, o código é enviado para o GitHub e abre-se um **Pull Request (PR)**, solicitando que a equipe revise o código antes de fundi-lo (merge) com a versão oficial do projeto.