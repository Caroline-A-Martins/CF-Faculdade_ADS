using System;

class Program {
    static void Main(string[] args) {
        int fat = 1;
        
        Console.Write("Digite um número: ");
        int num = int.Parse(Console.ReadLine());

        for (int i = 1; i <= num; i++) {
            fat *= i;
        }

        Console.WriteLine("O fatorial de " + num + " é " + fat);
    }
}
