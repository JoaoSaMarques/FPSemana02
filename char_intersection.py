intersecao = []

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

for char in palavra1:
    if char in palavra2 and char not in intersecao:
        intersecao.append(char)

resultado = ''
for char in intersecao:
    resultado += char

print(resultado)