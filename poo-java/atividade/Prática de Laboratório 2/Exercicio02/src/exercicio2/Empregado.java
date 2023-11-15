package org.me.exercicio2;
public abstract class Empregado {

    private String codigo, nome;
    private double salarioBase;

    public Empregado(String codigo, String nome, double salarioBase) {
        this.codigo = codigo;
        this.nome = nome;
        this.salarioBase = salarioBase;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getSalarioBase() {
        return salarioBase;
    }

    public void setSalarioBase(double salarioBase) {
        this.salarioBase = salarioBase;
    }

    public abstract double calculoSalario();

    @Override
    public String toString() {
        return String.format("%s: %s; %s: %s; %s: %.2f;\n", "Código", codigo, "Nome", nome, "Salário Base", salarioBase);
    }
}
