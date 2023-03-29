# Laboratorio 7.3
# Ejercicio 4
# María Angélica Rejas Núñez
# DNI: 70688752

from clase_Empleado import Empleado

emp1 = Empleado()
emp1.capturarEmpleado()

horaE = emp1.obtenerHoraEntrada().obtieneHora()
minE = emp1.obtenerHoraEntrada().obtieneMinuto()
segE = emp1.obtenerHoraEntrada().obtieneSegundo()

horaS = emp1.obtenerHoraSalida().obtieneHora()
minS = emp1.obtenerHoraSalida().obtieneMinuto()
segS = emp1.obtenerHoraSalida().obtieneSegundo()

print('\n\nIngreso:',end='')
if horaE > 8:
    print('Tarde')
else:
    if horaE == 8:
        if minE > 0:
            print('Tarde')
        else:
            print('Puntual')
    else:
        print('Temprano')


print('Salida:',end='')
if horaS > 17:
    print('Tarde')
else:
    if horaS == 17:
        if minS > 0:
            print('Tarde')
        else:
            print('Puntual')
    else:
        print('Temprano')
            








        
