// 4) Escreva um programa que calcule e exiba o resultado da seguinte expressão matemática: (Dica: O usuário deverá informar os valores para as variáveis A, B e C) A² * 5 –C / (B –A % 4)using System;

public class Program
{
    public static void Main(string[] args)
    {
       
        double a,b,c,res;

       Console.Write("Digite um número: ");
       a = double.Parse(Console.ReadLine());  

       Console.Write("Digite outro número: ");
       b = double.Parse(Console.ReadLine());  

       Console.Write("Digite outro número: ");
       c = double.Parse(Console.ReadLine()); 
       
       res = (a * a) * 5 - c / (b - a % 4);
       Console.Write(a+"² * 5 – " + c + "/ (" + b + " - " + a + " % 4) = " + res );
       Console.ReadKey();
        
       
    }
}