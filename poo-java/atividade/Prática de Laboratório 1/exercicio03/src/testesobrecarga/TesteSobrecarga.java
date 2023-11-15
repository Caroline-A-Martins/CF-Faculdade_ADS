package testesobrecarga;
import sobrecarga.Sobrecarga;

public class TesteSobrecarga {
    public static void main(String[] args) {
        Sobrecarga s1 = new Sobrecarga();
        s1.adiciona(4, 3);
        s1.adiciona(6, 7, 4);
        s1.adiciona(34.2, 8.99);
        s1.adiciona("José", "Almeida");

        Sobrecarga s2 = new Sobrecarga();
        s2.adiciona(65, 74);
        s2.adiciona(11, 27, 89);
        s2.adiciona(78.6, 11.50);
        s2.adiciona("Maria", "José");
    }
}

