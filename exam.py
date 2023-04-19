class Animal: #Creo la clase "Padre" Animal
    def __init__(self,nombre,patas,raza): #Agrego el init e instancio cada atributo
        self.nombre= nombre
        self.patas= patas
        self.raza= raza

class Perro(Animal): #Creo la subclase "hija" de Animal
    def __init__(self,nombre,patas,raza):
        super().__init__(nombre,patas,raza) #devuelvo e instancio de la clase a la subclase
        self.nombre= nombre
        self.patas= patas
        self.raza= raza

    def Ladrar(self): #Creo la accion de ladrar 
        print(f"{self.nombre} hace Woof Woof")

    def Correr(self): #Creo la accion de correr
        print(f"{self.nombre} esta Corriendo") 

class Pajaro(Animal): #Creo la subclase Pajaro
    def __init__(self, nombre, patas, raza):
        super().__init__(nombre, patas, raza) #Hago el super init para unirlo a la clase 
        self.nombre=nombre
        self.patas= patas
        self.raza= raza
    def Cantar(self): #Creo el metodo cantar()
        print(f"{self.nombre} el {self.raza} Esta cantando *Tweet Tweet*")
    
    def Volar(self):
        print(f"{self.nombre} el {self.raza} ¡Esta volando!")

    
    

if __name__== "__main__":
    Perro1 = Perro("Spike",4,"Pitbull") #Creo a el perro
    Perro1.Ladrar() #Ejecuto la accion mediante el main
    Perro1.Correr()
    print("----------------")
    Ave= Pajaro("Piolin",2,"Canario") #Creo al ave
    Ave.Cantar() #Ejecuto cantar()
    Ave.Volar() #Ejecuto volar()
