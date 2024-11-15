palavras = []
dicionario = {}
    
frase = input("Digite uma frase: ")
    
palavra = ""

# Split para separar
palavras = frase.split()

# contar a quantidade de letras
for palavra in palavras:
    dicionario[palavra] = len(palavra)

print(dicionario)
