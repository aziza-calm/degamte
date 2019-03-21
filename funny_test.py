import tkinter as tk
import tkinter.ttk
from tkinter import messagebox
import os
import sys
import time
import webbrowser
#import Image

def nextq():
	print ("Next question!")
	

def check(test, antwort):
	print ("Checked!")
	path = '/home/aziza/Downloads/Deutsch/degames/quote-2019-03-16-1552718622.jpg'
	if antwort == "an der Spree" or antwort == "An der Spree":
		#img = Image.open(path)
		#panel = tk.Label(root, image = img)
		print(antwort)
		rich = tk.Label(test, text="Richtig!")
		rich.pack()
	else:
		print(antwort)
		fal = tk.Label(test, text="Falsch!")
		fal.pack()
	bWeiter = tk.Button(test, text="Weiter", command=lambda: nextq())
	bWeiter.pack()

def callback(antwort):
    print(antwort.get())
    return True

def start_test():
	print ("Test started!")
	test = tk.Tk()
	test.title("Test")
	
	fr1_lab = tk.Label(test, text="Frage 1").pack()
	fr1 = tk.Label(test, text="An welchen Fluß liegt die Hauptstadt Deutschlands? (mit Praepasition und artikel)")
	fr1.pack()
	antwort = tk.StringVar()
	fr1_entry = tk.Entry(test, width=40, textvariable=antwort, validatecommand=callback(antwort))
	fr1_entry.pack()
	#fr1_entry.bind("<Return>", check)
	bCheck = tk.Button(test, text="Prüfen", command=lambda: check(test, fr1_entry.get()))
	bCheck.pack()


def goopage(root):
	webbrowser.open('https://accounts.google.com')
	bBegin = tk.Button(root, width=15, height=1, text="Start Test", command=lambda: start_test())
	bBegin.grid(row=2, column=0)
	

def show_readme():
	os.system("gedit README.md")

root = tk.Tk()
root.geometry("350x200+50+60")
root.title("Herzlichen willkommen!")

text = tk.Text(root, width=40, height=7)
text.grid(row=0, column=0, columnspan=2)
text.insert('1.0', "Hallo!\n")
text.insert('end', "Sie beginnen den Test. Sind Sie bereit?")

bJa = tk.Button(root, width=15, height=1, text="Ja! Natürlich!", command=lambda: start_test())
bJa.grid(row=1, column=0)

bWas = tk.Button(root, width=15, height=1, text="Was ist hier los?", command=lambda: show_readme())
bWas.grid(row=1, column=1)

root.mainloop()