import tkinter as tk
from random import randint

font0 = ("Arial", 48)
font1 = ("Arial", 64)

window = tk.Tk()
window.title("Tic-Tac-Toe")
window.geometry("600x700+100+50")
window.maxsize(600, 700)
window.minsize(600, 700)

window.rowconfigure(0, minsize = 100)
window.rowconfigure(1, minsize = 600)

player = "X"
stopped = False

frm_head = tk.Frame(
    window,
    relief = tk.FLAT,
)

frm_board = tk.Frame(
    window,
    relief = tk.FLAT,
)

btn_A1 = tk.Button(
    frm_board,
    font = font1,
    borderwidth = 5,
    command = lambda: button_clicked("A1")
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

lbl_status = tk.Label(
    frm_head,
    text = f"{player}'s Turn",
    font = font0,
)

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
            if check_win(): # if the game has finished
                won(player)
            else:
                player = "X" if (player == "O") else "O"
                lbl_status["text"] = f"{player}'s Turn"
    else:
        for btn in frm_board.winfo_children():
            btn["text"] = ""
        player = "X"
        lbl_status["text"] = f"{player}'s Turn"
        stopped = False

def check_win(): # determine if the game has finished, returns T/F
    pass # code here
    return False

def won(winner):
    global stopped
    stopped = True
    lbl_status["text"] = f"{winner} Wins!"

window.mainloop()