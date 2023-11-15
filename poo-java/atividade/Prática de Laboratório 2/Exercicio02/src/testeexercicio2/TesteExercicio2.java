package testeexercicio2;
import org.me.exercicio2.*;

public class TesteExercicio2 {
    public static void main(String[] args) {
        Engenheiro e1 = new Engenheiro("01AB", "Antonino Ferreira", 6500, "Departamento de Construções", "AF545864f5d47f5") {
        };
        Gerente g1 = new Gerente("02LK", "Julia Rodrigues", 7000, 856) {
        };

        e1.calculoSalario();
        g1.calculoSalario();

        System.out.printf("%s\n", e1);
        System.out.printf("%s\n", g1);
    }
}
