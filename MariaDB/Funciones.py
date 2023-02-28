import sys
import MySQLdb
from tabulate import tabulate

def Conectar(host,usuario,password,nombrebd):
    try:
        db = MySQLdb.connect(host,usuario,password,nombrebd)
        return db
    except MySQLdb.Error as e:
        print("No puedo conectar a la base de datos:",e)
        sys.exit(1)

def Desconectar_BD(db):
    db.close()

def listar(db):
    
    cursor = db.cursor()

    query = "SELECT * FROM Administrador"
    cursor.execute(query)

    admini = cursor.fetchall()
    print("")
    print("")
    print("ID\t\tNombre\t\tApellido\tDNI")
    print("-----------------------------------------------------------")
    for row in admini:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
        print("")
        print("")

    cursor.close()

def buscar (db,poblacion):
    
    cursor = db.cursor()

    query = "SELECT Nombre FROM Comunidad WHERE Poblacion = %s"
    cursor.execute(query, (poblacion,))

    result = cursor.fetchone()

    cursor.close()


    if result is not None:
        return result[0]
    else:
        return None

        

def buscar_m(db,min_val, max_val):
    
    cursor = db.cursor()

    print("Búsqueda de contratos:")
    print("")
    query = "SELECT C_Contrato,DNI,Honorarios FROM Contrato WHERE Honorarios >= %s AND Honorarios <= %s"

    cursor.execute(query, (min_val, max_val))

    resultados = cursor.fetchall()

    cursor.close()

    resultadoss= False

    for row in resultados:
        resultadoss = True
        print("Contrato\t\tDNI\t\tHonorarios")
        print("-----------------------------------------------------------")
        print(f"{row[0]}\t{row[1]}\t{row[2]}")
        print("")
        print("")
    
    if not resultadoss:
        print("No se encontraron resultados")
        print("")
        print("")

def Administrador_comunidad(db,DNI):
    cursor = db.cursor()

    print("Búsqueda de Administrador:")
    print("")
    query="select Nombre from Comunidad where C_Comunidad IN  (Select C_Comunidad from Contrato  Where DNI= %s)"

    cursor.execute(query, (DNI,))

    resultados = cursor.fetchall()

    cursor.close()
    
    resultados_encontrados = False
    for t in resultados:
        resultados_encontrados = True
        print("Comunidad")
        print("---------")
        print(f"{t[0]}")
        print("")
        print("")
    if not resultados_encontrados:
        print("")
        print("-------------------------------------------------")
        print("Este Administrador no tiene Contratos o no Existe")
        print("-------------------------------------------------")
        print("")

def Inserta_Comunidad(db, nuevo):
    cursor = db.cursor()
    print("Insertar nuevos registros en Comunidad: ")
    print("")
    sql = "INSERT INTO Comunidad (C_Comunidad, Nombre, Calle, Poblacion, C_Postal) VALUES (%s, %s, %s, %s, %s)"
    values = (nuevo["C_Comunidad"], nuevo["Nombre"], nuevo["Calle"], nuevo["Poblacion"], nuevo["C_Postal"])
    cursor.execute(sql, values)
    
    try:
        db.commit()
        print("")
        print("Insertado correctamente")
        print("")
    except:
        print("")
        print("Error al insertar.")
        print("")
        db.rollback()

def borrar(db, num):
    sql = "DELETE FROM Contrato WHERE DNI IN (SELECT DNI FROM Administrador WHERE NumColegiado = %s)"
    cursor = db.cursor()

    try:
        cursor.execute(sql, (num))
        if cursor.rowcount == 0:
            print("No se encontraron registros relacionados en la tabla Contrato.")
        else:
            sql = "DELETE FROM Administrador WHERE NumColegiado = %s"
            cursor.execute(sql, (num,))
            db.commit()
            print("")
            print(f"Se borró los contratos y el administrador con NumColegiado '{num}'.")
            print("")
    except:
        print("")
        print("Error al borrar el administrador.")
        print("")
        db.rollback()

def Aumentar(db, porcentaje, num_colegiado):
    sql = f"UPDATE Contrato SET Honorarios = Honorarios * '{1 + int(porcentaje)/100}' WHERE DNI IN (SELECT DNI FROM Administrador WHERE NumColegiado = '{num_colegiado}')"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        if cursor.rowcount == 0:
            print("")
            print("-----------------------------------------------------------")
            print("No se encontró un administrador con ese número de colegiado")
            print("-----------------------------------------------------------")
            print("")
        else:
            print("")
            print("------------------------------------------------")
            print(f"Se han actualizado {cursor.rowcount} contratos.")
            print("------------------------------------------------")
            print("")
    except:
        print("Error al cambiar")
        db.rollback()