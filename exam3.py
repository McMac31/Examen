def area(base,altura): #Creo la funcion 
        return base*altura #Devuelvo la funcion multiplicandola

if __name__=="__main__":
    base= int(input("Ingrese el valor de la base "))
    altura= int(input("Ingrese el valor de la altura "))
    print(area(base,altura))