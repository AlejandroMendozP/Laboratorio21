import time
import threading
import random

def consultar(archivo, tiempo):
    print(f"Consultando...{archivo}")
    time.sleep(tiempo)
    print(f"Consulta exitosa: {archivo}")

tareas = [
    ("Archivo A", random.uniform(1, 5)),
    ("Archivo B", random.uniform(1, 5)),
    ("Archivo C", random.uniform(1, 5))
]

inicio = time.time()

hilos = []
for nombre, tiempo in tareas:
    h = threading.Thread(target=consultar, args=(nombre, tiempo))
    h.start()
    hilos.append(h)

for h in hilos:
    h.join()

fin = time.time()
print(f"Tiempo total: {fin - inicio:.2f} segundos")