import java.util.Scanner;

public class Teste {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Digite o nome da secretaria: ");
        String nomeSec = input.nextLine();

        System.out.print("Digite o CPF da secretaria: ");
        String cpfSec = input.nextLine();

        System.out.print("Digite o salário da secretaria: ");
        double salarioSec = input.nextDouble();

        input.nextLine(); // Consumir a quebra de linha após o próximoDouble()

        System.out.print("Digite o departamento da secretaria: ");
        String deptoSec = input.nextLine();

        System.out.print("Digite o idioma da secretaria: ");
        String idiomaSec = input.nextLine();

        Secretaria sec = new Secretaria(nomeSec, cpfSec, salarioSec, deptoSec, idiomaSec);

        System.out.print("Digite o nome do vendedor: ");
        String nomeVen = input.nextLine();

        System.out.print("Digite o CPF do vendedor: ");
        String cpfVen = input.nextLine();

        System.out.print("Digite o salário do vendedor: ");
        double salarioVen = input.nextDouble();

        input.nextLine(); // Consumir
    }
}
