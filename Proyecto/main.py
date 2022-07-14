import sqlite3
from flask import Flask, render_template, Response, request, redirect, session, url_for

app = Flask(__name__)

#app.secret_key = ""

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
  print(name)
  conn = sqlite3.connect('ODS.db')
  q = f"""INSERT INTO Ranking(Nombre, Puntaje) VALUES('{name}', 0)"""
  conn.execute(q)
  conn.commit()
  conn.close()
  return render_template('juego.html')

@app.route("/game/final")
def mostrar_final():
  return render_template('fin-juego.html')

app.run(host='0.0.0.0', port=81)