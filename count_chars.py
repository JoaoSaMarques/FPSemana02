palavras = []
dicionario = {}
    
frase = input("Digite uma frase: ")
    
palavra = ""

#organiza, remove whitespaces e conta o tamanho
for char in frase:
    if char == " ":
        if palavra:  
            palavras.append(palavra)
            dicionario[palavra] = len(palavra)
            palavra = ""
                
    else:
            palavra += char

#necessário para o '?'
if palavra: 
    palavras.append(palavra)
    dicionario[palavra] = len(palavra)

print(dicionario)
