from asyncio import windows_events
from msilib.schema import Class
import sqlite3
import random
from flask import Flask, render_template, Response, request, redirect, session, url_for, jsonify


app = Flask(__name__)

app.secret_key = "hjdfbhasdasdjkashdkasd"

@app.route("/")
def index():
  if 'preguntas' in session:
    preguntas = session['preguntas']
    print(preguntas)
  return render_template('index.html')

@app.route("/register")
def guardarnickname():
  session['preguntas'] = []
  session['idLaptops'] = []
  session['preguntasCompletas'] = 0
  session['lista_incorrecta'] = []
  session['lista_correctas'] = []
  #session['laptopsCorrectas'] = False
  return render_template('nickname.html')
  
@app.route("/ranking")
def ranking():
  conn = sqlite3.connect('ODS.db')
  q = f"""SELECT * from Ranking
          ORDER BY Puntaje DESC
          LIMIT 10"""
  x = conn.execute(q)
  lista = x.fetchall() 
  print(lista)
  return render_template('ranking.html', lineamostrar = lista)
  conn.close()

@app.route("/ayuda")
def informacion():
  return render_template('ayuda.html')

@app.route("/acercaDeNosotros")
def acercaDe():
  return render_template('acerca_de_nosotros.html')

@app.route("/game", methods=['POST', 'GET'])
def mostrar_juego():
  if session['preguntasCompletas'] < 18:
    if request.method == 'POST':
      name = request.form['nombre']
      session['name'] = name
      session['puntos'] = 0
      
      print(name)
      
      conn = sqlite3.connect('ODS.db')

      if (name != ""):
        q = f"""INSERT INTO Ranking(Nombre, Puntaje) VALUES('{name}', 0)"""
        conn.execute(q)
        conn.commit()
      conn.close()
    return render_template('juego.html', puntosFinales = session['puntos'], lista_desact = session['idLaptops'], lista_correctas = session['lista_correctas'], lista_incorrecta = session['lista_incorrecta'])
  else:
    return redirect("/game/final")


@app.route("/puntos", methods=['POST', 'GET'])
def guardar_puntaje():
  conn = sqlite3.connect('ODS.db')
  if request.method == "POST":
        search_term = request.form
        search = search_term["value"]
        print(search)
        
        q = f"""SELECT RtaCorrecta FROM Preguntas25"""
        q2 = f"""SELECT RtaCorrecta FROM Preguntas50"""
        q3 = f"""SELECT RtaCorrecta FROM Preguntas100"""
        
        lista = [x[0] for x in conn.execute(q).fetchall()]
        lista2 = [x2[0] for x2 in conn.execute(q2).fetchall()]
        lista3 = [x3[0] for x3 in conn.execute(q3).fetchall()]
        
        if search in lista:
          session['puntos'] = session['puntos'] + 25
          session['lista_correctas'].append(session['id'])
          print("se sumaron 25")
        elif search in lista2:
          session['puntos']= session['puntos'] + 50
          session['lista_correctas'].append(session['id'])
          print("se sumaron 50")
        elif search in lista3:
          session['puntos'] = session['puntos'] + 100
          session['lista_correctas'].append(session['id'])
          print("se sumaron 100")
        elif search not in lista and search not in lista2 and search not in lista3:
          session['lista_incorrecta'].append(session['id'])
  
  print(session['puntos'])
  print(session['lista_incorrecta'])
  print(session['lista_correctas'])
  return render_template('juego.html')

@app.route("/game/pregunta/<nivel>/<id>")
def mostrar_pregunta(nivel, id):
    session['id'] = id
    session['idLaptops'].append(id)
    session['preguntasCompletas'] += 1
    print(session['preguntasCompletas'])
    print(session['preguntasCompletas'] < 17)

    if nivel == "25":
      numRandomPregunta = random.randint(1, 6)
      while(numRandomPregunta in session['preguntas']):
        numRandomPregunta = random.randint(1, 6)
      #session['preguntas'].append(numRandomPregunta)
      print(session['preguntas'])
      print(numRandomPregunta)
    
    if nivel == "50":
      numRandomPregunta = random.randint(7, 12)
      while(numRandomPregunta in session['preguntas']):
        numRandomPregunta = random.randint(7, 12)
      #session['preguntas'].append(numRandomPregunta)
      print(session['preguntas'])
      print(numRandomPregunta)
    
    if nivel == "100":
      numRandomPregunta = random.randint(13, 18)
      while(numRandomPregunta in session['preguntas']):
        numRandomPregunta = random.randint(13, 18)
      #session['preguntas'].append(numRandomPregunta)
      print(session['preguntas'])
      print(numRandomPregunta)
    
    session['preguntas'].append(numRandomPregunta)
    print(session['preguntas'])
    print(session['idLaptops'])

    conn = sqlite3.connect('ODS.db')
    q = f"""SELECT * FROM Preguntas 
            WHERE id_preguntas = {numRandomPregunta}"""
    print(conn.execute(q).fetchall())
    for row in conn.execute(q):
      pregunta1 = row[1]
      print(pregunta1)
      rta1 = row[2]
      print(rta1)
      rta2 = row[3]
      print(rta2)
      rta3 = row[4]
      print(rta3)
      rta4 = row[5]
      print(rta4)
    
    session['shuffleRtas'] = []
    session['shuffleRtas'].append(rta1)
    session['shuffleRtas'].append(rta2)
    session['shuffleRtas'].append(rta3)
    session['shuffleRtas'].append(rta4)
    respuestasMezcladas = random.sample(session['shuffleRtas'], len(session['shuffleRtas']))
    
    return render_template('preguntas.html', pregunta = pregunta1, respuesta1=respuestasMezcladas[0], respuesta2=respuestasMezcladas[1], respuesta3=respuestasMezcladas[2], respuesta4=respuestasMezcladas[3])
    conn.close()

    


@app.route("/game/final")
def mostrar_final():
  conn = sqlite3.connect('ODS.db')
  nicknameParaSumarPuntos = '"' + session['name'] + '"'
  q = f"""UPDATE Ranking
          SET Puntaje = {session['puntos']}
          WHERE Nombre = {nicknameParaSumarPuntos}"""
  conn.execute(q)
  print(nicknameParaSumarPuntos)
  conn.commit()
  session.pop('preguntas', None)
  session.pop('idLaptops', None)
  conn.close()
  return render_template('fin-juego.html', puntosFinales = session['puntos'])

app.run(host='0.0.0.0', port=5000)