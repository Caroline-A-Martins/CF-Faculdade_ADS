package sobrecarga;

public class Sobrecarga {
    private int resultado;
    public void calcula(int x){
        resultado = x/2;
    }
    public void calcula(int y, int w, int z, int v){
        resultado = y + w + z + v;
    }
    public void calcula(int a, int b){
        resultado = a - b;
    }
    public void calcula(int c, int d, int e){
        resultado = c * d * e;
    }
    public void imprimeCalculo(){
        System.out.println("Resultado: " + resultado);
    }       
}
