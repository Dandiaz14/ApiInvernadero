from flask import Flask, request
import mysql.connector
from usuario import Usuario 

conexion = mysql.connector.connect(user="dan",
						   password="12345",
						   database="invernadero")
cursor = conexion.cursor()						   

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

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