from guizero import App, Box, PushButton, Text, TextBox
import random

outcome  = None
outcome2 = None


 

def calculate_answer():
    print(number)
    if int(answer.value) == number:
        outcome.visible=True
    else:
        outcome2.visible = True


def play_command():
    print ("play command")
    clue1.clear()
    clue2.clear()
    clue3.clear()
    if number >= 50:
        clue1.append("The number is \ngreater or equal to 50")
        print ("greater")
    else:
        print("less")        
        clue1.append("The number is \nless than 50")
        
    if number % 2 == 0:
        clue3.append("The number is even")
    else:
        clue3.append("The number is odd")
        
    for i in range(1,13):
        if number % i == 0:
            clue2.append("\nIt is multiple of " + str(i))
            
    clue1.visible= True
    clue2.visible= True
    clue3.visible= True
    
app = App (title  = "Number Guessing")
app.bg = "blue"
app.full_screen=True

board = Box(app, layout="grid")
play = PushButton (board,image="Play_Button.png", grid=[2, 1], command=play_command)
number = random.randrange(1, 100)


clue1 = Text(board, size = 30, text="", grid=[1, 2], width=19, color = "green", visible = False)
clue2 = Text(board, size = 30, text="", grid=[2, 2], width=19, color = "yellow", visible = False)
clue3 = Text(board, size = 30, text="", grid=[3, 2], width=19, color = "white", visible = False)

answer = TextBox(board, text="", grid =[2, 3])

outcome = Text(board, size=20, text="correct", grid=[2, 5], visible = False)
outcome2 = Text(board, text="incorrect", grid=[2, 6], visible = False)

put = PushButton(board, text="Answer", grid=[2, 4], command = calculate_answer)

play.clear()

app.display()

















