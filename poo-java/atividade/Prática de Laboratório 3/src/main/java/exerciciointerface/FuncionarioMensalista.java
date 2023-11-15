package exerciciointerface;

public class FuncionarioMensalista extends Funcionario implements Pagamento {
    private double salarioMensal;
    
    public FuncionarioMensalista(double salarioMensal, String nome,String sobrenome, String cpf) {
        super(nome, sobrenome, cpf);
        this.salarioMensal = salarioMensal;
    }

    public double getSalarioMensal() {
        return salarioMensal;
    }
    
    public void setSalarioMensal(double salarioMensal) {
    this.salarioMensal = salarioMensal < 0 ? 0 : salarioMensal;
    }

    @Override
    public double getPagamento() {
    return getSalarioMensal();
    }

    @Override
    public String toString() {
    return String.format("%s%s %s \n%s %.2f\n", super.toString(),
    "Salário Mensal: ", this.getSalarioMensal(), "Pagamento: ",
    this.getPagamento());
    }
}