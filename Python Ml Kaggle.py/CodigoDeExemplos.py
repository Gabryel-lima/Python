import pandas as pd

""" # salva o caminho do arquivo para facilitar o acesso
melbourne_file_path = 'C:/Users/gabry/OneDrive/Área de Trabalho/Python/Python Ml.py/melb_data.csv'
# lê os dados e armazena em um DataFrame chamado melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# imprime um resumo dos dados em Melbourne data
print(melbourne_data.describe()) """


# Selecionando modelo de dados
# import pandas as pd

melbourne_file_path = 'C:/Users/gabry/OneDrive/Área de Trabalho/Python/Python Ml.py/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
melbourne_data.columns

# Os dados de Melbourne têm alguns valores ausentes (algumas casas para as quais algumas variáveis ​​não foram registradas).
# Aprenderemos a lidar com valores ausentes em um tutorial posterior.
# Seus dados de Iowa não têm valores ausentes nas colunas que você usa.
# Portanto, vamos pegar a opção mais simples por enquanto e retirar as casas de nossos dados.
# Não se preocupe tanto com isso por enquanto
# embora o código seja:

# dropna descarta valores ausentes (pense em na como "não disponível")
melbourne_data = melbourne_data.dropna(axis=0)



# Selecionando o Objetivo de Previsão
y = melbourne_data.Price

# Escolhendo as Características
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

# Por convenção é chamado de 'x'
x = melbourne_data[melbourne_features]

# Vamos revisar rapidamente os dados que usaremos
x.describe()
x.head()



# Contruindo o modelo

# Importando biblioteca
from sklearn.tree import DecisionTreeRegressor

# Definir modelo. Especifique um número para random_state para garantir os mesmos resultados a cada execução
melbourne_model = DecisionTreeRegressor(random_state=1)

# Modelo adequado
melbourne_model.fit(x,y)

# Ajustar modelo
DecisionTreeRegressor(random_state=1)

print("Fazendo previsões para as 5 casas a seguir:")
print(x.head())
print("As previsões são:")
print(melbourne_model.predict(x.head()))

####################################################################
from sklearn.tree import DecisionTreeRegressor

# Definindo uma função chamada 'get_mae' que recebe como argumentos o número máximo de folhas da árvore de decisão,
# os conjuntos de treinamento e validação (atributos e rótulos), e retorna o erro absoluto médio (mae).

model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
# Criando um objeto do tipo 'DecisionTreeRegressor' com o número máximo de folhas especificado 
# e atribuindo-o à variável 'model'.

model.fit(train_X, train_y)
# Ajustando o modelo criado aos dados de treinamento fornecidos, usando os métodos 'fit' do objeto 'model'.

preds_val = model.predict(val_X)
# Fazendo a predição do modelo com base nos atributos do conjunto de validação e atribuindo o resultado 
# à variável 'preds_val'.

mae = mean_absolute_error(val_y, preds_val)
# Calculando o erro absoluto médio entre as predições do modelo e as rótulos verdadeiras do conjunto de validação
# usando o método 'mean_absolute_error' da biblioteca 'sklearn.metrics' e atribuindo o resultado à variável 'mae'.

#return(mae)
mae

# Retornando o valor do erro absoluto médio calculado.


####################################################################


#O código de carregamento de dados é executado neste ponto.

import pandas as pd

#Carregando dados
melbourne_file_path = 'C:/Users/gabry/OneDrive/Área de Trabalho/Python/Python Ml.py/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

#Filtrando linhas com valores faltantes
filtered_melbourne_data = melbourne_data.dropna(axis=0)

#Escolhendo o alvo e as características
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea',
'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

from sklearn.model_selection import train_test_split

#Dividindo os dados em dados de treinamento e validação, tanto para as características quanto para o alvo
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)


#comparando o MAE com diferentes valores de max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    meu_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Número máximo de nós folha: %d \t Erro absoluto médio: %d" %(max_leaf_nodes, meu_mae))


####################################################################


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

#Criando um modelo de Floresta Aleatória Regressor
forest_model = RandomForestRegressor(random_state=1)

#Treinando o modelo com dados de treinamento
forest_model.fit(train_X, train_y)

#Fazendo previsões com dados de validação
melb_preds = forest_model.predict(val_X)

#Calculando o erro absoluto médio entre as previsões e os valores reais
print(mean_absolute_error(val_y, melb_preds))