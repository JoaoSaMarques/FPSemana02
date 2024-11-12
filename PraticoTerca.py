List = []

n =  input("Input a string here: ")
a = n.replace(" ", "")

for char in a:
    List.append(char)
    
print(List)
print(len(List), " characters in string.")