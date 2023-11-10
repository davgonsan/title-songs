import os
import shutil

# Directorio actual donde se encuentran las canciones
directorio_actual = "/home/roadcode/Music"

# Directorio donde se moverán las canciones de Canserbero
directorio_destino = "/home/roadcode/Music/Rap/Canserbero"

# Lista de palabras clave que identifican las canciones de Canserbero
palabras_clave = ["Canserbero", "Apa y Can", "Muerte", "Vida", "Guía Para La Acción"]

# Crear el directorio 'Canserbero' si no existe
if not os.path.exists(directorio_destino):
    os.makedirs(directorio_destino)

# Obtener la lista de archivos en el directorio actual
archivos = os.listdir(directorio_actual)

# Iterar sobre los archivos y mover los de Canserbero al nuevo directorio
for archivo in archivos:
    for palabra_clave in palabras_clave:
        if palabra_clave.lower() in archivo.lower():
            origen = os.path.join(directorio_actual, archivo)
            destino = os.path.join(directorio_destino, archivo)
            shutil.move(origen, destino)
            print(f"Se movió {archivo} a la carpeta 'Canserbero'")
            break
