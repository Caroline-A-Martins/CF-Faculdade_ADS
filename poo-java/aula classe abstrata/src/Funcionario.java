// Superclasse abstrata Funcionario
abstract class Funcionario {
    // Atributos protegidos
    protected String nome;
    protected double salario;

    // Método construtor
    public Funcionario(String nome, double salario) {
        this.nome = nome;
        this.salario = salario;
    }

    // Métodos set e get para nome
    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    // Métodos set e get para salario
    public void setSalario(double salario) {
        this.salario = salario;
    }

    public double getSalario() {
        return salario;
    }

    // Método abstrato reajuste
    public abstract void reajuste();
}
