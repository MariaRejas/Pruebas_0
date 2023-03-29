#PREG 5

###########################################################################################################

def encriptado(texto):
    llave = input("Ingrese llave: ")
    texto_mayus = texto.upper()

    #Se reemplazan las vocales con tildes por vocales normales
    reemplazar_1 = texto_mayus.maketrans("Á,É,Í,Ó,Ú","A,E,I,O,U")
    texto_casi_final = texto_mayus.translate(reemplazar_1)

    #Se reemplaza el abecedario por la llave
    reemplazar_2 = texto_casi_final.maketrans("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z",llave)
    texto_final = texto_casi_final.translate(reemplazar_2)
    
    return texto_final

###########################################################################################################


texto_original = input("Ingrese texto: ")
texto_encriptado = encriptado(texto_original)
print(texto_encriptado)












    


# María Angélica Rejas Núñez
