# Analisis de Circuitos: Trabajo Final 
Código del trabajo final de ADC de Rocío Gallo Padrón 97490, 1C2020

El objetivo del siguiente trabajo es el diseño de un filtro que cumpla con una determinada función de 
transferencia $H(s)$. 

## Distribucion del Codigo
Los fuentes se distribuyen cumpliendo tres funcionalidades principales:
 * `adc_tp.py`: Es el main del trabajo, donde se enuentra el parseo de argumentos de entrada y se llaman
 a las funciones que cumplen cada una de las consignas.
 * `exercices.py, functions.py`: Son los archivos que contienen las funcionalidades de las consignas del
 trabajo. 
 * `constants.py`: Contiene las constantes que se usan en todo el trabajo y las etiquetas de cada uno de los
 graficos.

## Uso de la Herramienta
Las simulaciones de este trabajo estan desarrolladas en Python3, para correr el programa es necesario tenerlo
instalado (instrucciones de instalacion para Mac).

```bash 
brew install python3
```

Es necesario tener el instalador de paquetes de Python3, pip3. Si no fue instalado al momento de descargar
Python3, se debera hacer una post instalacion de las presataciones faltantes.

```bash 
brew postinstall python3
```

Para correrlo son tambien necesarias las siguientes bibliotecas, luego de instalar pip3, se deben correr los 
siguientes comandos en una consola. 

```bash 
pip3 install matplotlib
pip3 install numpy
pip3 install scipy
```

Luego, descargar este repositorio, acceder a la carpeta en la que se encuentra y ejecutar el programa 
relacionado al ejercicio deseado.

#### Ejemplos

El siguiente comando ejecutaria el desarrollo del ejercicio 1
```bash 
python3 adc_tp.py 1
```

El siguiente comando ejecutaria el desarrollo del ejercicio 2a, imprimiendo el diagrama de Bode de modulo
```bash 
python3 adc_tp.py 2a -mag
```

Analogamente, para el diagrama de Bode de fase
```bash 
python3 adc_tp.py 2a -phase
```


## ¿Por que en ingles?

