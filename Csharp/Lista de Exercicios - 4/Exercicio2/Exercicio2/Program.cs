using System;

class Program
{
    static void Main(string[] args)
    {
        double[] notas = new double[15];

        for (int i = 0; i < 15; i++)
        {
            Console.Write($"Digite a nota do {i + 1}º aluno: ");
            notas[i] = double.Parse(Console.ReadLine());
        }

        double media = notas.Sum() / notas.Length;

        int alunosAcimaMedia = 0;
        int alunosAbaixoMedia = 0;

        for (int i = 0; i < 15; i++)
        {
            if (notas[i] >= media)
            {
                alunosAcimaMedia++;
            }
            else
            {
                alunosAbaixoMedia++;
            }
        }

        Console.WriteLine($"Média da turma: {media}");
        Console.WriteLine($"Alunos com nota igual ou superior à média: {alunosAcimaMedia}");
        Console.WriteLine($"Alunos com nota abaixo da média: {alunosAbaixoMedia}");
    }
}
