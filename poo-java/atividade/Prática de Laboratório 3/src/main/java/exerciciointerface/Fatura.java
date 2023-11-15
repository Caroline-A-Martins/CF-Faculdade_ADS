package exerciciointerface;

public class Fatura implements Pagamento {

    private int numero, quantidade;
    private String descricao;
    private double preco;

    public Fatura(int numero, String descricao, int quantidade, double preco) {
        this.numero = numero;
        this.descricao = descricao;
        this.quantidade = quantidade;
        this.preco = preco;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public int getQuantidade() {
        return quantidade;
    }
    
    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade < 0 ? 0 : quantidade;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco < 0 ? 0 : preco;
    }

    @Override
    public double getPagamento() {
        return this.getQuantidade() * this.getPreco();
    }
    
    @Override
    public String toString() {
        return String.format("%s %d \n %s %s \n %s %d \n %s %.2f \n", "Número", this.getNumero(),
                "Descrição: ", this.getDescricao(), "Quantidade: ", this.getQuantidade(), "Preço: ", this.getPreco());
    }
}
