from msilib.schema import Class
import sqlite3
import random
from flask import Flask, render_template, Response, request, redirect, session, url_for

app = Flask(__name__)

app.secret_key = "hjdfbhasdasdjkashdkasd"

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/register")
def guardarnickname():
  return render_template('nickname.html')
  

@app.route("/ranking")
def ranking():
  
  conn = sqlite3.connect('ODS.db')

  q = f"""SELECT * from Ranking
          ORDER BY Puntaje DESC
          LIMIT 10"""
  x = conn.execute(q)
  conn.close()
  return render_template('ranking.html', lineamostrar = x)
  

@app.route("/ayuda")
def informacion():
  return render_template('ayuda.html')

@app.route("/game", methods=['POST', 'GET'])
def mostrar_juego():
  name = request.form['nombre']
  session['name'] = name
  session['puntos'] = 0

  print(name)
  conn = sqlite3.connect('ODS.db')
  if (name != ""):
    q = f"""INSERT INTO Ranking(Nombre, Puntaje) VALUES('{name}', 0)"""
    conn.execute(q)
    conn.commit()
    return render_template('juego.html')
  conn.close()

@app.route("/game/pregunta")
def mostrar_pregunta():
  hola = random.randint(1, 6)

  conn = sqlite3.connect('ODS.db')
  q = f"""SELECT Pregunta FROM Preguntas25 
          WHERE id_preguntas = {hola}"""
  for row in conn.execute(q):
    q2 = row[0]

  print(hola)
  return render_template('preguntas.html', pregunta = q2,respuesta1="Siu",respuesta2="Siuuuu")
  conn.close()

#def mostrar_pregunta50():
#  conn = sqlite3.connect('ODS.db')
#  x = f"""SELECT * FROM Preguntas50"""
#  return render_template('preguntas.html', pregunta = "HIOLA?",respuesta1="Siu",respuesta2="Siuuuu")

#def mostrar_pregunta100():
#  conn = sqlite3.connect('ODS.db')
#  v = f"""SELECT * FROM Preguntas100"""
#  return render_template('preguntas.html', pregunta = "HIOLA?",respuesta1="Siu",respuesta2="Siuuuu")

@app.route("/game/final")
def mostrar_final():
  return render_template('fin-juego.html')

app.run(host='0.0.0.0', port=81)