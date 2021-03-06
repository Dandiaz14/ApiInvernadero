from flask import Flask, request, make_response, jsonify
import mysql.connector
from usuario import Usuario 
import usuarioinvernadero

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
	respuesta = make_response(str(userDB.login(usuario, password)))
	respuesta.headers.add('Access-Control-Allow-Origin','*')
	return respuesta
	#print(userDB.login(usuario,password))
	#print(usuario,password)
	#return usuario + " " + password
	
@app.route("/invernadero/",methods=['GET'])
def invernadero():
	usuario = request.args.get('usuario')
	password = request.args.get('password')

	#inv = Invernadero(conexion, cursor)

	resultado = usuarioinvernadero.apivergas(usuario,password)
	print(resultado)

	return jsonify(resultado)

app.run(debug=True)