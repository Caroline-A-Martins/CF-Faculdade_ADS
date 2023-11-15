
package exercicio01;

public class Produto {
    private int cod;
    private double preco;
    private String descricao;

    public Produto(int cod, double preco, String descricao) {
        this.cod = cod;
        this.preco = preco;
        this.descricao = descricao;
    }

    public int getCod() {
        return cod;
    }

    public void setCod(int cod) {
        this.cod = cod;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }
    
    @Override
    public String toString() {
        return "Código: " + cod + " | Preço: R$" + preco + " | Descrição: " + descricao;
    }
    
}
