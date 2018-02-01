# Potato

A continuación se muestra **potato** para python. Este trabaja con selenium-webdriver y simplifica algunas tareas.

## Requisitos
* Python 3
* Gestor de paquetes **pip**

## Importar potato
Potato se importa como cualquier otra librería, las formas de importarlo son las siguientes:
```python
import potato
from potato import potato
import potato.potato
```

## Funciones

Potato tiene funciones que simplifican el uso de de selenium en python, estos son:

### Abrir el navegador
```python
open_browser() # por defecto abrirá firefox
open_browser('chrome') # abrirá google chrome
open_browser('phantomjs') # abrirá phantomjs (no recomendable)
```
* open_browser() abre el navegador que se indique en el _param_, por defecto viene definido **firefox**. 
* **Importante**: se debe tener el driver para utilizar dicho navegador
    - **Geckodriver** para Firefox
    - **Chromedriver** para Google Chrome
    - entre otros

### Abrir url
```python
open_url('http://www.google.com') # ingresará a la url que se indique en el parámetro
```

### Login
Hay dos formas de hacer login con potato:
```python
login('username', 'archivo/usuario.csv') # buscar al usuario en el path especificado (utiliza archivo csv)
generic_login(username='username', password='password') # se define el username (utiliza el name del input) y el password
```
1. Para el primer método **login(usuario, path)** se dice con qué usuario ingresar al sistema, y el path indica donde se encuentra el archivo csv que contiene los usuarios y contraseña de estos
    - Es importante que el formate del archivo csv esté ordenado primero con usuario y segundo con su contraseña:
    **usuario;password**
2. El segundo método usted deberá indicar que parámetros se deben pasar para hacer un login ¿qué se sugiere?: 
    - Primer valor, indicar el name del input del nombre de usuario, en este caso **username** e indicar el nombre de usuario, ejemplo: username='potato', password='potato'

### scroll down
```python
scroll_page(500) # se hará scroll de 500 (definidos por javascript) hacia abajo en la página
```

### Guardar screenshots
```python
save_screenshot('nombre screenshot') # se debe indicar el nombre que se le quiere poner al screenshot
```
* Se guardará un screenshot de lo que se vea en la pantalla del navegador abierto por potato. Este se guardará en formato .png con el nombre de la fecha y hora_nombre definido.
* Pero, ¿Dónde se guarda?: No te preocupes! potato al ejecutarlo creará directorio de evidecias en donde se ejecute el archivo, ahí irá almacenando los archivos que se descarguen y las capturas de pantalla.

### Filtro ingreso
```python
filtro_ingreso(key='value', key2='value2') # sirve para filtros, se define el name de este y el dato a entregar, pueden ser n registros
```

### Filtro select
```python
filtro_select('name', 'value') # para filtros selectbox, el primer parámetro es el name del select y el segundo el valor 
```
* Importante: el segundo parámetro entregado debe ser el nombre que se encuentra en el select

### Close
```python
close() # cierra el navegador
```