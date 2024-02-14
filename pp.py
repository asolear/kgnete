from pdf2image import convert_from_path
from PIL import Image
import os
import shutil
import glob
import datetime
from types import SimpleNamespace


def imagenes(pdf_path, carpeta_destino, resolucion_dpi=300):
    # Convierte el PDF a una lista de imágenes
    imagenes = convert_from_path(pdf_path, dpi=resolucion_dpi)
    ruta_carpeta = f"{carpeta_destino}/{pdf_path[:-4]}"
    if os.path.exists(ruta_carpeta):
        # Si existe, la borra con todo su contenido
        shutil.rmtree(ruta_carpeta)
    os.mkdir(ruta_carpeta)
    # Recorre todas las imágenes generadas
    for num_pagina, imagen in enumerate(imagenes):
        # Guarda la imagen en la carpeta de destino
        imagen_path = f"{carpeta_destino}/{pdf_path[:-4]}/pagina_{num_pagina + 1}.png"
        imagen.save(imagen_path, "PNG")
        pngs.append(f"![]({pdf_path[:-4]}/pagina_{num_pagina + 1}.png)\n")


def obtener_archivos_con_rutas(directorio):
    archivos_con_rutas = []
    # Utilizar glob para obtener la lista de archivos de manera recursiva
    archivos = glob.glob(os.path.join(directorio, "**", "*"), recursive=True)

    for archivo in archivos:
        if os.path.isfile(archivo) and ".pdf" in archivo.lower():
            # Almacenar el nombre del archivo y su ruta en la lista
            fecha_creacion = datetime.datetime.fromtimestamp(os.path.getctime(archivo))
            fecha_creacion = os.path.getctime(archivo)

            archivos_con_rutas.append((archivo, fecha_creacion))
            # print((archivo,fecha_creacion))

    tuplas = archivos_con_rutas
    #
    files = [tupla[0] for tupla in tuplas]
    nombres = [tit.split("/")[-1:][0][:-4] for tit in files]
    categoriass = [cat.split("/")[7:-1] for cat in files]
    #
    dates = [tupla[1] for tupla in tuplas]
    fechas = [
        datetime.datetime.fromtimestamp(date).strftime("%Y-%m-%d") for date in dates
    ]

    return nombres, categoriass, fechas


def md(carpeta_destino):
    #
    cats = ["FV", "Aisalada", "Conectadas"]
    lineascats = []
    lineascats.append(f"categories:\n")
    for cat in cats:
        lineascats.append(f"  - {cat}\n")
    f = open(f"{carpeta_destino}/pp.md", "w")
    lineas = [
        "---",
        "date: 2023-01-31 ",
        "authors:",
        "  - kgnete",
        f"{''.join(lineascats)}",
        "---",
        "#",
        f"{''.join(pngs)}",
    ]
    for linea in lineas:
        f.write(linea + "\n")
    f.close()
    print(pngs)

def cname():
        f = open(f"docs/CNAME", "w")
        f.write('kgnete.com')
        f.close()


if __name__ == "__main__":
    o = SimpleNamespace()
    cname()
    # Directorio que quieres explorar de manera recursiva
    directorio_raiz = "/home/pk/Desktop/web_pdfs_qroman17/docs/Tramites y Permisos"

    # Obtener la lista de archivos con rutas
    nombres, categoriass, fechas = obtener_archivos_con_rutas(directorio_raiz)

    pdfs = ["pp"]
    for pdf in pdfs:
        carpeta_destino = "docs/blog/posts"
        pngs = []
        imagenes(f"{pdf}.pdf", carpeta_destino, resolucion_dpi=100)
        md(carpeta_destino)
