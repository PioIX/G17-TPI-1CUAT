# G17-AplicacionWeb-ODS

## Proyecto interdisciplinario

### Primer cuatrimestre


Propuesta de trabajo                                                
Grupo:	17 División: A    
Link del PythonAnywhere: [(MatteoBobasso.pythonanywhere.com)]

LA CONTRIBUCIÓN DE Nicolas Gil Rodriguez FUE UN ERROR CUANDO HICIMOS EL COMMIT CON EL GITHUB DESKTOP

Integrantes:
Matteo Bobasso, Ramiro Boulos, Augusto Florio, Gabriel Iacomini y Felipe Vega Torre
____________________________________________________________________________


Título de la propuesta:  ODS QUIZ


Descripción de la propuesta:

Vamos a desarrollar una aplicación web que permita divulgar y conocer las características de los ODS en general y los ODS “Ciudades y comunidades sostenibles” y “Producción y consumos responsables” en particular.

La aplicación que desarrollaremos será un Quiz mediantes el cual con preguntas acerca de los distintos ODS elegidos, el jugador podrá adquirir conocimientos acerca del tema.

En sí, la página tendrá distintas pestañas. La pestaña principal consta del logo del juego y tres botones: jugar, ranking e información. La pestaña de información brindará una breve explicación acerca del juego y los ODS en los cuales nos enfocaremos.

Una vez clickeado el botón “jugar” se redirigirá al jugador hacia una nueva pestaña en la cual deberá ingresar un nickname el cual quedará guardado en la base de datos. Después de esto pasará a la pestaña de juego en donde se encontrarán un total de 18 laptops acomodadas en una tabla de 6x3 y un botón para volver a la pestaña principal. Estas laptops tendrán sobre sí su valor de puntaje. Mientras el valor sea más alto, la pregunta que contenga será más difícil. 

Al clickear sobre cualquiera de las laptops en pantalla, las preguntas y las respuestas aparecerán simulando que están dentro de la pantalla de la laptop. De las cuatro posibles respuestas el jugador deberá elegir únicamente una y si responde bien, se sumará a un “puntaje total” el valor de la laptop.

Cuando el usuario termine de responder todas las preguntas se le mostrará en pantalla el puntaje total obtenido y un botón “inicio” para volver a la pestaña principal. A la vez, en la base de datos, se va a estar guardando su puntaje para poder conformar el ranking de la página.
____________________________________________________________________________
Funcionalidad:

 * Preguntas y respuestas. 
 * Jugadores y sus puntajes en base de datos.
 * Ranking de jugadores.
 * Agregado y modificación de preguntas.
____________________________________________________________________________
Lenguaje para programar la aplicación:
 * Front-end:
   * HTML 5
   * CSS
   * JavaScript

 * Back-end:
   * Python
   * Framework (Flask)
   * SQLite 3
____________________________________________________________________________
Tareas

 * Investigación y redacción de preguntas y sus respuestas
 * Diseño de imagen y de la UI
 * Diseño de la base de datos 
 * Funciones de interacción con la base (API, Flask) 
 * Front-end del juego (HTML, CSS, JS)
 * Testeo 
 * Puesta en producción
____________________________________________________________________________
Responsabilidades

	Bobasso → 1, 3, 4, 6 y 7.
	Boulos → 1, 2, 5, 6 y 7.
	Florio → 1, 3, 4, 6 y 7.
	Iacomini → 1, 2, 5, 6 y 7.
	Vega Torre → 1, 2, 5, 6 y 7.

____________________________________________________________________________
 * Primer entregable (30/6)
   * Estructura de la base de datos
   * Reglas y puntajes
   * Maqueta html

 * Segundo entregable (7/7)
   * API en flask de preguntas y respuestas
   * Preguntas y respuestas
   * UI de preguntas y respuestas en conjunto con back-end
   * Pruebas de juego

* Tercer entregable (14/7)
   * Juego completo en línea
