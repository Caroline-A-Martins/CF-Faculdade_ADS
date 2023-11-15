using System;

class Program
{
    static void Main(string[] args)
    {
        string[] alunos = new string[10];
        double[,] notas = new double[10, 3];
        double[] medias = new double[10];

        // Lê os nomes dos alunos
        for (int i = 0; i < 10; i++)
        {
            Console.Write($"Digite o nome do aluno {i + 1}: ");
            alunos[i] = Console.ReadLine();
        }

        // Lê as notas de cada aluno
        for (int i = 0; i < 10; i++)
        {
            Console.WriteLine($"Digite as notas do aluno {alunos[i]}");
            for (int j = 0; j < 3; j++)
            {
                Console.Write($"Nota {j + 1}: ");
                notas[i, j] = double.Parse(Console.ReadLine());
            }
            // Calcula a média das notas do aluno
            medias[i] = (notas[i, 0] + notas[i, 1] + notas[i, 2]) / 3.0;
        }

        // Exibe o relatório com os dados dos alunos
        Console.WriteLine("Relatório dos Alunos:");
        for (int i = 0; i < 10; i++)
        {
            Console.Write($"Aluno: {alunos[i]} - Notas: {notas[i, 0]:N1}, {notas[i, 1]:N1}, {notas[i, 2]:N1} - Média: {medias[i]:N1} - ");

            // Verifica se o aluno foi aprovado ou reprovado
            if (medias[i] >= 7.0)
            {
                Console.ForegroundColor = ConsoleColor.Blue;
                Console.WriteLine("APROVADO");
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("REPROVADO");
            }
            Console.ResetColor();
        }
    }
}
