using System;

class Program
{
    static void Main(string[] args)
    {
        int[,] matriz = new int[5, 5];

        // Lê os elementos da matriz
        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                Console.Write($"Digite o valor da posição [{i},{j}]: ");
                matriz[i, j] = int.Parse(Console.ReadLine());
            }
        }

        // Calcula a soma de todos os elementos da matriz
        int somaTotal = 0;
        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                somaTotal += matriz[i, j];
            }
        }
        Console.WriteLine($"A soma de todos os elementos da matriz é: {somaTotal}");

        // Calcula a soma dos valores dos elementos de cada linha da matriz
        for (int i = 0; i < 5; i++)
        {
            int somaLinha = 0;
            for (int j = 0; j < 5; j++)
            {
                somaLinha += matriz[i, j];
            }
            Console.WriteLine($"A soma dos valores da linha {i + 1} da matriz é: {somaLinha}");
        }
    }
}
