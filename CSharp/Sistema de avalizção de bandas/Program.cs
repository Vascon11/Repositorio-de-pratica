//List<string> listasDasBandas = new List<string>{"U2", "The Beatles","Calipsu", "Metallica", "AC/DC", "Iron Maiden", "Guns N' Roses", "Led Zeppelin"};
using System.Linq;
Dictionary<string, List<int>> bandasRegistradas = new Dictionary<string, List<int>>();
bandasRegistradas.Add("Linkin Park", new List<int> {1,2,3,4,5,6,7,8,9,10});
bandasRegistradas.Add("Pink Floyd", new List<int>());
bandasRegistradas.Add("AC/DC", new List<int>());

void ExibirLogo()
{

Console.WriteLine(@"

░░░░░░░░░░██╗░░░██╗░█████╗░░██████╗░█████╗░░█████╗░███╗░░██╗░░███╗░░░░░░░░░░░
░░░░░░░░░░██║░░░██║██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░██║░████║░░░░░░░░░░░
░░░░░░░░░░╚██╗░██╔╝███████║╚█████╗░██║░░╚═╝██║░░██║██╔██╗██║██╔██║░░░░░░░░░░░
░░░░░░░░░░░╚████╔╝░██╔══██║░╚═══██╗██║░░██╗██║░░██║██║╚████║╚═╝██║░░░░░░░░░░░
░░░░░░░░░░░░╚██╔╝░░██║░░██║██████╔╝╚█████╔╝╚█████╔╝██║░╚███║███████╗░░░░░░░░░
░░░░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚══╝╚══════╝░░░░░░░░░");
}


void ExibirOpcoesDoMenu()
	{
    Console.Clear();
    ExibirLogo();

	Console.WriteLine("\nDigite 1 para registrar a banda");

	Console.WriteLine("Digite 2 para mostrar as bandas");

	Console.WriteLine("Digite 3 para avaliar uma banda");

	Console.WriteLine("Digite 4 para exibir a média de uma banda");

	Console.WriteLine("Digite -1 para sair\n");

	Console.WriteLine("Digite aqui:");

	string opcaoEscolhida = Console.ReadLine()!;

	int opcaoEscolhidaNumerica = int.Parse(opcaoEscolhida);

// o ! serve para a variavel nao aceitar um valor nulo

	switch(opcaoEscolhidaNumerica)

	{

		case 1: RegistrarBanda();
            break;

		case 2: MostrarBandasRegistradas();

			break;

		case 3: AvaliarUmaBanda();

			break;

		case 4: Exbirmediabanda();

			break;

		case -1: Console.WriteLine("Encerrando o programa, bye bye");

			break;

		default: Console.WriteLine("Opção Invalida");

			break;

	}

}



void RegistrarBanda()
{
     Console.Clear();
     ExibirTituloDaOpcao("Registro de bandas");
     Console.Write("\nDigite o nome da banda que deseja registrar: ");
     string nomeDaBanda = Console.ReadLine()!;
     bandasRegistradas.Add(nomeDaBanda, new List<int>{1});
     Console.WriteLine($"A banda {nomeDaBanda} foi registrada com sucesso!");	 
     Thread.Sleep(2000);
     Console.Clear();
     ExibirOpcoesDoMenu();
}


void MostrarBandasRegistradas()
{
    Console.Clear();
     ExibirTituloDaOpcao("Exibindo todas as bandas registradas ");
    foreach(string banda in bandasRegistradas.Keys)
    {
        Console.WriteLine($"Banda: {banda}");
    }
    Console.WriteLine("\nDigite qualquer tecla para volta para o menu!");
    Console.ReadKey();
    Console.Clear();
    ExibirOpcoesDoMenu();
}   


void AvaliarUmaBanda()
{
    //Qual banda deseja avaliar
    //se a banda existe no dicionario
    //se nao volta ao menu principal
    Console.Clear();
    ExibirTituloDaOpcao("Avaliar Banda");
    foreach(string banda in bandasRegistradas.Keys)
    {
        Console.WriteLine($"Banda: {banda}");
    }

    Console.Write("\nDigite o nome da banda que deseja avaliar: ");
    string nomedebanda = Console.ReadLine()!;
    if (bandasRegistradas.ContainsKey(nomedebanda))
    {
        Console.WriteLine($"Qual a nota que a banda {nomedebanda} merede: ");
        int nota = int.Parse(Console.ReadLine()!);
        bandasRegistradas[nomedebanda].Add(nota);
        Console.WriteLine($"\nA nota {nota} foi registrada com sucessoro para a banda {nomedebanda}");
        Thread.Sleep(4000);
        ExibirOpcoesDoMenu();
    }
    else
    {
        Console.WriteLine($"\nA banda {nomedebanda} não foi encontrada!");
        Console.WriteLine("Digite uma tecla para voltar ao menu principal!");
        Console.ReadKey();
        ExibirOpcoesDoMenu();
    }

}


void ExibirTituloDaOpcao(string titulo)
{
    int quantidadeDeLetras = titulo.Length;
    string asteriscos = string.Empty.PadLeft(quantidadeDeLetras, '*');
    Console.WriteLine(asteriscos);
    Console.WriteLine(titulo);
    Console.WriteLine(asteriscos + "\n");
}

void Exbirmediabanda()
{
    Console.Clear();
    ExibirTituloDaOpcao("Exibição da média das bandas");

    foreach (var banda in bandasRegistradas)
    {
        // banda.Key = Nome da banda (string)
        // banda.Value = Lista de notas (List<int>)
        
        Console.WriteLine($"Banda: {banda.Key}");
        
        if (banda.Value.Count > 0)
        {
            double media = banda.Value.Average();
            Console.WriteLine($"Média: {media:F1}");//F1 deixa uma casa decimal
        }
        else
        {
            Console.WriteLine("Média: (Sem avaliações)");
        }

        Console.WriteLine(new string('-', 20));
    }
    
    Console.WriteLine("\nPressione qualquer tecla para voltar...");
    Console.ReadKey(); // ReadKey é melhor que Read aqui
    ExibirOpcoesDoMenu();
}

ExibirOpcoesDoMenu();
