import csv
import os.path

def recuperatorio():
    def mainmenu():
        print("Bienvenido al portal de de Control de Prestaciones")
        CAMPOS = ['Beneficiario','Total','Auditoria']
        ARCHIVO = "prestaciones.csv"
        print("A continuación ingrese el nombre del archivo en el que desea trabajar")
        archivoUsuario = input("Nombre del archivo: ") + ".csv"

        print("Seleccione una opción para continuar: ")
        print("# 1 | Decodificar datos del archivo elegido")
        print("# 3 | Salir")

        userChoise = int(input("Seleccione opción 1, 2 o 3: "))

        while userChoise <= 0 or userChoise >= 4:
            print("*** A ingresado un dato incorrecto ***")
            userChoise = int(input("Porfavor seleccione opción 1, 2 o 3: "))
        

        while userChoise >=1 and userChoise <= 3:
            if userChoise == 1:
                decodificarCSV(archivoUsuario, CAMPOS)
                exit()
            else:
                print("¡Muchas gracias por confiar en nosotros!")
                exit()

    def decodificarCSV(archivoUsuario, campos):
      
        try:
            with open(archivoUsuario, 'r+', newline='') as file:
                with open("temporal.csv", 'w', newline='') as fileTwo:
                    writer = csv.DictWriter(fileTwo, fieldnames=campos)
                    writer.writeheader()
                    
                    for linea in file:
                        linea = linea.replace("?", "")
                        linea = linea.replace("%20%", " ")
                        print(linea)
                        linea = linea.rstrip()
                        newLine = linea.split(',')
                        writer.writerow({'Beneficiario': newLine[0], 'Total': newLine[1], 'Auditoria': newLine[2]})
                    parte2()
                    return 

        except IOError:
            print("Ocurrio un error con el archivo")

    def parte2():
        
        try:
           
            with open("temporal.csv", 'r', newline='') as archivoDatos:
                lectura = csv.DictReader(archivoDatos)
                contador = 0
                
                for linea in lectura:
                    
                    print(linea)

        except IOError:
            print("Ocurrio un error al guardar el archivo")
    mainmenu()
recuperatorio()