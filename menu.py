from prueba import load_file
from prueba import obtenerAutos
from prueba import mostrar_menu
from prueba import obtener_opcion
from prueba import filtrar_autos
from prueba import filtrar_autos2
from prueba import filtrar_autos3
from prueba import filtrar_autos4
from prueba import filtrar_autos5
from prueba import filtrar_autos6
autos = obtenerAutos()
palabras_validas = ["Agua", "Albaricoque", "Almendra", "Amaranto", "Amarillo", "Amatista", "Ámbar", "Anaranjado", "Avellana", "Azabache", "Azul", "Beige", "Bermejo", "Blanco", "Bronce", "Café", "Canela", "Caqui", "Caramelo", "Carbón", "Carmesí", "Carmín", "Carne", "Castaño", "Celeste", "Cereza", "Champán", "Chocolate", "Cian", "Ciruela", "Cobre", "Coral", "Crema", "Damasco", "Dorado","Morado", "Durazno", "Esmeralda", "Frambuesa", "Fucsia", "Grana", "Gris", "Guinda", "Hueso", "Humo", "Índigo", "Jazmín", "Jade", "Kaki", "Kiwi", "Lavanda", "Lila", "Lima", "Magenta", "Malva", "Mamey", "Marfil", "Marrón", "Melocotón", "Melón", "Menta", "Miel", "Mostaza", "Naranja", "Negro", "Níquel", "Ocre", "Oro", "Oliva", "Pardo", "Pistacho", "Plata", "Platino", "Plomo", "Púrpura", "Rojo", "Rosa", "Rubí", "Salmón", "Turquesa", "Uva", "Vainilla", "Verde", "Vinotinto", "Violeta", "Zafiro"]
palabras_validas2 = ["modelo", "marca", "año", "patente", "color"]
#-------------------------------------------------------------------------------------------------
nombre_usuario = input("Ingrese su nombre de usuario:")
fecha_actual = input("Ingrese la fecha actual:")
while True:
    color_favorito = input("Ingrese su color favorito de auto:")
    if color_favorito in palabras_validas:
        break
    else:
        print("Ingrese la palabra bien o escriba un color que exista.")
#-------------------------------------------------------------------------------------------------
while True:
    mostrar_menu()
    opcion = obtener_opcion()
#-------------------------------------------------------------------------------------------------
    if opcion == 0:
        print("Ingrese una opcion del 1 al 8.")
#-------------------------------------------------------------------------------------------------
    if opcion == 1:
        while True:
            filtro = input("Ingrese el modelo o marca a buscar:")
            resultados_filtro = filtrar_autos(autos, filtro)
            if resultados_filtro:
                print("Resultados de la busqueda:")
                for resultado in resultados_filtro:
                    print(resultado)
                break
            else:
                print("Escribalo correctamente(Con mayusculas o minusculas) o ah ocurrido algun error.")
        input("Aprete enter para volver al menu.")
#-------------------------------------------------------------------------------------------------
    if opcion == 2:
        while True:
            llave_filtro = input("Ingrese la llave para filtrar. (modelo, marca, año, patente, color):").lower()
            if llave_filtro in palabras_validas2:
                break
            else:
                print("Reingrese la palabra.")
        while True:
            parametro_filtro = input("Ingrese el parámetro para mostrar los autos disponibles con ese parametro:")
            resultados_filtro = filtrar_autos2(autos, llave_filtro, parametro_filtro)
            if resultados_filtro:
                print("Resultados de la busqueda:")
                for resultado in resultados_filtro:
                    print(resultado)
                break
            else:
                print("Reingrese la palabra.")
        input("Aprete enter para volver al menu.")
#-------------------------------------------------------------------------------------------------
    if opcion == 3:
            while True:
                llave_filtro = input("Ingrese la llave para filtrar. (modelo, marca, año, color):").lower()
                if llave_filtro in palabras_validas2:
                    break
                else:
                    print("Reingrese la palabra.")
            while True:
                parametro_filtro = input("Ingrese el parámetro para mostrar los autos disponibles con ese parametro:")
                resultados_filtro = filtrar_autos3(autos, llave_filtro, parametro_filtro)         
                if resultados_filtro:
                    print("Resultado:")
                    for i, resultado in enumerate(resultados_filtro):
                        print(f"{i+1}. {resultado}")                       
                    opcion_automovil = int(input("Ingrese el número del automóvil deseado: "))
                    if opcion_automovil >= 1 and opcion_automovil <= len(resultados_filtro):
                        auto_seleccionado = resultados_filtro[opcion_automovil - 1]
                        print(f"\n{nombre_usuario} emite certificado que:")
                        print(f"El vehículo {auto_seleccionado['marca']} {auto_seleccionado['modelo']} con patente {auto_seleccionado['patente']}")
                        print(f"De color {auto_seleccionado['color']}")
                        print(f"Queda registrado oficialmente a la fecha de {fecha_actual}")
                    else:
                        print("Numero no reconocido, ingrese un numero de los autos mostrados.")
                    break
            input("\nAprete enter para volver al menu.")
#-------------------------------------------------------------------------------------------------
    if opcion == 4:
        filtro = input("Ingrese la patente:")
        resultados_filtro = filtrar_autos4(autos, filtro)
        if resultados_filtro:
            print("Resultados de la busqueda:")
            for resultado in resultados_filtro:
                print(resultado)
        else:
            print("Escriba correctamente la patente o no se encuentra en la lista.")
        input("Aprete enter para volver al menu.")
#-------------------------------------------------------------------------------------------------
    if opcion == 5:
        def buscarPorRango():
            autos = obtenerAutos()
            rango_inicio = int(input("\nIngrese el primer año(Tiene que ser el año menor):"))
            rango_final = int(input("Ingrese el segundo año(Tiene que ser el año mayor):"))

            autos_en_rango = []
            for auto in autos:
                if rango_inicio <= auto["año"] <= rango_final: 
                    autos_en_rango.append(auto)

            print("\nLos autos creados entre los años ingresados:")
            for auto in autos_en_rango:
                print(f"Marca: {auto['marca']}, Modelo: {auto['modelo']}, Año: {auto['año']}")
        buscarPorRango()
        input("Aprete enter para volver al menu.")
#-------------------------------------------------------------------------------------------------
    if opcion == 6:
        while True:
            llave_filtro = input("Ingrese la llave para filtrar. (modelo, marca, año, patente, color):").lower()
            if llave_filtro in palabras_validas2:
                break
            else:
                print("Reingrese la palabra.")
        parametro_filtro = input("\nIngrese el parámetro para mostrar los autos disponibles con ese parametro:")
        resultados_filtro = filtrar_autos6(autos, llave_filtro, parametro_filtro)
        if resultados_filtro:
            print("\nResultados del filtro:")
            for i, resultado in enumerate(resultados_filtro):
                print(f"{i+1}. {resultado}")
            opcion_automovil = int(input("\nIngrese el número del automóvil deseado: "))
            if opcion_automovil >= 1 and opcion_automovil <= len(resultados_filtro):
                auto_seleccionado = resultados_filtro[opcion_automovil - 1]
                print(f"\nEl vehículo {auto_seleccionado['marca']} {auto_seleccionado['modelo']} con patente {auto_seleccionado['patente']} queda registrado al nombre de {nombre_usuario}")
            else:
                print("Numero no reconocido, ingrese un numero de los autos mostrados.")
        else:
            print("No se encontraron resultados según el filtro.")
        input("Aprete enter para volver al menu.")
#-------------------------------------------------------------------------------------------------
    if opcion == 7:
        def mostrarAutosPorColorFavorito():
            autos_color_favorito = []
            for auto in autos:
                if auto["color"].lower() == color_favorito.lower():
                    autos_color_favorito.append(auto)

            if len(autos_color_favorito) == 0:
                print("No se encontraron automóviles del color favorito ingresado.")
            else:
                print(f"Automóviles de su color favorito '{color_favorito}':")
                for auto in autos_color_favorito:
                    print(f"Marca: {auto['marca']}, Modelo: {auto['modelo']}, Año: {auto['año']}, Patente: {auto['patente']}")
        mostrarAutosPorColorFavorito()            
        input("Aprete enter para volver al menu.")
#-------------------------------------------------------------------------------------------------
    if opcion == 8:
        print("Saliendo del programa...")
        break
    print() 
#---------------------------------------------------------------------------------------------------