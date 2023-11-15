public class Vendedor extends Funcionario {
    private double comissao;
    private String regiao;

    public Vendedor(String nome, String cpf, double salario, double comissao, String regiao) {
        super(nome, cpf, salario);
        this.comissao = comissao;
        this.regiao = regiao;
    }

    public double getComissao() {
        return comissao;
    }

    public void setComissao(double comissao) {
        this.comissao = comissao;
    }

    public String getRegiao() {
        return regiao;
    }

    public void setRegiao(String regiao) {
        this.regiao = regiao;
    }
}
