Este archivo comenta como se realizo este proyecto.
Como es una aplicación sencilla y pequeña no es necesario crear la carpeta modules y se ingreso los datos y se genero desde un mod_consule.py que genere la base de datos y insert necesarios. Aqui esta el codigo fuente en como se fueron ingresando los datos, todas tienen que ir siendo ingresados separados en el sistema, pero termina siendo igual de rápido.
Otra forma es con el input de sqlite, tambien se puede exportar directamente con el script.

En este formato de archivo se ingresan y prueban los select, insert, create tables, para hacer update y tambien se utiliza como testing de la app.

El esquema del sistema es:
- db
-- views.py
-- wsgi.py
-- urls.py
-- settins.py
-- asgi.py
-- __init__.py
__ templates
___ frmVenta.html
___ index.html
___ venta.html
___ Verproductos


import sqlite3

con = sqlite3.connect('prueba2_django.db')
c = con.cursor()
c.execute ("""CREATE TABLE categoria (
	id number(3),
	nombre varchar(30) not null,
	constraint pk_categoria primary key(id)
);""")

con.commit()
con.close()

# check the database file
print (c)

c.execute (""" INSERT INTO categoria (id,nombre) values (11,'Dispositivo de entrada');
INSERT INTO categoria (id,nombre) values (12,'Almacenamiento');
INSERT INTO categoria (id,nombre) values (13,'Utilidades');
INSERT INTO categoria (id,nombre) values (14,'Multimedia'); """)

c.execute (""" CREATE TABLE producto ( 
	codigo number(4) constraint pk_producto primary key, 
	nombre varchar2(100) not null, 
	precio number(7), 
	stock number(5), 
	categoria number(3), 
	constraint chk_precio check (precio > 0),
	constraint fk_producto_categoria foreign key (categoria)
		references categoria(id)) """ )

c.execute (""" CREATE TABLE producto ( 
	codigo number(4) constraint pk_producto primary key, 
	nombre varchar2(100) not null, 
	precio number(7), 
	stock number(5), 
	categoria number(3), 
	constraint chk_precio check (precio > 0),
	constraint fk_producto_categoria foreign key (categoria)
		references categoria(id))""")

c.execute (""" INSERT INTO producto VALUES (1,'Mouse',3000,18,11);
INSERT INTO producto VALUES (2,'Teclado',5000,25,11);
INSERT INTO producto VALUES (3,'Pendrive 8GB',4000,10,12);
INSERT INTO producto VALUES (4,'HDD Externo 500GB',50000,6,12);
INSERT INTO producto VALUES (5,'Kit de limpieza',3000,20,13);
INSERT INTO producto VALUES (6,'Camara GoPro HD',12000,23,14)""")