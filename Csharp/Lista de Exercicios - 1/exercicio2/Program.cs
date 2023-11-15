//2 ) Escreva um programa que leia um número inteiro, 
//calculee exiba na tela o dobro deste número.
using System;
namespace exercicio2
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1;
            Console.WriteLine("Digite um número: ");
            num1 = int.Parse(Console.ReadLine());
            Console.WriteLine("Seu dobro é: " + (num1*2));
        Console.ReadKey();
        }
    }
}