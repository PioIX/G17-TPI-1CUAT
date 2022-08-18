var pix = document.getElementsByClassName("pixel");

for (var i = 0; i < pix.length; i++) {
  pix[i].style.animationDelay = Math.ceil(Math.random()*5000)+"ms";
}

/*function jugar(){

}

class Laptop{
  constructor(id, puntaje){
    this.puntaje = puntaje;
    this.id = id;
  }
}

Laptop1 = new Laptop(1, 25);
Laptop7 = new Laptop(7, 50)
Laptop13 = new Laptop(13, 100) 

class Jugador{
  constructor(nickname){
    this.nickname = nickname;
    this.puntos = [];
  }

  ganarPuntos()
}
*/

function changePic1(imagen){

  var imagenes = parseInt(imagen);

  if(imagenes >=1 && imagenes <=6){
    document.getElementById(imagen).src ="static/img/+25.png";
  } else if(imagenes >=7 && imagenes <=12){
    document.getElementById(imagen).src ="static/img/+50.png";
  } else if(imagenes >= 13 && imagenes <= 18){
    document.getElementById(imagen).src ="static/img/+100.png";
  }
  

}

function changePic2(imagen){

  var imagenes = parseInt(imagen);

  if(imagenes >=1 && imagenes <=6){
    document.getElementById(imagen).src ="static/img/tablet-apagada.png";
  } else if(imagenes >=7 && imagenes <=12){
    document.getElementById(imagen).src ="static/img/tablet-apagada.png";
  } else if(imagenes >= 13 && imagenes <= 18){
    document.getElementById(imagen).src ="static/img/tablet-apagada.png";
  }
  
}



function ingreso(){
  var nombre_jugador = document.getElementById("nickname").value;
  if (nombre_jugador == ""){
    alert("Debes ingresar un nickname")
  }

  var formulario = document.getElementById("form-ingreso");

}

function cambiarTexto() {
  var texto = "Hola";
  document.getElementsByClassName("cont-pregunta").innerHTML = texto;
}