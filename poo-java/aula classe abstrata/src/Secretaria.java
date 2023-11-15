// Subclasse Secretaria
class Secretaria extends Funcionario {
    // Atributos privados
    private String idioma;
    private String departamento;

    // Método construtor
    public Secretaria(String nome, double salario, String idioma, String departamento) {
        super(nome, salario);
        this.idioma = idioma;
        this.departamento = departamento;
    }

    // Métodos set e get para idioma
    public void setIdioma(String idioma) {
        this.idioma = idioma;
    }

    public String getIdioma() {
        return idioma;
    }

    // Métodos set e get para departamento
    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }

    public String getDepartamento() {
        return departamento;
    }

    // Implementação do método abstrato reajuste
    public void reajuste() {
        salario *= 1.15;
    }
}
