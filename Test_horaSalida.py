# Laboratorio 7.3
# Ejercicio 5
# María Angélica Rejas Núñez
# DNI: 70688752

from clase_Empleado import Empleado
emp1 = Empleado()
emp1.capturarEmpleado()

horaS = emp1.obtenerHoraSalida().obtieneHora()
minS = emp1.obtenerHoraSalida().obtieneMinuto()
segS = emp1.obtenerHoraSalida().obtieneSegundo()

if horaS > 17:
    if minS > 0:
        tmin = (horaS-17) * 60 + minS
    else:
        tmin = (horaS-17) * 60
    print('Debe pagarse horas extras')
    print('Total de minutos: ',tmin)
else:
    if horaS == 17:
        if minS > 0:
            print('\n\nDebe pagarse horas extras')
            print('Total de minutos: ',minS)
        else:
            print('\n\nNo se le paga horas extras')
    else:
        print('\n\nNo se le paga horas extras')
