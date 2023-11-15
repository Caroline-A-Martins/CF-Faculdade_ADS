// 3) Escreva um programa que leia um número inteiro, 
//calcule e exiba na tela o quadrado deste número. 
//(Usar função da classe Math). 

using System;

public class Program
{
    public static void Main(string[] args)
    {

        double num;

        Console.Write("Digite um número: ");
        num = double.Parse(Console.ReadLine()); 
        Console.Write("Seu quadruplo: " );
        Console.Write(Math.Pow(num, 4));
        Console.ReadKey();
           
    }
}