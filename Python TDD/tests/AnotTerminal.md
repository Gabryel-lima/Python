1) Começamos instalando a ferramenta de coverage do Pytest, o Pytest-cov, através do terminal/prompt de comando;
    pip install pytest-cov==3.0.0

2) Atualizamos o arquivo requirements.txt com o seguinte comando no terminal/prompt de comando;
    pip freeze > requirements.txt

3) Rodamos a ferramenta de cobertura de testes pela primeira vez com o seguinte código:
    pytest –cov=codigo tests/ 

4) Percebemos que alguns trechos de código do arquivo bytebank.py não estão sendo cobertos. Para localizar quais trechos são esses, utilizamos o seguinte comando:
    pytest –cov=codigo tests/ –cov-report term-missing

5) Aprendemos também, uma forma de gerar um relatório de cobertura de testes em HTML através do seguinte comando:
    pytest –cov=codigo tests/ –cov-report html

6) Pudemos visualizar que o trecho que não possui teste é aquele que possui o método __str__();

7) Para obter 100% de cobertura de testes, criamos um teste para o método __str__();

def test_retorno_str(self):
       nome, data_nascimento, salario = 'Teste', '12/03/2000', 1000  # given
       esperado = 'Funcionario(Teste, 12/03/2000, 1000)'

        funconario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funconario_teste.__str__() # when

        assert resultado == esperado  # then

8) Contudo, aprendemos que existem certos trechos de código que executam funcionalidades intrínsecas da linguagem Python e que não faz sentido testá-los, já que como pessoas desenvolvedoras, assumimos que a linguagem funciona como deveria.

9) Tendo isso em mente, apagamos o teste feito sobre o método __str__() e criamos o arquivo .coveragerc, que possui um propósito similar ao pytest.ini e possibilita a mudança de algumas configurações padrão do pytest-cov;

10) O arquivo .coveragerc dá a possibilidade de excluirmos linhas de código do bytebabank.py, cuja cobertura de teste não queremos verificar;

[run]

[report]

exclude_lines =
   def __str__

11) Melhoramos a execução da ferramenta de cobertura definindo no arquivo pytest.ini que sempre que digitarmos o código pytest no terminal, deve ser feita não apenas a execução dos testes, mas o relatório de cobertura de código;

    [pytest]

addopts = -v --cov=codigo tests/ --cov-report term-missing
markers =
    calcular_bonus: Teste para o metodo calcular_bonus

12) Também alteramos o arquivo .coveragerc para que sempre que executarmos o comando pytest –cov a análise de cobertura de testes seja feita apenas no arquivo bytebank.py, bem como, definimos que sempre que um relatório em HTML for gerado, ele deve ficar dentro de um diretório chamado coverage_relatorio_html.

    [run]

source = ./codigo

[report]

exclude_lines =
    def __str__

[html]

directory = coverage_relatorio_html

13) Para criarmos um relatório de testes no padrão xml, basta utilizar o seguinte comando no terminal/prompt de comando:
    pytest –junitxml report.xml

14) Para criar um relatório de cobertura no padrão xml, basta utilizar o seguinte comando no terminal/prompt de comando:

    pytest –cov-report xml