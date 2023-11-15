
package exercicio01;
public class CompactDisc extends Produto {
    private String album;
    private String artista;
    private String gravadora;

    public CompactDisc(int cod, double preco, String descricao,String album, String artista, String gravadora) {
        super(cod, preco, descricao);
        this.album = album;
        this.artista = artista;
        this.gravadora = gravadora;
    }

    public String getAlbum() {
        return album;
    }

    public void setAlbum(String album) {
        this.album = album;
    }

    public String getArtista() {
        return artista;
    }

    public void setArtista(String artista) {
        this.artista = artista;
    }

    public String getGravadora() {
        return gravadora;
    }

    public void setGravadora(String gravadora) {
        this.gravadora = gravadora;
    }
    
    @Override
    public String toString() {
        return super.toString() + " | Álbum: " + album + " | Artista: " + artista + " | Gravadora: " + gravadora;
    }
   
}
