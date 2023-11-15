using System;

class Program
{
    static void Main(string[] args)
    {
        int[,] matriz = new int[4, 5];

        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                Console.Write($"Digite o valor da posição [{i},{j}]: ");
                matriz[i, j] = int.Parse(Console.ReadLine());
            }
        }


        int somaPares = 0;
        int somaImpares = 0;

        int qtdPares = 0;
        int qtdImpares = 0;



        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                if (matriz[i, j] % 2 == 0)
                {
                    qtdPares++;
                    somaPares += matriz[i, j];
                }
                else
                {
                    qtdImpares++;
                    somaImpares += matriz[i, j];
                }
            }
        }

        double mediaPares = (qtdPares > 0) ? (double)somaPares / qtdPares : 0;
        double mediaImpares = (qtdImpares > 0) ? (double)somaImpares / qtdImpares : 0;

        Console.WriteLine($"Quantidade de números pares: {qtdPares}");
        Console.WriteLine($"Quantidade de números ímpares: {qtdImpares}");
        Console.WriteLine($"Soma dos números pares: {somaPares}");
        Console.WriteLine($"Soma dos números ímpares: {somaImpares}");
        Console.WriteLine($"Média dos números pares: {mediaPares}");
        Console.WriteLine($"Média dos números ímpares: {mediaImpares}");
    }
}