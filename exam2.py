lista = [5, 3, 12, -6, -3, 1, 6, 8, -12]
lst=[list for list in lista if list >=0] #Excluyo los valores negativos de la lista con list comprehension
print(lst)

for i in lista: #creo un bucle for para cada numero
    print(i) #imprimo numero por numero
    if i==6: #si el numero es igual a 6
        print("HOLA 6") #debajo imprime hola 6
