package org.me.exercicio2;

public abstract class Gerente extends Empregado {
    private double bonus;
    
    public Gerente(String codigo, String nome, double salarioBase, double bonus) {
        super(codigo, nome, salarioBase);
        this.bonus = bonus;
    }

    public double getBonus() {
        return bonus;
    }

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }
    
    @Override
    public double calculoSalario() {
        double salario = this.getSalarioBase();
        
        double salarioBase = salario + bonus;
        
        this.setSalarioBase(salarioBase);
        
        return salarioBase;
    }
    
    @Override
    public String toString() {
        return String.format("%s%s: %.2f;\n", super.toString(), "Bônus", bonus);
    }
}
