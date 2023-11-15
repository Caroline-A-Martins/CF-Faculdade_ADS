public class Analista extends Funcionario {

    private String projeto;

    public Analista(int matricula, String nome, String rg, String projeto) {
        super(matricula, nome, rg);
        this.projeto = projeto;
    }

    public String getProjeto() {
        return projeto;
    }

}

