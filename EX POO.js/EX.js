```
public class Funcionario {
    private String nome;
    private String cpf;
    private double salario;

    public double getBonificacao() {
        return this.salario * 0.1;
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getCpf() {
        return cpf;
    }
    public void setCpf(String cpf) {
        this.cpf = cpf;
    }
    public double getSalario() {
        return salario;
    }
    public void setSalario(double salario) {
        this.salario = salario;
    }
}
```
A `class Funcionario` contém: `Atributos privados`(nome, cpf, salario) e seus respectivos `getters e setters` + o `getBonificação` que não necessariamente precisa existir(**Podemos criar get e set mesmo não existindo um atributo relacionado**) 
#
## **Herança(`Extends`)**
```
public class Gerente extends Funcionario {
    private int senha;

    public void setSenha(int senha) {
        this.senha = senha;
    }

    public boolean autentica(int senha) {
        if (this.senha == senha) {
            return true;
        } else {
            return false;
        }
    }
}
```
`Gerente` herda as caracteristicas, comportamentos e os getters e setters da `class Funcionario`.

A class Funcionario é que consideramos de:
- Classe Mãe ou Pai
- Base Class
- Super Class

E a class Gerente é a que chamamos de: 
- Class filho
#
## **Modificador `protected`**
Está entre o `public` e o `private` -> private < protected < public

O modificador `protected` é pouco visto no dia a dia, e sim sendo usado mais o método `getter` para exibição do atributo em questão.

- `private` - somente visivel dentro da class
- `protected` - visivel para os filhos
- `public` - visivel em todos os lugares
#
## **Palavra chave `super`**
Usado indicar que o atributo utilizado na class filho está sendo herdado da Super Class - Que nesse caso é a class Funcionario - Assim deixando claro pra o desenvolvedor que ele precisa subir a hierarquia para encontrar o atributo em questão.
```
    public double getBonificacao() { 
        return super.salario;
    } 
```
## **Assinatura**
`public double getBonificacao()` - Essa escrita é chamada de assinatura. 

Quando sobrescrevemos a assinatura que está presente na Super Class na class filho ela precisa ter: a mesma `visibilidade`, mesmo `retorno`, mesmo `nome` e os mesmos `parâmetros`.
#
## **`super` com métodos**
```
public double getBonificacao() {
    return super.getBonificacao() + super.getSalario();
}
```
Indica que os métodos estão presente na Super Class(Funcionario)
#
## **Sobrecarga**
Muito mais simples do que a sobrescrita e não é dependente da herança.

Por exemplo, na nossa classe `Gerente`, imagine um outro novo método `autentica` que recebe além da `senha` também o `login`:
```
public class Gerente extends Funcionario {

    private int senha;

    public void setSenha(int senha) {
        this.senha = senha;
... (79 linhas)