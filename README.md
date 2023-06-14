# Python Projects

## Gestor de proyectos en python

### Descripción

Script escrito en python para gestionar proyectos desde la terminal, valido para Linux.

![img](/img/img.png)

### Instrucciones

**Listar proyectos** `project -l, --listar`

**Cambiar al directorio del proyecto** `project -d carpeta, --directorio carpeta`

**Abrir proyecto en VSCode** `project -v carpeta, --vscode carpeta`

**Crear nuevo proyecto** `project -c carpeta, --crear carpeta`

**Eliminar proyecto**: `project -e carpeta, --eliminar carpeta`

### Requisitos

- Para el correcto funcionamiento debe tener instalado Visual Studio Code, *instalación de tipo binario* `/usr/bin/code` de lo contrario debe modificar la instrucción dependiendo de si es flatpak o snap, en la linea 34:

`command = f"cd ~/Github/{folder} && code . && exec $SHELL"`

- Debe tener creada la carpeta $HOME/Github (/home/{user}/Github)
