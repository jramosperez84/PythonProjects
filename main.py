#!/usr/bin/env python3

import argparse
import os
import subprocess

def menu():
    print("\n[*] Gestor de proyectos\n")
    print("\t[-l] Listar proyectos\t\t"+"Uso: project.py -l")
    print("\t[-d] Abrir directorio\t\t"+"Uso: project.py -f nombre_de_proyecto")
    print("\t[-v] Abrir en VSCode\t\t"+"Uso: project.py -v nombre_de_proyecto")
    print("\t[-c] Crear proyecto\t\t"+"Uso: project.py -c nombre_de_proyecto")
    print("\t[-e] Eliminar proyecto\t\t"+"Uso: project.py -e nombre_de_proyecto\n")
    print("\t[-h] Menú de ayuda\t\t"+"Uso: project.py -h\n")

def list_projects():
    command = "ls -1 -d $HOME/Github/*/ | xargs -I {} basename {} | sort -f"
    output = os.popen(command).read()
    folder_string = output.split()
    print()
    print("- Lista de proyectos:\n")
    for folders in folder_string:
        print("\t[*] " + folders)
    print()

def open_folder(folder):
    command = f"cd ~/Github/{folder} && exec $SHELL"
    try:
        subprocess.run(command, shell=True)
    except FileNotFoundError:
        print("No existe el proyecto")

def open_code(folder):
    command = f"cd ~/Github/{folder} && code . && exec $SHELL"
    try:
        subprocess.run(command, shell=True)
    except FileNotFoundError:
        print("No existe el proyecto")

def delete_project(folder):
    command = f"rm -rf ~/Github/{folder} && exec $SHELL"
    try:
        subprocess.run(command, shell=True)
    except FileNotFoundError:
        print("No se pudo eliminar el proyecto")

def make_project(folder):
    git_init = "git init"
    git_branch = "git branch -M main"

    try:
        subprocess.run(f"mkdir ~/Github/{folder} && cd ~/Github/{folder} && {git_init} && {git_branch}", shell=True, check=True)
    except subprocess.CalledProcessError:
        print("No se pudo crear el proyecto")

def args_list():
    parser = argparse.ArgumentParser(description="Gestor de proyectos")
    parser.add_argument("-l", "--listar", action="store_true", help="Listar proyectos")
    parser.add_argument("-d", "--directorio", metavar="folder", help="Cambiar al directorio del proyecto")
    parser.add_argument("-v", "--vscode", metavar="folder", help="Abrir proyecto en VSCode")
    parser.add_argument("-c", "--crear", metavar="folder", help="Crear nuevo proyecto")
    parser.add_argument("-e", "--eliminar", metavar="folder", help="Eliminar proyecto")

    args, unknown_args = parser.parse_known_args()

    if unknown_args:
        menu()
    elif args.listar:
        list_projects()
    elif args.directorio:
        open_folder(args.directorio)
    elif args.vscode:
        open_code(args.vscode)
    elif args.crear:
        make_project(args.crear)
    elif args.eliminar:
        delete_project(args.eliminar)
    else:
        menu()

def main():
    args_list()

if __name__ == "__main__":
    main()

