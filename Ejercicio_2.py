#PREG 2

import random

#######################################################################################

def ADN(adn): #Función 1
    #Longitud incorrecta
    while adn<20 or adn>1000:
        print("¡ERROR!, el tamaño debe estar entre 20 y 1000")
        adn = int(input("Ingrese la longitud de la cadena [20, 1000]: "))

    #Desarrollo de longitud correcta
    bases_nitro = "ACGT"
    cadena_adn = []
    for i in range(adn):
        cadena_adn.append(random.choice(bases_nitro))
    cadenaADN = "".join(cadena_adn)
    return  cadenaADN

#######################################################################################


#######################################################################################

def encontrar_Gen(genoma): #Funcion 2
    encontrar = False
    inicio = -1
    print("Resultados: ")
    for i in range(len(genoma)-2):
        triple = genoma[i:i+3]
        if triple == "ATG": #Comienzo de tripleta
            inicio = i+3
            print(" ")
            
        elif (triple == "TAG" or triple == "TAA" or triple == "TGA") and inicio != -1:
            #Posible gen encontrado
            gen = genoma[inicio:i]
            if len(gen)%3 == 0:
                encontrar = True
                print(gen)
                inicio = -1 #Comienza a buscar el siguiente gen en el genoma

    
    if encontrar:
        print("No se encuentra ningún gen")

######################################################################################


long_correct = int(input("Ingrese la longitud de la cadena [20, 1000]: "))
cadena = ADN(long_correct)#Invocación de la función 1
print("La cadena de ADN es:\n",cadena)
encontrar_Gen(cadena) #Invocacion de la función 2
