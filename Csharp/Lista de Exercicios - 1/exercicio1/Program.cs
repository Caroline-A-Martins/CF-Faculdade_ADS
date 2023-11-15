// 1 ) Escreva um programa que armazene em variáveis o seu nome, 
//sua idade e a cidade onde reside. 
//Na sequencia exiba o conteúdo destas variáveis na tela. 
using System;

namespace exercicio1
{
    class Program
    {
    public static void Main(string[] args)
    {
        string nome, cidade;
        int idade;

        Console.Write("Seu nome: ");
        nome = Console.ReadLine();

        Console.Write("Sua idade: ");
        idade = int.Parse(Console.ReadLine());

        Console.Write("Sua cidade: ");
        cidade = Console.ReadLine();
        Console.WriteLine();
        
        Console.Write(nome + ", " + idade + "anos, " + cidade);
        
        Console.ReadKey();
        }
    }
}