import mysql.connector
import hashlib
import getpass
#from invernadero import Invernadero

conexion = mysql.connector.connect(user='dan',password='12345',database='invernadero')
cursor = conexion.cursor()

#usuario = input("Correo: ")
#contra = input("Password: ")
def apivergas(usuario, password):
	invernaderos = []

	select = ("SELECT * FROM usuario WHERE correo = %s AND password = %s")
	h = hashlib.new('sha256',bytes(password, 'utf-8'))
	h = h.hexdigest()
	cursor.execute(select,(usuario, h))

	resultado = cursor.fetchall()
	for row in resultado:
		code = row[0]
		break

	if resultado:
		cursor.execute("SELECT * FROM usuarioinvernadero WHERE id_usuario = %s;", (code,))
		rows = cursor.fetchall()
		for row in rows:
			cursor.execute("SELECT * FROM invernadero WHERE id = %s;", (row[1],))
			invern = cursor.fetchone()
			#inv_object = self.cursor.fetchone()
			inv_object = invern
			inv = {
				'id': inv_object[0],
				'nombre': inv_object[1],
				'ubicacion' : inv_object[2],
				'id_dueno' : inv_object[3]
			}
			invernaderos.append(inv)
		return invernaderos
	else:
		print ("Usuario/Contraseña Incorrectos")
