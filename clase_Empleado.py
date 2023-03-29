# Laboratorio 7.3
# Ejercicio 3
# María Angélica Rejas Núñez
# DNI: 70688752


from clase_Persona import Persona
from clase_Tiempo import Tiempo

class Empleado(Persona): #Hereda de Persona pero se compone de Tiempo
    def __init__(self):
        self.__horaEntrada = Tiempo(8,0,0)
        self.__horaSalida = Tiempo(17,0,0)

    def establecerHoraEntrada(self,hE):
        self.__horaEntrada.estableceHoraT(hE.obtieneHora(),hE.obtieneMinuto(),hE.obtieneSegundo())
        
    def establecerHoraSalida(self,hS):
        self.__horaSalida.estableceHoraT(hS.obtieneHora(),hS.obtieneMinuto(),hS.obtieneSegundo())

    def obtenerHoraEntrada(self):
        return self.__horaEntrada

    def obtenerHoraSalida(self):
        return self.__horaSalida

    def establecerEmpleado(self,hE,hS):
    #Solicita la hora de entrada y salida del teclado
    #Con ayuda de los métodos de la clase Tiempo
        self.establecerHoraEntrada(hE)
        self.establecerHoraSalida(hS)

    def capturarEmpleado(self):
        print('Hora de ingreso')
        self.__horaEntrada.capturarHora()
        print('\n\nHora de salida')
        self.__horaSalida.capturarHora()
        self.establecerEmpleado(self.obtenerHoraEntrada(),self.obtenerHoraSalida())

    def imprimirEmpleado(self,num):
        print('Empleado ',num)
        super().__init__() #inicializar dni, nombre
        print(self.imprimirPersona())
        
