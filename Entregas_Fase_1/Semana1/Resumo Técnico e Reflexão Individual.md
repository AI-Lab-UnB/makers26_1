
# Resumo Técnico
  - Resumo sobre as funções do Git e do Github
## O que é Git e Github?
  - Git é um sistema de controle de versões de um programa, ele facilita a gestão e compartilhamento do projeto, bem como a coloboração entre os seus desenvolvedores;
  - Git é decentralizado o que significa que não é necessário um servidor central;
  - O Github é uma das várias plataformas que hospedam repositórios Git. O Github providencia uma interface para gerenciar o código, bem como diversas plataformas que ajudam a organizar o repositório.


## Principais Vantagens do Git
### Controle de Versões
  - Como todas as alterações submetidas são salvas, é possível voltar versões caso algum erro seja cometido.
### Colaboração
  - Por meio do repositório que pode ser acessado por todos os membros da equipe, é mais fácil dos desenvolvedores fazerem o software juntos sem se atrapalharem, pois um membro da equipe pode rapidamente atualizar seus arquivos para depois fazer suas própias alterações enquanto outros fazem o mesmo.
### Repositorios Remotos
  - Como os repositórios são remotos, não é necessário se deslocar para locais específicos para usá-los, a pessoa consegue acessar o repositório em qualquer lugar, desde que tenha acesso à internet.
### Muitas ferramentas disponíveis
  - O git já esta consolidado no universo da programação, por essa razão existem diversas ferramentas para facilitar o seu uso.
### Velocidade
  - É muito rápido e fácil de atualizar o repositório e pegar mudanças do repositório.
### Código Aberto e Gratuito
  - O Git é uma ferramenta de código aberto, o que significa que todos podem contribuir com ela facilitando implementações de novas funções e correção de bugs. Além disso, é gratuito permitido que todos possam utiliza-la.
### Branchs (Ramificações)
  - Uma branch é uma linha independente de desenvolvimento do código, isso permite que alterações e implementações de novas funções sejam feitas sem afetar o programa principal.

## Comandos que realizam o ciclo de enviar e receber do repositório remoto
  - Esses são os comandos centrais para trabalhar com um repositório git.
### `1º git init`
  - Deve ser o primeiro comando digitado, ele inicializa um novo repositorio local na pasta do projeto;
  - Cria uma pasta oculta chamada ".git"
### `2º git add`
  - Comando que adiciona arquivos para a Staging Area(Região intermediária entre a pasta do projeto e o repositório local);
  - É possível adicionar arquivo por arquivo, adicionar uma pasta inteira ou digitar `git add .` para colocar todos os arquivos da pasta do projeot na staging area.
### `3º git commit
  - Comando que traz os itens da Staging Area e leva para o repositório local e é usado da seguinte forma:
  - `git commit -m "mensagem do commit"`
  - É possivel torcar `-m` por `-am` para dar um git add em arquivos que foram modificados ou deletados, mas não em arquivos novos.
### `4º git remote`
  - Comando para indicar o endereço do repositório remoto que receberá os itens do repositório local. É usado da seguinte forma:
  - `git remote add {nome que você quiser dar ao repostiório} {endereço do repositório}`
  - Normalmente damos ao repositório o nome de "origin".
### `5º git push`
  - Comando para enviar os arquivos do repositório local para o repositório remoto;
  - `git push -u {nome do repositório} {nome da branch em que os arquivos serão enviados}`
  - o que git push falha caso o repositório local não esteja na mesma versão que a branch do repositório remoto. Ex: Desenvolvedor 1 cria o repositório e faz o commit do arquivo X, o Desenvolvedor 2 tenta enviar o arquivo Y para o repositório, porém o git não conssegui enviar o arquivo Y.
### `5º git pull`
  - Esse é o comando que permite sincronizar o repositório local com o remoto, permitindo que o Desenvolvedor 2, do exemplo anterior, consiga enviar o arquivo 2;
  - `git pull -u {nome do repositório} {nome da branch em que você deseja puxar os arquivos}`
  - Git pull é a junção de dois comandos: git fetch (adquire os commits do repositório remoto sem alterar a pasta do projeto) e git merge (Junta as mudanças do git fetch com a pasta do projeto).
## Outros comandos importantes
### Comandos para trabalhar com branchs
  - `git branch`
    - Chamado sozinho lista todas branchs locais e destaca a branch atual com um "*";
    - acrescentando a tag -r faz o comando listar as branchs do repositório remoto;
    - adicionando um texto qualquer que não seja uma tag faz o git criar uma nova branch cujo nome é o texto digitado. OBS: ao fazer isso o git não muda para a branch nova.
    - Para mudar o nome de uma branch: `git branch -m {nome antigo} {nome novo}`
  - `git checkout`
    - `git checkout {nome da branch}` muda de branch.
    - `git checkout -b {nome da branch}`cria e muda para a branch criada.
  -`git clone {url do repositorio}`
    - Crie uma cópia local do repositório com todas suas branchs e seus respectivos commits;
    - O repositório é colocado em uma pasta cujo nome é o mesmo do repositório é possível escolher um nome diferente se for colocado um nome depois do url do repositorio.
  - `git log`
    - Lista todos os commits que foram feitos no repositório;
    - É através desse comando que é possível verificar um commit que estragou uma branch.
  - `git status`
    - Mostra oa branch atual, arquivos que estão na staging area, arquivos modificados cujas modificações não estão na Staging Area, e arquivos novos que não foram adicionados ao git.
## Arquivo `.gitignore`
  - Um arquivo que lista pastas e arquivos que não se deseja que sejam enviados ao git como o arquivo `.env`.

# Reflaxão individual: "O que é desenvolvimento profissional"
Desenvolviemnto profissional é o processo contínuo de aprendizado e aprimoramento de habilidades à carreira Profissional. Se trata de se manter relevante na sua área de atuação, não apenas por meio de conhecimento técnico, mas também sabendo como trabalhar em uma equipe, a fim de não se estagnar em sua carreira profissional.
