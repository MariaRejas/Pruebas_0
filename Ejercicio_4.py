#PREG 4

##################################################################################################

def reemplazar(caracter):
      reemplaza = caracter.maketrans("Ü,ü,Ñ,ñ,Á,á,É,é,Í,í,Ó,ó,Ú,ú","U,u,N,n,A,a,E,e,I,i,O,o,U,u")
      frase_final = caracter.translate(reemplaza)
      return frase_final

##################################################################################################


frase = input("Ingrese una frase: ")
respuesta = reemplazar(frase)
print('"'+respuesta+'"')
        




























# María Angélica Rejas Núñez
