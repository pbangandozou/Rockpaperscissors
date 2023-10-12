from tkinter import *
import random
from turtle import color

# Creating a tkinter window object
root = Tk()
root.geometry("600x600")
root.title("Rock Paper Scissor Game")
root.config(bg='green')
win=0
cpuwin=0

# Game logic
comp_val = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}

# Turning on buttons for the user
def reset_game():
    rockButton["state"] = "active"
    paperButton["state"] = "active"
    ScissorsButton["state"] = "active"
    text1.config(text="Player			 ")
    text3.config(text="Computer")
    text4.config(text="")

# Turning off buttons for the user
def button_disable():
    rockButton["state"] = "disable"
    paperButton["state"] = "disable"
    ScissorsButton["state"] = "disable"

# If the player selected rock
def playerClickedRock():
    global win
    global cpuwin
    c_v = comp_val[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        win = win +1
        match_result = "Player Win"
        #color change
        root['background']='yellow'
        
    else:
        cpuwin = cpuwin +1
        match_result = "Computer Win"
    text4.config(text=match_result)
    text1.config(text="Rock      ")
    text3.config(text=c_v)
    playerScoreText["text"]="Player Score: "+str(win)
    button_disable()

# If the player selected paper
def playerClickedPaper():
    global win
    global cpuwin
    c_v = comp_val[str(random.randint(0, 2))]
    if c_v == "Paper":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        cpuwin = cpuwin +1
        match_result = "Computer Win"
    else:
        win = win +1
        match_result = "Player Win"
        root['background']='red'
    text4.config(text=match_result)
    text1.config(text="Paper      ")
    text3.config(text=c_v)
    playerScoreText["text"]="Player Score: "+str(win)

    button_disable()

# If the player selected scissor
def playerClickedScissors():
    global win
    global cpuwin
    c_v = comp_val[str(random.randint(0, 2))]
    if c_v == "Rock":
        cpuwin = cpuwin +1
        match_result = "Computer Win"
    elif c_v == "Scissor":
        match_result = "Match Draw"
    else:
        win = win +1
        match_result = "Player Win"
        root['background']='purple'
    text4.config(text=match_result)
    text1.config(text="Scissor      ")
    text3.config(text=c_v)
    playerScoreText["text"]="Player Score: "+str(win)
    button_disable()

#Changes color as the Player wins
#  def colorchange():
#      if player win = True 
#          chnage color 
#      else:
#          keep color the same 


# Add labels, frames, and buttons
Label(root,
    text="Welcome to Rock Paper Scissors, CSCI 120!",
    font="normal 30 bold",
    fg="brown").pack(pady=25)

frame = Frame(root)
frame.pack()

text1 = Label(frame,
        text="Player			 ",
        font=10)

text2 = Label(frame,
        text="VS			 ",
        font="normal 10 bold")

text3 = Label(frame, text="Computer", font=20)
# Pack the labels in the frame
text1.pack(side=LEFT)
text2.pack(side=LEFT)
text3.pack()

#Display the wins for both cpu and player 
playerScoreText = Label(root, text="score", font=20)
playerScoreText.pack()
# Create the result label
text4 = Label(root,
        text="",
        font="normal 20 bold",
        bg="white",
        width=15,
        borderwidth=2,
        relief="solid")
text4.pack(pady=20)

# Create another frame for the buttons
frame1 = Frame(root)
frame1.pack()

# Create the buttons
rockButton = Button(frame1, text="Rock",
            font=20, width=9,
            command=playerClickedRock)

paperButton = Button(frame1, text="Paper ",
            font=20, width=9,
            command=playerClickedPaper)

ScissorsButton = Button(frame1, text="Scissor",
            font=20, width=9,
            command=playerClickedScissors)

# Pack the buttons in the frame
rockButton.pack(side=LEFT)
paperButton.pack(side=LEFT)
ScissorsButton.pack(side=LEFT)

# Create a reset button
Button(root, text="Reset", font=20, width=9, command=reset_game).pack()

# Start the event loop
root.mainloop()
