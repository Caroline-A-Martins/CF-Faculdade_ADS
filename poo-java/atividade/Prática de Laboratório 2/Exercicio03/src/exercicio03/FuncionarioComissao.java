package exercicio03;

public abstract class FuncionarioComissao extends Funcionario {
    private double vendaBruta;
    private double comissao;

    public FuncionarioComissao(String nome, String sobrenome, String cpf,double vendaBruta, double comissao) {
        super(nome, sobrenome, cpf);
        this.vendaBruta = vendaBruta;
        this.comissao = comissao;
    }

    public double getVendaBruta() {
        return vendaBruta;
    }

    public void setVendaBruta(double vendaBruta) {
        this.vendaBruta = vendaBruta < 0 ? 0 : vendaBruta;
    }

    public double getComissao() {
        return comissao;
    }

    public void setComissao(double comissao) {
        this.comissao = comissao > 0 && comissao < 1 ? comissao : 0;
    }

    public double calcularSalario() {
        return this.vendaBruta * this.comissao;
    }
    
    @Override
    public String toString() {
        return super.toString() +
                "\nVenda bruta: R$" + String.format("%.2f", this.vendaBruta) +
                "\nComissão: " + String.format("%.2f", this.comissao * 100) + "%";
    }

    void setVendaBruta() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }

    void setComissao() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
}



    