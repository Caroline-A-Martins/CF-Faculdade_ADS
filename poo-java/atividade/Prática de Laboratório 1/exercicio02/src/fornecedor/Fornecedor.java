package fornecedor;

public class Fornecedor {
    private String empresa, endereco, inscricao_estadual, nome_contato;

    public Fornecedor(String empresa, String endereco, String inscricao_estadual, String nome_contrato) {
        this.empresa = empresa;
        this.endereco = endereco;
        this.inscricao_estadual = inscricao_estadual;
        this.nome_contato = nome_contato;
    }
    public void setEmpresa(String empresa) {
            this.empresa = empresa;
    }
    public void setEndereco(String endereco) {
            this.endereco = endereco;
    }
    public void setInscricaoEstadual(String inscricao_estadual) {
            this.inscricao_estadual = inscricao_estadual;
    }
    public void setNomeContato(String nome_contato) {
            this.nome_contato = nome_contato;
    }
    public String getEmpresa() {
            return empresa;
    }
    public String getEndereco() {
            return endereco;
    }
    public String getInscricaoEstadual() {
            return inscricao_estadual;
    }
    public String getNomeContato() {
            return nome_contato;
    }
}

    
