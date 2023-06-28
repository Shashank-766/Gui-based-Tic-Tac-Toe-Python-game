from tkinter import *
import random
import pygame
from pygame import mixer


pygame.init()
mixer.music.load("bg_music.mp3")
mixer.music.play(-1, 0.0)


def next_turn(row, column, label):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=("Player " + players[1] + " Turn"))

            elif check_winner() is True:
                label.config(text=("Player " + players[0] + " Wins The Game"))

            elif check_winner() == "Tie":
                label.config(text="Game Ends in Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=("Player " + players[0] + " Turn"))

            elif check_winner() is True:
                label.config(text=("Player " + players[1] + " Wins The Game"))

            elif check_winner() == "Tie":
                label.config(text="Game Ends in Tie!")


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="#CE2D42")
            buttons[row][1].config(bg="#CE2D42")
            buttons[row][2].config(bg="#CE2D42")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="#CE2D42")
            buttons[1][column].config(bg="#CE2D42")
            buttons[2][column].config(bg="#CE2D42")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="#CE2D42")
        buttons[1][1].config(bg="#CE2D42")
        buttons[2][2].config(bg="#CE2D42")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="#CE2D42")
        buttons[1][1].config(bg="#CE2D42")
        buttons[2][0].config(bg="#CE2D42")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#CE2D42")
        return "Tie"

    else:
        return False


def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game(label):
    global player

    player = random.choice(players)

    label.config(text="Player " + player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#077265", activebackground="#077265",
                                        activeforeground="#077265", highlightbackground="black",
                                        highlightcolor="white", highlightthickness=0, bd=5)


def main_window():
    w.destroy()
    window = Tk()
    window.resizable(False,False)
    window.title("Tic-Tac-Toe Game by Shashank")
    window.configure(background="#031237")

    label1 = Label(window, text="Tic-Tac-Toe ", font=('impact', 20, "italic "), fg="white",
                   pady=10, width=45, bg="#031237", activebackground="#077265",
                   activeforeground="#077265", highlightbackground="black",
                   highlightcolor="white", highlightthickness=0, bd=5)
    label1.pack(side="top")
    label = Label(window, text="Player " + player + " Turn", font=('impact', 28, "italic "),
                  fg="white", pady=10, width=21, bg="#031237",
                  activebackground="#077265", activeforeground="#077265",
                  highlightbackground="black", highlightcolor="white",
                  highlightthickness=0, bd=5)

    label.pack(side="top")

    reset_button = Button(window, text="Restart", font=('impact', 20, "italic"), fg="white",
                          pady=10, width=29, bg="#077265",
                          activebackground="#077265", activeforeground="#077265",
                          highlightbackground="black", highlightcolor="white",
                          highlightthickness=0, bd=5, command=lambda label=label: new_game(label))

    frame = Frame(window, background="#077265")
    frame.pack(side="top")
    reset_button.pack(side="top")

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="", font=('impact', 20, "italic"),
                                          fg="white", width=9, height=2, bg="#077265",
                                          activebackground="#077265", activeforeground="#077265",
                                          highlightbackground="black", highlightcolor="white",
                                          highlightthickness=0, bd=5,
                                          command=lambda row=row, column=column, label=label: next_turn(row, column, label))
            buttons[row][column].grid(row=row, column=column)
    label3 = Label(window, text="This Game is made by Shashank Jaiswal ",
                   font=('impact', 9, "italic "), fg="white", pady=10,
                   width=63, bg="#031237",
                   activebackground="#077265", activeforeground="#077265",
                   highlightbackground="black", highlightcolor="white",
                   highlightthickness=0, bd=5)
    label3.pack()
    window.mainloop()


players = ["X", "0"]
player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

w = Tk()
img = PhotoImage(file="img.png")
w.title("Tic-Tac-Toe Game by Shashank")
w.configure(background="#031237")
w.geometry("440x280")
my_canvas = Canvas(w, width=800, height=800, bg="#031237")
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0, 0, image=img, anchor="nw")
my_canvas.create_text(200, 220, text="LOADING!.....", font=('impact', 25, "italic "), fill="white")
w.after(5000, main_window)
w.mainloop()
