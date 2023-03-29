# Laboratorio 7.3
# Ejercicio 2
# María Angélica Rejas Núñez
# DNI: 70688752

class Tiempo:
    def __init__(self,hh,mm,ss):
        self.__hora = hh
        self.__minuto = mm
        self.__segundo = ss

    def estableceHora(self,hh):
        self.__hora = hh

    def estableceMinuto(self,mm):
        self.__minuto = mm

    def estableceSegundo(self,ss):
        self.__segundo = ss

    def estableceHoraT(self,hh,mm,ss):
    #Establece despues de la hora, minuto y segundo
        self.estableceHora(hh)
        self.estableceMinuto(mm)
        self.estableceSegundo(ss)

    def capturarHora(self):
    #Captura desde el teclado
        hora = int(input('Hora: '))
        minuto = int(input('Minuto: '))
        segundo = int(input('Segundo: '))
        self.estableceHoraT(hora,minuto,segundo)
        
    def obtieneHora(self):
        return self.__hora

    def obtieneMinuto(self):
        return self.__minuto

    def obtieneSegundo(self):
        return self.__segundo

    def imprimeUniversal(self):
        cad = str(self.obtieneHora())+'hh '+str(self.obtieneMinuto())+'mm '+str(self.obtieneSegundo())+'ss '
        print(cad)

    def imprimeEstandar(self):
        hh = self.obtieneHora()
        if hh >= 12:
            hora = hh - 12
            mer = 'PM'

        else:
            hora = hh
            mer = 'AM'
        cad = str(hora)+':'+str(self.obtieneMinuto())+':'+str(self.obtieneSegundo())+mer
        print(cad)
        
