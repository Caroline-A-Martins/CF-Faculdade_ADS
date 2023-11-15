public class Aplicacao {

    public static void main(String[] args) {

        Gerente gerente = new Gerente(12345, "Fulano", "1234567", "TI", 10);

        System.out.println("Matrícula: " + gerente.getMatricula());
        System.out.println("Nome: " + gerente.getNome());
        System.out.println("RG: " + gerente.getRg());
        System.out.println("Departamento: " + gerente.getDepartamento());
        System.out.println("Número de pessoas: " + gerente.getNumPessoas());

        Analista analista = new Analista(54321, "Beltrano", "7654321", "Sistema de Gestão");

        System.out.println("Matrícula: " + analista.getMatricula());
        System.out.println("Nome: " + analista.getNome());
        System.out.println("RG: " + analista.getRg());
        System.out.println("Projeto: " + analista.getProjeto());

    }

}



