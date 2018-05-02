#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os

BASE_DIR = os.getcwd() # ruta actual del archivo

# generar log
'''los parámetros a entregar son
- mensaje: el mensaje a enviar
- path = path de donde se desea guardar el archivo log (opcional)
- nombre_archivo = nombre del archiv (opcional)
- sobreescribit = booleano (opcional)
- tipo_mensaje = valores permitidos: ['info', 'debug', 'warning'] (opcional)
'''
def generar_log(mensaje, **config):
    keys_config = []
    for key in config.keys():
        keys_config.append(key)
    # -- path del log
    if not 'path' in keys_config:
        path_archivo = BASE_DIR
    else:
        path_archivo = config['path']
    # -- nombre del archivo log
    if not 'nombre_archivo' in keys_config:
        nombre_archivo = 'ArchivoDeuda.log'
    else:
        nombre_archivo = config['nombre_archivo']
    # -- definir el archivo log
    fichero_log = os.path.join(path_archivo, nombre_archivo)
    # -- escritura 'w' o 'a'
    if not 'sobreescribir' in keys_config:
        sobreescribir = False
    else:
        sobreescribir = config['sobrescribir']
    if sobreescribir == True:
        tipo = 'w'
    else:
        tipo = 'a'
    # -- configurar salida del log
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filename = fichero_log,
                    filemode = tipo,)
    # -- definir tipo de mensaje
    if not 'tipo_mensaje' in keys_config:
        tipo_mensaje = 'info'
    else:
        tipo_mensaje = config['tipo_mensaje']
    # -- escribir mensaje
    if tipo_mensaje == 'debug':
        logging.debug(mensaje)
    elif tipo_mensaje == 'warning':
        logging.warning(mensaje)
    else:
        logging.info(mensaje)