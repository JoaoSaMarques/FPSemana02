intersecao = []

palavra1 = input("Primeira palavra: ")
palavra2 = input("Segunda palavra: ")

#Organize as palavras, se as letras de palavra2 já estão, mantei-se, se não, adiciona.
for char in palavra1:
    if char in palavra2 and char not in intersecao:
        #organiza os caracteres
        intersecao.append(char)

#Adiciona ao resultado os caracteres dentro da lista
resultado = ""
for char in intersecao:
    resultado += char

print(resultado)