import sqlite3
from flask import Flask, render_template, request, send_from_directory, url_for, flash, redirect

app = Flask(__name__)

#app.secret_key = ""

@app.route("/")
def mostar_index():
  return render_template('index.html')

@app.route("/register")
def guardar_nickname():
  conn = sqlite3.connect('ODS.db')

  q = f"""INSERT INTO Nombres
      Values (1)"""
  z = conn.execute(q)
  conn.commit(z)
  return render_template('nickname.html')
  conn.close()
  
@app.route("/ranking")
def ranking():
  conn = sqlite3.connect('ODS.db')

  q = f"""SELECT * from Ranking
          ORDER BY Puntaje DESC
          LIMIT 10"""
  x = conn.execute(q)
  return render_template('ranking.html', lineamostrar = x)
  conn.close()

@app.route("/información")
def informacion():
  return render_template('informacion.html')

app.run(host='0.0.0.0', port=81)