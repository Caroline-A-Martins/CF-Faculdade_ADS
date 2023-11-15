public class Secretaria extends Funcionario {
    private String departamento;
    private String idioma;

    public Secretaria(String nome, String cpf, double salario, String departamento, String idioma) {
        super(nome, cpf, salario);
        this.departamento = departamento;
        this.idioma = idioma;
    }

    public String getDepartamento() {
        return departamento;
    }

    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }

    public String getIdioma() {
        return idioma;
    }

    public void setIdioma(String idioma) {
        this.idioma = idioma;
    }
}
