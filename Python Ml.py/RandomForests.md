# Introdução

As árvores de decisão deixam você com uma decisão difícil. Uma árvore profunda com muitas folhas vai superajustar porque cada predição está vindo de dados históricos de apenas algumas casas em sua folha. Mas uma árvore rasa com poucas folhas terá um desempenho ruim porque não captura tantas distinções nos dados brutos.

Mesmo as técnicas de modelagem mais sofisticadas de hoje enfrentam essa tensão entre subajuste e superajuste. Mas muitos modelos têm ideias inteligentes que podem levar a um desempenho melhor. Vamos olhar para a floresta aleatória como exemplo.

A floresta aleatória usa muitas árvores e faz uma previsão fazendo a média das previsões de cada árvore componente. Geralmente tem uma precisão preditiva muito melhor do que uma única árvore de decisão e funciona bem com parâmetros padrão. Se você continuar modelando, pode aprender mais modelos com desempenho ainda melhor, mas muitos deles são sensíveis a obter os parâmetros corretos.

# Exemplo

Você já viu o código para carregar os dados algumas vezes. No final do carregamento de dados, temos as seguintes variáveis:

train_X
val_X
train_y
val_y
Construímos um modelo de floresta aleatória de forma semelhante à forma como construímos uma árvore de decisão no scikit-learn - desta vez usando a classe RandomForestRegressor em vez de DecisionTreeRegressor.

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))
191669.7536453626

# Conclusão

Provavelmente há espaço para mais melhorias, mas esta é uma grande melhoria em relação ao melhor erro de árvore de decisão de 250.000. Existem parâmetros que permitem alterar o desempenho da Floresta Aleatória, assim como alteramos a profundidade máxima da única árvore de decisão. Mas uma das melhores características dos modelos de Floresta Aleatória é que eles geralmente funcionam razoavelmente bem mesmo sem esse ajuste.
