###
from datetime import date

#Exercicios = Manipulação de Arquivo
#Exercicio 01
try:
    with open("tabuada9.txt", "w") as arq:
        for i in range(1, 11):
            arq.write(f"9 x {i} = {9*i}\n")

        print("Tabuada gravada no arquivo com sucesso!")
except IOError as e:
    print(f"Erro ao gravar o arquivo: {e}")


#Exercicio 02
try: 
    nome = input("Nome: ")
    rg = input("RG: ")
    cpf = input("CPF: ")
    ano_nascimento = int(input("Ano de nascimento: "))

    idade = date.today().year - ano_nascimento

    with open("pessoa.txt", "w") as arq:
        arq.write(f"Nome: {nome}\n")
        arq.write(f"RG: {rg}\n")
        arq.write(f"CPF: {cpf}\n")
        arq.write(f"Idade: {idade}\n")

    print("Dados gravados no arquivo com sucesso!")
except ValueError:
    print("Erro: Ano de nascimento deve ser um número inteiro.")
except IOError as e:
    print(f"Erro ao gravar o arquivo: {e}")

#Exercicio 03
try:
    linhas = []

    with open("arquivo.txt", "r") as arq:
        linhas = arq.readlines()

    print("Linhas do arquivo em lista:")
    print(linhas)
except FileNotFoundError:
    print("Erro: Arquivo 'arquivo.txt' não encontrado.")

#Exercicio 04
try:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    media = (nota1 + nota2) / 2
    status = "Aprovado" if media >= 6 else "Reprovado"

    with open("aluno.txt", "w") as arq:
        arq.write(f"Nome: {nome}\n")
        arq.write(f"Média: {media:.2f}\n")
        arq.write(f"Situação: {status}\n")

    print("Dados do aluno gravados no arquivo com sucesso!")
except ValueError:
    print("Erro: As notas devem ser números.")
#Exercicio 05
try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    soma = n1 + n2
    sub = n1 - n2
    mult = n1 * n2
    div = n1 / n2 if n2 != 0 else "Impossível (divisão por zero)"

    with open("resultados.txt", "w") as arq:
        arq.write(f"Soma: {soma}\n")
        arq.write(f"Subtração: {sub}\n")
        arq.write(f"Multiplicação: {mult}\n")
        arq.write(f"Divisão: {div}\n")

    print("Resultados salvos no arquivo com sucesso!")
except ValueError:
    print("Erro: Digite apenas números inteiros.")