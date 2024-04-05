import sqlite3
from tkinter import *
connect = sqlite3.connect("animeDatabase.db")
c = connect.cursor()

class animeGUI:

  def recommend(self):
    print("hi")

  def __init__(self):
    self.root = Tk()

    def task():
      print("The button was clicked!")

    def sp(event):
      print("The button was clicked!")

    self.root.geometry("1000x500")
    self.root.title("Anime Recomendation")
    self.root.resizable(False, False)

    paddingLabel = Label(self.root, text = "")
    paddingLabel.grid(row = 0, column = 0, padx = 70)

    welcomeLabel = Label(self.root, text = "Enter an anime genre!", font = ("Arial", 15))
    welcomeLabel.grid(row = 1, column = 2, padx = (230,0))

    textbox = Entry(self.root, font=('Arial', 16))
    textbox.grid(row = 2, column = 2, padx = (200,0))

    button1 = Button(text = "Search", command = task, font=("Arial", 12))
    button1.grid(row = 2, column = 3)

    self.root.bind("<Return>", sp)

    hello = "hi"

    label1 = Label(self.root, text = "1. " + hello)
    label1.grid(row = 3, column = 1)

    self.root.mainloop()

animeGUI()