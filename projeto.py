from collections import Counter

texto = input('Digite um texto: ')

palavras = texto.split()
quantidade_palavras = len(palavras)

letras = texto.replace(' ','')
num_letras = len(letras)   

palavra_mais_frequente = Counter(palavras).most_common(5)

media = num_letras / quantidade_palavras

print(f'O texto contém {quantidade_palavras} palavras.')

print(f'O texto possui {num_letras} letras.')

print(f'A média de caracteres por palavra é: {media:.2f}.')