#Parcial 2 de Simon Villa Escobar
#Las explicaciones (sustentaciones) del codigo estan al final de este codigo
import time
import threading


cola_aterrizaje = []
cola_despegue = []
cola_aterrizado = []
cola_despegado = []
cola_menor_a_mayor = sorted(cola_aterrizaje + cola_despegue + cola_aterrizado + cola_despegado, key=lambda avion: avion.duracion_vuelo)
cola_mayor_a_menor = sorted(cola_aterrizaje + cola_despegue + cola_aterrizado + cola_despegado, key=lambda avion: avion.duracion_vuelo, reverse=True)


#Estamos creando los objetos "avion" con los datos requeridos
class Avion:
    def __init__(self, numero, tipo_vuelo, hora_despegue, hora_aterrizaje, duracion_vuelo, prioridad, puerta_salida, puerta_entrada, estado):
        self.numero = numero
        self.tipo_vuelo = tipo_vuelo
        self.hora_despegue = hora_despegue
        self.hora_aterrizaje = hora_aterrizaje
        self.duracion_vuelo = duracion_vuelo
        self.prioridad = prioridad
        self.puerta_salida = puerta_salida
        self.puerta_entrada = puerta_entrada
        self.estado = estado


#Agregamos los aviones a la cola correspondiente, es decir a cola_despegue o cola_aterrizaje
def agregar_vuelo():
    numero = input("Ingrese el número del vuelo: ")
    tipo_vuelo = input("Ingrese el tipo de vuelo (Escrbir 'aterrizaje' o 'despegue'): ")
    hora_despegue = input("Ingrese la hora de despegue (HH:MM): ")
    hora_aterrizaje = input("Ingrese la hora de aterrizaje (HH:MM): ")
    duracion_vuelo = (calcular_minutos(hora_aterrizaje) - calcular_minutos(hora_despegue))
    prioridad = input("Ingrese la prioridad del vuelo (1: Comercial, 2: Militar, 3: Especial, 4: Emergencia): ")
    puerta_salida = input("Ingrese la puerta de salida: ")
    puerta_entrada = input("Ingrese la puerta de entrada: ")
    estado = input("Ingrese el estado del vuelo (1.On time, 2.Delayed o 3.Cancelled): ")

    avion = Avion(numero, tipo_vuelo, hora_despegue, hora_aterrizaje, duracion_vuelo, prioridad, puerta_salida, puerta_entrada, estado)


#Este if va a organizar la cola de aterrizaje segun la prioridad y el estado. Un avion de alta prioridad pasara de primero. Un avion de estado "Delayed" pasara antes que un avion "On time"
    if tipo_vuelo == "aterrizaje":
        if not cola_aterrizaje:
            cola_aterrizaje.append(avion)
        else:
            avion_agregado = False  # Se inicializa la variable que indica si el avión ha sido agregado
            for a in range(len(cola_aterrizaje)):
                if avion.prioridad >= cola_aterrizaje[a].prioridad or avion.estado >= cola_aterrizaje[a].estado:
                    for b in range(len(cola_aterrizaje)):
                        if avion.prioridad > cola_aterrizaje[b].prioridad:
                            for c in range(len(cola_aterrizaje)):
                                if avion.prioridad >= cola_aterrizaje[c].prioridad and avion.estado >= cola_aterrizaje[
                                    c].estado:
                                    cola_aterrizaje.insert(c, avion)
                                    avion_agregado = True  # Se cambia el valor de la variable
                                    break
                            if avion_agregado:
                                break
                            cola_aterrizaje.insert(b, avion)
                            avion_agregado = True  # Se cambia el valor de la variable
                            break
                        else:
                            for d in range(len(cola_aterrizaje)):
                                if avion.estado >= cola_aterrizaje[d].estado and avion.prioridad >= cola_aterrizaje[
                                    d].prioridad:
                                    cola_aterrizaje.insert(d, avion)
                                    avion_agregado = True  # Se cambia el valor de la variable
                                    break
                        if avion_agregado:
                            break
                if avion_agregado:
                    break
            if not avion_agregado:  # Si el avión no ha sido agregado a la cola, se agrega al final
                cola_aterrizaje.append(avion)

        print("El avión se ha agregado a la cola de aterrizaje.")


#Este if organiza la cola de despegue segun la prioridad y el estado. Un avion de alta prioridad pasara de primero. Un avion de estado "Delayed" pasara antes que un avion "On time"
    if tipo_vuelo == "despegue":
        if not cola_despegue:
            cola_despegue.append(avion)
        else:
            avion_agregado = False  # Se inicializa la variable que indica si el avión ha sido agregado
            for a in range(len(cola_despegue)):
                if avion.prioridad >= cola_despegue[a].prioridad or avion.estado >= cola_despegue[a].estado:
                    for b in range(len(cola_despegue)):
                        if avion.prioridad > cola_despegue[b].prioridad:
                            for c in range(len(cola_despegue)):
                                if avion.prioridad >= cola_despegue[c].prioridad and avion.estado >= cola_despegue[
                                    c].estado:
                                    cola_despegue.insert(c, avion)
                                    avion_agregado = True  # Se cambia el valor de la variable
                                    break
                            if avion_agregado:
                                break
                            cola_despegue.insert(b, avion)
                            avion_agregado = True  # Se cambia el valor de la variable
                            break
                        else:
                            for d in range(len(cola_despegue)):
                                if avion.estado >= cola_despegue[d].estado and avion.prioridad >= cola_despegue[
                                    d].prioridad:
                                    cola_despegue.insert(d, avion)
                                    avion_agregado = True  # Se cambia el valor de la variable
                                    break
                        if avion_agregado:
                            break
                if avion_agregado:
                    break
            if not avion_agregado:  # Si el avión no ha sido agregado a la cola, se agrega al final
                cola_despegue.append(avion)

        print("El avión se ha agregado a la cola de despegue.")




#Si tengo una hora de forma HH:MM, con esta funcion encuentro cuantos minutos es exactamente
def calcular_minutos(hora):
    partes = hora.split(":")
    horas = int(partes[0])
    minutos = int(partes[1])
    return horas * 60 + minutos


#Si tengo una cantidad de minutos, con esta funcion la paso a una forma de hora HH:MM
def minutos_a_hora(minutos):
    horas = minutos // 60
    minutos = minutos % 60
    return f"{horas:02d}:{minutos:02d}"


#Esta funcion imprime cola_aterrizaje
def imprimir_aterrizaje():
    if cola_aterrizaje:
        print("Aviones en cola de aterrizaje:")
        for avion in cola_aterrizaje:
            print(f"Número de vuelo: {avion.numero}, Tipo: {avion.tipo_vuelo}, Hora de despegue: {avion.hora_despegue}, Hora de aterrizaje: {avion.hora_aterrizaje}, Duración de vuelo: {avion.duracion_vuelo} minutos, Prioridad: {avion.prioridad}, Puerta de salida: {avion.puerta_salida}, Puerta de entrada: {avion.puerta_entrada}, Estado: {avion.estado}")
    else:
        print("No hay aviones en cola de aterrizaje.")


#Esta funcion imprime cola_aterrizado, es decir los aviones que ya aterrizaron
def imprimir_aterrizado():
    if cola_aterrizado:
        print("Aviones aterrizados:")
        for avion in cola_aterrizado:
            print(f"Número de vuelo: {avion.numero}, Tipo: {avion.tipo_vuelo}, Hora de despegue: {avion.hora_despegue}, Hora de aterrizaje: {avion.hora_aterrizaje}, Duración de vuelo: {avion.duracion_vuelo} minutos, Prioridad: {avion.prioridad}, Puerta de salida: {avion.puerta_salida}, Puerta de entrada: {avion.puerta_entrada}, Estado: {avion.estado}")
    else:
        print("No hay aviones aterrizados.")


#Esta funcion imprime cola_despegue
def imprimir_despegue():
    if cola_despegue:
        print("Aviones en cola de despegue:")
        for avion in cola_despegue:
            print(f"Número de vuelo: {avion.numero}, Tipo: {avion.tipo_vuelo}, Hora de despegue: {avion.hora_despegue}, Hora de aterrizaje: {avion.hora_aterrizaje}, Duración del vuelo: {avion.duracion_vuelo} minutos, Prioridad: {avion.prioridad}, Puerta de salida: {avion.puerta_salida}, Puerta de entrada: {avion.puerta_entrada}, Estado: {avion.estado}")
    else:
        print("No hay aviones en cola de despegue")

#Esta funcion imprime cola_despegado
def imprimir_despegado():
    if cola_despegado:
        print("Aviones despegados:")
        for avion in cola_despegado:
            print(f"Número de vuelo: {avion.numero}, Tipo: {avion.tipo_vuelo}, Hora de despegue: {avion.hora_despegue}, Hora de aterrizaje: {avion.hora_aterrizaje}, Duración de vuelo: {avion.duracion_vuelo} minutos, Prioridad: {avion.prioridad}, Puerta de salida: {avion.puerta_salida}, Puerta de entrada: {avion.puerta_entrada}, Estado: {avion.estado}")
    else:
        print("No hay aviones despegados.")


#Esta funcion puede borrar aviones de cualquier lista, yo la voy a utilizar para borrar los aviones de estado "Cancelled" o para evitar que un avión "Cancelled" aterrize o despegue
def borrarCancelled(cola):
    for avion in cola:
        if avion.estado == 3:
            cola.remove(avion)
            return True
    return False


#Este contador es como el reloj en mi programa
contador = 0
def contar():
    global contador #El contador representa los minutos del dia,por eso tengo una funcion minutos_a_hora para poder dar la hora cuando ejecutamos el programa
    while True:
        time.sleep(1)
        contador += 3
        if contador >= 1440: #Como solo hay 1440 minutos en un día, cunado el contador llegue a 1440, el contador volvera a 0, es media noche
            contador = 0
#El contador aumenta de 3 para que (con la ayuda del comentario en la linea 282), si un avion utiliza una pista, esa pista no podra ser utilizada duranto tres minutos


hilo_contador = threading.Thread(target=contar)
hilo_contador.daemon = True
hilo_contador.start()


#Esta funcion dice el estado de un avion, si va a despegar, si ya despego, si va a aterrizar o si ya aterrizo.
def verifEst(num):
    for i in range(len(cola_aterrizaje)):
        if cola_aterrizaje[i].numero == num:
            print(f"El avion del vuelo {cola_aterrizaje[i].numero} aún no ha aterrizado, le hora de llegada es: {cola_aterrizaje[i].hora_aterrizaje} y está de {i+1} en la cola")
    for i in range(len(cola_aterrizado)):
        if cola_aterrizado[i].numero == num:
            print(f"El avion del vuelo {cola_aterrizado[i].numero} aterrizo a las {cola_aterrizado[i].hora_aterrizaje}")
    for i in range(len(cola_despegue)):
        if cola_despegue[i].numero == num:
            print(f"El avion del vuelo {cola_despegue[i].numero} aún no ha despegado, la hora de salida es: {cola_despegue[i].hora_despegue} y está de {i+1} en la cola")
    for i in range(len(cola_despegado)):
        if cola_despegado[i].numero == num:
            print(f"El avion del vuelo {cola_despegado[i].numero} despego a las {cola_despegado[i].hora_despegue} ")



#Esta funcion muestra la puerta de llegada o de entrada de un avion.
def consultarPuerta(num):
    for i in range(len(cola_aterrizaje)):
        if cola_aterrizaje[i].numero == num:
            print(f"La puerta de llegada del vuelo {cola_aterrizaje[i].numero} es: {cola_aterrizaje[i].puerta_entrada}")
    for i in range(len(cola_aterrizado)):
        if cola_aterrizado[i].numero == num:
            print(f"La puerta de llegada del vuelo {cola_aterrizado[i].numero} es: {cola_aterrizado[i].puerta_entrada}")
    for i in range(len(cola_despegue)):
        if cola_despegue[i].numero == num:
            print(f"La puerta de salida del vuelo {cola_despegue[i].numero} es: {cola_despegue[i].puerta_salida}")
    for i in range(len(cola_despegado)):
        if cola_despegado[i].numero == num:
            print(f"La puerta de salida del vuelo {cola_despegado[i].numero} es: {cola_despegado[i].puerta_salida}")


#Esta funcion es la que sanciona un avion si se atrasa y no despega a tiempo
def vueloAtrazado(num):
    for i in range(len(cola_despegue)):
        if cola_despegue[i].numero == num:
            cola_despegue.insert(i + 10, cola_despegue.pop(i))
            print(f"El vuelo {cola_despegue[i].numero} esta sancionado, pasa de la posicion {i+1} a la posicion {i+11}")
            break
        else:
            print(f"No hay ningun vuelo con el numero: {num}")


#Esta funcion es la que puede poner toda la cola de aterrizaje en "Delayed" o en "Cancelled"
def listaEsperaAterrizaje(nume):
    if nume == "1":
        for avion in cola_aterrizaje:
            avion.estado = "1"
    if nume == "2":
        for avion in cola_aterrizaje:
            avion.estado = "2"
    if nume == "3":
        for avion in cola_aterrizaje:
            avion.estado = "3"


#Esta funcion es la que puede poner toda la cola de despegue en "Delayed" o en "Cancelled"
def listaEsperaDespegue(numer):
    if numer == "1":
        for avion in cola_despegue:
            avion.estado = "1"
    if numer == "2":
        for avion in cola_despegue:
            avion.estado = "2"
    if numer == "3":
        for avion in cola_despegue:
            avion.estado = "3"



if __name__ == "__main__":
    opcion = 9999999999
    while opcion != 0:

        borrarCancelled(cola_despegado)
        borrarCancelled(cola_aterrizado)
        #La linea 279 y 278 impiden que un avion de estado "Cancelled" entre en la lista de aviones que despegaron o aterrizaron, ya que fueron cancelados


#En la linea 285 y 298, se crearon dos valores bool, para que cuando un avión utilice una pista, el bool cambie de valor y esta  pista no puede ser utilizada inmediatamente
        flag = True
        while flag:
            for avion in cola_despegue:
                m = calcular_minutos(avion.hora_despegue)
                if contador >= m:
                    if avion.estado != "3":
                        avion.est = "despegado"
                        cola_despegado.append(avion)
                        cola_despegue.remove(avion)
                        print(f"El avión {avion.numero} despegó...")
                        flag = False
            flag = False

        flag2 = True
        while flag2:
            for avion in cola_aterrizaje:
                m = calcular_minutos(avion.hora_aterrizaje)
                if contador >= m:
                    if avion.estado != "3":
                        avion.est = "Aterrizado"
                        cola_aterrizado.append(avion)
                        cola_aterrizaje.remove(avion)
                        if avion.prioridad == "4":      #Si el avion que aterriza es "Emergencia", los otros aviones tienen un retraso de 30 minutos, que sea para despegar o aterrizar
                            print("Delayed flight")
                            for avion_despegue in cola_despegue:
                                mT = calcular_minutos(avion_despegue.hora_despegue) + 30
                                avion_despegue.hora_despegue = minutos_a_hora(mT)
                            for avion_aterrizaje in cola_aterrizaje:
                                mTemp = calcular_minutos(avion_aterrizaje.hora_aterrizaje) + 30
                                avion_aterrizaje.hora_aterrizaje = minutos_a_hora(mTemp)
                            flag2 = False
                        if avion.prioridad == "2":  #Si el avion que aterriza es "Militar", los otros aviones  tienen un retraso de 10 minutos, que sea para despegar o aterrizar
                            print("Delayed")
                            for avion_despegue in cola_despegue:
                                mT = calcular_minutos(avion_despegue.hora_despegue) + 10
                                avion_despegue.hora_despegue = minutos_a_hora(mT)
                            for avion_aterrizaje in cola_aterrizaje:
                                mTemp = calcular_minutos(avion_aterrizaje.hora_aterrizaje) + 10
                                avion_aterrizaje.hora_aterrizaje = minutos_a_hora(mTemp)
                            flag2 = False
                        print(f"El avión {avion.numero} aterrizó...")
                        flag2 = False
            flag2 = False

        print("\nMenú:")
        print("1. Agregar un avión")
        print("2. Imprimir lista de despegue")
        print("3. Imprimir lista de aterrizaje")
        print("4. Impimir la lista de aviones que ya aterrizaron")
        print("5. Imprimir la lista de aviones que ya despegaron")
        print("6. Verificar el estado de un vuelo")
        print("7. Verificar la puerta de un vuelo")
        print("8. Sancionar un vuelo si está atrasado")
        print("9. Modificar el estado de la lista de espera")
        print("10. Imprimir una lista de todos los vuelos de la duracion de vuelo mas corta a la mas larga")
        print("11. Imprimir una lista de todos los vuelos de la duracion de vuelo mas larga a la mas corta")
        print("0. Salir")
        print("Hora: ", minutos_a_hora(contador))

        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 1:
            agregar_vuelo()
        elif opcion == 2:
            imprimir_despegue()
            c = len(cola_despegue)
            print(f"{c} aviones van a despegar")
        elif opcion == 3:
            imprimir_aterrizaje()
            d = len(cola_aterrizaje)
            print(f"{d} aviones van a aterrizar")
        elif opcion == 4:
            imprimir_aterrizado()
            a = len(cola_aterrizado)
            print(f"{a} aviones aterrizaron")
        elif opcion == 5:
            imprimir_despegado()
            b = len(cola_despegado)
            print(f"{b} aviones despegaron")
        elif opcion == 6:
            num = (input("Ingrese el numero del vuelo que quieres mirar el estado: "))
            verifEst(num)
        elif opcion == 7:
            nu = (input("Ingrese el numero del vuelo que quieres mirar la puerta: "))
            consultarPuerta(nu)
        elif opcion == 8:
            n = (input("Ingrese el numero del vuelo que está atrasado: "))
            vueloAtrazado(n)

        elif opcion == 9:
            numm = (input("Cambiar el estado de los aviones en 1.la lista de despegue o 2. La lista de aterrizaje: "))
            if numm == "1":
                nume = (input("Quieres poner la fila en 1.On Time, 2. Delayed o 3.Cancelled: "))
                listaEsperaDespegue(nume)
            if numm == "2":
                numer = (input("Quieres poner la fila en 1.On Time, 2. Delayed o 3.Cancelled: "))
                listaEsperaAterrizaje(numer)

        elif opcion == 10:      #Esta funcion no es del parcial, era para ensayar
            cola_menor_a_mayor = sorted(cola_aterrizaje + cola_despegue + cola_aterrizado + cola_despegado,
                                        key=lambda avion: avion.duracion_vuelo)
            for avion in cola_menor_a_mayor:
                print(f"Avión número {avion.numero} - Duración de vuelo: {avion.duracion_vuelo}")

        elif opcion == 11:      #Esta funcion no es del parcial, era para ensayar
            cola_mayor_a_menor = sorted(cola_aterrizaje + cola_despegue + cola_aterrizado + cola_despegado,
                                        key=lambda avion: avion.duracion_vuelo, reverse=True)
            for avion in cola_mayor_a_menor:
                print(f"Avión número {avion.numero} - Duración de vuelo: {avion.duracion_vuelo}")


        elif opcion == 0:
            print("Saliendo del programa...")
        else:
            print("Opción inválida, por favor seleccione una opción válida.")




