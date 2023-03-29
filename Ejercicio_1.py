#PREG 1
 
import random

##########################################################################

def ADN(adn):
    #Longitud incorrecta: Bucle
    while adn<20 or adn>1000:
        print("¡ERROR!, el tamaño debe estar entre 20 y 1000")
        adn = int(input("Ingrese la longitud de la cadena [20, 1000]: "))

    #Desarrollo de cadena con longitud correcta
    bases_nitro = "ACGT"
    cadena_adn = []
    for i in range(adn):
        cadena_adn.append(random.choice(bases_nitro))
    cadenaADN = "".join(cadena_adn)
    return  cadenaADN

##########################################################################

dna = int(input("Ingrese la longitud de la cadena [20, 1000]: "))
adn1 = ADN(dna) #Invocación de la función
print("La cadena ADN es: ", adn1) #Respuesta con longitud correcta



