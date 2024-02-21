from pdf2image import convert_from_path
from PIL import Image
import os
import shutil
import glob
import datetime
from types import SimpleNamespace


def imagenes(file, carpeta_destino, resolucion_dpi=300):
    o.pngs=[]
    pdf_path, o.archivo = os.path.split(file)
    # Convierte el PDF a una lista de imágenes
    imagenes = convert_from_path(file, dpi=resolucion_dpi)
    ruta_carpeta = f"{carpeta_destino}/{o.archivo[:-4]}"
    if os.path.exists(ruta_carpeta):
        # Si existe, la borra con todo su contenido
        shutil.rmtree(ruta_carpeta)
    os.mkdir(ruta_carpeta)
    # Recorre todas las imágenes generadas
    for num_pagina, imagen in enumerate(imagenes):
        # Guarda la imagen en la carpeta de destino
        imagen_path = f"{ruta_carpeta}/pagina_{num_pagina + 1}.png"
        imagen.save(imagen_path, "PNG")
        o.pngs.append(f"![]({o.archivo[:-4]}/pagina_{num_pagina + 1}.png)\n")


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
    o.files = [tupla[0] for tupla in tuplas]
    o.nombres = [tit.split("/")[-1:][0][:-4] for tit in o.files]
    o.categoriass = [cat.split("/")[7:-2] for cat in o.files]
    #
    dates = [tupla[1] for tupla in tuplas]
    o.fechas = [
        datetime.datetime.fromtimestamp(date).strftime("%Y-%m-%d") for date in dates
    ]

    return o.files, o.nombres, o.categoriass, o.fechas


def md(date,cats):
    carpeta_destino = "docs/blog/posts"
    #
    
    lineascats = []
    lineascats.append(f"categories:\n")
    for cat in cats:
        lineascats.append(f"  - {cat}\n")
    f = open(f"{carpeta_destino}/{o.archivo[:-4]}.md", "w")
    lineas = [
        "---",
        f"date: {date}",
        "authors:",
        "  - Fotovoltaica",
        f"{''.join(lineascats)}",
        "---",
        "#",
        f"{''.join(o.pngs)}",
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
    carpeta_destino="/home/pk/Desktop/mkdocs/docs/blog/posts"
    # Directorio que quieres explorar de manera recursiva
    directorio_raiz = "/home/pk/Desktop/web_pdfs_qroman17/docs/Tramites y Permisos"
    directorio_raiz = "/home/pk/Desktop/web_pdfs_qroman17/docs/Proyectos/Fotovoltaica/08_ANEJOS/INCENTIVOS_NEXT_GENERATION"
    directorio_raiz = "/home/pk/Desktop/pdfs/docs/aa"
    # directorio_raiz = "/home/pk/Desktop/web_pdfs_qroman17/assets/fichatecnica"


    # Obtener la lista de archivos con rutas
    o.files, o.nombres, o.categoriass, o.fechas = obtener_archivos_con_rutas(directorio_raiz)


    for ii, file in enumerate(o.files):

        pngs = []
        imagenes(file, carpeta_destino, resolucion_dpi=100)
        md(o.fechas[ii],o.categoriass[ii])
