//Criar um programa que gerencie o estoque de uma loja. Utilize um dicionário para armazenar produtos e 
//suas quantidades em estoque e mostre, a partir do nome de um produto, sua quantidade em estoque. 


Dictionary<String, int> produtos = new Dictionary<string, int>
{
    ["Alface"] = 6,
    ["Pão"] = 54,
    ["Maçã"] = 15,
    ["Manteiga"] = 10,
    ["Ovos"] = 12,
    ["Leite"] = 8,
    ["Café"] = 7,
    ["Frutas"] = 10,
    ["Cebola"] = 6,
    ["Tomate"] = 6,
    ["Batata"] = 7,
    ["Milho"] = 5,
    ["Queijo"] = 8,
    ["Iogurte"] = 9,
    ["Arroz"] = 5,
    ["Lenzes"] = 4,
    ["Temperos"] = 3,
};

int Busca (String nomeProduto)
{
    if (produtos.ContainsKey(nomeProduto)){
        return produtos[nomeProduto];
    } else
    {
        return 0;
    }
}

Console.WriteLine("A loja possui os seguintes itens\n");


foreach (KeyValuePair<String, int> produto in produtos)
{
    Console.WriteLine($"- {produto.Key}");
}
Console.WriteLine("\nQual produto voce quer saber?\n");

var solicitacao = Console.ReadLine()!;

int quantidade = Busca(solicitacao);

if (produtos.ContainsKey(solicitacao))
{
    Console.WriteLine($"O produto {solicitacao} está com {quantidade} disponíveis.");
}
else
{
    Console.WriteLine($"Desculpe, o produto '{solicitacao}' não foi encontrado no estoque.");
}