#Desarrollado por David Vigil 05/09/2024
def cifrarAfin(mensaje, a, b): #Función para cifrar utilizando una función afín. Recibe el mensaje a cifrar, el valor de a y el valor de b.
    #ABC no puede ser distinto a este, ya que se utilizan los inversos multiplicativos de 37 porque todos todos los numeros del 1 al 36 tienen inverso multiplicativo en módulo 37.
    ABC = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
    result = ""
    for letra in mensaje:
        if letra.upper() in ABC:
            letraCifrada = ABC[(ABC.index(letra.upper())*a+b)%len(ABC)] #Fórmula para cifrar utilizando una función afín.
            result += str(letraCifrada)
        else:    
            result += letra #Incluye los caracteres que no están en el alfabeto, pero no los cifra. Esto es útil para los espacios.
    return result

def descifrarAfin(criptograma, a, b): #Función para descifrar utilizando una función afín. Recibe el criptograma a descifrar, el valor de a y el valor de b.
    ABC = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
    INV = [1,19,25,28,15,31,16,14,33,26,27,34,20,8,5,7,24,35,2,13,30,32,29,17,3,10,11,4,23,21,6,22,9,12,18,36] #Inversos multiplicativos de 37, enumerados desde el 1
    result = ""
    for letra in criptograma:
        if letra.upper() in ABC:
            letraDescifrada = ABC[((ABC.index(letra.upper())-b)*INV[a-1])%len(ABC)] #Fórmula para descifrar utilizando una función afín.
            result += str(letraDescifrada)
        else:
            result += letra #Incluye los caracteres que no están en el alfabeto, pero no los descifra. Esto es útil para los espacios.
    return result

#a debe ser <= 36
#Aquí se utiliza a=1 y b=7 porque así fue requerido en el ejercicio. A puede ser cualquier valor entre 1 y 36.
a=1 #Aquí se pueden solicitar los valores de a y b al usuario, indicando que a debe ser <= 36 y b puede ser cualquier valor.
b=7 #En este ejercicio son 1 y 7 respectivamente.
mensaje = input("Introduce el mensaje a cifrar: ") #Solicitamos el mensaje a cifrar
print(cifrarAfin(mensaje, a, b)) #Imprimimos el criptograma utilizando la función cifrarAfin
criptograma = input("Introduce el criptograma a descifrar: ") #Solicitamos el criptograma a descifrar
print(descifrarAfin(criptograma, a, b)) #Imprimimos el mensaje descifrado utilizando la función descifrarAfin