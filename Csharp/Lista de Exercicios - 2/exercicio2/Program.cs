using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args){
            Console.Write("Digite o primeiro número: ");
            int v1 = int.Parse(Console.ReadLine());

            Console.Write("Digite o segundo número: ");
            int v2 = int.Parse(Console.ReadLine());

            Console.WriteLine("Números ímpares em ordem decrescente:");

                if (v2 < v1)
                {
                    int aux = v1;
                    v1 = v2;
                    v2 = aux;
                }

                for (int i = v2; i >= v1; i--)
                {
                    if (i % 2 == 1)
                    {
                        Console.WriteLine(i);
                    }
                }
            }
        }
    }

