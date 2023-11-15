package testebobrecarga;

import sobrecarga.Sobrecarga;

public class TesteSobrecarga {
    public static void main(String[] args){
        Sobrecarga s = new Sobrecarga();
        s.calcula(10);
        s.imprimeCalculo();
        s.calcula(10, 20);
        s.imprimeCalculo();
        s.calcula(3, 4, 5);
        s.imprimeCalculo();
        s.calcula(10, 20, 30, 40);
        s.imprimeCalculo();       
    }  
}
