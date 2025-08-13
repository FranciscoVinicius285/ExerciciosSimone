#Exercicio 01:
cadeiaDeDna = input("Digite a cadeia: ").upper()
inversaoDaCadeia = ''.join(reversed(cadeia))
print(cadeiaDeDna)
print(inversaoDaCadeia)



#Exercicio 02:
with open('Exer02.txt', 'r') as arquivo:
   conteudo =  arquivo.read()
print(len(conteudo.split()))


#Exercicio 03:
with open("ListaAnimais.txt", 'r') as arquivo:
    conteudoArq = arquivo.read()

    print(conteudoArq.replace(", ","_"))


#Exercicio 04:
with open("TextEx04.txt", 'r') as arquivo:
    conteudoArq = arquivo.read()

palavras_unicas = list(set(conteudoArq.split()))
print(palavras_unicas)
