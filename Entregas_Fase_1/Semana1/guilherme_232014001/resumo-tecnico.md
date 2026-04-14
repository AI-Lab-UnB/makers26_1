# **Resumo Técnico - Git & GitHub**

## **Introdução**

### **O que é Git**
Git é um **sistema de controle de versão** que ajuda os desenvolvedores a manter um rastreio de mudanças e alterações durante suas aplicações e projetos de desenvolvimento de código. Ele permite colaborar com outros desenvolvedores e manejar multiplas versões de um projeto.

Git é um sistema **descentralizado**, não necessitando necessariamente de um sevidor central controlando tudo, e **distribuido**, pois cada desenvolvedor terá uma cópia do repositório do projeto completo instalado na sua prórpia máquina como todo o histórico, branches, tags, commits, arquivos...

Dessa forma, é necessário que todo desenvolvedor saiba pelo menos os báscios de como esse sistema de controle de versionamento funciona. 

| **Funcionalidade**         | **Descrição** |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| Sistema Distribuído      | Cada desenvolvedor possui uma cópia completa do repositório e de todo o histórico localmente.                                  |
| Controle de Versão       | Permite acompanhar alterações nos arquivos ao longo do tempo e recuperar versões anteriores.                                   |
| Colaboração              | Facilita o trabalho em equipe, permitindo que várias pessoas contribuam simultaneamente.                                       |
| Ramificações (Branching) | Possibilita criar ramificações independentes para desenvolver funcionalidades ou corrigir erros sem afetar a versão principal. |
| Mesclagem (Merging)      | Permite unir alterações feitas em diferentes branches em uma única versão do projeto.                                          |
| Repositórios Remotos     | Suporta repositórios hospedados em serviços como GitHub, GitLab ou Bitbucket.                                                  |
| Ferramentas Extensas     | Possui ampla integração com IDEs, automações, CI/CD e outras ferramentas de desenvolvimento.                                   |
| Área de Staging          | Permite selecionar quais alterações serão incluídas no próximo commit antes de confirmá-las.                                   |
| Velocidade               | A maioria das operações é realizada localmente, tornando o Git rápido e eficiente.                                             |
| Gratuito e Open Source   | O Git é gratuito, de código aberto e pode ser utilizado livremente.                                                            |

### **O que é GitHub**
GitHub é uma plataforma web que é usada para colaboração e controle de versão. Nela, usuários podem hospedar seus repositórios, interagir com outros usuários, ver projetos, controlar seu gerenciar seu código. Nele desenvolvedores podem usar funcionalidades como: *bug tracking*, pedidos de funcionalidades para repositórios públicos, correção contínua, gerenciamento de tarefas e *wikis*.

Em resumo, GitHub é apenas uma plataforma web que hospeda seus repositórios Git, com interfaces mais intuitívas e eficientes. Esse é uma das várias outras plataformas que pode hospedar repositórios Git.

---

## **Configuração Inicial**
Antes de utilizar o Git, é necessário baixá-lo e configurar o nome e o e-mail que aparecerão nos commits:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@email.com"
```

---

## **Principais Comandos**
No terminal, esses são os comandos básicos do Git:
| **Comando** | **Descrição** |
| --- | --- |
| `git init` | Inicializa um novo repositório Git na pasta atual. |
| `git clone <url-do-repositorio>` | Faz uma cópia de um repositório remoto para a máquina local. |
| `git status` | Mostra os arquivos modificados, adicionados ou não rastreados. |
| `git add .` | Adiciona todos os arquivos alterados para a área de staging. |
| `git commit -m "mensagem"` | Salva as alterações realizadas em um commit. |
| `git pull` | Atualiza o repositório local com a versão mais recente do repositório remoto. |
| `git push` | Envia os commits locais para o repositório remoto. |
| `git log` | Exibe o histórico de commits realizados no projeto. |
| `git rm arquivo.txt` | Remove um arquivo do repositório. |

---

## **Branching**
Uma **branch** é uma ramificação independente do projeto. Ela permite desenvolver funcionalidades ou corrigir problemas sem alterar diretamente a branch principal (main).

Dessa forma, vários desenvolvedores podem trabalhar ao mesmo tempo em diferentes partes do projeto sem causar conflitos imediatamente.

Exemplo de fluxo:
```text
main
 ├── feat/tela-login
 ├── fix/erro-cadastro
 └── docs/resumo-tecnico
 ```

 ### **Comandos da Branch**
| **Comando** | **Descrição** |
| --- | --- |
| `git branch` | Lista todas as branches existentes. |
| `git branch nome-da-branch` | Cria uma nova branch. |
| `git switch nome-da-branch` | Troca para outra branch. |
| `git switch -c nome-da-branch` | Cria uma branch e já troca para ela. |
| `git branch -d nome-da-branch` | Remove uma branch que não será mais utilizada. |

 Exemplo:
 ```bash
 git switch -c feat/tela-login
 ```
 Esse comando cria uma branch chamada *feat/tela-login* e já troca para ela.

---

## **Merge e Pull Request**
Depois de finalizar as alterações em uma branch, por meio do Git, elas podem ser unidas à outra branch por meio de merge.

```bash
git merge nome-da-branch
```

No GitHub, essa integração normalmente é feita por um **Pull Request (PR)**. O PR permite que o desenvolvedor explique a funcionalidade que foi desenvolvida, alterada ou removida e promove a boa prática de outras pessoas revisem as alterações antes de aprová-las. Isso ajuda a evitar erros e melhora a organização do projeto.

---

## **Segurança**

### **Chave SSH**
Uma forma mais segura de conectar o GitHub ao computador é utilizando **chaves SSH**. Com elas, não é necessário digitar usuário e senha toda vez que for enviar ou baixar alterações do repositório.

Comando para gerar uma chave SSH:
```bash
ssh-keygen -t ed25519 -C "seuemail@email.com"
```
Depois disso, basta adicionar a chave pública gerada à conta do GitHub.

### **.gitignore**
O arquivo `.gitignore` é utilizado para impedir que determinados arquivos ou pastas sejam enviados ao repositório. Isso é importante para evitar o envio de arquivos temporários, dependências e informações sensíveis.

Exemplo:
```text
node_modules/
.env
dist/
.vscode/
```

O arquivo .env, por exemplo, geralmente contém senhas, chaves de API e outras informações privadas, portanto não deve ser enviado ao GitHub.