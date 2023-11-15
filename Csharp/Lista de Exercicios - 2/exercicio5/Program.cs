using System;

class Program {
    static void Main(string[] args) {
        int maior = int.MinValue;
        
        for (int i = 0; i < 15; i++) {
            Console.Write("Digite o " + (i+1) + "º número: ");
            int num = int.Parse(Console.ReadLine());
            
            if (num > maior) {
                maior = num;
            }
        }
        
        Console.WriteLine("O maior número digitado foi: " + maior);
    }
}
