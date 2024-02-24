from pdf2image import convert_from_path
from PIL import Image
import os
import shutil
import glob
import datetime
from types import SimpleNamespace


def imagenes(file,nombre, carpeta_destino, resolucion_dpi=300):

    if 1:
        o.pngs = []
        # Convierte el PDF a una lista de imágenes
        imagenes = convert_from_path(file, dpi=resolucion_dpi)
        ruta_carpeta = f"{carpeta_destino}"
        if os.path.exists(ruta_carpeta):
            # Si existe, la borra con todo su contenido
            shutil.rmtree(ruta_carpeta)
        os.mkdir(ruta_carpeta)
        # Recorre todas las imágenes generadas
        for num_pagina, imagen in enumerate(imagenes):
            # Guarda la imagen en la carpeta de destino
            imagen_path = f"{ruta_carpeta}/pagina_{num_pagina + 1}.png"
            imagen.save(imagen_path, "PNG")
            o.pngs.append(f"![]({nombre}/pagina_{num_pagina + 1}.png)\n")


def obtener_archivos_con_rutas(directorio):
    
    archivos_con_rutas = []

    carpetas = [nombre for nombre in os.listdir(directorio) if os.path.isdir(os.path.join(directorio, nombre))]
    archivos=[]
    for carpeta in carpetas:
        archivos.append(glob.glob(os.path.join(directorio, carpeta, "*zRES*")))
    archivos = [elemento for sublista in archivos for elemento in sublista if elemento]



    o.archivos=archivos
    
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
    o.nombres = [
        # os.path.basename(os.path.dirname(tit)).split("_")[1] for tit in o.files
        os.path.basename(os.path.dirname(tit)) for tit in o.files
    ]
    o.listaCategorias = [directorio.split("/")[-1:] for cat in o.files]
    dates = [tupla[1] for tupla in tuplas]
    o.fechas = [
        datetime.datetime.fromtimestamp(date).strftime("%Y-%m-%d") for date in dates
    ]

    return o.files, o.nombres, o.listaCategorias, o.fechas


def md(nombre, date, cats):
    carpeta_destino = "docs/blog/posts"
    #

    lineascats = []
    lineascats.append(f"categories:\n")
    for cat in cats:
        lineascats.append(f"  - {cat}\n")
    f = open(f"{carpeta_destino}/{nombre}.md", "w")
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

class archivos:
    def cname():
        f = open(f"docs/CNAME", "w")
        f.write("kgnete.com")
        f.close()


    def authors():
        f = open(f"docs/blog/.authors.yml", "w")
        lineas=["authors:",
        "  Fotovoltaica:",
        "    name: Fotovoltaica",
        "    description: Proyectos",
        "    avatar: /img/casaFV.png",
        "  Aislada:",
        "    name: Aislada",
        "    description: Fotovoltaica",
        "    avatar: /img/sol.png"]

        for linea in lineas:
            f.write(linea + "\n")
        f.close()
        

if __name__ == "__main__":
    if 1:
        # exec(open("aa.py").read())
        archivos.cname()
        archivos.authors()


        o = SimpleNamespace()
        carpeta_destino="/home/pk/Desktop/mkdocs/docs/blog/posts"
        
        if 1:
            try:
                shutil.rmtree(carpeta_destino)
            except:
                ''''''
            os.mkdir(carpeta_destino)
                    
        if 1:
            directorios= ["/home/pk/Desktop/pdfs/md2pdf/Proyectos/Fotovoltaica"]

            for directorio in directorios:
                o.files, o.nombres, o.listaCategorias, o.fechas = obtener_archivos_con_rutas(directorio)
                print(o.files, o.nombres, o.listaCategorias, o.fechas)
                for ii, file in enumerate(o.files):
                    
                    imagenes(o.files[ii],o.nombres[ii], f"{carpeta_destino}/{o.nombres[ii]}", resolucion_dpi=100)
                    md(o.nombres[ii],o.fechas[ii],o.listaCategorias[ii])