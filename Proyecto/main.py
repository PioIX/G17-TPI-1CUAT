from msilib.schema import Class
import sqlite3
import random
from flask import Flask, render_template, Response, request, redirect, session, url_for, jsonify

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
  session['preguntas25'] = []
  session['preguntas50'] = []
  session['preguntas100'] = []

  print(name)
  conn = sqlite3.connect('ODS.db')
  if (name != ""):
    q = f"""INSERT INTO Ranking(Nombre, Puntaje) VALUES('{name}', 0)"""
    conn.execute(q)
    conn.commit()
    return render_template('juego.html')
  conn.close()

@app.route("/puntos", methods=['POST', 'GET'])
def guardar_puntaje():
  z = request.get_json()
  print(z)
  return render_template('juego.html')
  

@app.route("/game/pregunta")
def mostrar_pregunta25():
  hola = random.randint(1, 6)
  while(hola in session['preguntas25']):
    hola = random.randint(1, 6)
  session['preguntas25'].append(hola)
  
  conn = sqlite3.connect('ODS.db')
  q = f"""SELECT * FROM Preguntas25 
          WHERE id_preguntas = {hola}"""
  for row in conn.execute(q):
    q2 = row[1]
    q3 = row[2]
    q4 = row[3]
    q5 = row[4]
    q6 = row[5]
    
  session['respuestas'] = []
  session['respuestas'].append(q3)
  session['respuestas'].append(q4)
  session['respuestas'].append(q5)
  session['respuestas'].append(q6)
  q7 = random.sample(session['respuestas'], len(session['respuestas']))  
  return render_template('preguntas.html', pregunta = q2, respuesta1=q7[0], respuesta2=q7[1], respuesta3=q7[2], respuesta4=q7[3])
  conn.close()

@app.route("/game/pregunta")
def mostrar_pregunta50():
  hola = random.randint(1, 6)
  while(hola in session['preguntas50']):
    hola = random.randint(1, 6)
  session['preguntas50'].append(hola)
  
  conn = sqlite3.connect('ODS.db')
  q = f"""SELECT * FROM Preguntas50 
          WHERE id_preguntas = {hola}"""
  for row in conn.execute(q):
    q2 = row[1]
    q3 = row[2]
    q4 = row[3]
    q5 = row[4]
    q6 = row[5]

  session['respuestas2'] = []
  session['respuestas2'].append(q3)
  session['respuestas2'].append(q4)
  session['respuestas2'].append(q5)
  session['respuestas2'].append(q6)
  q7 = random.sample(session['respuestas2'], len(session['respuestas2']))  
  print(hola)
  return render_template('preguntas.html', pregunta = q2, respuesta1=q7[0], respuesta2=q7[1], respuesta3=q7[2], respuesta4=q7[3])
  conn.close()

@app.route("/game/pregunta")
def mostrar_pregunta100():
  hola = random.randint(1, 6)
  while(hola in session['preguntas100']):
    hola = random.randint(1, 6)
  session['preguntas100'].append(hola)
  
  conn = sqlite3.connect('ODS.db')
  q = f"""SELECT * FROM Preguntas100 
          WHERE id_preguntas = {hola}"""
  for row in conn.execute(q):
    q2 = row[1]
    q3 = row[2]
    q4 = row[3]
    q5 = row[4]
    q6 = row[5]

  session['respuestas3'] = []
  session['respuestas3'].append(q3)
  session['respuestas3'].append(q4)
  session['respuestas3'].append(q5)
  session['respuestas3'].append(q6)
  q7 = random.sample(session['respuestas3'], len(session['respuestas3']))  
  
  
  print(session['respuestas3'])
  return render_template('preguntas.html', pregunta = q2, respuesta1=q7[0], respuesta2=q7[1], respuesta3=q7[2], respuesta4=q7[3])
  conn.close()

@app.route("/game/final")
def mostrar_final():
  return render_template('fin-juego.html')

app.run(host='0.0.0.0', port=81)