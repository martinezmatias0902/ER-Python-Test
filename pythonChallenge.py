from io import open
import csv, os
import os.path

def contarDiasVacacionesTomados(lista):
    return {i:lista.count(i) for i in lista}

def ingresarEmpleados(archivo, campos):
    guardar = "si"
    empleados = []
    while guardar == "si":
        empleado = {}

        for campo in campos:
            empleado[campo] = input(f"Ingrese {campo} del empleado: ")
        empleados.append(empleado)
        guardar = input("Desea seguir agregando vendedores? Si/No: ")

    try:
        archivoExistente = os.path.isfile(archivo)
        with open(archivo, 'a', newline='') as file:
            guardarArchivo = csv.DictWriter(file, fieldnames=campos)

            if not archivoExistente:
                guardarArchivo.writeheader()

            guardarArchivo.writerows(empleados)
            print("Los datos se subieron con éxito... :D")
            return
    except IOError:
        print("Ocurrio un error con el archivo, vuelva a intentarlo D:")

def informeEmpleados(archivo):
    try:
        with open("vacacionesTomadas.csv", 'r', newline='') as file:
            linea = file.readline()
            diccionario = {}
            lista = []
            reader = csv.reader(file)
            for row in reader:
                listaProvisoria = row
                diccionarioProvisorio = {}
                diccionarioProvisorio["Legajo"] = listaProvisoria[0]
                diccionarioProvisorio["Fecha"] = listaProvisoria[1]
                lista.append(diccionarioProvisorio)
            
            """  resultado = contarDiasVacacionesTomados(lista)
            print(resultado) """
            print(lista)
            return lista

            """ while linea:
                linea = linea.rstrip('\n')
                campos = linea.split(',')
                diccionario["Legajo"] = campos[0]
                diccionario["Fecha"] = campos[1]
                lista.append(diccionario)
                linea = file.readline() """
   
            
            return diccionario
        
        """ with open(archivo,'r', newline='') as file:
            lectura_csv = csv.DictReader(file)
            campos = lectura_csv.fieldnames

            for linea in lectura_csv:
                print(f"# Empleado/a {linea[campos[1]]} {linea[campos[2]]} con legajo numero {linea[campos[0]]} tiene {linea[campos[3]]} dias de vacaciones.")
            return """
    except IOError:
        print("Ocurrio un error con el archivo")





# 7 a
def menuPrincipal():
    ARCHIVO = "LegajoEmpleados.csv"
    CAMPOS = ['Legajo', 'Apellido', 'Nombre', 'Total Vacaciones']

    while True:
        print("Elija una opcion: \n 1.Ingresar nuevos empleados \n 2.Informe de días de vacaciones disponibles \n 3.Salir")
        opcion = input("")

        if opcion == "3":
            exit()
        if opcion == "1":
            ingresarEmpleados(ARCHIVO, CAMPOS)
        if opcion == "2":
            informeEmpleados(ARCHIVO)
        else:
            print("Por favor elija una opcion valida :D")

menuPrincipal()