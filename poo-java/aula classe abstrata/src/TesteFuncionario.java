
// Classe de teste
public class TesteFuncionario {
    public static void main(String[] args) {
        // Criando um objeto da classe Vendedor
        Vendedor vendedor = new Vendedor("João", 2000.0, "São Paulo", 0.2);

        // Alterando os atributos do vendedor
        vendedor.setRegiao("Rio de Janeiro");
        vendedor.setComissao(0.3);

        // Chamando o método reajuste do vendedor
        vendedor.reajuste();

        // Imprimindo os atributos do vendedor
        System.out.println("Nome: " + vendedor.getNome());
        System.out.println("Salário: " + vendedor.getSalario());
    }
}
