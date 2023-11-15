using System;

class Program {
    static void Main(string[] args) {
        int num, pares = 0, impares = 0, positivos = 0, negativos = 0;
        string resposta = "N";
    
        while (resposta.ToUpper() != "S") {
            Console.Write("Digite um número (ou S para sair): ");
            if (!int.TryParse(Console.ReadLine(), out num)) {
                Console.WriteLine("Valor inválido! Tente novamente.");
                continue;
            }

            if (num % 2 == 0) {
                pares++;
            } else {
                impares++;
            }

            if (num > 0) {
                positivos++;
            } else if (num < 0) {
                negativos++;
            }

            Console.Write("Deseja encerrar o programa? (S/N): ");
            resposta = Console.ReadLine();
        }

        Console.WriteLine("Foram digitados {0} números pares, {1} números ímpares, {2} números positivos e {3} números negativos.", pares, impares, positivos, negativos);
    }
}
