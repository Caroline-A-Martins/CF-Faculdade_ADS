public class Funcionario {

    private int matricula;
    private String nome;
    private String rg;

    public Funcionario(int matricula, String nome, String rg) {
        this.matricula = matricula;
        this.nome = nome;
        this.rg = rg;
    }

    public int getMatricula() {
        return matricula;
    }

    public String getNome() {
        return nome;
    }

    public String getRg() {
        return rg;
    }

}