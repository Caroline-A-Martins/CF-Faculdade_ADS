using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

using System.Threading.Tasks;

 

namespace ConsoleApplication1 {
    class Program{
        static void Main(string[] args) {

            String nome; 
            float n1, n2; 

 
            Console.WriteLine("Informe o nome do aluno(a): ");
            nome = Console.ReadLine();

            n1 = lerNota(); 
            n2 = lerNota() ; 
            calcularMedia(n1, n2); 
        }

        static float lerNota(){

            float nota; 

            Console.WriteLine("Informe nota: "); 
            nota = float.Parse(Console.ReadLine()); 
            return nota; 
        }
        static float calcularMedia(float n1,float n2){ 

            float media;

            media = (n1 + n2) / 2;
            if (media >= 7.0){
                Console.WriteLine("A média está aprovada"); 
            }else{
                Console.WriteLine("A média está reprovada"); 
            }
            return media; 

        }
    }
} 
