# Desarrollado por David Vigil 27/09/2024
# Este programa obtiene el periodo máximo y la secuencia cifrante al indicarle un polinomio primitivo y una semilla de 8 bits.
def obtenerSecuenciaCifrante(pol, sem):
    semAux = sem.copy() #Copia de la semilla en una lista auxiliar que se irá modificando
    indices = []
    secuencia = []
    for i in range(len(pol)): #Se obtienen los índices de los 1's en el polinomio
        if pol[i] == 1:
            indices.append(i)
    while True: #Ciclo para obtener la secuencia cifrante
        for element in indices: #Se recorren los índices de los 1's en el polinomio
            if indices.index(element) == 0: 
                nuevoBit = semAux[element] #Si es el primer índice, se toma el bit correspondiente de la semilla
                continue
            else: #Si no es el primer índice, se hace un XOR con el bit correspondiente de la semilla
                nuevoBit ^= semAux[element]
        semAux.insert(0, nuevoBit) #Se añade el nuevo bit al inicio de la lista auxiliar
        secuencia.append(semAux.pop()) #Se añade el último bit de la lista auxiliar a la secuencia cifrante y se elimina de la lista auxiliar
        if semAux == sem: #Si la lista auxiliar es igual a la semilla, se ha completado un ciclo
            print()
            return secuencia
def pedirDatos():
    count = 0
    try: #Se intenta convertir los valores a enteros
        pol = list(map(int, input("Ingresa el polinomio primitivo: "))) #Se solicita al usuario el polinomio primitivo
        sem = list(map(int, input("Ingresa la semilla de 8 bits: "))) #Se solicita al usuario la semilla|
    except: #Si no se pueden convertir a enteros, se imprime un mensaje de error
        print("\nLos valores deben ser binarios")
        return pedirDatos()
    if len(pol) != len(sem): #Si el polinomio y la semilla no tienen la misma longitud, se imprime un mensaje de error
        print("\nEl polinomio y la semilla deben tener la misma longitud\n")
        return pedirDatos()
    else: #Si el polinomio y la semilla tienen la misma longitud, se verifica que los valores sean binarios
        for i in pol:
            if i != 0 and i != 1:
                print("\nLos valores deben ser binarios\n")
                return pedirDatos()
        for i in sem:
            if i != 0 and i != 1:
                print("\nLos valores deben ser binarios\n")
                return pedirDatos()
        for i in range(len(pol)): #Se verifica que el polinomio tenga al menos 2 unos
            if pol[i] == 1:
                count += 1
        if count < 2:
            print("\nEl polinomio debe tener al menos 2 unos\n")
            return pedirDatos()
        if 1 not in sem: #Se verifica que la semilla y el polinomio tengan al menos un 1
            print("\nLa semilla debe tener al menos un 1\n")
            return pedirDatos()
        return pol, sem


pol, sem = pedirDatos()
sec = obtenerSecuenciaCifrante(pol, sem)
print("Secuencia cifrante: ", end="")
for i in sec:
    print(i, end="")
print("\nPeriodo: ", len(sec))
print("Periodo máximo: ", 2**len(pol)-1) #Se imprime el periodo máximo