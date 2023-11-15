package faculdade;

public class Faculdade {
    private String nome;
    private String curso;
    private String ra;
    private double nota;
    private double mensalidade;
    
    
    public void setNome (String nome){
        this.nome = nome;
    }
    
    public void setCurso (String curso){
        this.curso = curso;
    }
    
    public void setRa (String ra){
        this.ra = ra;
    }
    
    public void setNota (double nota){
        this.nota = nota;
    }
    
    public void setMensalidade (double mensalidade){
        this.mensalidade = mensalidade;
    }
    
    public String getNome(){
        return nome;
    }
    
    public String getCurso(){
        return curso;
    }
    
    public String getRa(){
        return ra;
    }
    
    public double getNota(){
        return nota;
    }
    
    public double getMensalidade(){
        return mensalidade;
    }
    
    public double descontoMensalidade(double nota){
        if (nota >= 9)
            return mensalidade * 0.50;    
        else
            return mensalidade;  
    }
}


