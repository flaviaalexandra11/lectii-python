import turtle
import random


# Creare ecran.
screen = turtle.Screen()
screen.setup(750, 425)
screen.bgpic('images/pond.png')

# Creare turtle (jucator 1)
player1 = turtle.Turtle()
player1.color("#006600")
player1.shape("turtle")
player1.penup()
player1.goto(-200, 100)

# Creare turtle (jucator 2)
player2 = player1.clone()
player2.color("#cc0000")
player2.penup()
player2.goto(-200, -100)

# Desenare destinatie jucator 1
player1.goto(300, 60)
player1.pendown()
player1.circle(40)
player1.penup()
player1.goto(-200, 100)

# Desenare destinatie jucator 2
player2.goto(300, -140)
player2.pendown()
player2.circle(40)
player2.penup()
player2.goto(-200, -100)

# Creare zar
zar = [1, 2, 3, 4, 5, 6]

while True:
    if player1.pos() >= (300, 100):
        print("Player 1 Wins!")
        break
    elif player2.pos() >= (300, -100):
        print("Player 2 Wins!")
        break
    else:
        player1_turn = input("[Player1] Press 'Enter' to roll the zar: ")
        result = random.choice(zar)
        print("The result of the zar roll is: {}".format(result))

        distance = 20 * result
        print("The number of steps will be: {}".format(distance))
        if player1.pos()[0] + distance >= 300:
            player1.goto(300, 100)
        else:
            player1.forward(distance)

        player2_turn = input("[Player 2] Press 'Enter' to roll the zar: ")
        result = random.choice(zar)
        print("The result of the zar roll is: {}".format(result))

        distance = 20 * result
        print("The number of steps will be: {}".format(distance))
        if player2.pos()[0] + distance >= 300:
            player2.goto(300, -100)
        else:
            player2.forward(distance)

screen.mainloop()
