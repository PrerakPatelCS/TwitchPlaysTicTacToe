import math
import time
from twitch_plays_hackru import TwitchPlaysOnline, TwitchPlaysOffline
import turtle
import random

square = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
state = ['', '', '', '', '', '', '', '', '']


twitch_options = {
    "PASS": "oauth:pd6h82bj4trrkfwu2mn4eidpalm8aw",
    "BOT": "TwitchPlaysBotBro",
    "CHANNEL": "mynameiskooloop",
    "OWNER": "mynameiskooloop",
    "OPTIONS": ["1","2","3","4","5","6","7","8","9"],
    "VOTE_INTERVAL": 5
}

# Initalize the TwitchPlays bot.

tPlays = TwitchPlaysOnline(**twitch_options)

result="1"











def drawBoard():
    for i in range(2):
        drawer.penup()
        drawer.goto(-300, 100 - 200 * i)
        drawer.pendown()
        drawer.forward(600)

    drawer.right(90)

    for i in range(2):
        drawer.penup()
        drawer.goto(-100 +200 * i, 300)
        drawer.pendown()
        drawer.forward(600)

    num = 1
    for i in range(3):
        for j in range(3):
            drawer.penup()
            drawer.goto(-290 + j * 200, 280 - i * 200)
            drawer.pendown()

            drawer.write(num, font = ("Arial", 12))
            num += 1







    screen.update()

drawer = turtle.Turtle()
turtle.title("Tic Tac Toes")
drawer.pensize(10)
drawer.ht()

screen = turtle.Screen()
screen.tracer(0)

def drawX(square):
    x = 0
    y = 0
    if square == 1:
        x = -200 + 200 * 0
        y = 200 - 200 * 0
    elif square == 2:
        x = -200 + 200 * 1
        y = 200 - 200 * 0
    elif square == 3:
        x = -200 + 200 * 2
        y = 200 - 200 * 0
    elif square == 4:
        x = -200 + 200 * 0
        y = 200 - 200 * 1
    elif square == 5:
        x = -200 + 200 * 1
        y = 200 - 200 * 1
    elif square == 6:
        x = -200 + 200 * 2
        y = 200 - 200 * 1
    elif square == 7:
        x = -200 + 200 * 0
        y = 200 - 200 * 2
    elif square == 8:
        x = -200 + 200 * 1
        y = 200 - 200 * 2
    elif square == 9:
        x = -200 + 200 * 2
        y = 200 - 200 * 2


    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.setheading(60)

    for i in range(2):
        drawer.forward(75)
        drawer.backward(150)
        drawer.forward(75)
        drawer.left(60)

    screen.update()

def drawO(square):
    x = 0
    y = 0
    if square == 1:
        x = -200 + 200 * 0
        y = 200 - 200 * 0
    elif square == 2:
        x = -200 + 200 * 1
        y = 200 - 200 * 0
    elif square == 3:
        x = -200 + 200 * 2
        y = 200 - 200 * 0
    elif square == 4:
        x = -200 + 200 * 0
        y = 200 - 200 * 1
    elif square == 5:
        x = -200 + 200 * 1
        y = 200 - 200 * 1
    elif square == 6:
        x = -200 + 200 * 2
        y = 200 - 200 * 1
    elif square == 7:
        x = -200 + 200 * 0
        y = 200 - 200 * 2
    elif square == 8:
        x = -200 + 200 * 1
        y = 200 - 200 * 2
    elif square == 9:
        x = -200 + 200 * 2
        y = 200 - 200 * 2

    drawer.penup()
    drawer.goto(x, y +75)
    drawer.pendown()

    drawer.setheading(0)

    for i in range(180):
        drawer.forward((150 * math.pi)/180)
        drawer.right(2)

    screen.update()



drawBoard()


def reset():
    drawer.reset()
    j = 0
    for i in square:
        square[j] = j
        j = j+1
    screen.update()
    drawer.pensize(10)
    drawer.ht()
    drawBoard()
    main()

def computerMove(state):
    openSpots = [0]*9
    m = 1
    print(state)
    while m <= 9:
        if state[m-1] == '':
            openSpots[m-1] = m
        m = m+1
    print(openSpots)
    position = random.choice(openSpots)
    while position == 0:
        position = random.choice(openSpots)
    print(position)
    n = 0
    while n < 9:
        openSpots[n] = 0
        n = n+1
    return position


def main():
    time.sleep(5)
    result = tPlays.vote_result()
    if result is None:
        result = "0"
    player = 1
    status = -1

    while status == -1:
        if player % 2 == 1:
            player = 1
        else:
            player = 2



        if player == 1:
            choice = int(result)
            mark = 'X'
        else:
            choice = int(computerMove(state))
            mark = 'O'
        state[choice - 1] = mark


        print('\nPlayer', player)
        # result goes here





        if player == 1:
            mark = 'X'
        else:
            mark = 'O'



        if choice == 1 and square[1] == 1:
            square[1] = mark
            if player == 1:
                drawX(choice)
            else:
                drawO(choice)
        elif choice == 2 and square[2] == 2:
            square[2] = mark
            if player == 1:
                drawX(choice)
            else:
                drawO(choice)
        elif choice == 3 and square[3] == 3:
            square[3] = mark
            if player == 1:
                drawX(choice)
            else:
                drawO(choice)
        elif choice == 4 and square[4] == 4:
            square[4] = mark
            if player == 1:
                drawX(choice)
            else:
                drawO(choice)
        elif choice == 5 and square[5] == 5:
            square[5] = mark
            if player == 1:
                drawX(choice)
            else:
                drawO(choice)
        elif choice == 6 and square[6] == 6:
            square[6] = mark
            if player == 1:
                drawX(choice)
            else:
                drawO(choice)
        elif choice == 7 and square[7] == 7:
            square[7] = mark
            if player == 1:
                drawX(choice)
            else:
                drawO(choice)
        elif choice == 8 and square[8] == 8:
            square[8] = mark
            if player == 1:
                drawX(choice)
            else:
                drawO(choice)
        elif choice == 9 and square[9] == 9:
            square[9] = mark
            if player == 1:
                drawX(choice)
            else:
                drawO(choice)
        else:
            print('Invalid move ')

            player -= 1

        time.sleep(5)
        status = game_status()

        if status ==-1:
            result=tPlays.vote_result()
            if result is None:
                result = "0"


        player += 1

    print('RESULT')
    if status == 1:

        print('Player', player - 1, 'win')
    else:
        print('Game draw')

    p = 0
    while p < 9:
        state[p] = ''
        p = p + 1
    reset()




def game_status():
    if square[1] == square[2] and square[2] == square[3]:
        return 1
    elif square[4] == square[5] and square[5] == square[6]:
        return 1
    elif square[7] == square[8] and square[8] == square[9]:
        return 1
    elif square[1] == square[4] and square[4] == square[7]:
        return 1
    elif square[2] == square[5] and square[5] == square[8]:
        return 1
    elif square[3] == square[6] and square[6] == square[9]:
        return 1
    elif square[1] == square[5] and square[5] == square[9]:
        return 1
    elif square[3] == square[5] and square[5] == square[7]:
        return 1
    elif square[1] != 1 and square[2] != 2 and square[3] != 3 and square[4] != 4 and square[5] != 5 and square[
        6] != 6 and square[7] != 7 and square[8] != 8 and square[9] != 9:
        return 0
    else:
        return -1



main()

