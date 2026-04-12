//Criar um programa que simule um sistema de login utilizando um dicionário para armazenar nomes de usuário e senhas.

Dictionary<String, String> Cadastros = new Dictionary<string, string>
{
    ["vascon1"]="senha123"
};

void Validar(string usuarioDigitado, string senhaDigitada)
{
    while (true)
    {
        if (Cadastros.ContainsKey(usuarioDigitado) && Cadastros[usuarioDigitado]==senhaDigitada)
    {
        Console.WriteLine($"\nAcesso liberado! Bem-vindo, {usuarioDigitado}.");
        break;
    }
    else
    {
        Console.WriteLine("Usuário ou senha incorretos.");
    }
    }
}

Console.Clear();
Console.WriteLine("Qual é seu usuario?");
String user = Console.ReadLine()!;
if (Cadastros.ContainsKey(user))
{
    Console.WriteLine("\nDigite sua senha:");
    String password = Console.ReadLine()!;
    Validar(user, password);
}
else
{
    Console.WriteLine($"Não foi encontrado o usuario com o nome {user}!");
}