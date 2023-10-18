# Exportador de nombres de archivos

Este script de Python recopila los nombres de archivo en una carpeta específica y los exporta en varios formatos, incluyendo archivos de texto (TXT), hojas de cálculo Excel (XLS), y hojas de cálculo Excel modernas (XLSX).

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas de Python:

- `os`
- `xlwt` (para crear archivos XLS)
- `openpyxl` (para crear archivos XLSX)

Puedes instalar estas bibliotecas usando pip:

`pip install xlwt openpyxl`

## Uso

1. Configura la ruta de la carpeta que contiene los archivos que deseas procesar modificando la variable `carpeta` en el código.

```python
carpeta = '/ruta/a/tu/carpeta'


## Archivos Generados
El script generará los siguientes archivos en el directorio de trabajo:

archivos.txt: Contiene la lista de nombres de archivo en formato de texto.
archivos.xls: Una hoja de cálculo Excel (XLS) con los nombres de archivo.
archivos.xlsx: Una hoja de cálculo Excel moderna (XLSX) con los nombres de archivo.
Contribuciones
Si deseas contribuir a este proyecto, siéntete libre de hacerlo a través de pull requests.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

¡Disfruta usando esta herramienta para exportar los nombres de archivo en tu carpeta!


Asegúrate de reemplazar "nombre_del_script.py" en la sección de Uso con el nombre de tu archivo de Python si es diferente. También, asegúrate de incluir una licencia adecuada en un archivo `LICENSE` en el mismo directorio si es necesario.