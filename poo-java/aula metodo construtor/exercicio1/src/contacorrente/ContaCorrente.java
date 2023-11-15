package contacorrente;

public class ContaCorrente {
    private String nome, cpf, email, telefone;
    private double saldo;

    public ContaCorrente (String nome, String cpf, String email,
    String telefone, double saldo){
        this.nome = nome;
        this.cpf =  cpf;
        this.email = cpf;
        this.telefone = telefone;
        this.saldo = saldo;
    }

    public void credito(double valor){
        saldo = saldo + valor ;
    }
    public void debito(double valor){
        saldo = saldo - valor ;
    }

    public String getNome(){
        return nome;
    }
    public String getCpf() {
        return cpf;
    }
    public String getEmail() {
        return email;
    }
    public String getTelefone() {
        return telefone;
    }
    public double getSaldo() {
        return saldo;
    }

}
