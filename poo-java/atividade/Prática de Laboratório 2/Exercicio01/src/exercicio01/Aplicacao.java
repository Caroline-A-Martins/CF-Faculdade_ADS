
package exercicio01;

public class Aplicacao {
    public static void main(String[] args) {
    
    Livro livro = new Livro(123, 50.00, "Dom Casmurro", "Machado de Assis", "Editora ABC", "978-3-16-148410-0", 1899);
    
    CompactDisc cd = new CompactDisc(456, 30.00,"I Want It All","Greatest Hits", "Queen", "EMI");

    System.out.printf("Livro: %s\n", livro.toString());
    System.out.printf("CD: %s\n", cd.toString());
    }
}
