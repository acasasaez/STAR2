# STAR2
El enunciado de nuestra tarea era el siguiente:

El reto consiste en programar una función que dibuje estrellas como la que aparece a continuación con un número de puntas dado.

![estrella](https://user-images.githubusercontent.com/91721826/146766174-6b6d5639-503d-4493-abf4-9537eb7cf623.png)

Para poder presentarlo se ha creado un repositorio en GitHub, cuya direccioón es:https://github.com/acasasaez/STAR2.git

El diagrama de flujo que representa mi código es el siguiente:
![figma de la estrella](https://user-images.githubusercontent.com/91721826/146793232-8a50b53e-a5f5-410b-b3ab-df9c562fe6f1.jpg)


*NOTA: Tener en cuenta que a la hora de crear el código: se ha considerado que no existen estrellas con menos de 5 puntas y solo funciona para los casos en los que n =2a+1, siendo a un número natural (>1), (pues en otros casos la fórmula que determina el ángulo no es válida).

Mi código en esta tarea es el siguiente:

```import turtle 
turtle.fillcolor("purple")
turtle.beingfill()
a = int(input("Introduzca el número de estrellas: "))
c = 1
while c != a:
    turtle.forward(250)
    turtle.right (180-(180/a))
    if c == a +1:
        break
turtle.end_fill()
