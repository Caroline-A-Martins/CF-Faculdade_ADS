//8)Escreva um programa que leia dois números inteiros, sendo armazenados respectivamente nas variáveis A e B. O programa deverá inverter os valores entre as variáveis, de modo que o valor da variável A seja atribuído na variável B e vice-versa. Ao final exibir os valores de cada variável. 
using System;
public class Program
{
    public static void Main(string[] args)
    {
        int c=0;

        Console.WriteLine("Digite um valor: ");
        int a = int.Parse(Console.ReadLine());
        Console.WriteLine("Digite outro valor: ");
        int b = int.Parse(Console.ReadLine());

        Console.WriteLine("Valores lidos, {0} e {1}",a,b);
        
        c=a;
        a=b;
        b=c;
        
        Console.WriteLine("Valores invertidos, {0} e {1}",a,b);
        Console.ReadKey();
    }
}
