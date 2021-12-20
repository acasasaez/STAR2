import turtle 
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