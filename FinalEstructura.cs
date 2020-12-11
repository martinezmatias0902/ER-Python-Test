using System;
using System.Collections;
using System.Text.RegularExpressions;
namespace EDDatosFinal
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            int opcion = 0;
            int loop = 0;
            Stack MiPatentes = new Stack();
            do
            {
                Console.Clear();
                Console.WriteLine("[0] Administrador de Patentes");
                Console.WriteLine("[1] Crear una pila de patentes, seleccione: 1 ");
                Console.WriteLine("[2] Borrar pila de patentes, seleccione: 2 ");
                Console.WriteLine("[3] Agregar Patente, seleccione: 3 ");
                Console.WriteLine("[4] Borrar Patente, seleccione: 4 ");
                Console.WriteLine("[5] Listar todas las patentes, seleccione: 5 ");
                Console.WriteLine("[6] Listar última patente, seleccione: 6 ");
                Console.WriteLine("[7] Listar primera patente, seleccione: 7 ");
                Console.WriteLine("[8] Consultar cantidad de patentes, seleccione: 8 ");
                Console.WriteLine("[9] Salir, seleccione: 9 ");
                opcion = int.Parse(Console.ReadLine());
                switch (opcion)
                {
                    case 1:
                        Console.Clear();
                        MiPatentes = new Stack();
                        Console.WriteLine("La pila fue creada con éxito, presione alguna tecla para continuar...");
                        Console.ReadKey();
                        break;
                    case 2:
                        Console.Clear();
                        MiPatentes.Clear();
                        Console.WriteLine("La pila fue borrada con éxito, presione alguna tecla para continuar...");
                        Console.ReadKey();
                        break;
                    case 3:
                        Console.Clear();
                        Console.WriteLine("Bienvenido al administrador de nuevas patentes");
                        Console.WriteLine("Las patentes deben seguir el siguiente formato: ");
                        Console.WriteLine("Debe contener 3 digitos entre la a-Z y 3 digitos entre 0-9");
                        Console.WriteLine("A continuación ingrese la nueva patente: ");
                        string patente = Console.ReadLine();
                        if (!Regex.IsMatch(patente, "^[a-z-A-Z]{3}[0-9]{3}$"))
                        {
                            Console.WriteLine("Patente incorrecta, respete el formato indicado porfavor.");
                        }
                        else
                        {
                            MiPatentes.Push(patente);
                            Console.WriteLine("La patente {0} fue agregada con éxito.", patente);
                        };
                        Console.ReadKey();
                        break;
                    case 4:
                        Console.Clear();
                        Console.WriteLine("Bienvenido al administrador de borrado de patentes");
                        MiPatentes.Pop();
                        loop = 0;
                        foreach (string patentes in MiPatentes)
                        {
                            loop++;
                            Console.WriteLine("Patentes disponibles:");
                            Console.WriteLine("{0} - {1}", loop, patentes);
                        }
                        Console.ReadKey();
                        break;
                    case 5:
                        Console.Clear();
                        Console.WriteLine("Bienvenido al administrador de listado de patentes");
                        Console.WriteLine("Las patentes guardadas en nuestro sistema son las siguientes:");
                        loop = 0;
                        foreach (string patentes in MiPatentes)
                        {
                            loop++;
                            Console.WriteLine("Patente número {0}", loop);
                            Console.WriteLine("{0} - {1}", loop, patentes);
                        }
                        Console.ReadKey();
                        break;
                    case 6:
                        Console.Clear();
                        Console.WriteLine("Bienvenido a la consulta de listado de última patente");
                        Object[] arr = MiPatentes.ToArray();
                        Console.WriteLine("La última Patente es {0}", arr[arr.Length - 1]);
                        Console.ReadKey();
                        break;
                    case 7:
                        Console.Clear();
                        Console.WriteLine("Bienvenido a la consulta de listado de la primera patente");
                        Console.WriteLine("La primer Patente es {0}", MiPatentes.Peek());
                        Console.ReadKey();
                        break;
                    case 8:
                        Console.Clear();
                        Console.WriteLine("La cantidad de Patentes Almacenadas es {0}", MiPatentes.Count);
                        Console.ReadKey();
                        break;
                    case 9:
                        Console.Clear();
                        Console.WriteLine("Gracias por utulizar nuestra app");
                        Environment.Exit(0);
                        break;
                }
            } while (opcion != 9);
        }
    }
}