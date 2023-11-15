public class Testeempresa {
    public static void main(String[] args) {
       Programador p1 = new Programador();
       p1.setNome("Chaves");
       p1.setCpf("122344");
       p1.setSalario(2000.00);
       p1.setLinguagem("Java");
       p1.setProjeto("Vendas");
      
        System.out.println("Nome: " + p1.getNome());
        System.out.println("CPF: " + p1.getCpf());
        System.out.println("Salário: " + p1.getSalario());
        System.out.println("Projeto: " + p1.getProjeto());
        System.out.println("Linguagem: " + p1.getLinguagem());    
      
      
    }
   
}