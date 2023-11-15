// 5) Escreva um programa que leia a idade de uma pessoa e exiba na telase esta pessoa é maior ou menor de idade (considerar 18 anos para maior idade). (Dica: Usar operadores ternários)
using System;
public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Digite sua idade: ");
        int idade = int.Parse(Console.ReadLine());

        string res = (idade >= 18) ? ("Maior de idade") : ("Menor de idade");

        Console.WriteLine(res);
        Console.ReadKey();    
   
    }
}