from datos import *
from modulo_ciudades import *

RUTA_CIUDADES = "ciudades.json"

def ejecutable ():
    while True:
        print('''
            *************MENÚ INICIAL************
            *********1.Registra tu ciudad********
            **********2.Edita tu ciudad***********
            ***********3.Ver ciudades *************
            *************0.salir *************'''
        )

        
        
        
        
        

        opc = (input("Escoja su opcion: "))
        if opc == "1":
            datosCiudades = bajar_datos(RUTA_CIUDADES)
            agregar_ciudad(datosCiudades)
            datosCiudades = subir_datos(datosCiudades,RUTA_CIUDADES)
        elif opc == "2":
            datosCiudades = bajar_datos(RUTA_CIUDADES)
            editar_ciudad(datosCiudades)
            datosCiudades = subir_datos(datosCiudades,RUTA_CIUDADES)
        elif opc == "3":
            datosCiudades = bajar_datos(RUTA_CIUDADES)
            ver_ciudades(datosCiudades)
            datosCiudades = subir_datos(datosCiudades,RUTA_CIUDADES)
        elif opc == "0":
            print("SALIENDO...")
            break
        else:
            print("opcion invalida")
            




