package testeproduto;
import produto.Produto;
import java.util.Scanner;

public class TesteProduto {
    public static void main(String[] args) {
        //com printf e exiba o valor do desconto.
        Produto p1 = new Produto ();
        Scanner leia = new Scanner(System.in);
        String desc;
        int qtde;
        double val;
      
        System.out.println("Informe a descrição do produto");
        desc = leia.nextLine();
        System.out.println("Informe a quantidade");
        qtde = leia.nextInt();
        System.out.println("Informe o preço");
        val = leia.nextDouble();
       
        //alterando os atributos
        p1.setDescricao(desc);
        p1.setQuantidade(qtde);
        p1.setPreco(val);
       
        //retornando os valores
        System.out.println("Descrição: " + p1.getDescricao());
        System.out.println("Quantidade: "  + p1.getQuantidade());
        System.out.println("Preço: " + p1.getPreco());
        System.out.printf("Desconto %.2f \n",p1.calculaDesconto(val));
       
       
       }
      
   }
    