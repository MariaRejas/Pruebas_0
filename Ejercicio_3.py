#PREG 3

##################################################################################

def frecuencia(caracter):
    print("Resultados:")
    No_repet = "".join(dict.fromkeys(caracter)) #Se eliminan caracteres repetidos
    
    for i in range(len(No_repet)):
            carac_n = No_repet[i]
            if caracter.count(carac_n) == 1:
                print('"'+carac_n+'"', " : ", caracter.count(carac_n), "vez")
                
            else:
                print('"'+carac_n+'"', " : ", caracter.count(carac_n), "veces")
                
    
##################################################################################

            
frase = input("Ingrese frase:\n")
frecuencia(frase)   

    



















# María Angélica Rejas Núñez
