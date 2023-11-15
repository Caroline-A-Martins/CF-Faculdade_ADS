//9)Escreva um programa que receba valores inteirospara as variáveis W, X, Y e Z e calcule a expressão lógica ((X >= Y) AND (Z <=X)) OR ((X == W) AND (Y == Z)) OR (NOT(X != W)).

using System;
public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Informe o valor de x: ");
        int x = int.Parse(Console.ReadLine());
       
        Console.WriteLine("Informe o valor de z: ");
        int y = int.Parse(Console.ReadLine());
       
        Console.WriteLine("Informe o valor de z: ");
        int z = int.Parse(Console.ReadLine());
       
        Console.WriteLine("Informe o valor de w: ");
        int w = int.Parse(Console.ReadLine());

        bool calc = ((x >= y) && (z <= x)) || ((x == w) && (y == z)) || (!(x != w ));

        Console.WriteLine("((" + x + " >= " + y + ") && (" + z + " <= " + x + ")) || ((" + x + " == " + w + ") && (" + y + " == " + z + ")) || (!(" + x + "!=" + w + "))");
        Console.WriteLine("Resultado: {0}",calc);
        
        Console.ReadKey();
    }
}
