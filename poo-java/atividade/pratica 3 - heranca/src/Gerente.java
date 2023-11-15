public class Gerente extends Funcionario {

    private String departamento;
    private int numPessoas;

    public Gerente(int matricula, String nome, String rg, String departamento, int numPessoas) {
        super(matricula, nome, rg);
        this.departamento = departamento;
        this.numPessoas = numPessoas;
    }

    public String getDepartamento() {
        return departamento;
    }

    public int getNumPessoas() {
        return numPessoas;
    }

}
