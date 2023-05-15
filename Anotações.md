__init__(self, [...]): é chamado quando um objeto é criado a partir de uma classe, e é usado para inicializar o estado do objeto.

__repr__(self): retorna uma representação em string do objeto, geralmente usado para fins de depuração.

__str__(self): retorna uma representação em string mais amigável do objeto para uso humano.

__len__(self): retorna o número de elementos em um objeto que pode ser medido, como uma lista ou uma string.

__getitem__(self, key): permite que um objeto seja acessado usando a notação de colchetes, como obj[índice].

__setitem__(self, key, value): permite que um objeto seja atribuído usando a notação de colchetes, como obj[índice] = valor.

__delitem__(self, key): permite que um item seja excluído de um objeto usando a notação de colchetes, como del obj[índice].

__iter__(self): permite que um objeto seja iterado usando um loop for.

__next__(self): usado em conjunto com __iter__ para fornecer a próxima iteração em um loop for.

__call__(self, [...]): permite que um objeto seja chamado como uma função, como obj(argumentos).

__eq__(self, other): compara dois objetos para determinar se eles são iguais.

__ne__(self, other): compara dois objetos para determinar se eles são diferentes.

__lt__(self, other): compara dois objetos para determinar se um é menor que o outro.

__gt__(self, other): compara dois objetos para determinar se um é maior que o outro.

__le__(self, other): compara dois objetos para determinar se um é menor ou igual ao outro.

__ge__(self, other): compara dois objetos para determinar se um é maior ou igual ao outro.

__add__(self, other): adiciona dois objetos.

__sub__(self, other): subtrai dois objetos.

__mul__(self, other): multiplica dois objetos.

__truediv__(self, other): divide dois objetos usando a divisão de ponto flutuante.

__floordiv__(self, other): divide dois objetos usando a divisão de chão (sem ponto flutuante).

__mod__(self, other): retorna o resto da divisão de dois objetos.

__pow__(self, other): eleva um objeto à potência de outro objeto.

Esses são apenas alguns dos métodos dunder mais comuns em Python. Há muitos outros, dependendo do que você está tentando fazer em seu código.

---

***Acessar o virtual venv:***

***python -m venv venv***

---

***Ativando:***

***.\venv\Scripts\Activate***

---

***Desativando:***

***deactivate***

---

***É uma boa prática deixar os packages do venv listados no txt:***

***pip freeze > requierements.txt***

---

***Abrindo o help do Django:***

***django-admin help***

CASO PERCA A SECRET_KEY:

python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

---

***Iniciando o projeto no django:***

***django-admin startproject setup .***

***É bom estar ciente de que o interpretador esteja selecionado como o Python venv.***

---

***Como rodar o server do arquivo manager.py:***

***python manage.py runserver***

***Agora todas as minhas alterações estão sendo visualizadas pelo servidor.***

---

***Para acessar deve ser entar neste link no terminal:***

***Starting development server at http://127.0.0.1:8000/***

---

***No arquivo settings definindo a lingua e horário:***

***LANGUAGE_CODE = 'pt-br'***

***TIME_ZONE = 'America/Sao_Paulo'***

---

1) Crie um novo arquivo chamado `.env` no diretório raiz da aplicação para armazenar a `SECRET_KEY`

 **Conteúdo do arquivo `.env`** :

```ini
SECRET_KEY=<chave aleatória>COPIAR CÓDIGO
```

2) Instale o pacote `python-dotenv`

   pip install python-dotenv
3) Importe os pacotes `python-dotenv` e `os` no arquivo `settings.py`

```javascript
from pathlib import os
from dotenv import load_dotenv
```

4) Importe a `SECRET_KEY` do arquivo `.env` e coloque dentro da variável `SECRET_KEY` no arquivo `settings.py`

```lua
load_dotenv()
SECRET_KEY = str(os.getenv('SECRET_KEY'))
```

5) Gere um arquivo `.gitignore` no diretório raiz do projeto e inclua o arquivo `.env` como conteúdo

 **Conteúdo do `.gitignore`** :

```bash
.env
```

Pronto! Assim deixamos o projeto mais seguro, impedindo que dados sensíveis fiquem à mercê de `commits` descuidados.

Todos esses arquivos devem estar na pasta venv.

---

Depois, parar o servidor e criar o repositório novo no git:

git init
git commit -m "Um_nome_de_exemplo"
git branch -M main
#git remote add origin git@github.com:Gabryel-lima/Django.git
git push -u origin 'main ou master'

---

Na venv definindo o app e seu nome:

python manage.py startapp

ython manage.py startapp galeria

---

1) Acesse o arquivo `views.py` dentro do diretório do app `galeria` e crie um função responsável por mostrar um HTML da página principal do site;

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Bem vindo à minha primeira página!!!!</h1>')
```

2) Crie um novo arquivo chamado `urls.py` dentro do diretório da aplicação `galeria`;
3) Crie uma “palheta” de urls dentro do arquivo `urls.py` (do diretório `galeria`) que leve à função `index`;

```javascript
from django.urls import path
from galeria.views import index

urlpatterns = [
    path('', index)
]
```

4) Altere o arquivo `urls.py` do diretório do projeto (`setup`) para incluir a "palheta" de urls mencionada no `urls.py` de `galeria`;

```javascript
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls'))
]
```

Pronto! Agora, ao subir o servidor, veremos nossa primeira página personalizada com os dizeres: **Bem vindo à minha primeira página!!!!**

---

Por fora vamos criar uma pasta chamada templates e passar o caminho dela no setup.settings, na constante:

'DIRS':[os.path.join(BASE_DIR,'templates')],

E no templates abrimos um arquivo html.index.

---
