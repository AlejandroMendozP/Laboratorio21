with open("archivo_original.txt", "r") as f_leer:
    with open("archivo_copiado.txt", "w") as f_escribir:
        for linea in f_leer:
            f_escribir.write(linea)

with open("archivo_binario_original.dat", "rb") as f_leer_b:
    with open("archivo_binario_copiado.dat", "wb") as f_escribir_b:
        for linea in f_leer_b:
            f_escribir_b.write(linea)