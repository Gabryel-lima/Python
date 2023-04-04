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