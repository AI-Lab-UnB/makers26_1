# Relatório de Acompanhamento - Semana 9

## 1. Objetivo da Semana

De acordo com o cronograma da Fase 2, a Semana 9 teve como foco a implementação da autenticação e do controle de acesso do sistema.

A entrega esperada para a semana incluía:

- Cadastro de usuários;
- Login;
- Hash de senha;
- Sessão/JWT;
- Rotas protegidas.

No contexto do projeto OnBoarding Digital, essa etapa é essencial para garantir que usuários possam acessar o sistema com segurança e que permissões diferentes sejam aplicadas para RH e colaboradores.

## 2. Entregas Realizadas

Durante a Semana 9, a equipe avançou nos seguintes pontos:

- Integração da tela de login com o backend;
- Envio de e-mail e senha para o endpoint `POST /auth/login`;
- Recebimento do token JWT após login;
- Armazenamento do token no frontend;
- Manutenção da sessão do usuário após atualização da página;
- Implementação de logout;
- Uso do endpoint `GET /auth/me` para identificar o usuário autenticado;
- Redirecionamento do usuário conforme o perfil;
- Criação de painéis separados para RH e colaborador;
- Proteção básica das telas autenticadas;
- Implementação de rotas protegidas para cadastro de usuários por RH;
- Uso de hash de senha no backend;
- Validação de permissão para impedir acesso indevido às rotas de cadastro.

## 3. Análise das Issues da Semana 9

### Issue #8 - Integrar Tela Login com Backend
.

A tela de login foi conectada ao backend. O frontend envia as credenciais para `POST /auth/login`, recebe o token JWT e trata erro de credenciais inválidas.


### Issue #9 - Implementar Sessão do Usuário

O token JWT está sendo armazenado no `localStorage`, permitindo manter o usuário autenticado após atualizar a página. Também foi implementado logout, com remoção do token e redirecionamento para login.


### Issue #10 - Criar Tela de Usuário Autenticado

A issue solicitava uma página `/dashboard`, mas a equipe optou por criar dois painéis separados:

- `/RH_dashboard`;
- `/colaborador_dashboard`.


### Issue #11 - Validar Endpoints de Autenticação Existentes

Essa issue ainda precisa de revisão pois está incompleta


### Issue #12 - Padronizar Respostas de Erro da API


Existe PR aberto relacionado à padronização das respostas de erro, mas ele ainda não foi integrado à branch principal de desenvolvimento.


### Issue #13 - Revisar Regras de Permissão entre RH e Colaborador


O backend já protege as rotas de cadastro de colaboradores e usuários RH, permitindo acesso apenas para usuários com perfil de RH.


## 4. Pontos Positivos

- A equipe avançou bem na base de autenticação;
- O backend está organizado em rotas, schemas, modelos e serviços;
- O login já está integrado com a API;
- O sistema já consegue identificar o usuário autenticado;
- A separação entre painel RH e painel do colaborador faz sentido para o produto;
- O controle de acesso por perfil começou a ser implementado;



## 7. Conclusão da Semana 9

A entrega da Semana 9 está bem encaminhada. A equipe implementou os principais elementos de autenticação, sessão e controle inicial de acesso.

[Repositorio do projeto](https://github.com/daisha19/Onboarding-Digital)