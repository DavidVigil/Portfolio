# Desarrollado por David Vigil 27/09/2024
# Este programa obtiene el periodo máximo y la secuencia cifrante al indicarle un polinomio primitivo y una semilla de 8 bits.
pol = [1, 1, 0, 0, 0, 0, 1, 1] #Polinomio primitivo x^8 + x^7 + x^2 + x + 1
#pol = [1, 0, 0, 0, 0, 1] #Polinomio primitivo x^8 + x^7 + x^2 + x + 1
sem = [1, 1, 0, 0, 0, 0, 1, 1] #Semilla 11000011
#sem = [0, 0, 0, 1, 1, 1] #Semilla 11000011
def obtenerSecuenciaCifrante(pol, sem):
    semAux = sem.copy() #Copia de la semilla en una lista auxiliar que se irá modificando
    indices = []
    secuencia = []
    periodo = 0
    for i in range(len(pol)):
        if pol[i] == 1:
            indices.append(i)
    while True:
        for element in indices:
            if indices.index(element) == 0:
                nuevoBit = semAux[element]
                continue
            else:
                nuevoBit ^= semAux[element]
        semAux.insert(0, nuevoBit) #Se añade el nuevo bit al inicio de la lista auxiliar
        secuencia.append(semAux.pop())
        periodo += 1
        if semAux == sem: #Si la lista auxiliar es igual a la semilla, se ha completado un ciclo
            print()
            return secuencia
def pedirDatos():
    try:
        pol = list(map(int, input("Ingresa el polinomio primitivo: "))) #Se solicita al usuario el polinomio primitivo
        sem = list(map(int, input("Ingresa la semilla de 8 bits: "))) #Se solicita al usuario la semilla|
    except:
        print("\nLos valores deben ser binarios")
        return pedirDatos()
    if len(pol) != len(sem):
        print("\nEl polinomio y la semilla deben tener la misma longitud\n")
        return pedirDatos()
    else:
        for i in pol:
            if i != 0 and i != 1:
                print("\nLos valores deben ser binarios\n")
                return pedirDatos()
        for i in sem:
            if i != 0 and i != 1:
                print("\nLos valores deben ser binarios\n")
                return pedirDatos()
        if 1 not in sem:
            print("\nLa semilla debe tener al menos un 1\n")
            return pedirDatos()
        return pol, sem
pol, sem = pedirDatos()
sec = obtenerSecuenciaCifrante(pol, sem)
print(sec)
print("Secuencia cifrante: ", end="")
for i in sec:
    print(i, end="")
print("\nPeriodo: ", len(sec))
print("Periodo máximo: ", 2**len(pol)-1) #Se imprime el periodo máximo