# Resumo: Introdução ao GIT e GitHub.

## Git é um sistema de versão de controle que auxilia durante o desenvolvimento de aplicações e softwares ao possibilitar colaboração entre devs, rastreamento de versões e salvar o código para uso futuro. O Git é descentralizado, o que significa que não é necessário um server central para guardar as informações fornecidas pelo Git, sendo uma cópia do reposítorio salva na máquina.

* Funcionalidades e características do Git:
    + Colaboração: Permite que diferentes pessoas editem e salvem o mesmo código
    + Branching: Permite que o trabalho seja divido entre secções diferentes, o que garante maior organização, e segurança com o código principal.
    + Merging: Depois de separar o código em diferentes branchs, é permitido fundir o código de uma branch em outra, principalmente na branch main/master
    + Rastreamento de versão: Permite retornar a uma versão antiga do código para debugging ou mudança de planos durante o desenvolvimento do software.
    + Repositórios remotos: Permite salvar o código em um repósitorio remoto, assim permitindo que outras pessoas acessem e facilitando o armazenamento do código.

  # Diferença entre Git e GitHub:
  ## O Git se mostra como ferramenta que serve para auxiliar desenvolvedores durante a construção de um software. Já o GitHub é um site/aplicação que serve para guardar Git e interagir e manipular ele. Assim como GitHub, existem outros tipos de plataformas que possuem o mesmo objetivo, como o GitLab e o BitBucket.

  # Workflow:
    * O workflow do Git pode ser separado em quatro principais estágios: Working Directoru, Staging Area, Local Repository, Remote Repository.
    + Working Directory: Local onde se "coda" e se cria os arquivos
    + Staging Area: Local onde se prepara os arquivos para o commit
    + Local Repository: Local onde o Git salva localmente as mudanças feitas nos arquivos
    + Remote Repostitory: Repositório remoto onde está salvos os arquivos em uma plataforma online (GitHub, BitBucket, GitLab)

* Principais comandos utilizados durante o uso do Git:
+ 'git init': Adiciona um novo repositório
+ 'git add': Leva o arquivo da Working Area para a Staging Area
+ 'git commit': Salva e muda os arquivos para o repositório local
+ 'git push': Manda as mudanças e arquivos para o repositório remoto
+ 'git pull': Os arquivos locais recebem as mudanças mais recentes do repositório remoto
+ 'git clone': A partir de um repositório remoto, clona os arquivos e os salva localmente

# Outras definições no Git:
## '.gitignore': Arquivo onde se determina outros arquivos que não serão mandados para o repositório remoto por medida de segurança, como chaves de API.
## Terminal x Interface: O Git pode ser normalmente utilizado por comandos na interface, como os mostrados acima. Porém, plataformas como o GitHub podem se utilizar de uma interface "user-friendly" para tornar os comandos mais lúdicos e fáceis de entender.