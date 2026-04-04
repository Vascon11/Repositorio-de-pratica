//Criar um dicionário que represente um aluno, com uma lista de notas
//e mostre a média de suas notas na tela.

Dictionary<string, int> alunos = new Dictionary<string, int>
{
    ["Alice"] = 9,
    ["Roberto"] = 5,
    ["Maria"] = 8,
    ["Gabriel"] = 10,
    ["Joao"] = 2
};
int quantidade=0;
int soma = 0;
foreach(KeyValuePair<String, int> notas in alunos)
{
    Console.WriteLine($"Nome: {notas.Key} - nota: {notas.Value}");
    quantidade++;
    soma+=notas.Value;
}
Console.WriteLine($"A media da turma foi de {(double)soma/quantidade}");