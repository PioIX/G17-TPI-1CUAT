import sqlite3
from flask import Flask, render_template, Response, request, redirect, url_for

app = Flask(__name__)

#app.secret_key = ""

@app.route("/")
def mostar_index():
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
  

@app.route("/información")
def informacion():
  return render_template('ayuda.html')

@app.route("/game")
def mostrar_juego():
  return render_template('juego.html')

app.run(host='0.0.0.0', port=81)