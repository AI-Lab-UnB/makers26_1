# ------------------------------GitHub-&-Git--------------------------------- 

Resumo técnico explicitando a plataforma do GitHub e sua Ferramenta Git.

---
## ================[ GitHub: a plataforma de colaboração ]==================     

Plataforma de hospedagem e colaboração baseada em nuvem que usa do sistema Git para o controle de versão.
Ele funciona como o hub central para projetos de software, com uma interface gráfica que facilita o gerenciamento de repositórios, a revisão de código (Pull Requests) e o rastreamento de problemas. 
Além disso, a plataforma também pode funcionar como uma rede social para desenvolvedores compartilhar seus portfólios e a contribuirem em projetos open-source.

## =================[ Git: o sistema de controle de versão ]==================

Software de controle de versões desenhado por Linus Torvald, o criador do Linux. Sua principal função é a de monitorar alterações nos arquivos, permitindo que múltiplos colaboradores trabalhem simultaneamente em diferentes funcionalidades através de ramificações (branches), sem que um sobrescreva o trabalho do outro.

---

## =================[ Git Workflow: o fluxo do trabalho ]===================

Estruturado por três camadas: working directory, staging area e local repository.

No **working directory**, é a pasta no seu computador onde os arquivos do seu projeto estão fisicamente localizados e onde você realiza as edições.

No **staging area** (Área de Retenção), também chamada de Index, é a sala de espera do Git. É onde é selecionado e organizado as mudanças feitas no working directory. 

No **local repository**, terceira e última etapa do fluxo de trabalho. Onde o Git armazena o histórico de todas as versões, ramificações (branches) e commits do projeto.

---
## || Operações Fundamentais para o Ciclo Basico ||
São as operações que possibilitam o trajeto seguro de arquivos de um repositorio local ao remoto e vice-versa.
### `I. --> git init`
    git init
Comando utilizado na inicialização de um novo repositório local na pasta do seu projeto (diretório de trabalho)

Isso cria uma nova pasta oculta nomeada por **`.git`**, onde é feito o armazenamento de dados essenciais como o proprio historico, referências de branches e a pasta objects, por exemplo. Além disso, permitindo o funcionamento das operações do git.

### `II. --> git add`
    git add <arquivo1> <arquivo2> //--> adiciona arquivos especificos 
    // ou 
    git add . //--> para adicionar todo o dir. atual 

Comando de preparação das alterações feita no diretorio de trabalho (working directory) para o commit, movendo-as, então, para a Área de Retenção. (staging area)

### `III. --> git commit`
    git commit -m 'msg'

Comando de registro de alterações preparadas na staging area no repositório local, criando um "ponto de verificação" no histórico.

Utilize o comando **`git commit -m 'msg'`** para gerar seu commit com descrição. Boas pratícas do git!

### `IV. --> git remote`
    git remote add [nome] [url]
Comando que gerencia conexões com repositórios remotos, permitindo visualizar, adicionar, remover ou renomear atalhos (como origin) para URLs de projetos hospedados.

Por convenção o campo **`<nome>`** é chamado por padrão de "origin." Serve como um atalho para a url do repositório remoto.

### `V. --> git push`
    git push [nome-repo] [nome-da-branch]
Comando que envia commits locais para um repositório remoto. Atualizando a branch remota com as alterações da branch local, permitindo a colaboração.

### `VI. --> git pull`
    git pull [nome-repo-remoto] [nome-branch]
Comando que atualiza o repositório local com as alterações de um repositório remoto.
Sendo a combinação de dois comandos em sequência: **`git fetch`** e **`git merge`**.

> **git fetch**: Baixa os novos commits do servidor remoto, mas sem alterar os arquivos locais.

> **git merge**: Mescla automaticamente essas alterações no branch atual de trabalho.

### `VII. --> git clone`
    git clone [url-do-repositorio] nome-da-pasta
Comando que cria uma cópia local de um repositório remoto existente, baixando a versão mais recente e todo o histórico de commits e branches.

### `VIII. --> git status & git log`
    git status
    git log

No **git status**, este comando mostra o estado atual da pasta de trabalho e da staging area, exibindo informações sobre arquivos que foram modificados, deletados ou novos. 
É eficiente para entender o que foi acrescentado com o git add e o que está pronto para o commit.

No **git log**, este comando exibe o histórico de commits passados que já foram salvos no repositório remoto.

### `IX. --> git checkout & git branch` 
    git checkout [nome-da-branch] //--> Troca de branch
    git checkout -b [nome-da-branch] //--> Cria e troca de branch
    git checkout -- <arquivo> //--> Desfaz alterações locais em um arquivo

    git branch //--> Lista todas as branches
    git branch [nome-da-branch] //--> Cria nova branch mas sem trocar
    git branch -m [nome-antigo] [nome-novo] //--> Renomeia branch existente

No **git checkout**, este comando multifuncional alterna entre branches ou restaura arquivos no working directory

No **git branch**, é a ferramenta principal para gerenciar as branches.

---

## `.gitignore`
Ordena o git a ignorar arquivos de sistema, dependências e dados sensíveis. (Chaves API, arquivos `.env`, `node_modules`)

---

## Reflexão: Desenvolvimento Profissional

Desenvolvimento profissional não é apenas aprender coisas difíceis, mas conseguir transformar o complexo em algo simples e acessível, sem perder o entendimento do que está sendo feito e por que está sendo feito. Mais do que acumular conhecimento, trata-se de compreender os processos, as intenções e os impactos do próprio trabalho, criando clareza tanto para si quanto para os outros. Nesse sentido, evoluir profissionalmente é aprofundar a consciência sobre aquilo que se faz, buscando não só fazer melhor, mas fazer com propósito e entendimento real.

















