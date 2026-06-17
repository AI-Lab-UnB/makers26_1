## Conceitos Fundamentais

### Git
- Sistema de controlo de versões **distribuído**
- Guarda uma cópia completa do repositório localmente
- Funciona como uma **"máquina do tempo"** para o código
- Permite rastrear alterações e reverter versões

### GitHub
- Plataforma web para hospedar repositórios Git
- Facilita colaboração com:
  - Issues
  - Pull Requests
  - GitHub Actions (CI/CD)
  - Wikis
  - Gestão de projetos

---

### Configuração inicial

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
git config --global init.defaultBranch main

---

### Fluxo do Git
Working Directory → Staging Area → Repositório Local → Repositório Remoto

---

### Comandos do Git
git init              # Inicializa um repositório
git status            # Mostra o estado dos arquivos
git add .             # Adiciona arquivos ao staging
git commit -m "msg"   # Cria um commit
git push              # Envia para o repositório remoto
git pull              # Atualiza repositório local
git clone <url>       # Clona um repositório
git fetch             # Baixa alterações sem aplicar
git log               # Histórico de commits


## Branching e Pull Requests

### Criar e mudar de branch

```bash
git checkout -b feature/login

### Enviar Branch
```bash
git push -u origin feature/login

## Fluxo de trabalho
Criar uma nova branch
Desenvolver a funcionalidade
Commitar as alterações
Abrir um Pull Request no GitHub
Revisar e fazer o merge

## Merge e Limpeza
git merge feature/login       # Merge local  
git branch -d feature/login   # Deleta branch local  
git pull origin main          # Atualiza branch principal

### Observações:
Faltou a parte de Integração continua com o Vercel e alguns aspectos de CI e CD, pois esse eu não consegui entender direito pelo vídeo e vou precisar revisar e aprender de outra forma.


## Reflexão individual:  “O que é desenvolvimento profissional?”
Desenvolvimento profissional para mim é o processo de melhoria continua no que tange o ambito profissional, isto é, melhorar a comunicação caso seja um aspecto importante para a área profissional, melhorar a execução tornar as ações e tarefas mais praticas e sustentáveis, além de claro conhecimento se tornando cada vez mais autonomo e com capacidade para resolver problemas.