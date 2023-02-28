from Funciones import *
db = Conectar("localhost","oscar","oscar","hola")

salir = False

while not salir:
    print("1. Listar administradores")
    print("2. Buscar Administrador por intervalos de Honorarios")
    print("3. Buscar Comunidad por Provincia")
    print("4. Mostrar el nombre de la comunidad que han tenido contrato con el Administrador X")
    print("5. Insertar nueva Comunidad")
    print("6. Borra los contratos y el colegido por su numero de identificacion ")
    print("7. Aumentar los honorarios del contrato de un Administrador con su numero de colegiado")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    
   

    if opcion == "1":
        administr = listar(db)
        if administr:
            for a in administr:
                print(a)
                
    
    elif opcion=="2":
        
        print("Introduce los Valores:")
        print("")
        valor_min=input("Minimo 1: ")
        valor_max=input("Maximo 900000: " )
        print("")
    
        buscar_m(db,valor_min, valor_max)
        
    elif opcion=="3":
        
        poblacion = input("Ingrese la población: ")

        comunidad =buscar(db,poblacion)

        if comunidad is not None:
                print("")
                print("-----------------------------------------------------------")
                print(f"La comunidad con población en {poblacion} es {comunidad}.")
                print("-----------------------------------------------------------")
                print("")
        else:
                print("")
                print("------------------------------------------------------")
                print(" No se encontró ninguna comunidad con esa población.")
                print("------------------------------------------------------")
                print("")

    
    elif opcion=="4":
        
        print("Introduce el DNI de un Administrador: ")
        print("")
        admi=input("DNI: ")
        print("")
    
        print("")
        Administrador_comunidad(db,admi)
        print("")

    elif opcion == "5":
        nuevo = {}
        print("")
        try:
            nuevo["C_Comunidad"] = input("Codigo de Comunidad: ")
            nuevo["Nombre"] = input("Nombre: ")
            nuevo["Calle"] = input("Calle: ")
            nuevo["Poblacion"] = input("Ciudad: ")
            nuevo["C_Postal"] = int(input("Codigo Postal: "))
        except:
            print("Error al ingresar datos. Por favor, inténtelo de nuevo.")
            continue
        print("")
        print("")
        Inserta_Comunidad(db, nuevo)
        print("")
        print("")

    elif opcion == "6":
        
        Num= input("Numero del Colegiado: ")

        borrar(db,Num)

    elif opcion == "7":
        
        Num= input("Porcentajes que deseas aumentar: ")
        a=input("Numero de Colegiado: ")

        Aumentar(db,Num,a)

    elif opcion == "8":
        salir = True
        print("")
        print("¡HASTA PRONTO!")