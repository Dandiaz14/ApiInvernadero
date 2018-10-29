import hashlib

class Usuario:
	def __init__(self, conexion, cursor):
		self.conexion = conexion
		self.cursor = cursor

	def crear(self, usuario, contra, tipo):
		insertar = ("INSERT INTO usuario(correo,password,tipo) VALUES(%s,%s,%s)")
		h = hashlib.new('sha256',bytes(contra, 'utf-8'))
		h = h.hexdigest()
		self.cursor.execute(insertar,(usuario, h, tipo))
		self.conexion.commit()

	def login(self, usuario, contra):
		select = ("SELECT * FROM usuario WHERE correo = %s AND password = %s")
		h = hashlib.new('sha256',bytes(contra, 'utf-8'))
		h = h.hexdigest()
		self.cursor.execute(select,(usuario, h))

		resultado = self.cursor.fetchall()

		if resultado:
			return True
		else:
			return False