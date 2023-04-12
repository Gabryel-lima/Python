# Usando Pandas para se familiarizar com seus dados

O primeiro passo em qualquer projeto de aprendizado de máquina é se familiarizar com os dados. Você usará a biblioteca Pandas para isso. Pandas é a principal ferramenta que os cientistas de dados usam para explorar e manipular dados. A maioria das pessoas abrevia Pandas em seu código como pd. Fazemos isso com o comando:

###### #import pandas as pd

A parte mais importante da biblioteca Pandas é o DataFrame. Um DataFrame contém o tipo de dados que você pode pensar como uma tabela. Isso é semelhante a uma planilha no Excel, ou uma tabela em um banco de dados SQL.

Pandas tem métodos poderosos para a maioria das coisas que você deseja fazer com esse tipo de dados.

Como exemplo, vamos olhar para dados sobre preços de casas em Melbourne, Austrália. Nos exercícios práticos, você aplicará os mesmos processos a um novo conjunto de dados, que tem preços de casas em Iowa.

Os dados de exemplo (Melbourne) estão no caminho do arquivo ../input/melbourne-housing-snapshot/melb_data.csv.

Carregamos e exploramos os dados com os seguintes comandos:

---



# salva o caminho do arquivo para facilitar o acesso

melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'

# lê os dados e armazena em um DataFrame chamado melbourne_data

melbourne_data = pd.read_csv(melbourne_file_path)

# imprime um resumo dos dados em Melbourne data

melbourne_data.describe()

---



Os resultados mostram 8 números para cada coluna em seu conjunto de dados original. O primeiro número, a contagem, mostra quantas linhas possuem valores não ausentes.

Valores ausentes surgem por muitos motivos. Por exemplo, o tamanho do segundo quarto não seria coletado ao pesquisar uma casa com 1 quarto. Voltaremos ao assunto de dados ausentes.

O segundo valor é a média (mean), que é a média aritmética. Abaixo disso, std é o desvio padrão, que mede quão numericamente espalhados os valores estão.

Para interpretar os valores mínimo (min), 25%, 50%, 75% e máximo (max), imagine ordenar cada coluna do menor para o maior valor. O primeiro (menor) valor é o mínimo. Se você for um quarto do caminho pela lista, encontrará um número que é maior que 25% dos valores e menor que 75% dos valores. Esse é o valor do 25% (pronunciado "vigésimo quinto percentil"). Os percentis de 50 e 75 são definidos analogamente, e o máximo é o número mais alto.
