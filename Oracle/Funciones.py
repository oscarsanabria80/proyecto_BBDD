import sys
import cx_Oracle

def Conectar(user,password,dsn):
    try:
        db = cx_Oracle.connect(user,password,dsn)
        return db
    except cx_Oracle.Error as e:
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

    cursor.close()

def buscar_m(db,min_val, max_val):
    
    cursor = db.cursor()

    print("Búsqueda de contratos:")
    print("")
    query = "SELECT C_Contrato,DNI,Honorarios FROM Contrato WHERE Honorarios >= :min_val AND Honorarios <= :max_val"

    cursor.execute(query, min_val=min_val, max_val=max_val)

    resultados = cursor.fetchall()

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
    cursor.close()

def buscar (db,poblacion):
   
    cursor = db.cursor()

    query = "SELECT Nombre FROM Comunidad WHERE Poblacion = :poblacion"
    cursor.execute(query,{'poblacion': poblacion})

    result = cursor.fetchone()

    cursor.close()

    if result is not None:
        return result[0]
    else:
        return None
    
def Administrador_comunidad(db,DNI):
    cursor = db.cursor()

    print("Búsqueda de Administrador:")
    print("")
    query="select Nombre from Comunidad where C_Comunidad IN  (Select C_Comunidad from Contrato  Where DNI= :DNI)"

    cursor.execute(query, {'DNI': DNI})

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
    sql = "INSERT INTO Comunidad (C_Comunidad, Nombre, Calle, Poblacion, C_Postal) VALUES ( :1, :2, :3, :4,:5)"
    values = (nuevo["C_Comunidad"], nuevo["Nombre"], nuevo["Calle"], nuevo["Poblacion"], nuevo["C_Postal"])
    cursor.execute(sql, values)
    
    try:
        db.commit()
        print("")
        print("Insertado correctamente")
        print("")
    except:
        print("Error al insertar.")
        db.rollback()

def borrar(db, num):
    try:
        cursor = db.cursor()
        sql = "DELETE FROM Contrato WHERE DNI IN (SELECT DNI FROM Administrador WHERE NumColegiado = :num)"
        cursor.execute(sql, {'num': num})
        
        if cursor.rowcount == 0:
            print("No se encontraron registros relacionados en la tabla Contrato.")
        else:
            sql = "DELETE FROM Administrador WHERE NumColegiado = :num"
            cursor.execute(sql, {'num': num})
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

    try:
        porcentaje = int(porcentaje)
    except ValueError:
        print("El porcentaje no es un número válido.")
        return
    
    cursor = db.cursor()
    try:
       
        sql = "UPDATE Contrato SET Honorarios = Honorarios * :factor WHERE DNI IN (SELECT DNI FROM Administrador WHERE NumColegiado = :num)"
        cursor.execute(sql, {'factor': 1 + porcentaje/100, 'num': num_colegiado})
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
            
    except cx_Oracle.DatabaseError as e:

        print("Error al cambiar:", e)
        db.rollback()

