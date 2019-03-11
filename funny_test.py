import tkinter as tk
import tkinter.ttk
from tkinter import messagebox
import os
import sys
import time
import webbrowser

def goopage(root):
	webbrowser.open('https://accounts.google.com')
	bBegin = tk.Button(root, width=15, height=1, text="Start Test")
	bBegin.grid(row=2, column=0)
	

def show_readme():
	os.system("gedit README.md")

root = tk.Tk()
root.geometry("500x200+70+60")
root.title("Herzlichen willkommen!")

text = tk.Text(root, width=50, height=10)
text.grid(row=0, column=0, columnspan=2)
text.insert('1.0', "Hallo!\n")
text.insert('end', "Sie beginnen den Test. Sind Sie bereit?")

bJa = tk.Button(root, width=15, height=1, text="Ja! Natürlich!", command=lambda: goopage(root))
bJa.grid(row=1, column=0)

bWas = tk.Button(root, width=15, height=1, text="Was ist hier los?", command=lambda: show_readme())
bWas.grid(row=1, column=1)

root.mainloop()