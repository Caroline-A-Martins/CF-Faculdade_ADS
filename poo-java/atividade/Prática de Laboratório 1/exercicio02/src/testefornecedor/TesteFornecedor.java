package testefornecedor;
import fornecedor.Fornecedor;

public class TesteFornecedor {
    public static void main(String[] args) {
        Fornecedor f1 = new Fornecedor("Amanda", "RUA A", "123456", "15999999999");
        Fornecedor f2 = new Fornecedor("Caroline", "RUA C", "78910", "15888888888");
        System.out.printf("Fornecedor: %s; Endereço: %s; Inscrição Estadual: %s; Contato: %s; \n", f1.getEmpresa(), f1.getEndereco(), f1.getInscricaoEstadual(), f1.getNomeContato());
        System.out.printf("Fornecedor: %s; Endereço: %s; Inscrição Estadual: %s; Contato: %s; \n", f2.getEmpresa(), f2.getEndereco(), f2.getInscricaoEstadual(), f2.getNomeContato());
    }
}
