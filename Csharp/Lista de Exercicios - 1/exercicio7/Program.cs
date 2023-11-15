//7)Escreva um programa queleia o nome de duas pessoas e ao final exiba:
//a)O nome das duas pessoas com todos os caracteres maiúsculos;
//b)A quantidade de caracteres de cada nome;
//c)Apenas os três primeiros caracteres de cada nome.
using System;
public class Program
{
    public static void Main(string[] args)
    {
        string nome1, nome2;
        
        Console.Write("Digite um nome: ");
        nome1 = Console.ReadLine();
        
        Console.Write("Digite outro nome: ");
        nome2 = Console.ReadLine();
        Console.WriteLine("--------------------------------------");

        int tamanho1 = nome1.Length;
        int tamanho2 = nome2.Length;

        Console.WriteLine("{0} em maiúsculo fica: {1} ",nome1, nome1.ToUpper());
        Console.WriteLine("Quantidade de letras: {0} ",tamanho1);
        Console.WriteLine("As 3 primeiras letras: {0} ",nome1.Substring(0,3));
        Console.WriteLine("--------------------------------------");
        Console.WriteLine("{0} em maiúsculo fica: {1} ",nome2, nome2.ToUpper());
        Console.WriteLine("Quantidade de letras: {0} ",tamanho2);
        Console.WriteLine("As 3 primeiras letras: {0} ",nome2.Substring(0,3));
        Console.ReadKey();

    }
}