#Esto hoja son puras difiniciones, todo el resto esta en menu.py
def load_file (file_name:str="Autos1",extension:str=".csv") -> list:
	lista = []
	file_name += extension
	file = open(file_name,"r")

	for count, line in enumerate(file):
		line = line.strip()
		aux = line.split(";")
		lista.append(aux)
	file.close()
	return lista
#Esto hoja son puras difiniciones, todo el resto esta en menu.py
def obtenerAutos (nombre_archivo:str="Autos1",tipo_lista:str="diccionario") -> list:
	lista = load_file(nombre_archivo)
	if (tipo_lista.lower() == "lista"):
		return lista
	
	lista_autos = []
	for elemento in lista:
		aux = {
			"modelo":elemento[1],
			"marca":elemento[0],
			"año":int(elemento[2]),
			"patente":elemento[3],
			"color":elemento[4]
		}
		lista_autos.append(aux)
	return lista_autos
#Esto hoja son puras difiniciones, todo el resto esta en menu.py
def validar_seleccion (sel, lista:list) -> bool:
	if (str(sel).isnumeric()):
		if (int(sel) in range(len(lista)+1)):
			return True
	return False
#Esto hoja son puras difiniciones, todo el resto esta en menu.py
def mostrar_menu():
    print("=== MENÚ ===")
    print("Que opcion desea realizar.")
    print("Opcion 1","Buscar un auto por Modelo/Marca"),
    print("Opción 2","Mostrar la lista de autos escrita"),
    print("Opción 3","Imprimir certificado"),
    print("Opción 4","Buscar un auto por una patente."),
    print("Opción 5","Buscar un auto entre los años ingresados."),
    print("Opción 6","Registrar un auto a su nombre"),
    print("Opción 7","Mostrar los autos relacionados a su color favorito"),
    print("Opcion 8","Salir del programa."),
#Esto hoja son puras difiniciones, todo el resto esta en menu.py
def obtener_opcion():
    while True:
        opcion = input("\nSelecciona una opción: ")
        if opcion.isdigit() and int(opcion) in range(10):
            return int(opcion)
        print("Opción inválida, porfavor ingresa un numero del 1 a la 8")
#Esto hoja son puras difiniciones, todo el resto esta en menu.py
def filtrar_autos(lista_autos, filtro):
    resultados = []
    for auto in lista_autos:
        if auto.get('modelo') == filtro or auto.get('marca') == filtro:
            resultados.append(auto)
    return resultados
#Esto hoja son puras difiniciones, todo el resto esta en menu.py
def filtrar_autos2(lista_autos, atributo, valor):
    resultados = []
    for auto in lista_autos:
        if str(auto.get(atributo)) == valor:
            resultados.append(auto)
    return resultados
#Esto hoja son puras difiniciones, todo el resto esta en menu.py
def filtrar_autos3(lista_autos, atributo, valor):
    resultados = []
    for auto in lista_autos:
        if str(auto.get(atributo)) == valor:
            resultados.append(auto)
    return resultados
#Esto hoja son puras difiniciones, todo el resto esta en menu.py
def filtrar_autos4(lista_autos, filtro):
    resultados = []
    for auto in lista_autos:
        if auto.get('patente') == filtro:
            resultados.append(auto)
    return resultados
#Esto hoja son puras difiniciones, todo el resto esta en menu.py
def filtrar_autos5(lista_autos, filtro):
    resultados = []
    for auto in lista_autos:
        if auto.get('año') == filtro:
            resultados.append(auto)
    return resultados
#Esto hoja son puras difiniciones, todo el resto esta en menu.py
def filtrar_autos6(lista_autos, atributo, valor):
    resultados = []
    for auto in lista_autos:
        if str(auto.get(atributo)) == valor:
            resultados.append(auto)
    return resultados
#Esto hoja son puras difiniciones, todo el resto esta en menu.py
def mostrarAutosPorColorFavorito():
            autos_color_favorito = []
            for auto in autos:
                if auto["color"].lower() == color_favorito.lower():
                    autos_color_favorito.append(auto)
#------NO CAMBIAR ---------
from autoHerramientas import *
#---------------------------
#puede cargar cualquier archivo cambiando este parametro
nombre_archivo = "Autos1"

#puede cambiar la forma de la lista entre:
#lista de diccionario -> tipo_lista = "diccionario"
#lista de listas -> tipo_lista = "lista"
tipo_lista = "diccionario"

lista_autos = obtenerAutos(nombre_archivo,tipo_lista)