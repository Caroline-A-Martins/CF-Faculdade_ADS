
package exercicio03;
public class FuncionarioMensalista extends Funcionario {
    
    private double salarioMensal;

    public FuncionarioMensalista( int par, String nome, String sobrenome, String cpf) {
        super(nome, sobrenome, cpf);
        this.salarioMensal = salarioMensal;
    }
    
    public double getSalario() {
        return salarioMensal;
    }

    public void setSalario(double salario) {
        this.salarioMensal = salario;
    }
    
    public void setSalarioMensal(){
        this.salarioMensal = (salarioMensal < 0) ? 0 : salarioMensal;
    }
    
    @Override
    public double calculaSalario() {
        return salarioMensal;
    }
    
    @Override
    public String toString() {
        return super.toString() + "\nSalário Mensal: R$ " + salarioMensal;
    }
}
