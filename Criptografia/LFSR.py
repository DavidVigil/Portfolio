# Desarrollado por David Vigil 27/09/2024
# Este programa obtiene el periodo máximo y la secuencia cifrante al indicarle un polinomio primitivo y una semilla de 8 bits.
def pedirDatos(): #Función para solicitar al usuario el polinomio primitivo y la semilla
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
def obtenerCerosYUnos(sec): #Función para obtener el número de ceros y unos en la secuencia cifrante
    ceros = unos = 0
    for i in sec:
        if i == 1:
            unos += 1
        elif i == 0:
            ceros += 1
    return ceros, unos
def obtenerDuos(sec): #Función para obtener el número de 00's, 01's, 10's y 11's en la secuencia cifrante
    cerosceros = cerosunos = unosceros = unosunos = 0
    secStr = ""
    for i in sec: #Se convierte la secuencia cifrante a una cadena de bits
        secStr += str(i)
    for i in range(len(sec)):  #Se cuentan los 00's
        if sec[i] == 0:
            try:
                if sec[i+1] == 0:
                    cerosceros += 1
            except:
                break
    cerosunos = secStr.count("01") #Se cuentan los 01's
    unosceros = secStr.count("10") #Se cuentan los 10's
    for i in range(len(sec)):  #Se cuentan los 11's
        if sec[i] == 1:
            try:
                if sec[i+1] == 1:
                    unosunos += 1
            except:
                break
    return cerosceros, cerosunos, unosceros, unosunos
def obtenerTrios(sec): #Función para obtener el número de 000's, 001's, 010's, 011's, 100's, 101's, 110's y 111's en la secuencia cifrante
    ceroscerosceros = ceroscerosunos = cerosunosceros = cerosunosunos = unoscerosceros = unoscerosunos = unosunosceros = unosunosunos = 0
    secStr = ""
    for i in sec: #Se convierte la secuencia cifrante a una cadena de bits
        secStr += str(i)
    for i in range(len(sec)): #Se cuentan los 000's
        if sec[i] == 0:
            try:
                if sec[i+1] == 0:
                    if sec[i+2] == 0:
                        ceroscerosceros += 1
            except:
                break
    ceroscerosunos = secStr.count("001") #Se cuentan los 001's
    for i in range(len(sec)): #Se cuentan los 010's
        if sec[i] == 0:
            try:
                if sec[i+1] == 1:
                    if sec[i+2] == 0:
                        cerosunosceros += 1
            except:
                break
    cerosunosunos = secStr.count("011") #Se cuentan los 011's
    unoscerosceros = secStr.count("100") #Se cuentan los 100's
    for i in range(len(sec)): #Se cuentan los 101's
        if sec[i] == 1:
            try:
                if sec[i+1] == 0:
                    if sec[i+2] == 1:
                        unoscerosunos += 1
            except:
                break
    unosunosceros = secStr.count("110") #Se cuentan los 110's
    for i in range(len(sec)): #Se cuentan los 111's
        if sec[i] == 1:
            try:
                if sec[i+1] == 1:
                    if sec[i+2] == 1:
                        unosunosunos += 1
            except:
                break
    return ceroscerosceros, ceroscerosunos, cerosunosceros, cerosunosunos, unoscerosceros, unoscerosunos, unosunosceros, unosunosunos
def pedirD(): #Función para solicitar el valor de d al usuario
    try:
        d = int(input("Ingresa el valor de d: ")) #Se solicita al usuario el valor de d
        if d > (len(sec)+1)//2: #Si el valor de d es mayor a la mitad entera de la secuencia, se imprime un mensaje de error
            print("El valor de d debe ser menor o igual a la mitad entera del tamaño total de la secuencia ({})".format((len(sec)+1)//2))
            return pedirD()
    except:
        print("El valor de d debe ser un entero")
        return pedirD() #Si el valor de d no es un entero, se vuelve a llamar a la función
    return d
def tercerPostulado(sec, d): #Función para obtener el tercer postulado de Golomb
    sum = 0
    for i in range(len(sec)):
        sum += sec[i] ^ sec[d]
    res = sum/len(sec)
    return res
secStr = ""
pol, sem = pedirDatos()
sec = obtenerSecuenciaCifrante(pol, sem)
for i in sec: #Se imprime la secuencia cifrante
    secStr += str(i)
print("Secuencia cifrante: ", secStr)
print("Periodo: ", len(sec))
print("Periodo máximo: ", 2**len(pol)-1) #Se imprime el periodo máximo
print("\n--------- Postulados de Golomb ---------")
ceros, unos = obtenerCerosYUnos(sec)
print("Número de ceros en la secuencia: ", ceros)
print("Número de unos en la secuencia: ", unos)
print("\n--- Postulado 1 ---")
print("Diferencia entre unos y ceros: ", abs(unos-ceros))
print("\n--- Postulado 2 ---")
print("a) Longitud 1: Debe ser menor o igual a la mitad entera del tamaño total de la secuencia ({})".format((len(sec)+1)//2))
print("Tamano de la secuencia: ", len(sec))
print("Ceros:", ceros)
print("Unos:", unos)
print("\nb) Longitud 2: Debe ser menor o igual a la cuarta parte entera del tamaño total de la secuencia ({})".format((len(sec)+1)//4))
cerosceros, cerosunos, unosceros, unosunos = obtenerDuos(sec)
print("Número de 00's:", cerosceros)
print("Número de 01's:", cerosunos)
print("Número de 10's:", unosceros)
print("Número de 11's:", unosunos)
print("\nc) Longitud 3: Debe ser menor o igual a la octava parte entera del tamaño total de la secuencia ({})".format((len(sec)+1)//8))
ceroscerosceros, ceroscerosunos, cerosunosceros, cerosunosunos, unoscerosceros, unoscerosunos, unosunosceros, unosunosunos = obtenerTrios(sec)
print("Número de 000's:", ceroscerosceros)
print("Número de 001's:", ceroscerosunos)
print("Número de 010's:", cerosunosceros)
print("Número de 011's:", cerosunosunos)
print("Número de 100's:", unoscerosceros)
print("Número de 101's:", unoscerosunos)
print("Número de 110's:", unosunosceros)
print("Número de 111's:", unosunosunos)
print("\n--- Postulado 3 ---")
d = pedirD()
print("Cálculo del tercer postulado de Golomb:", tercerPostulado(sec, d).__round__(2))