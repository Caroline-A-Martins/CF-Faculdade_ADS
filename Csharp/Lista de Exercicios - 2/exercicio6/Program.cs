using System;

class Program {
    static void Main(string[] args) {
        float media = 0;
        int i;
    
        Console.WriteLine("--- CALCULADORA DE MÉDIA ---");

        for(i = 0; i < 10; i++){
            Console.Write("Digite o " + (i+1) + "º nota: ");
            float nota = float.Parse(Console.ReadLine());
            if (nota < 0 || nota > 10){
                Console.WriteLine("Nota invalida! Digite um valor ente 0 e 10");
                i--;
            }else{
                media += nota;
            } 
        }
        media /=i;
        Console.WriteLine("A média total é: " + media);
    }
}