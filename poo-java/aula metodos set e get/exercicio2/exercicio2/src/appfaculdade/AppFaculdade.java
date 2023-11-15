package appfaculdade;

import faculdade.Faculdade;

public class AppFaculdade {
    public static void main(String[] args) {
        Faculdade f1 = new Faculdade();
        
        f1.setNome("Maria");
        f1.setCurso("ADS");
        f1.setRa("123456");
        f1.setNota(10);
        f1.setMensalidade(400.00);
        
        System.out.println("Nome: " + f1.getNome() );
        System.out.println("RA: " + f1.getRa() );
        System.out.println("Curso: " + f1.getCurso() );
        System.out.println("Nota: " + f1.getNota() );
        System.out.println("Mensalidade: " + f1.descontoMensalidade(10));
        
        
            
        }
        
    }
    