package produto;

public class Produto {
    private String descricao;
    private int quantidade;
    private double preco;
    
    public void setDescricao (String descricao){
        this.descricao = descricao;
    }
    public void setQuantidade (int quantidade){
        this.quantidade = quantidade;
    }
    public void setPreco (double preco){
        this.preco = preco;
    }
    public String getDescricao(){
        return descricao;
    }
    public int getQuantidade(){
        return quantidade;
    }
    public double getPreco(){
        return preco;
    }
    public double calculaDesconto(double preco){
        if (preco >= 100.00) 
           return preco * 0.10 * quantidade;
        else
           return preco * 0.05 * quantidade;                     
    }
}
    
