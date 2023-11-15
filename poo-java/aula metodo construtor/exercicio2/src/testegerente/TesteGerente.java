package testegerente;

public class TesteGerente {
    private String nome, email, idade;
    private double salario;

    public TesteGerente (String n, String e, String i, 
    double s){
        this.nome = n; 
        this.email = e; 
        this.idade = i; 
        this.salario = s; 
    }

    public void status(){
        System.out.println("Nome: " + getNome(nome));
        System.out.println("Email: " + getEmail(email));
        System.out.println("Idade: " + getIdade(idade));
        System.out.println("Salario: " + getSalario(salario));
        }

    public String getNome(String n){
        return this.nome;
    }
    public void setNome(String n){
        this.nome = n;
    }

    public String getEmail(String e){
        return this.email;
    }

    public void setEmail(String e){
        this.email = e;
    }

    public String getIdade(String i){
        return this.idade;
    }

    public void setIdade(String i){
        this.idade = i;
    }

    public double getSalario(double s){
        return this.salario;
    }

    public void setSalario(double s){
        this.salario = s;
    }


 
}
