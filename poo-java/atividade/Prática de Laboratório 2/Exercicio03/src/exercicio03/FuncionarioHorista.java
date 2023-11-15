
import exercicio03.Funcionario;

public abstract class FuncionarioHorista extends Funcionario{
    private double salarioHora; 
    private int numeroHoras;
    public FuncionarioHorista(String nome, String sobrenome, String cpf, double salarioHora, int numeroHoras) {
        super(nome, sobrenome, cpf);
        this.salarioHora = salarioHora;
        this.numeroHoras = numeroHoras;
    }

    public double getSalarioHora() {
        return salarioHora;
    }

    public int getNumeroHoras() {
        return numeroHoras;
    }
    
    public void setSalarioHora() {
        this.salarioHora = salarioHora < 0 ? 0 : salarioHora;
    }
    
    public void setNumeroHoras() {
        this.numeroHoras = numeroHoras > 0 && numeroHoras <= 168 ? numeroHoras : 0;
    }
    
    @Override
    public double calculaSalario() {
        if (numeroHoras <= 40) {
            salarioHora = this.getSalarioHora() * this.getNumeroHoras();
        } else {
            salarioHora = 40 * this.getSalarioHora() + (this.getNumeroHoras() -40) * this.getSalarioHora() * 1.5;
        }
        
        return salarioHora;
    }
    
    @Override
    public String toString() {
        return super.toString() + "\nSalário Hora: R$ " + salarioHora + "\nHoras Trabalhadas: R$ " + numeroHoras;
    }
}