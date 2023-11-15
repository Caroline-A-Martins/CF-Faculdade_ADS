//6)Escreva um programa que leia um valor em Reais (R$), leia também a cotação do Dólar, realize o cálculo da conversão de moeda (de Reais para Dólares) e exiba na tela o resultado.
using System;
public class Program
{
    public static void Main(string[] args)
    {
        double dolar =5.17;
        
        Console.WriteLine("Digite um valor: ");
        double valor = double.Parse(Console.ReadLine());
        Console.WriteLine("R$" +valor + "convertido em dolar é U$" + (valor * dolar));
        Console.ReadKey();

    }
}