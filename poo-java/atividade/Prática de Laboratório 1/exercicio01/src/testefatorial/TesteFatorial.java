package testefatorial;
import java.util.Scanner;
import fatorial.Fatorial;


public class TesteFatorial {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Fatorial valor = new Fatorial();

        System.out.print("Digite um número inteiro: ");

        int numero = scanner.nextInt();
        valor.setNumero(numero);

        int fatorial = valor.calcularFatorial();
        System.out.printf("O fatorial de %d é %d. \n", numero, fatorial);
    }
}
