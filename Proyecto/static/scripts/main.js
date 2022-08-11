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


function mostarPuntos25(elememento){
  console.log(elememento)
  elememento.outerHTML =`<img name="tablet-25" src="/static/img/+25.png"></img>`;
  elememento.style.width = "75%";
  elememento.style.height = "95%";
  
} 

function volverNormal(elememento){
  console.log(elememento)
  elememento.outerHTML =`<img name="tablet-25" src="/static/img/tablet-apagada.png" alt="" onclick="" onmouseover="mostarPuntos25(this)">`;
  elememento.style.width = "75%";
  elememento.style.height = "95%";
}*/

function changePic1(imagen){
  /*switch (imagen) {
    case "1":
      document.getElementById(imagen).src ="static/img/+25.png";
      break;
    case "2":
      document.getElementById(imagen).src ="static/img/+25.png";
      break;
    case "3":
      document.getElementById(imagen).src ="static/img/+25.png";
      break;
    case "4":
      document.getElementById(imagen).src ="static/img/+25.png";
      break;
    case "5":
    document.getElementById(imagen).src ="static/img/+25.png";
      break;
    case "6":
      document.getElementById(imagen).src ="static/img/+50.png";
      break;
    case "7":
      document.getElementById(imagen).src ="static/img/+50.png";
      break;
    case "8":
      document.getElementById(imagen).src ="static/img/+50.png";
      break;
    case "9":
      document.getElementById(imagen).src ="static/img/+50.png";
      break;
    case "10":
      document.getElementById(imagen).src ="static/img/+50.png";
      break;
    case "11":
    document.getElementById(imagen).src ="static/img/+50.png";
      break;
    case "12":
      document.getElementById(imagen).src ="static/img/+50.png";
      break;
  }*/

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
  document.getElementById(imagen).src ="static/img/tablet-apagada.png";
}

function changePic3(imagen){
  document.getElementById(imagen).src ="static/img/+50.png";
}

function changePic4(imagen){
  document.getElementById(imagen).src ="static/img/tablet-apagada.png";
}





function ingreso(){
  var nombre_jugador = document.getElementById("nickname").value;
  console.log(nombre_jugador);
}