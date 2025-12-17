import time
import asyncio
import random

async def consultar(archivo, tiempo):
    print(f"Consultando...{archivo}")
    await asyncio.sleep(tiempo)
    print(f"Consulta exitosa: {archivo}")

tareas = [
    ("Archivo A", random.uniform(1, 5)),
    ("Archivo B", random.uniform(1, 5)),
    ("Archivo C", random.uniform(1, 5))
]

inicio = time.time()

async def main():
   inicio = time.time()
   await asyncio.gather(
       consultar("Archivo A", random.uniform(1, 5)),
       consultar("Archivo B", random.uniform(1, 5)),
       consultar("Archivo C", random.uniform(1, 5))
    
    )
   
print("Tiempo total:", time.time() - inicio)
asyncio.run(main())