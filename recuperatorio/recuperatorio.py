#Recuperatorio Martinez Matias, IFTS 1° B

import csv
import os.path

def recuperatorio():

    def mainmenu():
        print("Bienvenido al portal de estados de los gastos de viáticos de empeados")
        CAMPOS = ['Legajo', 'Apellido', 'Nombre']
        ARCHIVOVIATICOS = "RegistroViaticos.csv"

        print("A continuación ingrese el nombre del archivo en el que desea trabajar")
        archivoUsuario = input("Nombre del archivo: ")
        
        print("Seleccione una opción para continuar: ")
        print("# 1 | Ingresar datos de nuevos empleados")
        print("# 2 | Consultar gastos en viaticos de un empleado")
        print("# 3 | Salir")

        userChoise = int(input("Seleccione opción 1, 2 o 3: "))

        while userChoise <= 0 or userChoise >= 4:
            print("*** A ingresado un dato incorrecto ***")
            userChoise = int(input("Porfavor seleccione opción 1, 2 o 3: "))
        

        while userChoise >=1 and userChoise <= 3:
            if userChoise == 1:
                print("Opcion 1")
                ingresarEmpleadosLegajo(archivoUsuario, CAMPOS)
                exit()
            elif userChoise == 2:
                print("Opcion 2")
                consultarLegajo(archivoUsuario, ARCHIVOVIATICOS)
                exit()
            else:
                print("¡Muchas gracias por confiar en nosotros!")
                exit()

    def datosEntrada(datos):
        seguir = "si"
        listaEmpleados = []
        while seguir =="si":
            trabajador = {}
            for campo in datos :
                if campo == "Legajo" or campo == "Gastos" :
                    while True:
                        trabajador[campo] = input(f"Ingrese {campo} del trabajador: ")
                        try:
                            trabajador[campo] = int(trabajador[campo])
                            break
                        except ValueError:
                            print("No es un numero entero.")
                else:
                    trabajador[campo] = input(f"Ingrese {campo} del trabajador: ")
            listaEmpleados.append(trabajador)
            seguir = input("Desea seguir? si/no: ")

        return listaEmpleados
            
    def ingresarEmpleadosLegajo(nombreArchivo, nuevosDatos):
        print("Bienvenido al Sistema para agregar nuevos usuarios al legajo de viáticos")
        try:
            archivo = os.path.isfile(nombreArchivo)
            if archivo:
                print(f"Usted a selecionado el archivo con el nombre: {nombreArchivo}")
                print("Seleccione una opción para continuar: ")
                print(f"# 1 | Modificar el archivo {nombreArchivo}")
                print(f"# 2 | Sobreescribir el archivo {nombreArchivo}")
                opcion = int(input("Ingrese opcion 1 o 2: "))

                if opcion == 1:
                    modoArchivo = 'a'
                    titulo = 'no'
                elif opcion == 2:
                    modoArchivo = 'w'
                    titulo = 'si'
                else:
                    print("Porfavor, seleccione una opcion valida :) ")
            else:
                modoArchivo = 'w'
                titulo = 'si'

            listaEmpleados = datosEntrada(nuevosDatos)

            with open(nombreArchivo, modoArchivo, newline='') as file:
                file_csv = csv.DictWriter(file, fieldnames = nuevosDatos)

            if titulo == 'si':
                file_csv.writeheader()

            file_csv.writerows(listaEmpleados)

            print("El archivo se guardo correctamente. ")

            return

        except IOError:
            print("Hubo un error con el archivo.")


    def consultarLegajo(archivoLegajos, archivoViaticos):
        if os.path.isfile(archivoLegajos) and os.path.isfile(archivoViaticos) == True:
            try:
                with open(archivoLegajos, 'r', newline='') as archivoDeLegajos,open (archivoViaticos, 'r', newline='') as archivoDeViaticos:
                    lecturaCsvLegajos = csv.DictReader(archivoDeLegajos, delimiter=';')

                    legajos = lecturaCsvLegajos.fieldnames

                    lecturaCsvViaticos = csv.DictReader(archivoDeViaticos, delimiter=';')

                    gastos = lecturaCsvViaticos.fieldnames

                    contador = 0  

                    ingreso_legajo= input("Numero de legajo del empleado: ")
                    for linea in lecturaCsvViaticos:
                        legajo = linea[gastos[0]]
                        if legajo == ingreso_legajo:
                            contador += int(linea[gastos[1]])
                        
                    for linea in lecturaCsvLegajos:
                        if contador < 5000:
                            print(f"Legajo : {linea[legajos[0]]} {linea[legajos[2]]} {linea[legajos[1]]}, gasto ${contador}.")
                        else:
                            print(f"Legajo : {linea[legajos[0]]} {linea[legajos[2]]} {linea[legajos[1]]}, gasto ${contador} y se ha pasado del presupuesto por ${contador-5000}")
                    
            except IOError:
                print("Hubo un error al abrir el archivo.")

    mainmenu()
recuperatorio()
                