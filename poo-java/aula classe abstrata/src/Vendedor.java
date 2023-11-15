
// Subclasse Vendedor
class Vendedor extends Funcionario {
    // Atributos privados
    private String regiao;
    private double comissao;

    // Método construtor
    public Vendedor(String nome, double salario, String regiao, double comissao) {
        super(nome, salario);
        this.regiao = regiao;
        this.comissao = comissao;
    }

    // Métodos set e get para regiao
    public void setRegiao(String regiao) {
        this.regiao = regiao;
    }

    public String getRegiao() {
        return regiao;
    }

    // Métodos set e get para comissao
    public void setComissao(double comissao) {
        this.comissao = comissao;
    }

    public double getComissao() {
        return comissao;
    }

    // Implementação do método abstrato reajuste
    public void reajuste() {
        salario *= 1.1;
    }
}
