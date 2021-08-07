import tkinter
from tkinter import *
from tkinter import messagebox
import random 
from random import shuffle

answers = ["America", "India", "Australia", "Antartica", "Italy", "Iran"]
questions = []

for i in answers:
     words = list(i)
     shuffle(words)
     questions.append(words)

num = random.randint(0, len(questions)-1)

def initial():
    global questions, num
    lb1.configure(text = questions[num])

def answercheck():
    global questions, num, answers
    userinput = e1.get()
    if userinput == answers[num]:
        messagebox.showinfo("SUCCESS","Your answer is correct")
    else:
        messagebox.showinfo("ERROR","Your answer is wrong")
        e1.delete(0,END)

def resetswitch():
    global questions, answers, num
    num = random.randint(0, len(questions)-1)
    lb1.configure(text = questions[num])
    e1.delete(0,END)

window = Tk()
window.geometry("300x300")
window.configure(background = "#03203C" )
window.title("JumbleBot")

lb1 = Label (window, font = '20', bg = "#03203C", fg = "#CAD5E2")
lb1.pack(pady = 30, ipadx = 5, ipady = 5)

answer = StringVar()
e1 = Entry (window, textvariable = answer)
e1.pack(ipady = 5, ipadx = 5)

b1 = Button(window, text = "Check", bg = "#1FAA59", width = 20,command = answercheck )
b1.pack(pady = 40)

b2 = Button(window, text = "Reset", bg = "#BF3325", width = 20, command = resetswitch )
b2.pack()

initial()
window.mainloop()