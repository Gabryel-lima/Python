#Exercicio 1

#Crie uma classe "Pessoa" que possua os seguintes atributos:

    #nome
    #idade
    #endereço
    #E as seguintes ações (métodos):

    #envelhecer (aumenta a idade em 1 ano)
    #mudar_endereço (permite mudar o endereço da pessoa)

""" class Pessoa():
    def __init__(self,nome,idade,endereço):
        self.nome = nome
        self.idade = idade
        self.endereço = endereço
    
    def envelhecer(self):
        self.idade += 1

    def mudar_endereço(self,endereço):
        self.endereço = endereço """

#Execicio 2

#Crie uma classe "Livro" que tenha atributos "título", "autor" e "páginas" e métodos "ler()" e "info()". O método "ler()" deve imprimir na tela "Lendo [título] de [autor]". O método "info()" deve imprimir na tela "[título] tem [páginas] páginas, escrito por [autor]"
""" 
class Livro():
    def __init__(self,título,autor,páginas):
        self.título = título
        self.autor = autor
        self.páginas = páginas


    def Ler(self):
        print(f'Lendo {self.título} de autor {self.autor}.')

    def Info(self):
        print(f'{self.título} tem {self.páginas}páginas, escrito por {self.autor}.')
 """
#Execicio 3

#Crie uma classe chamada Carro que representa um carro. A classe deve conter as seguintes informações:

"""     Marca
    Modelo
    Ano
    Velocidade atual (em km/h)
    Quantidade de combustível no tanque (em litros)
A classe deve ter os seguintes métodos:

    abastecer(quantidade): adiciona a quantidade de combustível especificada ao tanque.
    acelerar(velocidade): aumenta a velocidade atual em velocidade km/h.
    frear(velocidade): diminui a velocidade atual em velocidade km/h.
    mostrar_velocidade(): imprime a velocidade atual.
    mostrar_tanque(): imprime a quantidade de combustível no tanque.
 """
""" class Carro():
    def __init__(self,Marca,Modelo,Ano,Velocidade_Atual,Qtd_combustível):
        self.Marca = Marca
        self.Modelo = Modelo
        self.Ano = Ano
        self.Velocidade_Atual = Velocidade_Atual
        self.Qtd_combustível = Qtd_combustível

    def Abastecer(self,quantidade):
        self.Qtd_combustível += quantidade

    def Acelerar(self,aceleração):
        self.Velocidade_Atual += aceleração

    def Frear(self,desaceleração):
        self.Velocidade_Atual -= desaceleração

    def Mostrar_Velocidade(self):
        print(f'A velocidade atual é de {self.Velocidade_Atual} Km/h.')

    def Mostrar_Tanque(self):
        print(f'A quantidade de combustível é de {self.Qtd_combustível}')
 """

#Exercicio 4


