import os
import eyed3
import shutil

def obtener_genero(archivo):
    # Utiliza eyed3 para obtener el género de la canción
    audiofile = eyed3.load(archivo)
    if audiofile.tag and audiofile.tag.genre:
        return audiofile.tag.genre.name
    return None

def organizar_por_genero(directorio_actual, directorio_destino):
    # Crear el directorio destino si no existe
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)

    # Obtener la lista de archivos en el directorio actual
    archivos = os.listdir(directorio_actual)

    # Iterar sobre los archivos y organizar por género
    for archivo in archivos:
        ruta_archivo = os.path.join(directorio_actual, archivo)
        genero = obtener_genero(ruta_archivo)

        if genero:
            # Crear un directorio para el género si no existe
            directorio_genero = os.path.join(directorio_destino, genero)
            if not os.path.exists(directorio_genero):
                os.makedirs(directorio_genero)

            # Mover el archivo al directorio del género
            destino = os.path.join(directorio_genero, archivo)
            shutil.move(ruta_archivo, destino)
            print(f"Se movió {archivo} a la carpeta '{genero}'")

if __name__ == "__main__":
    # Directorio actual donde se encuentran las canciones
    directorio_actual = "/home/roadcode/Music"

    # Directorio donde se organizarán las canciones por género
    directorio_destino = "/home/roadcode/Music/PorGenero"

    organizar_por_genero(directorio_actual, directorio_destino)
