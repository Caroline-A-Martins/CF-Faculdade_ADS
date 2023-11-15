package fatorial;
public class Fatorial {
    private int numero;

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public int getNumero() {
        return numero;
    }
   
    public int calcularFatorial() {
        int fatorial = 1;
        for (int i = 2; i <= numero; i++) {
            fatorial *= i;
        }

        return fatorial;
    }
}

