# Resumo Técnico de Git & GitHub

Git é um sistema de controle de versão distribuído utilizado no desenvolvimento de software. Ele não depende de um servidor central, cada desenvolvedor possui uma cópia completa do repositório na própria máquina. Isso o torna rápido, eficiente e resiliente.

O GitHub, por sua vez, é uma plataforma web que hospeda repositórios Git remotos e oferece ferramentas de colaboração como issues, pull requests e wikis. É importante não confundir os dois: Git é a ferramenta de versionamento, enquanto o GitHub é o serviço que hospeda esses repositórios na nuvem.

Além disso, fluxo de trabalho do Git gira em torno de três áreas principais na máquina local: o diretório de trabalho, onde os arquivos são editados; a staging area, onde as mudanças são preparadas antes de serem salvas; e o repositório local, onde os commits ficam armazenados. Existe ainda o repositório remoto, que pode ser o GitHub ou serviços similares como GitLab e Bitbucket.

Na prática, o processo começa com `git init` para inicializar o repositório. Em seguida, os arquivos modificados são adicionados à staging com `git add`, confirmados com `git commit -m "mensagem"` e enviados ao repositório remoto com `git push`. Para baixar alterações feitas por outros desenvolvedores, utiliza-se o `git pull`. Já para obter uma cópia completa de um repositório remoto pela primeira vez, usa-se o `git clone`.

Outro recurso importante é o `.gitignore`, um arquivo que lista tudo aquilo que não deve ser enviado ao repositório, como arquivos `.env` contendo chaves de API e credenciais sensíveis. Para autenticação segura com o GitHub, recomenda-se o uso de chaves SSH, geradas com o comando `ssh-keygen` e cadastradas nas configurações da conta do GitHub, eliminando a necessidade de inserir senha a cada operação.

Por fim, o conceito de branching é fundamental para um fluxo de trabalho organizado. Branches permitem desenvolver funcionalidades ou corrigir bugs de forma isolada, sem afetar o código principal. O fluxo típico envolve:

1. Criar um branch com `git checkout -b`
2. Desenvolver a funcionalidade
3. Commitar as mudanças
4. Enviar o branch ao remoto com `git push`
5. Abrir um **Pull Request** no GitHub para revisão
6. Mesclar ao branch principal com `git merge`
7. Deletar o branch com `git branch -d`


# Reflexão Individual: O que é desenvolvimento profissional?

Desenvolvimento profissional significa aprimorar as habilidades não só técnicas mas também interpessoais. Saber programar, analisar dados ou dominar uma ferramenta é importante, mas tão importante quanto é saber se comunicar, trabalhar em equipe e lidar com situações de pressão. Essas habilidades, juntas, são o que realmente define um profissional. Esse aprimoramento não acontece de uma hora para outra. É um processo gradual, construído ao longo de experiências, erros e aprendizados. 