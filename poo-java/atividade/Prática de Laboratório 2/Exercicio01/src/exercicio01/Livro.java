
package exercicio01;
public class Livro extends Produto {
    
    private String autor;
    private String editora;
    private String isbn;
    private int ano;

    public Livro(int cod, double preco, String descricao,String autor, String editora, String isbn, int ano) {
        super(cod, preco, descricao);
        this.autor = autor;
        this.editora = editora;
        this.isbn = isbn;
        this.ano = ano;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public String getEditora() {
        return editora;
    }

    public void setEditora(String editora) {
        this.editora = editora;
    }

    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }
    
     @Override
    public String toString() {
        return super.toString() + " | Autor: " + autor + " | Editora: " + editora + " | ISBN: " + isbn + " | Ano: " + ano;
    }
}
