# ProjectROVER
ROVER code compendium

Introduction
---------------

This is a code assembly and restructuration of the past creation of project ROVER.
At the beggining you will be able to control the 6wheel platform of Rover. Later on you will be able the control any platform of rover with this code.

PD
----------------
PPB

TODO
---------------------
---------------------
- joystick produce un vector de velocidad polar normalizado enter -1 y 1
- arduino.h: comunicacion entre fitpc y arduino
- hbridge: define la señal que debera crear la arduino mas adelante
- chassis.h: recibe vector polar de velocidad y calcula la velocidad especifica para cada rueda.
- rover.h: agrupa todas las clases y adapta la cantidad de ruedas a cantidad de puentes H.
- implementacion main: agregar elementos por medio un vector(arreglo) y tener la incializacion de los objetos en un archivo aparte (XML?) 
