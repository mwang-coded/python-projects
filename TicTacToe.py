import turtle
t = turtle.Turtle()
t.speed(7)
t.pensize(3)

# boolean for invalid choice
error = False

# boolean variables for positions that have already been taken
taken1 = False
taken2 = False
taken3 = False
taken4 = False
taken5 = False
taken6 = False
taken7 = False
taken8 = False
taken9 = False

# boolean True if a player has won
win = False

# sets will contain all positions chosen by each player
player1 = set()
player2 = set()

# all winning combinations
winList = {frozenset({1, 2, 3})}
winList.add(frozenset({4, 5, 6}))
winList.add(frozenset({7, 8, 9}))
winList.add(frozenset({1, 4, 7}))
winList.add(frozenset({2, 5, 8}))
winList.add(frozenset({3, 6, 9}))
winList.add(frozenset({1, 5, 9}))
winList.add(frozenset({3, 5, 7}))

# will hold the combination that won the game
winningCombination = frozenset({0})

# count number of turns passed
turn = 0

# track which player's turn it is currently
player = 0


def announce_result():
    global win, player

    # announce tie
    if win is False:
        t.goto(-200, -40)
        t.pendown()
        t.color("black")
        t.write("TIE GAME...", False, "left", ("Arial", 56, "bold"))
        t.color("red")

    # announce winner
    else:
        strike_through_win()
        t.goto(-220, -40)
        t.pendown()
        t.color("black")
        t.write("PLAYER " + str(player) + " WINS!", False, "left", ("Arial", 56, "bold"))
        t.color("red")


def draw_the_board():
    t.penup()
    t.goto(-100, -250)
    t.left(90)

    t.pendown()
    t.forward(500)
    t.penup()
    t.goto(100, -250)

    t.pendown()
    t.forward(500)
    t.penup()
    t.goto(-250, -100)

    t.pendown()
    t.right(90)
    t.forward(500)
    t.penup()
    t.goto(-250, 100)

    t.pendown()
    t.forward(500)


def draw_x():
    t.penup()
    t.backward(50)

    t.pendown()
    t.left(45)
    t.forward(140)
    t.penup()
    t.right(135)
    t.forward(100)
    t.right(135)

    t.pendown()
    t.forward(140)
    t.setheading(0)


# with valid choice, sends turtle to chosen position
def go_to_choice():
    global taken1, taken2, taken3, taken4, taken5
    global taken6, taken7, taken8, taken9, turn, error

    if choice == 1 and taken1 is False:
        t.goto(-200, 150)
        taken1 = True
    elif choice == 2 and taken2 is False:
        t.goto(0, 150)
        taken2 = True
    elif choice == 3 and taken3 is False:
        t.goto(200, 150)
        taken3 = True
    elif choice == 4 and taken4 is False:
        t.goto(-200, -50)
        taken4 = True
    elif choice == 5 and taken5 is False:
        t.goto(0, -50)
        taken5 = True
    elif choice == 6 and taken6 is False:
        t.goto(200, -50)
        taken6 = True
    elif choice == 7 and taken7 is False:
        t.goto(-200, -250)
        taken7 = True
    elif choice == 8 and taken8 is False:
        t.goto(0, -250)
        taken8 = True
    elif choice == 9 and taken9 is False:
        t.goto(200, -250)
        taken9 = True
    else:
        print("Error, not a valid choice.")
        turn -= 1
        error = True


# draw a line through the winning positions
def strike_through_win():
    global winningCombination

    t.pensize(10)
    if winningCombination == frozenset({1, 2, 3}):
        t.goto(-250, 200)
        t.pendown()
        t.forward(500)
    elif winningCombination == frozenset({4, 5, 6}):
        t.goto(-250, 0)
        t.pendown()
        t.forward(500)
    elif winningCombination == frozenset({7, 8, 9}):
        t.goto(-250, -200)
        t.pendown()
        t.forward(500)
    elif winningCombination == frozenset({1, 4, 7}):
        t.goto(-200, 250)
        t.right(90)
        t.pendown()
        t.forward(500)
    elif winningCombination == frozenset({2, 5, 8}):
        t.goto(0, 250)
        t.right(90)
        t.pendown()
        t.forward(500)
    elif winningCombination == frozenset({3, 6, 9}):
        t.goto(200, 250)
        t.right(90)
        t.pendown()
        t.forward(500)
    elif winningCombination == frozenset({1, 5, 9}):
        t.goto(-250, 250)
        t.right(45)
        t.pendown()
        t.forward(707)
    elif winningCombination == frozenset({3, 5, 7}):
        t.goto(-250, -250)
        t.left(45)
        t.pendown()
        t.forward(707)
    t.penup()


# MAIN CODE STARTS
print("Let's play Tic-Tac-Toe!")

draw_the_board()
t.penup()

# one cycle of loop for each turn. break if a player wins
while turn < 9 and win is False:

    # reset error at the beginning of each turn
    error = False

    # track which player's turn it is currently
    player = turn % 2 + 1

    # receive position choice from player
    choice = int(input("Player " + str(player) + ", please choose position 1-9: "))

    go_to_choice()

    # if player 1's turn, draw x
    if player == 1 and error is False:
        t.color("red")
        draw_x()
        t.penup()

        # add choice to list of player 1's positions
        player1.add(choice)

    # else if player 2's turn, draw o
    elif player == 2 and error is False:
        t.color("blue")
        t.pendown()
        t.speed(0)
        t.circle(50)
        t.speed(7)
        t.penup()

        # add choice to list of player 2's positions
        player2.add(choice)

    # traverse through every possible winning combination to check if the
    # combination is a subset of player 1's or player 2's positions
    for x in winList:
        if x.issubset(player1) or x.issubset(player2):
            win = True
            winningCombination = x

    turn += 1

announce_result()
print("Game finished.")
turtle.exitonclick()
