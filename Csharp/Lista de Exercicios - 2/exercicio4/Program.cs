using System;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Digite o primeiro número: ");
        int v1 = int.Parse(Console.ReadLine());

        Console.Write("Digite o segundo número: ");
        int v2 = int.Parse(Console.ReadLine());

        int impar = 0;

        if (v2 < v1)
        {
            int aux = v1;
            v1 = v2;
            v2 = aux;
        }

        for (int i = v1; i <= v2; i++)
        {
            if (i % 2 == 1)
            {
                impar++;
            }
        }

        Console.WriteLine($"Quantidade de números ímpares: {impar}");
    }
}
