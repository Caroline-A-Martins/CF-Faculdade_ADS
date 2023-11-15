package exercicio03;

public class Aplicação {
    public static void main(String[] args) {
        FuncionarioMensalista f1 = new FuncionarioMensalista(4500, "Joaquim", "Ferreira", "44444444444") {};
        FuncionarioHorista f2 = new FuncionarioHorista("Leila", "Carvalho", "55555555555", 78.8, 40){};
        FuncionarioComissao f3 = new FuncionarioComissao("Luiza", "Dantas", "77777777777", 7896.66, 0.5) {};
       
        f1.setSalarioMensal();
       
        f2.setNumeroHoras();
        f2.setSalarioHora();
       
        f3.setComissao();
        f3.setVendaBruta();
       
        System.out.printf("%s\n\n", f1);
       
        System.out.printf("%s\n", f2);
        System.out.printf("Salário: %.2f\n\n", f2.calculaSalario());
       
        System.out.printf("%s\n", f3);
        System.out.printf("Salário: %.2f\n\n", f3.calculaSalario());
    }
}