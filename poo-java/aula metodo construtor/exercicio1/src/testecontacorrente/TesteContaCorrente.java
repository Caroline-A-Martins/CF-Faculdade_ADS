package testecontacorrente;
import java.util.Scanner;
import contacorrente.ContaCorrente;
public class TesteContaCorrente {
    public static void main(String[] args) {
        ContaCorrente c1 = new ContaCorrente("José","123455","jose@gmail","998888",100.00);
        ContaCorrente c2 = new ContaCorrente("Ana","2345555","ana@fatec","887788",200.00);
        Scanner leia = new Scanner(System.in);
        double vr_deb, vr_cred;
       System.out.println("Conta 1");
       System.out.println("Nome:" + c1.getNome());
       System.out.println("CPF: " + c1.getCpf());
       System.out.println("E-mail: " + c1.getEmail());
       System.out.println("Telefone: " + c1.getTelefone());
       System.out.printf("Saldo inicial:%.2f \n ", c1.getSaldo() );
      
       System.out.println("Informe o valor do crédito da conta 1");
       vr_cred = leia.nextDouble();
       c1.credito(vr_cred);
       System.out.println("Informe o valor do débito da conta 1");
       vr_deb = leia.nextDouble();
       c1.debito(vr_deb);
       System.out.printf("Saldo final conta 1 %.2f \n", c1.getSaldo());
       
       System.out.println("Conta 2");
       System.out.println("Nome:" + c2.getNome());
       System.out.println("CPF: " + c2.getCpf());
       System.out.println("E-mail: " + c2.getEmail());
       System.out.println("Telefone: " + c2.getTelefone());
       System.out.printf("Saldo inicial:%.2f \n ", c2.getSaldo() );
      
       System.out.println("Informe o valor do crédito da conta 2");
       vr_cred = leia.nextDouble();
       c2.credito(vr_cred);
       System.out.println("Informe o valor do débito da conta 2");
       vr_deb = leia.nextDouble();
       c2.debito(vr_deb);
       System.out.printf("Saldo final conta 1 %.2f \n", c2.getSaldo());
       
    }
   
}
