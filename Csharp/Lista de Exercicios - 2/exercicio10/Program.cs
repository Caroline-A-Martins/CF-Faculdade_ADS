using System;

class Program {
    static void Main(string[] args) {
        string cod;
        int num_hrs;
        int semanaSalario;
        int totsalario;
        int excedido;
        string resposta = "N";


        while (resposta.ToUpper() != "S") {
            
            Console.WriteLine("Codigo do operador: ");
            cod = Console.ReadLine();
            Console.WriteLine("Número de horas trabalhadas por semana: ");
            num_hrs = int.Parse(Console.ReadLine());

            if (num_hrs > 50){
                excedido = (num_hrs - 50) * 20;
                semanaSalario = num_hrs * 10 + excedido;
                Console.WriteLine("O funcionario {0} trabalha {1} horas, tem um salário semanal de R$ {2}, com um acréscimo de R$ {3} por trabalhar mais de 50 horas",cod, num_hrs,semanaSalario,excedido);
            } else {
                semanaSalario = num_hrs * 10;
                Console.WriteLine("O funcionario {0} trabalha {1} horas, tem um salário de R$ {2}",cod, num_hrs,semanaSalario);
            }

            totsalario = semanaSalario*4;
            Console.WriteLine("Seu salario mensal é de {0}", totsalario);

            Console.Write("Deseja encerrar o programa? (S/N): ");
            resposta = Console.ReadLine();
        }
    }
}
