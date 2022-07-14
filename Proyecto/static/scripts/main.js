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
}*/


function mostarPuntos25(elememento){
  console.log(elememento)
  elememento.outerHTML =`<img name="tablet-25" src="/static/img/+25.png" style="flex; width: 35%; height: 80%; " alt="" onclick="" onmouseout="volverNormal(this)"></img>`;
  
}

function volverNormal(elememento){
  console.log(elememento)
  elememento.outerHTML =`<img name="tablet-25" src="/static/img/tablet-apagada.png" alt="" onclick="" onmouseover="mostarPuntos25(this)">`;
  
}