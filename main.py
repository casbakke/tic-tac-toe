import tkinter as tk # for graphical interface

font0 = ("Arial", 48)
font1 = ("Arial", 64)

window = tk.Tk() # main window object
window.title("Tic-Tac-Toe")
window.geometry("600x700+100+50") # entire widow will be 600x700px, opens at coords (100, 50)
window.maxsize(600, 700) # lock window to a fixed size
window.minsize(600, 700)

window.rowconfigure(0, minsize = 100) # header will be 100px tall
window.rowconfigure(1, minsize = 600) # body will be 600x600px

player = "X" # first player upon launch is always X
stopped = False # this allows the buttons to be used

frm_head = tk.Frame( # header frame containing the status widget
    window,
    relief = tk.FLAT,
)

frm_board = tk.Frame( # board frame containing the 9 button widgets
    window,
    relief = tk.FLAT,
)

# button widgets
btn_A1 = tk.Button(
    frm_board, # button container
    font = font1, # text font
    borderwidth = 5, # button border width
    command = lambda: button_clicked("A1") # calls button_clicked("A1") upon click
)

btn_A2 = tk.Button(
    frm_board,
    font = font1,
    borderwidth = 5,
    command = lambda: button_clicked("A2")
)

btn_A3 = tk.Button(
    frm_board,
    font = font1,
    borderwidth = 5,
    command = lambda: button_clicked("A3")
)

btn_B1 = tk.Button(
    frm_board,
    font = font1,
    borderwidth = 5,
    command = lambda: button_clicked("B1")
)

btn_B2 = tk.Button(
    frm_board,
    font = font1,
    borderwidth = 5,
    command = lambda: button_clicked("B2")
)

btn_B3 = tk.Button(
    frm_board,
    font = font1,
    borderwidth = 5,
    command = lambda: button_clicked("B3")
)

btn_C1 = tk.Button(
    frm_board,
    font = font1,
    borderwidth = 5,
    command = lambda: button_clicked("C1")
)

btn_C2 = tk.Button(
    frm_board,
    font = font1,
    borderwidth = 5,
    command = lambda: button_clicked("C2")
)

btn_C3 = tk.Button(
    frm_board,
    font = font1,
    borderwidth = 5,
    command = lambda: button_clicked("C3")
)

lbl_status = tk.Label( # status label at the top of the screen
    frm_head,
    text = f"{player}'s Turn",
    font = font0,
)

# display widgets
frm_board.rowconfigure((0,1,2), minsize = 200)
frm_board.columnconfigure((0,1,2), minsize = 200)

frm_head.grid(row = 0, column = 0)
frm_board.grid(row = 1, column = 0)

lbl_status.grid(row = 0, column = 0, sticky = "nesw")

btn_A1.grid(row = 0, column = 0, sticky = "nesw")
btn_A2.grid(row = 0, column = 1, sticky = "nesw")
btn_A3.grid(row = 0, column = 2, sticky = "nesw")
btn_B1.grid(row = 1, column = 0, sticky = "nesw")
btn_B2.grid(row = 1, column = 1, sticky = "nesw")
btn_B3.grid(row = 1, column = 2, sticky = "nesw")
btn_C1.grid(row = 2, column = 0, sticky = "nesw")
btn_C2.grid(row = 2, column = 1, sticky = "nesw")
btn_C3.grid(row = 2, column = 2, sticky = "nesw")

# events
def button_clicked(ident): # when a button is clicked
    global stopped
    global player # get current player (letter)
    if not stopped:
        txt = eval(f"btn_{ident}")["text"] # get the corresponding button object
        if txt == "": # if the button has no text
            eval(f"btn_{ident}")["text"] = player # set text to player's letter
            if check_win(): # if the game has been won
                won(player)
            elif check_draw(): # if the game is drawn
                draw()
            else: # instead continue playing
                player = "X" if (player == "O") else "O"
                lbl_status["text"] = f"{player}'s Turn"

    else: # if the game is stopped, reset the board
        for btn in frm_board.winfo_children(): # get all buttons in the window
            btn["text"] = "" # set button text to null
        player = "X" if (player == "O") else "O"
        lbl_status["text"] = f"{player}'s Turn"
        stopped = False

def check_win(): # determine if the game has finished, returns T/F
    pass

    a1 = btn_A1["text"]
    a2 = btn_A2["text"]
    a3 = btn_A3["text"]
    b1 = btn_B1["text"]
    b2 = btn_B2["text"]
    b3 = btn_B3["text"]
    c1 = btn_C1["text"]
    c2 = btn_C2["text"]
    c3 = btn_C3["text"]

    # top row
    if a1 != "":
        if a1 == a2 == a3:
            return True
    
    # middle row
    if b1 != "":
        if b1 == b2 == b3:
            return True

    # bottom row
    if c1 != "":
        if c1 == c2 == c3:
            return True

    # left column
    if a1 != "":
        if a1 == b1 == c1:
            return True

    # middle column
    if a2 != "":
        if a2 == b2 == c2:
            return True

    # right column
    if a3 != "":
        if a3 == b3 == c3:
            return True

    # NW/SE diagonal
    if a1 != "":
        if a1 == b2 == c3:
            return True

    # NE/SW diagonal
    if a3 != "":
        if a3 == b2 == c1:
            return True

    return False

def check_draw(): # determine if the game board has been filled up with no winner
    str = ""
    for tile in frm_board.winfo_children(): # get each tile on the board
        str = str + tile["text"] # concatenate tile's text to a temporary string
    if len(str) != 9: # if the string does not have 9 values
        return False # continue the game
    else:
        return True # announce a draw

def won(winner): # stop the game and announce the winner
    global stopped
    stopped = True # disables the game buttons
    lbl_status["text"] = f"{winner} Wins!"

def draw(): # stop the game and announce a draw
    global stopped
    stopped = True
    lbl_status["text"] = "Draw!"

window.mainloop()