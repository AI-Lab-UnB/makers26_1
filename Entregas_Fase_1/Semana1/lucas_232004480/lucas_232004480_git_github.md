## Git e GitHub Resumo técnico

### 1. O que é Git
Git é um sistema de controle de versão distribuído que permite rastrear mudanças no código-fonte durante o desenvolvimento de software. Ele registra o histórico do projeto como uma sequência de commits, cada um representando uma versão do código em um momento específico.

Com Git, você pode:
- voltar para versões antigas do projeto;
- comparar o que mudou entre duas versões;
- trabalhar em ramificações diferentes sem afetar o trabalho principal.

---

### 2. O que é GitHub
GitHub é uma plataforma online que hospeda repositórios Git e facilita a colaboração entre desenvolvedores.

GitHub oferece:
- repositórios remotos para guardar o código;
- controle de acesso com permissões para equipes;
- pull requests para revisão e aprovação de mudanças;
- issues para organizar tarefas, bugs e melhorias;
- GitHub Actions para automação de testes e deploy;
- GitHub Pages para publicar sites estáticos.

Além disso, GitHub inclui recursos de documentação, monitoramento de dependências e segurança.

---

### 3. Como começar: instalando e configurando o Git

**Windows**
- Baixe o instalador em [git-scm.com](https://git-scm.com).
- Execute o instalador e aceite as opções padrão.
- Abra o Git Bash ou PowerShell.

**Linux**
- Use o gerenciador de pacotes da sua distribuição:
  - Debian/Ubuntu: `sudo apt install git`
  - Fedora: `sudo dnf install git`
  - Arch: `sudo pacman -S git`
- Abra o terminal.

Após instalar o Git, configure seu nome e email:

```
git config --global user.name "Seu Username"            # Configura o nome de usuário globalmente
git config --global user.email "seuemail@example.com"   # Configura o email globalmente
```
---

### 4. Primeiros comandos básicos do Git

```
git init            # Inicializa um repositório Git local
git add <arquivo>   # Adiciona um arquivo ao stage
git add .           # Adiciona todos os arquivos modificados ao stage
git status          # Verifica o estado dos arquivos
git log             # Exibe o histórico de commits
```
---

### 5. Clonar um repositório do GitHub
Para trabalhar com um projeto existente do GitHub, use o clone:

```
git clone <URL do repositório>  # Clona o repositório remoto para o computador
```
---

### 6. Criar repositório local e conectar ao GitHub
Crie um repositório local e, depois, vincule-o a um repositório remoto no GitHub:

```
git init                        # Inicializa um repositório local
git remote add origin <URL>     # Adiciona o repositório remoto
git push -u origin main         # Envia o histórico para o GitHub
```
---

### 7. Como fazer commits
Para salvar mudanças no histórico local:

```
git add <arquivo>                       # Adiciona arquivo ao stage
# ou
git add .                               # Adiciona todos os arquivos modificados ao stage

git status                              # Verifica o que está staged
git commit -m "Mensagem descritiva"     # Salva as mudanças com uma mensagem
```

Se o repositório já estiver conectado ao GitHub:

```
git push                                # Envia as mudanças para o GitHub
```
---

### 8. O que é o git pull
`git pull` baixa mudanças do repositório remoto e as mescla na branch local.

```
git pull        # Baixa e mescla mudanças do remoto
git fetch       # Baixa mudanças sem mesclar
git merge       # Mescla mudanças localmente
```
---

### 9. Como funciona as branches
Branches são ramificações do projeto. A branch principal é geralmente `main`, e outras branches servem para desenvolver recursos ou corrigir bugs sem afetar o código principal.

Comandos comuns de branch:

```
git branch              # Lista branches
git checkout -b <nome>  # Cria e muda para nova branch
git checkout <nome>     # Muda para branch existente
git merge <branch>      # Mescla outra branch na branch atual
```
---

### 10. O que é Pull request
Pull request (PR) é uma solicitação no GitHub para revisar e mesclar mudanças de uma branch em outra. Permite comentários, revisão de código e aprovação antes da integração.

---

### 11. Merging
Merging combina mudanças de uma branch para outra. Se houver alterações conflitantes no mesmo arquivo, o Git pedirá que você resolva o conflito manualmente.

```
git merge <branch>  # Mescla a branch indicada na branch atual
```
---

### 12. SSH Keys
SSH Keys são chaves criptográficas usadas para autenticação segura com o GitHub.

---

### 13. O que é o README
`README.md` é o arquivo que descreve o projeto, explica sua finalidade, como instalar e como usar.

---

### 14. O que é o .gitignore
`.gitignore` lista arquivos e pastas que o Git deve ignorar, como arquivos gerados, de configuração local ou dados sensíveis.

---



