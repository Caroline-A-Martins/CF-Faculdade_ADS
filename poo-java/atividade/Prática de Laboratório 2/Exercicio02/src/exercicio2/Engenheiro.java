package org.me.exercicio2;
public abstract class Engenheiro extends Empregado {
    private String departamento, CREA;
    
    public Engenheiro(String codigo, String nome, double salarioBase, String departamento, String CREA) {
        super(codigo, nome, salarioBase);
        this.departamento = departamento;
        this.CREA = CREA;
    }

    public String getDepartamento() {
        return departamento;
    }

    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }

    public String getCREA() {
        return CREA;
    }

    public void setCREA(String CREA) {
        this.CREA = CREA;
    }
    
    @Override
    public double calculoSalario() {
        double salario = this.getSalarioBase();
        
        double salarioBase = salario + (salario * 0.5);
        
        this.setSalarioBase(salarioBase);
        
        return salarioBase;
    }
    
    @Override
    public String toString() {
        return String.format("%s%s: %s; %s: %s;\n", super.toString(), 
                "Departamento", departamento, 
                "CREA", CREA);
    }
}
