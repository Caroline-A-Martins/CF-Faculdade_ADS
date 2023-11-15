using System;

class Program
{
    static void Main(string[] args)
    {
        string[] nomes = new string[10];
        double[] precos = new double[10];

        for (int i = 0; i < 10; i++)
        {
            Console.Write($"Digite o nome do produto {i + 1}: ");
            nomes[i] = Console.ReadLine();

            Console.Write($"Digite o preço do produto {i + 1}: ");
            precos[i] = double.Parse(Console.ReadLine());
        }

        Console.Write("Digite um valor para pesquisar os produtos: ");
        double valor = double.Parse(Console.ReadLine());

        Console.WriteLine("Produtos com preço até R$ " + valor + ":");
        for (int i = 0; i < 10; i++)
        {
            if (precos[i] <= valor)
            {
                Console.WriteLine(nomes[i] + " - R$ " + precos[i]);
            }
        }
    }
}
