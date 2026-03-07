void Espacamento()
{
    Console.WriteLine("====================================================================================================");
}

void logotipo()
{
       Console.WriteLine(@"
░█████╗░░█████╗░██╗░░░░░██╗░░░██╗██╗░░░░░░█████╗░██████╗░░█████╗░██████╗░░█████╗░  ░█████╗░░░░██╗░██╗░
██╔══██╗██╔══██╗██║░░░░░██║░░░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██████████╗
██║░░╚═╝███████║██║░░░░░██║░░░██║██║░░░░░███████║██║░░██║██║░░██║██████╔╝███████║  ██║░░╚═╝╚═██╔═██╔═╝
██║░░██╗██╔══██║██║░░░░░██║░░░██║██║░░░░░██╔══██║██║░░██║██║░░██║██╔══██╗██╔══██║  ██║░░██╗██████████╗
╚█████╔╝██║░░██║███████╗╚██████╔╝███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║██║░░██║  ╚█████╔╝╚██╔═██╔══╝
░╚════╝░╚═╝░░╚═╝╚══════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ░╚════╝░░╚═╝░╚═╝░░░");
}

(float, float) entradadado()
{
    Console.WriteLine("Digite um numero aqui:");
    int primeironumero = int.Parse(Console.ReadLine()!);

    Console.WriteLine("Digite o segundo numero aqui:");
    int segundonumero = int.Parse(Console.ReadLine()!);

    return (primeironumero, segundonumero);
}


void Calculadora(){
    int SistemaCalculadora = 0;
    while (SistemaCalculadora == 0) {
        Console.Clear();
        Espacamento();
        logotipo();
        Espacamento();
        
        var (primeironumero, segundonumero) = entradadado();

        Console.Clear();
        Espacamento();
        logotipo();
        Espacamento();
        
        Console.WriteLine(@$"
        Voce escolheu os seguintes numeros:
        primeiro numero: {primeironumero}
        Segundo numero: {segundonumero}
        ");

        Espacamento();


        Console.WriteLine(@"
        Digite 1 para somar
        Digite 2 para subtrair
        Digite 3 para multiplicar
        digite 4 para dividir
        ");

        Espacamento();

        string opcaoEscolhida = Console.ReadLine()!;
        float opcaoEscolhidaNumerica = float.Parse(opcaoEscolhida);

        if (opcaoEscolhidaNumerica == 1)
        {
            Console.WriteLine(@$"   Voce escolheu somar: 
            {primeironumero} + {segundonumero} = {primeironumero + segundonumero}
            ");
        }
        else if (opcaoEscolhidaNumerica == 2)
        {
            Console.WriteLine(@$"   Voce escolheu subtrair:
            {primeironumero} - {segundonumero} = {primeironumero - segundonumero}
            ");
        }
        else if (opcaoEscolhidaNumerica == 3)
        {
            Console.WriteLine(@$"   Voce escolheu multiplicar:
            {primeironumero} * {segundonumero} = {primeironumero * segundonumero}
            ");
        }
        else if (opcaoEscolhidaNumerica == 4)
        {
            Console.WriteLine(@$"   Voce escolheu dividir:
            {primeironumero} / {segundonumero} = {primeironumero / segundonumero}
            ");
        }
        else
        {
            Console.WriteLine("Opção inválida");
        }

        Espacamento();

        Console.WriteLine("\nDigite [0] para volta para o menu e [1] para encerrar a calculadora");
        string PergundaPrograma = Console.ReadLine()!;
        SistemaCalculadora = int.Parse(PergundaPrograma);
        if (SistemaCalculadora == 1)
        {
            Console.Clear();
        }
    }
}

Calculadora();