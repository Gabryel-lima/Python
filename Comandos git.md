Se você deseja verificar o histórico de alterações, as mensagens de commits, o nome do autor daquele commit e outras informações sobre o projeto, existe um comando do git que pode te ajudar. Este comando é o `git log`.

Como já sabemos, os commits possuem hashs que os identificam de uma forma única, isto é, não existem dois commits com o mesmo hash. Com o git log podemos ver o hash e várias outras informações do commit.

Podemos visualizar todos os commits, um em cada linha com o comando:

```lua
git log --oneline
```

Se, em vez de menos informações, quisermos ver mais como as alterações do commit, podemos usar:

```bash
git log -p
```

Também podemos pesquisar as informações do autor daquele commit com o comando:

```bash
git log --author="user_name"
```

E pesquisar informações por data:

```lua
git log --since=1.month.ago --until=1.day.ago
```

No comando acima, estamos buscando as informações do commit desde um mês atrás até um dia atrás.

Você também pode formatar a visualização das informações de commit com o comando:

```perl
git log --pretty="format:%h %s"
```

Este traz o hash seguido da mensagem de commit. Para saber mais formas de exibir as informações de commit, [aqui tem uma lista](https://devhints.io/git-log-format) de maneiras que você pode fazer isso.

Bem legal, não é? E se eu te contar que existem vários outros parâmetros que podemos passar no `git log`? Se você deseja saber mais sobre como exibir as informações de seus commits, você pode conferir [neste link](https://devhints.io/git-log).

---

Imagine que você esteja trabalhando em um projeto que já está configurado em um repositório de origem, e deseja colaborar com esse projeto. Com o git clone, é possível criar uma cópia de desenvolvimento em um repositório local, e todas as alterações que você fizer serão gerenciadas a partir desse repositório. O comando `git clone` é usado para selecionar um **repositório existente** e criar um clone ou uma cópia dele em um  **repositório local** .

O comando `git clone` cria uma cópia de um repositório git existente, e esse repositório pode ser **local** ou  **remoto** . Além disso, essa cópia é um  **repositório git completo** , com seu próprio histórico, gerenciamento de seus próprios arquivos e é um ambiente isolado como um todo do repositório original.

Por conveniência, a clonagem cria uma **conexão remota** apontando para o repositório original. E é essa conexão que facilita muito a interação com o repositório central. Você pode consultar um exemplo demonstrando o `git clone` [aqui](https://www.atlassian.com/br/git/tutorials/setting-up-a-repository)!

Com o `git clone` você também pode clonar o repositório para uma pasta específica:

```xml
git clone <repositorio> <meu-projeto-clone>
```

O repositório localizado em `repositorio` é clonado para uma pasta chamada `meu-projeto-clone`.

Você também pode configurar o `git clone` e clonar o repositório a partir de uma **branch** específica, diferente da original dessa forma:

```bash
git clone -branch new_feature <repositorio>
```

O exemplo acima clonaria apenas a **branch** `new_feature` de `repositorio`. Outras configurações de opções do `git clone` você pode consultar [neste link](https://git-scm.com/docs/git-clone).

---

* Caminho 1: criar uma branch para cada aula do curso com o comando:

```css
git checkout -b nome-da-branch
```

Com esse comando, você cria uma nova branch e muda automaticamente para ela para dar início ao desenvolvimento.

* Caminho 2: criar uma branch para cada aula do curso com o comando:

```undefined
git branch nome-da-branch
```

Essa é outra forma de criar uma branch. Nesse caso, ela é criada, mas não há a mudança automática para esta nova ramificação. Para isso, você pode usar o comando `git switch nome-da-branch`.

---

# Guia do Git para iniciantes

O Git é uma ferramenta de controle de versão muito utilizada no desenvolvimento de software. Com o Git, você pode acompanhar o histórico de alterações em seus arquivos, colaborar com outras pessoas em um projeto e restaurar versões anteriores de seus arquivos.

## Instalação e configuração

Para começar a usar o Git, você precisa instalá-lo em seu computador. Acesse o site oficial do Git e baixe a versão para o seu sistema operacional. Depois de instalado, configure suas informações de usuário:

git config --global user.name "Seu nome"
git config --global user.email "seu-email@exemplo.com"

## Criando um repositório

Para criar um novo repositório Git, crie uma nova pasta em seu computador e inicialize o Git dentro dela:

mkdir meu-repositorio
cd meu-repositorio
git init

## Adicionando arquivos e fazendo commits

Para adicionar um arquivo ao repositório, use o comando `git add`:

git add nome-do-arquivo

Você também pode adicionar todos os arquivos da pasta de uma só vez:

git add .

Depois de adicionar os arquivos, faça um commit com uma mensagem que descreva as alterações:

git commit -m "Minha primeira alteração"

## Visualizando o histórico

Você pode ver o histórico de alterações em um repositório Git usando o comando `git log`:

git log

## Clonando um repositório existente

Para clonar um repositório existente em seu computador, use o comando `git clone` seguido da URL do repositório:

git clone https://github.com/usuario/nome-do-repositorio.git

## Enviando alterações para o servidor remoto

Para enviar as alterações feitas em seu repositório para o servidor remoto, use o comando `git push`:

git push origin sua-branch

Antes de fazer o push pela primeira vez, você precisa adicionar o servidor remoto com o comando `git remote add`:

git remote add origin https://github.com/usuario/nome-do-repositorio.git
