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
            
            #return lista
            new_datalist = []
            items_found = []
            for element in lista:
                if (not element in items_found):
                    # items_found acumula los dic que ya se analizaron para no repetirlos
                    items_found.append(element)
                    elem_count = lista.count(element) # Se cuentan los elementos
                    if elem_count > 1:
                        # Si hay mas de 1 repeticion, crear el diccionario nuevo
                        new_elem = {}
                        new_elem['text'] = element['text']
                        new_elem['type'] = element['type']
                        new_elem['cantidad'] = elem_count 
                        new_datalist.append(new_elem)
            print(new_datalist)

    except IOError:
        print("Ocurrio un error con el archivo, vuelva a intentarlo D:")


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