# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import pandas as pd

def procesar_directorios(directorio_principal, carpeta_destino, archivo_salida):
    subdirectorios = [sub for sub in os.listdir(directorio_principal) if os.path.isdir(os.path.join(directorio_principal, sub))]
    datos_procesados = []  
    
    for subdirectorio in subdirectorios:
        ruta_subdirectorio = os.path.join(directorio_principal, subdirectorio)
        archivos = [archivo for archivo in os.listdir(ruta_subdirectorio)]
        
        for archivo in archivos:
            ruta_archivo = os.path.join(ruta_subdirectorio, archivo)
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo_lectura:
                contenido_linea = archivo_lectura.readline().strip()
                datos_procesados.append([contenido_linea, subdirectorio])
    
    dataframe = pd.DataFrame(datos_procesados, columns=["phrase", "target"])
    
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
    
    ruta_salida = os.path.join(carpeta_destino, archivo_salida)
    dataframe.to_csv(ruta_salida, index=False)


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """


    procesar_directorios("files/input/test", "files/output", "test_dataset.csv")
    procesar_directorios("files/input/train", "files/output", "train_dataset.csv")

pregunta_01()