#Desarrollado por David Vigil 06/09/2024
#Se usan 2 funciones para separar para obtener bloques de 8 caracteres. Si se desea hacer todo en una función, es necesario modificar el bloque try-except para que se adapte a la longitud del bloque que se desea obtener
def separarMensaje4(mensaje): #Esta función recibe un mensaje y lo separa en bloques de 4 caracteres
    texto = []
    if len(mensaje)%4 == 0:
        bloques = (len(mensaje)//4)
    else:
        bloques = (len(mensaje)//4)+1
    c=0
    for i in range(0, bloques):
        if mensaje[c] not in ABC:
            c+=1
            continue
        else:
            try:
                texto.append(mensaje[c]+mensaje[c+1]+mensaje[c+2]+mensaje[c+3]) 
            except IndexError:
                try:
                    texto.append(mensaje[c]+mensaje[c+1]+mensaje[c+2]+"X") 
                except IndexError:
                    try:
                        texto.append(mensaje[c]+mensaje[c+1]+"XX")
                    except IndexError:
                        try:
                            texto.append(mensaje[c]+"XXX")
                        except:
                            break
            finally:
                c+=4
    return texto
def agruparMensaje2(mensaje): #Esta función recibe una lista de bloques de 4 caracteres y los agrupa de dos en dos para formar bloques de 8 caracteres que ya se pueden cifrar usando Lucifer
    texto = []
    if len(mensaje)%2 == 0:
        bloques = (len(mensaje)//2)
    else:
        bloques = (len(mensaje)//2)+1
    c=0
    for i in range(0, bloques):
        try:
            texto.append(mensaje[c]+mensaje[c+1]) 
        except IndexError:
            try:
                texto.append(mensaje[c]+"XXXX") 
            except:
                break
        finally:
            c+=2
    return texto
def cifrarLucifer(texto, ABC, s, p, rondas): #Esta función recibe un texto, el alfabeto, la sustitución s, la permutación p y el número de rondas. Cifra con s y, y desciifra con -s y la permutación inversa de p
    resultado = ""
    aux = []
    for elemento in texto:
        izq = []
        der = []
        for i in range(4): #Aquí se construye el lado izquierdo y derecho de cada elemento de 8 caracteres
            izq.append(elemento[0:4][i])
            der.append(elemento[4:8][i]) #Aquí puede ir el numero de rondas
        for r in range(0, rondas): #Este ciclo se encarga de realizar las rondas de cifrado
            for j in range(len(izq)): #En lugar de usar len, se puede poner un 4, ya que el tamaño de izq siempre es 4
                izq[j] = ABC[(ABC.index(izq[j])+s)%len(ABC)] #Aquí se aplica la sustitución s en lado izquierdo
            for i in range(4): #Este ciclo es necesario porque la igualdad aux = izq actualiza constantemente el valor de aux, no se guarda una sola vez. Por lo tanto, se necesita un ciclo para guardar cada valor de izq en aux.
                aux.append(izq[i])
            for i in range(4):
                izq[i] = aux[int(p[i])-1] #Este ciclo es el que realiza la permutación en el lado izquierdo
            aux = []
            for i in range(4): #Estos 3 ciclos for intercambian los valores de izq y der, terminando la ronda
                aux.append(izq[i])
            izq = []
            for i in range(4):
                izq.append(der[i])
            der = []
            for i in range(4):
                der.append(aux[i])       
            aux = []
        for caracter in izq+der: #Se unen los lados izquierdo y derecho para formar el bloque de 8 caracteres y se almacena en la variable resultado
            resultado += caracter
    return resultado
def pedirP(): #Esta función solicita al usuario la permutación p de 4 dígitos que contenga los números del 1 al 4
    p = str(input("Introduce la permutación p de 4 dígitos: ")) #Se solicita al usuario la permutación
    if len(p) == 4 and '1' in p and '2' in p and '3' in p and '4' in p: #Se verifica que la permutación sea de 4 dígitos y que contenga los números del 1 al 4
        return p
    else:
        print("La permutación debe ser de 4 dígitos y contener los números del 1 al 4.")
        pedirP() #Si la permutación no cumple con los requisitos, se vuelve a llamar a la función

#Es importante definir el abecedario que se va a utilizar en este algoritmo
ABC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',' ',',','.','!','¡','¿','?',';',':','(',')','[',']','{','}','-','_','+','=','*','/','&','%','$','#','@','|','<','>','^','~','`','¬','á','é','í','ó','ú','Á','É','Í','Ó','Ú']
pinv = ""
s = int(input("Introduce el valor de s: ")) #Se solicita al usuario el valor para la sustitución
p = pedirP() #Se solicita al usuario la permutación
rondas = int(input("Introduce el número de rondas: ")) #Se solicita al usuario el número de rondas
print("")
print("---------- Cifrado Lucifer ----------")
mensaje = input("Ingresa el mensaje que deseas cifrar: ") #Mensaje a cifrar
#Es importante separar el mensaje con estas 2 funciones. Esto se puede simplificar en el futuro
texto = separarMensaje4(mensaje)
texto = agruparMensaje2(texto)
print("Criptograma: ", cifrarLucifer(texto, ABC, s, p, rondas)) #Se imprime el criptograma
print("")
print("---------- Descifrado Lucifer ----------")
for i in range(4): #Aquí se calcula la permutación inversa que se puede mostrar al usuario. Para descifrar es necesario restar 1 a cada valor de la permutación inversa
    pinv += str(p.index(str(i+1))+1)
print("Permutación inversa: ", pinv)
criptograma = input("Ingresa el criptograma que deseas descifrar: ") #Criptograma a descifrar
texto = separarMensaje4(criptograma)
texto = agruparMensaje2(texto)
print("Mensaje claro", cifrarLucifer(texto, ABC, s*-1, pinv, rondas)) #Se imprime el mensaje claro

