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



var listaJugadores = [];

class Jugador{
  constructor(nickname){
    this.nickname = nickname;
    this.puntos = 0;
    
  }
}

function asignarNickname(){
  var nombre_jugador = document.getElementById("nickname").value;

  if (nombre_jugador != ""){
    Jugador1 = new Jugador(nombre_jugador);
    listaJugadores.push(Jugador1);
  }
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

function cambiarTexto() {
  var texto = "Hola";
  document.getElementById("preguntilla").innerHTML = texto;
}

function enviarRespuesta(boton) {
  console.log(boton)
  console.log(boton.value)
  $.ajax({
    url:"/puntos",
    type:"POST",
    data: {"value":boton.value},
    success: function(response){
      //document.getElementById("id").submit();
      window.location = '/game';
    },
    });
}
