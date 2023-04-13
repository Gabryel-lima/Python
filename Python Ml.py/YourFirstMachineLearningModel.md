# Selecting Data for Modeling

O conjunto de dados é muito grande para ser compreendido ou mesmo impresso de forma legível. Como podemos reduzir essa quantidade esmagadora de dados para algo que possamos entender?

Começaremos escolhendo algumas variáveis usando nossa intuição. Mais tarde, outros cursos mostrarão técnicas estatísticas para priorizar variáveis automaticamente.

Para escolher variáveis/colunas, precisamos ver uma lista de todas as colunas no conjunto de dados. Isso é feito com a propriedade `columns` do DataFrame (a última linha de código abaixo).

#import pandas as pd

#melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
#melbourne_data = pd.read_csv(melbourne_file_path)
#melbourne_data.columns

O conjunto de dados de Melbourne tem alguns valores faltantes (algumas casas para as quais algumas variáveis não foram registradas). Aprenderemos a lidar com valores faltantes em um tutorial posterior. Seus dados de Iowa não têm valores faltantes nas colunas que você usa. Portanto, vamos escolher a opção mais simples por enquanto e eliminar as casas dos nossos dados.

Não se preocupe muito com isso agora, embora o código seja:

#dropna drops missing values (think of na as "not available")

#melbourne_data = melbourne_data.dropna(axis=0)

Existem muitas maneiras de selecionar um subconjunto de seus dados. O curso Pandas aborda isso com mais profundidade, mas nos concentraremos em duas abordagens por enquanto:

* Notação ponto, que usamos para selecionar o "objetivo de previsão".
* Seleção com uma lista de colunas, que usamos para selecionar as "características".

## Selecionando o Objetivo de Previsão

Você pode retirar uma variável com a notação ponto. Essa única coluna é armazenada em uma série, que é amplamente como um DataFrame com apenas uma única coluna de dados.

Usaremos a notação ponto para selecionar a coluna que queremos prever, que é chamada de objetivo de previsão. Por convenção, o objetivo de previsão é chamado de `y`. Então, o código que precisamos para salvar os preços das casas nos dados de Melbourne é:

#y = melbourne_data.Price

## Escolhendo as Características

As colunas que são inseridas em nosso modelo (e posteriormente usadas para fazer previsões) são chamadas de "características". No nosso caso, seriam as colunas usadas para determinar o preço da casa. Às vezes, você usará todas as colunas, exceto o objetivo como características. Outras vezes, será melhor usar menos características.

Por enquanto, construiremos um modelo com apenas algumas características. Mais tarde, você verá como iterar e comparar modelos construídos com diferentes características.

Selecionamos várias características fornecendo uma lista de nomes de colunas dentro de colchetes. Cada item dessa lista deve ser uma string (entre aspas).

Aqui está um exemplo:

#melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

Por convenção, esses dados são chamados de `X`.

#X = melbourne_data[melbourne_features]

Vamos revisar rapidamente os dados que usaremos

#X.describe()

#X.head()

# Visualização dos dados

Visualizar os dados com esses comandos é uma parte importante do trabalho de um cientista de dados. Com frequência, você encontrará surpresas no conjunto de dados que merecem uma inspeção mais detalhada.

# Construindo o modelo

Para criar seus modelos, você usará a biblioteca scikit-learn. Ao codificar, esta biblioteca é escrita como sklearn, como você verá no código de exemplo. O scikit-learn é facilmente a biblioteca mais popular para modelagem dos tipos de dados geralmente armazenados em DataFrames.

Os passos para construir e usar um modelo são:

Definir: Que tipo de modelo será? Uma árvore de decisão? Algum outro tipo de modelo? Alguns outros parâmetros do tipo de modelo também são especificados.
Ajustar: Capturar padrões dos dados fornecidos. Este é o coração da modelagem.
Prever: Exatamente o que parece.
Avaliar: Determinar quão precisas são as previsões do modelo.

Aqui está um exemplo de definição de um modelo de árvore de decisão com o scikit-learn e o ajuste com as características e a variável alvo.

---

#from sklearn.tree import DecisionTreeRegressor

# Define modelo. Especifique um número para random_state para garantir os mesmos resultados em cada execução

#melbourne_model = DecisionTreeRegressor(random_state=1)

# Ajustar modelo

melbourne_model.fit(X, y)
DecisionTreeRegressor(random_state=1)

---

Muitos modelos de aprendizado de máquina permitem algum nível de aleatoriedade no treinamento do modelo. Especificar um número para random_state garante que você obtenha os mesmos resultados em cada execução. Isso é considerado uma boa prática. Você pode usar qualquer número e a qualidade do modelo não dependerá significativamente do valor escolhido.

Agora temos um modelo ajustado que podemos usar para fazer previsões.

Na prática, você desejará fazer previsões para novas casas que estão entrando no mercado, em vez das casas para as quais já temos preços. Mas faremos previsões para as primeiras linhas dos dados de treinamento para ver como funciona a função de previsão.

---

#print("Fazendo previsões para as seguintes 5 casas:")
#print(X.head())
#print("As previsões são:")
#print(melbourne_model.predict(X.head()))

---
