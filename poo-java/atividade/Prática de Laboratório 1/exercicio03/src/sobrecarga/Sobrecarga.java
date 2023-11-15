package sobrecarga;

public class Sobrecarga {
    
    public void adiciona(int valor1, int valor2) {
            int resultado = valor1 + valor2;
            System.out.println("O resultado é: " + resultado);
    }
    public void adiciona(int valor1, int valor2, int valor3) {
            int resultado = valor1 + valor2 + valor3;
            System.out.println("O resultado é: " + resultado);
    }
    public void adiciona(double valor1, double valor2) {
            double resultado = valor1 + valor2;
            System.out.println("O resultado é: " + resultado);
    }
    public void adiciona(String nome, String sobrenome) {
            String resultado = nome + " " + sobrenome;
            System.out.println("O resultado é: " + resultado);
    }
}
