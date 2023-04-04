"""
Resolva os problemas a seguir, criando algoritmos em Python:

Exercício 1:
Escreva uma função que receba uma lista de inteiros e retorne uma nova lista contendo apenas os números pares da lista original.
"""
def lista_de_pares(lista):
    lista_pares = []
    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)
    return lista_pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = lista_de_pares(numeros)
print(pares)

"""
Exercício 2:
Escreva uma função que receba uma lista de palavras (strings) e retorne uma nova lista contendo apenas as strings com mais de 5 caracteres.
"""
def mais_de_cinco_caracteres(lista_palavras):
    nova_lista = []
    for palavra in lista_palavras:
        if len(palavra) > 5:
            nova_lista.append(palavra)
    return nova_lista

palavras = ['Python', 'programação', 'dados', 'científicos', 'data', 'science']
palavras_com_mais_de_cinco_caracteres = mais_de_cinco_caracteres(palavras)
print(palavras_com_mais_de_cinco_caracteres)



"""
Exercício 3
Escreva um programa que solicite ao usuário que digite uma frase e, em seguida, conte a frequência de cada letra na frase. O programa deve imprimir os resultados usando um dicionário.
"""
def contar_letras(frase):
    """Conta a frequência de cada letra em uma frase"""
    # Remove espaços em branco e converte para letras minúsculas
    frase = frase.replace(' ', '').lower()
    # Inicializa um dicionário vazio para armazenar as frequências
    frequencias = {}
    # Itera sobre cada letra na frase
    for letra in frase:
        # Verifica se a letra já está no dicionário
        if letra in frequencias:
            # Se estiver, incrementa a frequência em 1
            frequencias[letra] += 1
        else:
            # Se não estiver, adiciona a letra ao dicionário com frequência 1
            frequencias[letra] = 1
    return frequencias

# Solicita ao usuário que digite uma frase
frase = input('Digite uma frase: ')
# Chama a função contar_letras para contar a frequência de cada letra na frase
frequencias = contar_letras(frase)
# Imprime o dicionário de frequências
print(frequencias)


"""
Exercício 4
Escreva um programa que solicite ao usuário que digite um número entre 1 e 10 e imprima a tabuada desse número.
"""
# Solicita ao usuário que digite um número entre 1 e 10
numero = int(input("Digite um número entre 1 e 10: "))
# Verifica se o número está dentro do intervalo válido
if numero < 1 or numero > 10:
    print("Número inválido!")
else:
    # Imprime a tabuada do número
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")
"""
Exercício 5
Escreva uma função que pegue um dicionário de nomes de alunos e suas notas e retorne um novo dicionário contendo apenas os alunos que obtiveram uma nota de aprovação (no caso, nota de 6,0 ou superior).
"""
def alunos_aprovados(notas):
    """Retorna um novo dicionário contendo apenas os alunos que obtiveram nota de aprovação"""
    aprovados = {}
    for aluno, nota in notas.items():
        if nota >= 6.0:
            aprovados[aluno] = nota
    return aprovados

notas = {
    "João": 7.5,
    "Maria": 5.5,
    "José": 6.0,
    "Pedro": 8.0,
    "Ana": 4.5
}

aprovados = alunos_aprovados(notas)

print(aprovados)

"""
Exercício 6
Escreva um programa que gere uma lista de 30 números inteiros aleatórios entre 1 e 100 (inclusive). Em seguida, o programa deve calcular e exibir os valores de soma, média, máximo e mínimo da lista, além de mostrar a lista completa.
"""

import random

# Gera uma lista de 30 números inteiros aleatórios entre 1 e 100 (inclusive)
lista = [random.randint(1, 100) for _ in range(30)]

# Calcula a soma, média, máximo e mínimo da lista
soma = sum(lista)
media = soma / len(lista)
maximo = max(lista)
minimo = min(lista)

# Exibe os resultados
print("Lista completa:", lista)
print("Soma:", soma)
print("Média:", media)
print("Máximo:", maximo)
print("Mínimo:", minimo)
