# Archivos
logs = ["E:\PYTHON\QTC\log\H2_3-21G.log",
        "E:\PYTHON\QTC\log\H2_4-31G.log",
        "E:\PYTHON\QTC\log\H2_6-31G+.log",
        "E:\PYTHON\QTC\log\H2_6-31G++.log",
        "E:\PYTHON\QTC\log\H2_STO-3G.log"]

# palabras a buscar
palabras_clave = ['SCF', 'Mulliken']

try:
    # Abre archivo para guardar los resultados y añade al archivo
    with open("E:\PYTHON\QTC\log\prueba.txt", "a") as archivo_resultado:
        for nombre_archivo in logs:
            with open(nombre_archivo, 'r') as archivo:
                archivo_resultado.write(f"Archivo: {nombre_archivo}\n")
                print(f"Archivo: {nombre_archivo}")
                
                # Lee el archivo línea por línea
                lineas = archivo.readlines()

                for palabra_clave in palabras_clave:
                    archivo_resultado.write(f"{palabra_clave}\n")
                    print(f"{palabra_clave}")

                    # Recorre las líneas y busca la cadena
                    for linea in lineas:
                        if palabra_clave in linea:
                            s = []
                            for num in linea.split():
                                try:
                                    s.append(float(num))
                                except ValueError:
                                    pass

                            # para que no imprima listas vacías 
                            if len(s) >= 1:
                                                              
                                # Escribe en el archivo los numeros encontrados
                                archivo_resultado.write(f"{s}\n")
                                print(f"{s}")

except FileNotFoundError:
    print("archivo no encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")