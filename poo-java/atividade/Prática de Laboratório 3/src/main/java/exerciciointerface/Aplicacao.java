
package exerciciointerface;

public class Aplicacao {

    public static void main(String[] args) {
        Pagamento pag[] = new Pagamento[4];
        pag[0] = new Fatura(10, "Descrição da fatura 1", 20, 562.66);
        pag[1] = new Fatura(20, "Descrição da fatura 2", 6, 4569.99);
        pag[2] = new FuncionarioMensalista(1500.5, "João", "Marcelo","444444444444");
        pag[3] = new FuncionarioMensalista(7896.3, "Maria", "Cristina","5555555555");

        for (Pagamento pag1 : pag) {
        System.out.printf("%s", pag1.toString());
        }
    }
} 