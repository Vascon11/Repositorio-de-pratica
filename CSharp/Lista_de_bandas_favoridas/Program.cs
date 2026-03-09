//Criar uma lista de bandas vazia e adicionar suas bandas prediletas em seguida.

using System.Reflection;

class Programa
{
    private static List <string> Bandas = new List<string>{};
    private static bool repedicao = true;

    static void registrar()
        {
            Console.Clear();
            Console.WriteLine("Digite aqui a nova banda aqui:");
            string nova = Console.ReadLine()!;
            Bandas.Add(nova);
    }
    static void exibicao()
        {
            Console.Clear();
            foreach (string band in Bandas)
                {
                    Console.WriteLine(band);
                }
            Console.WriteLine("\nDigite qualquer tecla para voltar para o menu");
            Console.ReadKey();    
        }


    static void Main(){
        while (repedicao){
            Console.Clear();
            Console.WriteLine(@"
            Digite [1] para registrar uma nova banda
            Digite [2] para Mostrar a Lista
            Digite [3] para sair");
            
            string opcaoEscolha = Console.ReadLine()!;
            int opcaoEscolhidaNumerica = int.Parse(opcaoEscolha);

            switch (opcaoEscolhidaNumerica)
            {
                case 1:registrar();
                    break;
                case 2: exibicao();
                    break;
                case 3: repedicao = false;Console.Clear();
                    break;
                default:
                    Console.WriteLine("Opção inválida");
                    break;
        }
        }
    }
}
