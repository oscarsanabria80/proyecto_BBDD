import cx_Oracle

#Creamos primero el usuario

#CREATE USER orapyt IDENTIFIED BY 1234;
#GRANT CONNECT, RESOURCE TO orapyt;
#ALTER USER orapyt ACCOUNT UNLOCK;

#Establecer conexión con la base de datos
#dsn = XE o ORCL dependiendo de la version 
cnx = cx_Oracle.connect(user='orapyt', password='1234', dsn='localhost/xe')


cursor = cnx.cursor()

# Crear tabla Administrador
table_administrador = '''CREATE TABLE Administrador(
    NumColegiado  VARCHAR2(5),
    DNI           VARCHAR2(9),
    Nombre        VARCHAR2(15),
    Apellidos     VARCHAR2(40),
    constraint pk_DN PRIMARY KEY(DNI),
    constraint dniadmin CHECK(regexp_like(DNI,'^[0-9]{8}[A-Z]{1}$')))'''
    
cursor.execute(table_administrador)

# Crear tabla Comunidad
table_comunidad = '''CREATE TABLE Comunidad(
    C_Comunidad  VARCHAR2(10),
    Nombre        VARCHAR2(20),
    Calle         VARCHAR2(50),
    Poblacion     VARCHAR2(40),
    C_Postal  NUMBER(5),
    constraint pk_comu PRIMARY KEY(C_Comunidad),
    constraint poblacion_ok CHECK(Poblacion IN ('Sevilla','Cadiz','Huelva','Cordoba')))'''

cursor.execute(table_comunidad)

# Crear tabla Contrato
table_contrato = '''CREATE TABLE Contrato(
    C_Contrato VARCHAR2(6),
    DNI VARCHAR2(9),
    F_Inicio DATE,
    F_Final DATE,
    Honorarios NUMBER(5),
    C_Comunidad VARCHAR2(10),
    constraint pk_contr PRIMARY KEY(C_Contrato),
    constraint fk_admi FOREIGN KEY(DNI) REFERENCES Administrador(DNI),
    constraint fk_comunid FOREIGN KEY(C_Comunidad) REFERENCES Comunidad(C_Comunidad),
    constraint cod_correcto CHECK(regexp_like(C_Contrato,'^[a-zA-Z]{1}[0-9]{3}$')))'''

cursor.execute(table_contrato)

query1 ='''INSERT  INTO Administrador (NumColegiado,DNI,Nombre,Apellidos) VALUES ('356','20082233F','Jose','Sanabria Romero')'''
query2 ='''insert  into Administrador (NumColegiado,DNI,Nombre,Apellidos) VALUES ('258','20394532G','Carlos','Rodriguez Alvarez')'''
query3 ='''insert  into Administrador (NumColegiado,DNI,Nombre,Apellidos) VALUES ('245','45325642H','Javier','Rodriguez Perez')'''
query4 ='''insert  into Administrador (NumColegiado,DNI,Nombre,Apellidos) VALUES ('653','76587324J','Manuel','Boza Teran')'''

query5 = '''insert  into Comunidad (C_Comunidad,Nombre,Calle,Poblacion,C_Postal) VALUES ('FDSTGL','bartanl 5','Mendez Nuñez','Sevilla','41500')'''
query6 = '''insert  into Comunidad (C_Comunidad,Nombre,Calle,Poblacion,C_Postal) VALUES ('GFSWRG','bodegon 15','Castillo Espera','Cordoba','67543')'''
query7 = '''insert  into Comunidad (C_Comunidad,Nombre,Calle,Poblacion,C_Postal) VALUES ('HLFDWE','Galileo 8','Rodrigo','Cadiz','45634')'''
query8 = '''insert  into Comunidad (C_Comunidad,Nombre,Calle,Poblacion,C_Postal) VALUES ('FGRTHK','Costil 40','Paez teo','Huelva','76436')'''

query9 = '''insert  into Contrato (C_Contrato,DNI,F_Inicio,F_Final,Honorarios,C_Comunidad) VALUES ('F564','20082233F',TO_DATE('15/6/2018','DD/MM/YYYY'),TO_DATE('20/12/2020','DD/MM/YYYY'),50340,'FDSTGL')'''
query10 = '''insert into Contrato (C_Contrato,DNI,F_Inicio,F_Final,Honorarios,C_Comunidad) VALUES ('F543','20394532G',TO_DATE('25/12/2020','DD/MM/YYYY'),TO_DATE('22/12/2022','DD/MM/YYYY'),67845,'GFSWRG')'''
query11 = '''insert  into Contrato (C_Contrato,DNI,F_Inicio,F_Final,Honorarios,C_Comunidad) VALUES ('F354','45325642H',TO_DATE('16/6/2014','DD/MM/YYYY'),TO_DATE('20/12/2016','DD/MM/YYYY'),54567,'FDSTGL')'''

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