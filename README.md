### Hexlet tests and linter status:
[![Maintainability](https://qlty.sh/gh/mauricio23/projects/python-project-174/maintainability.svg)](https://qlty.sh/gh/mauricio23/projects/python-project-174)

[![Actions Status](https://github.com/mauricio23/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/mauricio23/python-project-174/actions)

[![hexlet-check](https://github.com/mauricio23/python-project-174/actions/workflows/hexlet-check.yml/badge.svg?event=push)](https://github.com/mauricio23/python-project-174/actions/workflows/hexlet-check.yml)

Descripción

Este proyecto emplea los distintos temas vistos durante el segundo módulo, como las estructuras anidadas, el manejo de archivos y la serialización y como utilizamos el tema de la recursividad, ademas tiene un manejo complejo sobre diccionarios y conjuntos que nos ayuda a realizar la separacion de archivos.

analizar que tipo de archivo es y extraer su contenido
la herramienta debe mirar que cambio entre dos archivos JSON y YAML, que se elimino, agrego o modifico

Requisitos minimos

Procesador: Doble núcleo
RAM: 4 GB
Almacenamiento: 5 GB de espacio libre en disco para la instalación y proyectos

instrucciones para ejecutar el codigo

python3 -m venv venv source venv/bin/ activate pip install -e . (ejecutar el codigo que quieras)

grabaciones ascinema

1. comparacion de archivos = https://asciinema.org/a/79Jsk4RZH1NV46ZJ
2. formato stylish con archivos json = https://asciinema.org/a/FkslCiEZRjOCGYH1
3. formato stylish con archivos yaml =  https://asciinema.org/a/bqigDF0bSerny2wK
4. formato plain con json = https://asciinema.org/a/m6tkhAzfNTMZmatT
5. formato plain con yaml = https://asciinema.org/a/13MRwJUS3V12Tndl

INSTALACION

1. https://github.com/mauricio23/python-project-174.git
2. python gendiff/scripts/gendiff.py file1.json file2.json
2.1 python -m  gendiff.scripts.gendiff .\tests\archivos\file1.yaml .\tests\archivos\file2.yml 
3. linea para comaparar archivos yml 
python gendiff/scripts/gendiff.py file1.yml file2.yml  
4. instruccion para wsl python3 -m  gendiff.scripts.gendiff tests/archivos/file1.yaml tests/archivos/file2.yml