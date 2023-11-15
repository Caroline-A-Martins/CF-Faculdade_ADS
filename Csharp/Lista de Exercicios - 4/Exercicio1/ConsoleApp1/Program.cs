using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        int[] numeros = new int[15];

        // Lê os números e armazena no vetor
        for (int i = 0; i < 15; i++)
        {
            Console.Write($"Digite o {i + 1}º número: ");
            numeros[i] = int.Parse(Console.ReadLine());
        }

        // Exibe os números nas posições pares
        Console.Write("Números nas posições pares: ");
        for (int i = 0; i < 15; i += 2)
        {
            Console.Write(numeros[i] + " ");
        }
    }
}
