using System;

class Program
{
    static void Main(string[] args)
    {
        int[,] matriz = new int[5, 5];
        Random random = new Random();

       
        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                matriz[i, j] = random.Next(1, 26);
            }
        }

        
        Console.WriteLine("Matriz:");
        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                Console.Write(matriz[i, j] + "\t");
            }
            Console.WriteLine();
        }

        int soma = 0;

        
        Console.Write("Valores das diagonais: ");
        for (int i = 0; i < 5; i++)
        {
            Console.Write(matriz[i, i] + ", ");
            soma += matriz[i, i];
        }
        Console.WriteLine("\nSoma dos valores das diagonais: " + soma);
    }
}
