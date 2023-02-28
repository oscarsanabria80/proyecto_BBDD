import mysql.connector

#Creamos primero la base de datos

#Create Database mapyt

# Establecer conexión con la base de datos
cnx = mysql.connector.connect(
    user='oscar',
    password='oscar',
    host='localhost',
    database='mapyt'
)

cursor = cnx.cursor()

# Crear tabla Administrador
table_administrador = (
    "CREATE TABLE IF NOT EXISTS Administrador("
    "NumColegiado  VARCHAR(5),"
    "DNI           VARCHAR(9),"
    "Nombre        VARCHAR(15),"
    "Apellidos     VARCHAR(40),"
    "constraint pk_DN PRIMARY KEY(DNI),"
    "constraint dniadmin CHECK(DNI rlike '^[0-9]{8}[A-Z]{1}$')"
    ");"
)
cursor.execute(table_administrador)

# Crear tabla Comunidad
table_comunidad = (
    "CREATE TABLE IF NOT EXISTS Comunidad("
    "C_Comunidad  VARCHAR(10),"
    "Nombre        VARCHAR(20),"
    "Calle         VARCHAR(50),"
    "Poblacion     VARCHAR(40),"
    "C_Postal  INT(5),"
    "constraint pk_comu PRIMARY KEY(C_Comunidad),"
    "constraint poblacion_ok CHECK(Poblacion IN ('Sevilla','Cadiz','Huelva','Cordoba'))"
    ");"
)
cursor.execute(table_comunidad)

# Crear tabla Contrato
table_contrato = (
    "CREATE TABLE IF NOT EXISTS Contrato("
    "C_Contrato   VARCHAR(6),"
    "DNI           VARCHAR(9),"
    "F_Inicio        DATE,"
    "F_Final         DATE,"
    "Honorarios  INT(5),"
    "C_Comunidad       VARCHAR(10),"
    "constraint pk_contr PRIMARY KEY(C_Contrato),"
    "constraint fk_admi FOREIGN KEY(DNI) REFERENCES Administrador(DNI),"
    "constraint fk_comunid FOREIGN KEY(C_Comunidad) REFERENCES Comunidad(C_Comunidad),"
    "constraint cod_correcto CHECK(C_Contrato rlike '^[a-zA-Z]{1}[0-9]{3}$')"
    ");"
)
cursor.execute(table_contrato)


    # Ejecutar los insert
query1 = ("insert IGNORE into Administrador VALUES ('356','20082233F','Jose','Sanabria Romero');")
query2 = ("insert IGNORE into Administrador VALUES ('258','20394532G','Carlos','Rodriguez Alvarez');")
query3 = ("insert IGNORE into Administrador VALUES ('245','45325642H','Javier','Rodriguez Perez');")
query4 = ("insert IGNORE into Administrador VALUES ('653','76587324J','Manuel','Boza Teran');")

query5 = ("insert IGNORE into Comunidad (C_Comunidad,Nombre,Calle,Poblacion,C_Postal) VALUES ('FDSTGL','bartanl 5','Mendez Nuñez','Sevilla','41500');")
query6 = ("insert IGNORE into Comunidad (C_Comunidad,Nombre,Calle,Poblacion,C_Postal) VALUES ('GFSWRG','bodegon 15','Castillo Espera','Cordoba','67543');")
query7 = ("insert IGNORE into Comunidad (C_Comunidad,Nombre,Calle,Poblacion,C_Postal) VALUES ('HLFDWE','Galileo 8','Rodrigo','Cadiz','45634');")
query8 = ("insert IGNORE into Comunidad (C_Comunidad,Nombre,Calle,Poblacion,C_Postal) VALUES ('FGRTHK','Costil 40','Paez teo','Huelva','76436');")

query9 = ("insert IGNORE into Contrato (C_Contrato,DNI,F_Inicio,F_Final,Honorarios,C_Comunidad) VALUES ('F564','20082233F',STR_TO_DATE('15/6/2018','%d/%m/%Y'),STR_TO_DATE('20/12/2020','%d/%m/%Y'),50340,'FDSTGL');")
query10 = ("insert IGNORE into Contrato (C_Contrato,DNI,F_Inicio,F_Final,Honorarios,C_Comunidad) VALUES ('F543','20394532G',STR_TO_DATE('25/12/2020','%d/%m/%Y'),STR_TO_DATE('22/12/2022','%d/%m/%Y'),67845,'GFSWRG');")
query11 = ("insert IGNORE into Contrato (C_Contrato,DNI,F_Inicio,F_Final,Honorarios,C_Comunidad) VALUES ('F354','45325642H',STR_TO_DATE('16/6/2014','%d/%m/%Y'),STR_TO_DATE('20/12/2016','%d/%m/%Y'),54567,'FDSTGL');")

cursor.execute(query1)
cursor.execute(query2)
cursor.execute(query3)
cursor.execute(query4)
cursor.execute(query5)
cursor.execute(query6)
cursor.execute(query7)
cursor.execute(query8)
cursor.execute(query9)
cursor.execute(query10)
cursor.execute(query11)

cnx.commit()

# Cerrar el cursor y la conexión
cursor.close()
cnx.close()