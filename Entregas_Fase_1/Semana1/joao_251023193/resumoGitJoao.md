# Resumo Técnico - Git

---

O Git é uma ferramenta de versionamento de código utilizada para armazenar versões antigas de códigos atuais.

Ele pode ser utilizado também para trabalho em grupo sem que o código principal seja afetado.

## Git Workflow

O workflow do Git consiste em salvar alterações do código e enviar para um repositório remoto. Geralmente, os repositórios remotos ficam armazenados no GitHub, uma plataforma voltada para isso.

## Branches e Merge

As branches são essenciais para trabalho em grupo quando se trata de um mesmo projeto, ela é uma linha alternativa ao código principal em que você pode fazer suas alterações sem prejudicar as outras branches. Após a sua parte ser concluída, você pode mandar um pull request para o dono do repositório remoto para ele dar merge no código.

*merge = aplicar alterações de uma branch alternativa na branch principal

## Alguns códigos

Os principais códigos são:

* git status: utilizado para ver a situação dos arquivos a serem commitados.

* git add: adiciona arquivos no stage, uma etapa antes do commit.

* git commit: aplica as mudanças de código no seu repositório remoto.

* git push: utilizado para atualizar o repositório remoto a partir do repositório local.

* git pull: atualiza seu repositório local a partir do repositório remoto.
