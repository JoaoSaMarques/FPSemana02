palavras = []
dicionario = {}
    
frase = input("Digite uma frase: ")
    
palavra = ""
    
for char in frase:
    if char == " ":
        if palavra:  
            palavras.append(palavra)
            dicionario[palavra] = len(palavra)
            palavra = ""
                
    else:
            palavra += char
            
if palavra: 
    palavras.append(palavra)
    dicionario[palavra] = len(palavra)

print(dicionario)
