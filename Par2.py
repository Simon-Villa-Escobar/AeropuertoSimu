import threading
import queue
import time
import random

MAX_TERMINALES = 5
cola_aterrizaje = queue.Queue()
cola_despegue = queue.Queue()
locks_terminales = [threading.Lock() for _ in range(MAX_TERMINALES)]    # Se crean los locks para cada terminal
aviones_despegados = 0
mutex_contador = threading.Lock()   # Lock para proteger el acceso al contador de aviones despegados

def avion_aterrizando():
    while True:
        avion = cola_aterrizaje.get()
        terminal_libre = -1
        for i, lock in enumerate(locks_terminales): # Se busca una terminal libre para aterrizar el avión
            if lock.acquire(blocking=False):
                terminal_libre = i
                break
        if terminal_libre == -1:
            cola_aterrizaje.put(avion)
            time.sleep(1)
        else:
            print(f'Avión {avion} aterrizó en la terminal {terminal_libre}')
            time.sleep(30)
            print(f'Avión {avion} se prepara para despegar')
            time.sleep(10)
            print(f'Avión {avion} ha despegado')
            with mutex_contador:
                global aviones_despegados
                aviones_despegados += 1
                if aviones_despegados == 15:
                    print('Todos los aviones han despegado. Fin del programa.')
                    exit()
            cola_despegue.put(avion)
            locks_terminales[terminal_libre].release()
        cola_aterrizaje.task_done()

def avion_despegando():
    while True:
        avion = cola_despegue.get()
        time.sleep(1)
        print(f'Avión {avion} ha dejado la cola de despegue')
        with mutex_contador:
            global aviones_despegados
            if aviones_despegados == 15:
                print('Todos los aviones han despegado. Fin del programa.')
                exit()
        cola_despegue.task_done()

def generar_aviones():
    for i in range(15):
        time.sleep(random.randint(1, 10))
        cola_aterrizaje.put(i)
        print(f'Avión {i} en cola de aterrizaje')

threading.Thread(target=generar_aviones).start()

for _ in range(5):
    threading.Thread(target=avion_aterrizando).start()
threading.Thread(target=avion_despegando).start()

cola_aterrizaje.join()
cola_despegue.join()
