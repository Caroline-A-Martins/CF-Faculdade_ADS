using System;
					
public class Program
{
	public static void Main()
	{
		Console.WriteLine("1)Escreva um programa que exiba na tela em ordem crescente, apenas os números pares existentes de 11 a 250. ");
		for (int x = 11; x <= 250; x++){
			if (x % 2 == 0 ){
				Console.Write(x + ", ");
			}
		}
	}
}