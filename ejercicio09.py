import multiprocessing
import time
import random

def consultar(archivo, tiempo):
   print(f"Consultando...{archivo}")
   time.sleep(tiempo)
   print(f"Finalizó {archivo}")
   
tareas = [
    ("Archivo A", random.uniform(1, 5)),
    ("Archivo B", random.uniform(1, 5)),
    ("Archivo C", random.uniform(1, 5))
]

if __name__ == "__main__":
   inicio = time.time()
   procesos = []
   for nombre, t in tareas:
    p = multiprocessing.Process(target=consultar, args=(nombre, t))
    p.start()
    procesos.append(p)
    
    for p in procesos:
       p.join()
    
    print("Tiempo total:", time.time() - inicio)