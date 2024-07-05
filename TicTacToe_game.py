from tkinter import *
import random

# Function to handle the next turn
def next_Turn(row, col):
    global player
    # Check if the button is empty and there's no winner yet
    if game_btns[row][col]['text'] == "" and check_Winner() == False:
        # Player X's turn
        if player == players[0]:
            game_btns[row][col]['text'] = player
            if check_Winner() == False:
                player = players[1]
                label.config(text=(players[1] + " Turn"))
            elif check_Winner() == True:
                label.config(text=(players[0] + " wins!!"))
            elif check_Winner() == 'tie':
                label.config(text=("No winners!!"))
        # Player O's turn
        elif player == players[1]:
            game_btns[row][col]['text'] = player
            if check_Winner() == False:
                player = players[0]
                label.config(text=(players[0] + " Turn"))
            elif check_Winner() == True:
                label.config(text=(players[1] + " wins!!"))
            elif check_Winner() == 'tie':
                label.config(text=("No winners!!"))

# Function to check if there's a winner or a tie
def check_Winner():
    # Check rows for a winner
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            game_btns[row][0].config(bg='green')
            game_btns[row][1].config(bg='green')
            game_btns[row][2].config(bg='green')
            return True
    
    # Check columns for a winner
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
            game_btns[0][col].config(bg='green')
            game_btns[1][col].config(bg='green')
            game_btns[2][col].config(bg='green')
            return True
    
    # Check diagonals for a winner
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        game_btns[0][0].config(bg='green')
        game_btns[1][1].config(bg='green')
        game_btns[2][2].config(bg='green')
        return True
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        game_btns[0][2].config(bg='green')
        game_btns[1][1].config(bg='green')
        game_btns[2][0].config(bg='green')
        return True
    
    # Check for a tie
    if check_Empty_Spaces() == False:
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg='red')
        return 'tie'
    else:
        return False

# Function to check if there are any empty spaces left
def check_Empty_Spaces():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

# Function to restart the game
def restart_Game():
    global player
    player = random.choice(players)
    label.config(text=(player + " Turn"))
    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg='white')

# Initialize the main window
root = Tk()
root.title("TicTacToe_Game")

# Define players and randomly select who starts first
players = ["X", "O"]
player = random.choice(players)

# Create a 3x3 grid of buttons
game_btns = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Display the current player's turn
label = Label(text=(player + " Turn"), font=50)
label.grid(row=0, column=0)

# Create a restart button
restart_btn = Button(text=("Restart"), font=20, command=restart_Game)
restart_btn.grid(row=1, column=0)

# Create a frame to hold the 3x3 grid of buttons
nine_btns = Frame(root)
nine_btns.grid(row=3, column=0)

# Initialize the buttons in the 3x3 grid
for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(nine_btns, text="", command=lambda row=row, col=col: next_Turn(row, col), width=6, height=3)
        game_btns[row][col].grid(row=row, column=col)

# Run the main loop
root.mainloop()
