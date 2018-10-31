from flask import Flask, request, make_response
import mysql.connector
from usuario import Usuario 

conexion = mysql.connector.connect(user="dan",
						   password="12345",
						   database="invernadero")
cursor = conexion.cursor()						   

app = Flask(__name__)

@app.route("/home/")
def hello():
	respuesta = make_response("Hello World!")
	respuesta.headers.add('Access-Control-Allow-Origin','*')
	return respuesta

@app.route("/login/",methods=['GET'])
def login():
	#print(request.args)
	usuario = request.args.get('usuario')
	password = request.args.get('password')

	userDB = Usuario(conexion,cursor)
	print(userDB.login(usuario,password))

	print(usuario,password)
	return usuario + " " + password


app.run(debug=True)