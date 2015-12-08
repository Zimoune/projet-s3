#i mporting modules
from tkinter import *
import random
import player as Player
import tictactoe as Game

# Situation at the beginning of the game
situation = Game.initSituation("tictactoe")

# Create players
human = Player.create('Joueur1', 'cross')
comp = Player.create('Joueur2', 'circle')

# dictionnary of positions
dico = {}

# current player
currentPlayer = None


def setCross(x1, y1, x2, y2):
    """
    ...
    """
    # Drawing and changing situation
    for c in dico:
        if dico[c] == (x1, y1, x2, y2):
            x, y = c
            if Game.get_color(situation, x, y) is None:
                # Draw the cross
                Canevas.create_line(x1, y1, x2, y2, width=2, fill='red', tags="dessin")
                Canevas.create_line(x1, y2, x2, y1, width=2, fill='red', tags="dessin")
                Game.set_color(situation, x, y, 'cross')
            else:
                return None


def setCircle(x1, y1, x2, y2):
    """
    ...
    """
    # Drawing and changing situation
    for c in dico:
        if dico[c] == (x1, y1, x2, y2):
            x, y = c
            if Game.get_color(situation, x, y) is None:
                # Draw the circle
                Canevas.create_oval(x1, y1, x2, y2, width=2, outline='blue', tags="dessin")
                Game.set_color(situation, x, y, 'circle')
            else:
                return None

def checker(event):
    """
    ...
    """
    global currentPlayer
    case = Canevas.find_closest(event.x, event.y)
    x1, y1, x2, y2 = Canevas.coords(case)
    winner = Game.getWinner(Game.game, situation, currentPlayer)
    if Game.isFinished(situation):
        if winner is None:
            Resultat.configure(text="equality !", bg='red')
        else:
            Resultat.configure(text = winner['name']+' won', bg='yellow')
    else:
        if currentPlayer is None:
            Resultat.configure(text=comp['name']+' to play')
            setCross(x1, y1, x2, y2)
            currentPlayer = human
        elif currentPlayer == human:
            Resultat.configure(text=comp['name']+' to play')
            setCircle(x1, y1, x2, y2)
            currentPlayer = comp
        else:
            Resultat.configure(text=human['name']+' to play')
            setCross(x1, y1, x2, y2)
            currentPlayer = human
        
        
    
def Reset():
    """
    ...
    """
    for tag in ('cross', 'circle'):
        for item in Canevas.find_withtag(tag):
            Canevas.dtag(item, tag)
    for item in Canevas.find_withtag("dessin"):
        Canevas.delete(item)        

      
""" Main Program """

def play():
    """
    ...
    """
    myWindows = Tk()
    myWindows.title('Tic Tac Toe')
    Width = 330
    Height = 330
    caseSize = 110

    frame = Frame(myWindows, borderwidth=2, relief=GROOVE)
    frame.pack(padx=10, pady=10)
    global Canevas
    Canevas = Canvas(frame, width = Width, height = Height, bg = 'grey')
    Canevas.pack()
    Canevas.bind("<Button-1>", checker)

    Color = 'dark grey'
    for i in range(3):
        for j in range(3):
            Carre = Canevas.create_rectangle(i*caseSize, j*caseSize, caseSize+(+i*caseSize), caseSize+(j*caseSize),
                                             outline='black', activewidth=2, fill=Color)
            dico[(2-j, i)] = tuple(Canevas.coords(Carre))
            if Color == 'dark grey':
                Color = 'grey'
            else:
                Color = 'dark grey'
    # imputing buttons and labels
    boutonReset = Button(myWindows, text='Recommencer', command=Reset)
    boutonReset.pack(side=LEFT, padx=10, pady=5)
    global Resultat
    Resultat=Label(myWindows, text="Loading...")
    Resultat.pack(side=LEFT)
    myWindows.mainloop()
