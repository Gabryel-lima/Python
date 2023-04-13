# O que é Validação de Modelo¶

Você vai querer avaliar quase todos os modelos que construir. Na maioria (embora nem todos) das aplicações, a medida relevante da qualidade do modelo é a precisão preditiva. Em outras palavras, as previsões do modelo serão próximas do que realmente acontece.

Muitas pessoas cometem um erro enorme ao medir a precisão preditiva. Elas fazem previsões com seus dados de treinamento e comparam essas previsões com os valores-alvo nos dados de treinamento. Você verá o problema com essa abordagem e como resolvê-lo em um momento, mas vamos pensar em como faríamos isso primeiro.

Você precisaria primeiro resumir a qualidade do modelo de uma forma compreensível. Se você comparar os valores de casas previstos e reais para 10.000 casas, provavelmente encontrará uma mistura de previsões boas e ruins. Olhar através de uma lista de 10.000 valores previstos e reais seria inútil. Precisamos resumir isso em uma única métrica.

Existem muitas métricas para resumir a qualidade do modelo, mas começaremos com uma chamada Mean Absolute Error (também chamada de MAE). Vamos quebrar essa métrica começando com a última palavra, erro.

O erro de previsão para cada casa é:

erro = real - previsto
Então, se uma casa custar $150.000 e você previu que custaria $100.000, o erro é de $50.000.

Com a métrica MAE, pegamos o valor absoluto de cada erro. Isso converte cada erro em um número positivo. Em seguida, tiramos a média desses erros absolutos. Esta é nossa medida de qualidade do modelo. Em inglês simples, pode ser dito como

Em média, nossas previsões estão erradas em cerca de X.

Para calcular o MAE, primeiro precisamos de um modelo. Isso é construído em uma célula oculta abaixo, que você pode revisar clicando no botão de código.

---


import pandas as pd

# Carregando os dados

melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

# Filtrando as linhas com valores faltantes na coluna Price

filtered_melbourne_data = melbourne_data.dropna(axis=0)

# Escolhendo a variável alvo (target) e as variáveis preditoras (features)

y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea',
                      'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

from sklearn.tree import DecisionTreeRegressor

# Definindo o modelo

melbourne_model = DecisionTreeRegressor()

# Treinando o modelo

melbourne_model.fit(X, y)

---


`DecisionTreeRegressor()`

Uma vez que temos um modelo, aqui está como calculamos o erro médio absoluto:

---



# Importando a função mean_absolute_error da biblioteca sklearn.metrics

from sklearn.metrics import mean_absolute_error

# Fazendo as previsões de preços de casas com o modelo melbourne_model

predicted_home_prices = melbourne_model.predict(X)

# Calculando o MAE (Mean Absolute Error) entre os valores reais y e as previsões predicted_home_prices

mean_absolute_error(y, predicted_home_prices)

---




# O Problema com Pontuações "In-Sample"


A medida que acabamos de calcular pode ser chamada de pontuação "in-sample". Usamos uma única "amostra" de casas tanto para construir o modelo quanto para avaliá-lo. Aqui está o motivo pelo qual isso é ruim.

Imagine que, no grande mercado imobiliário, a cor da porta não tenha relação com o preço da casa.

No entanto, na amostra de dados que você usou para construir o modelo, todas as casas com portas verdes eram muito caras. O trabalho do modelo é encontrar padrões que prevejam os preços das casas, então ele verá esse padrão e sempre preverá preços altos para casas com portas verdes.

Como esse padrão foi derivado dos dados de treinamento, o modelo parecerá preciso nos dados de treinamento.

Mas se esse padrão não se mantiver quando o modelo vir novos dados, o modelo será muito impreciso quando usado na prática.

Já que o valor prático dos modelos vem de fazer previsões em novos dados, medimos o desempenho em dados que não foram usados para construir o modelo. A maneira mais simples de fazer isso é excluir alguns dados do processo de construção do modelo e, em seguida, usar esses dados para testar a precisão do modelo em dados que ele ainda não viu. Esses dados são chamados de dados de validação.


# Codificando


A biblioteca scikit-learn tem uma função chamada train_test_split para dividir os dados em duas partes. Usaremos alguns desses dados como dados de treinamento para ajustar o modelo e usaremos os outros dados como dados de validação para calcular o erro absoluto médio.

Aqui está o código:


from sklearn.model_selection import train_test_split

# separa os dados em dados de treino e validação, para recursos e metas

# A divisão é baseada em um gerador de números aleatórios. Fornecer um valor numérico para

# o argumento random_state garante que obteremos a mesma divisão sempre que

# executar este script.

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

# Define modelo

melbourne_model = DecisionTreeRegressor()

# Ajusta o modelo

melbourne_model.fit(train_X, train_y)

# Obter preços previstos nos dados de validação

val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))

Uau!
Seu erro absoluto médio para os dados dentro da amostra foi de cerca de 500 dólares. Fora da amostra é mais de 250.000 dólares.

Esta é a diferença entre um modelo que é quase exatamente correto e um que é inutilizável para a maioria dos propósitos práticos. Como ponto de referência, o valor médio da casa nos dados de validação é de 1,1 milhão de dólares.
Portanto, o erro nos novos dados é de cerca de um quarto do valor médio da casa.

Há muitas maneiras de melhorar esse modelo, como experimentar para encontrar melhores recursos ou diferentes tipos de modelo.
