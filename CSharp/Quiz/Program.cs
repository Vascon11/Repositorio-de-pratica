//Crie um programa que implemente um quiz simples de perguntas e respostas.
// Utilize um dicionário para armazenar as perguntas e as respostas corretas.

int acertos = 0;
Dictionary<String, String> perguntas = new Dictionary<string, string>
{
    ["Qual é o país com o maior número de ilhas no mundo?"]="Suécia",
    ["Qual é o satélite natural da Terra?"] = "Lua",
    ["Qual é o maior animal terrestre do planeta?"] = "Elefante Africano",
    ["Qual unidade é usada para medir a intensidade do som?"] = "Decibel"
};

Console.Clear();

foreach(KeyValuePair<String, String> pergunta in perguntas)
{
    Console.WriteLine($"Pergunta: {pergunta.Key}");
    String resposta = Console.ReadLine()!;
    if (resposta == pergunta.Value)
    {
        Console.WriteLine("\nParabéns voce acertou\n");
        acertos+=1;
    }
    else
    {
        Console.WriteLine($"\nVoce errou a resposta era {pergunta.Value}\n");
    }
    Console.ReadKey();
    Console.Clear();
}

Console.WriteLine($"Parabéns! voce acertou {acertos} de 4 perguntas!");