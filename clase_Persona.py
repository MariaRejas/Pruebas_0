# Laboratorio 7.3
# Ejercicio 1 
# María Angélica Rejas Núñez
# DNI: 70688752

class Persona:
    def __init__(self):
        self.__dni = int(input('DNI: '))
        self.__nombreCompleto = input('Nombre Completo: ')

    def establecerDni(self,dni):
        self.__dni = dni

    def establecerNombre(self,nC):
        self.__nombreCompleto = nC

    def establecerPersona(self,dni,nC):
        self.establecerDni(dni)
        self.establecerNombre(nC)

    def capturarPersona(self):
    #Solicita el ingreso de datos e invoca a establecerPersona para inicializar atributos
        dni = int(input('DNI: '))
        nC = input('Nombre Completo: ')
        self.establecerPersona(dni,nC)
        
    def obtenerDni(self,dni):
        return self.__dni

    def obtenerName(self,nC):
        return self.__nombreCompleto

    def imprimirPersona(self):
        cad = 'DNI: '+str(obtenerDni())+'\n'+\
              'Nombre: '+obtenerName()
        print(cad)
        






    
