#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Notas: 
# Se han desarrollado métodos que simplifican algunas llamadas de selenium, tales como imprimir pantalla, o realizar scroll dentro de una página. A continuación se presentan dichos métodos
# separator(): Método para detectar OS y además devuelve el separador correspondiente para navegar dentro de directorios
# find_text(param): Método para encontrar elementos por el tipo o valor que tienen, este método puede ser usado para hayar inputs o botones
# carga_archivo(param, param2): Método para buscar un archivo de carga param = nombre del directorio, param2 = nombre del archivo
# save_screenshot(param): guarda una captura de pantalla, param = nombre de la captura
# scroll_page(param): método para hacer scroll a la página, param = cantidad de scroll


# importar librerías de SELENIUM
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# Otras librerías
import time # libreria de tiempo de esperas
import os   # librería para manipular archivos, obtener rutas, etc
import csv # librería para trabajar con archivos CSV
from datetime import datetime # librería de tiempo
import platform # librería para indicar versiones y tipos del OS
import random # librería random
import zipfile # librería para trabajar con archivos .zip
import sys

# cabeceras
BASE_DIR = os.getcwd() # ruta actual del archivo
GET_DATE = datetime.now().strftime('%Y%m%d-%H%M%S') # obtener fecha y hora actual para generar carpeta de evidencias 
DATE_NOW = datetime.now().strftime('%d-%m-%Y')

descarga_list = ['image/jpeg', 'image/png', 'application/postscript',
                'application/eps', 'application/x-eps', 'image/x-eps',
                'image/eps', 'application/pdf', 'application/octet-stream',
                'application/download', 'application/zip', 'text/plain']
descarga_lista = ",".join(str(i) for i in descarga_list)

# -- configuración firefox --
profile_firefox = webdriver.firefox.firefox_profile.FirefoxProfile()
profile_firefox.set_preference("browser.download.folderList", 2)
profile_firefox.set_preference("browser.download.manager.showWhenStarting", False)
profile_firefox.set_preference('browser.helperApps.neverAsk.saveToDisk', descarga_lista)
profile_firefox.set_preference("browser.helperApps.alwaysAsk.force", False)
profile_firefox.set_preference("plugin.disable_full_page_plugin_for_types", descarga_lista)
profile_firefox.set_preference("pdfjs.disabled", True)
profile_firefox.set_preference(
    "general.useragent.override",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0)"
    " Gecko/20100101 Firefox/26.0")
profile_firefox.set_preference("http.response.timeout", 60)
profile_firefox.set_preference("dom.max_script_run_time", 60)
# -- configuración firefox --

# -- configuración Chrome --


# obtener OS 
def separator():
    if 'windows'.casefold() in platform.system().casefold():
        separator = '\\'
    else:
        separator = '/'
    return separator

# método para buscar un elemento por valor o tipo
def find_text(text):
    try:
        valor = driver.find_elements_by_css_selector('[value="%s"]' %text)
        valor = valor[0]
    except:
        try:
            valor = driver.find_elements_by_css_selector('[title="%s"]' %text)
            valor = valor[0]
        except:
            try:
                valor = driver.find_elements_by_css_selector('[type="%s"]' %text)
                valor = valor[0]
            except:
                valor = False
    return valor 

# retorna una lista de elementos encontrados
def find_elements(text):
    valores = driver.find_elements_by_css_selector('[title="%s"]' %text)
    if len(valores) == 0:
        valores = driver.find_elements_by_css_selector('[value="%s"]' %text)
        if len(valores) == 0:
            valores = driver.find_elements_by_css_selector('[type="%s"]' %text)
    return valores 

# método para generar evidencias
def directorio_evidencia():
    if not os.path.exists('Evidencias'):
        os.makedirs('Evidencias')
    return BASE_DIR + separator() + 'Evidencias' + separator()

def evidencia_actual():
    nombre_dir = directorio_evidencia() + GET_DATE # obtener la ruta de la nueva carpeta
    if not os.path.exists(nombre_dir):
        os.makedirs(nombre_dir)
    return nombre_dir + separator() # retorna path de la nueva carpeta creada para la generacion de evidencias

# metodo para obtener path de los "archivos" importantes, acá se almacenan los archivos que se utilizarán para subir al sistema.
def archivos_necesarios(name):
    if os.path.exists(name):
        return BASE_DIR + separator() + name + separator()
    else:
        return BASE_DIR + separator()   # en caso de que no exista la carpeta, se buscará en el directorio raíz     

# cargar archivo
def carga_archivo(dir, archivo):
    return archivos_necesarios(dir) + archivo

# set preferences (ultimate)
global evidencia # variable global
evidencia = evidencia_actual()
# evidencia_actual().replace('\\', '/')
profile_firefox.set_preference("browser.download.dir", evidencia)
profile_firefox.set_preference("browser.download.downloadDir", evidencia)
profile_firefox.set_preference("browser.download.defaultFolder", evidencia)
profile_firefox.accept_untrusted_certs = True

'''Parametros de entrada:
- browser: navegador a levantar (se permite firefox y chrome); valor por defecto = 'firefox'
- driver_path: path en donde se encuentra en driver
- headless: indica si se requiere ejecutar el navegador en formato headless (booleano)
'''
def open_browser(browser = 'firefox', **data_extra):
    data_key = []
    for key in data_extra.keys():
        data_key.append(key)
    global driver
    browser = browser.lower()
    if browser == 'firefox':
        from selenium.webdriver.firefox.options import Options # firefox options
        firefox_options = Options()
        firefox_options.set_headless(data_extra['headless'])
        if 'driver_path' in data_key:
            driver = webdriver.Firefox(firefox_profile=profile_firefox, firefox_options=firefox_options, executable_path=data_extra['driver_path'])
        else:
            driver = webdriver.Firefox(firefox_profile=profile_firefox, firefox_options=firefox_options)
    elif browser == 'chrome':
        from selenium.webdriver.chrome.options import Options # chrome options
        if 'driver_path' in data_key:
            driver = webdriver.Firefox(executable_path=data_extra['driver_path'])
        else:
            driver = webdriver.Chrome()
    # driver.set_page_load_timeout(60)
    return driver
        
# metodo para abrir navegador
def open_url(url):
    if not 'http' in url:
        url = 'http://' + url
    return driver.get(url) # se obtiene por parámetro la url a abrir    

# guardar screenshot
def save_screenshot(name):
    time = datetime.now().strftime('%d%m%Y-%H%M%S')
    return driver.save_screenshot(evidencia+time+'_'+name+'.png')

# hacer scroll
def scroll_page(cantidad):
    return driver.execute_script('$(window).scrollTop(%s);' %int(cantidad))

# -- Fin cabeceras -- 

# login dnp
def login(user, name_file='potato/archivos/credenciales.csv'):
    result = {}
    with open(name_file, 'r') as fopen:
        reader = csv.reader(fopen, delimiter=";")
        for row in reader:
            key = row[0]
            if key in result:
                pass
            result[key] = row[1:]
    pswd = result[user][0] # la primera es la contraseña
    usr = driver.find_element_by_name('username') # usuario
    usr.clear() # limpiar, en caso de que exista data escrita
    usr.send_keys(user) 
    passwd = driver.find_element_by_name('password') # contaseña
    passwd.clear()
    passwd.send_keys(pswd)
    save_screenshot('login')  # guardar captura pantalla
    driver.find_element_by_css_selector('[type="submit"]').click() # click en submit del formulario

def generic_login(**kwargs):
    for key, value in kwargs.items():
        filtro = driver.find_element_by_name(key) # name porque son inputs de un formulario
        filtro.clear()
        filtro.send_keys(value)
    return find_text('submit').click()

def close():
    return driver.close()

# método para ingresar datos en inputs (se pueden ingresar los que quieran)
def filtro_ingreso(**kwargs):
    for key, value in kwargs.items():
        filtro = driver.find_element_by_name(key) # name porque son inputs de un formulario
        filtro.clear()
        filtro.send_keys(value)

# método para buscar y ejecutar filtros selectbox, el tipo_filtro es el texto por el que se busca
def filtro_select(filtro, tipo_filtro):
    # filtro solamente para efectos de un select
    select = Select(driver.find_element_by_name(filtro))
    select.select_by_visible_text(tipo_filtro)

