def agregar_ciudad(datos):
    datos = dict(datos)
    ciudad = {}
    
    ciudad["nombre"] = input("Ingrese el nombre de la Ciudad: ")
    ciudad["pais"] = input("Ingrese el nombre del pais en donde se encuentra la Ciudad: ")
    ciudad["codigo-postal"] = input("Ingrese el codigo postal de la Ciudad: ")
    ciudad["poblacion"] = input("Ingrese el numero aproximado de habitantes: ") + (" Personas")
    
    for ciudad_creada in datos["ciudades"]:
        if ciudad_creada == ciudad["nombre"]:
            print("La ciudad ya existe")
            return datos
        else:
            datos["ciudades"].append(ciudad)
            print("Ciudad Creada con exito!")
            return datos
        

        
def editar_ciudad(datos):
    
    for nombre_ciudad in datos["ciudades"]:
        print(nombre_ciudad["nombre"])
    
    busqueda = input("Ingrese el nombre de la ciudad que desea editar: ")
    
    for ciudad in datos["ciudades"]:
        if ciudad["nombre"] == busqueda:
            print("Ciudad encontrada!") 
            nuevo_nombre = input("Ingrese el nuevo nombre de la ciudad (Enter para dejar sin cambios): ")
            nuevo_pais = input("Ingrese el nuevo país de la ciudad (Enter para dejar sin cambios): ")
            nuevo_codigo = input("Ingrese el nuevo código postal de la ciudad (Enter para dejar sin cambios): ")
            habitantes = input("Ingrese el nuevo número de habitantes de la ciudad (Enter para dejar sin cambios): ")
            print("Ciudad editada con éxito!")
            if nuevo_nombre:
                ciudad["nombre"] = nuevo_nombre
            if nuevo_pais:
                ciudad["pais"] = nuevo_pais
            if nuevo_codigo:
                ciudad["codigo-postal"] = nuevo_codigo
            if habitantes:
                ciudad["poblacion"] = habitantes
            return datos
    
    print("Ciudad no encontrada")
    return datos

def ver_ciudades(datos):
    while True:
        opc = (input("¿Deseas filtrar la búsqueda por algo en específico? (1.Si / 2.No): "))
        if opc == "1":
            filtro = input("Ingrese el tipo de filtro (nombre, código postal o país): ")

            if filtro == "nombre":
                for ciudad in datos["ciudades"]:
                    print(ciudad["nombre"])
                ver_ciudad = input("Escoja el nombre de la ciudad que desea ver: ")
                for ciudad in datos["ciudades"]:
                    if ciudad["nombre"] == ver_ciudad:
                        print("Ciudad encontrada!")
                        print("Nombre:", ciudad["nombre"])
                        print("País:", ciudad["pais"])
                        print("Código postal:", ciudad["codigo-postal"])
                        print("Población:", ciudad["poblacion"])
                        return datos
                print("Ciudad no encontrada")
                return datos

            elif filtro == "codigo postal":
                for ciudad in datos["ciudades"]:
                    print(ciudad["codigo-postal"])
                ver_codigo = input("Escoja el código postal de la ciudad que desea ver: ")
                for ciudad in datos["ciudades"]:
                    if ciudad["codigo-postal"] == ver_codigo:
                        print("Ciudad encontrada!")
                        print("Nombre:", ciudad["nombre"])
                        print("País:", ciudad["pais"])
                        print("Código postal:", ciudad["codigo-postal"])
                        print("Población:", ciudad["poblacion"])
                        return datos
                print("Ciudad no encontrada")
                return datos

            elif filtro == "pais":
                for ciudad in datos["ciudades"]:
                    print(ciudad["pais"])
                ver_pais = input("Escoja el país de la ciudad que desea ver: ")
                for ciudad in datos["ciudades"]:
                    if ciudad["pais"] == ver_pais:
                        print("Si hay ciudades en este pais!")
                        print("Nombre:", ciudad["nombre"])
                        print("País:", ciudad["pais"])
                        print("Código postal:", ciudad["codigo-postal"])
                        print("Población:", ciudad["poblacion"])
                        return datos
                print("Ciudad no encontrada")
                return datos

            else:
                print("Opción de filtro no válida")
                return datos

        elif opc == "2":
            print("Listado de todas las ciudades:")
            for ciudad in datos["ciudades"]:
                print("Nombre:", ciudad["nombre"])
                print("País:", ciudad["pais"])
                print("Código postal:", ciudad["codigo-postal"])
                print("Población:", ciudad["poblacion"])
                print("-----------------------")
            return datos
        
        else:
            print("Opcion no valida")

                
                
    

            

    
        
    
    
