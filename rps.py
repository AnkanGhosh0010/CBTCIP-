#PROJECT ROCK PAPER SCISSORS
#Author: Ankan Ghosh
#Assigned by: Cipher Technologies
#date: 17.11.23 

from tkinter import *
from PIL import Image,ImageTk
from random import randint

#main window
root=Tk()

root.title("Rock Paper Scissors !")
root.configure(background="white")

#images
rock_img=ImageTk.PhotoImage(Image.open("rock.png"))
paper_img=ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img=ImageTk.PhotoImage(Image.open("scissors.png"))
rock_img_c=ImageTk.PhotoImage(Image.open("rock_c.png"))
paper_img_c=ImageTk.PhotoImage(Image.open("paper_c.png"))
scissors_img_c=ImageTk.PhotoImage(Image.open("scissors_c.png"))

#insert image
user_label=Label(root,image=paper_img,bg="white")
comp_label=Label(root,image=paper_img_c,bg="white")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#points
userScore=Label(root,text=0,font=("Helvetica", 15, "bold"),bg="white",fg="black")
userScore.grid(row=1,column=3)
compScore=Label(root,text=0,font=("Helvetica", 15, "bold"),bg="white",fg="black")
compScore.grid(row=1,column=1)


#indicator
user_indicator=Label(root,font=("Helvetica", 15, "bold"),text="USER",bg="black",fg="white").grid(row=0,column=3)
comp_indicator=Label(root,font=("Helvetica", 15, "bold"),text="COMP",bg="black",fg="white").grid(row=0,column=1)

#message
msg=Label(root,font=("Helvetica", 15, "bold"),bg="white")
msg.grid(row=3,column=2)

#update message

def updateMessage(a):
    msg['text']=a

#update user score
def updateUserScore():
    score=int(userScore["text"])
    score+=1
    userScore["text"]=str(score)

#update comp score
def updateCompScore():
    score=int(compScore["text"])
    score+=1
    compScore["text"]=str(score)    

#check winner
def checkWinner(user,comp):
    if user==comp:
        updateMessage("It's a TIE")
    elif user=="rock":
        if comp=="paper":
            updateMessage("You LOOSE")
            updateCompScore()
        else:
            updateMessage("You WIN")
            updateUserScore()
    elif user=="paper":
        if comp=="scissors":
            updateMessage("You LOOSE")
            updateCompScore()
        else:
            updateMessage("You WIN")
            updateUserScore()
    elif user=="scissors":
        if comp=="rock":
            updateMessage("You LOOSE")
            updateCompScore()
        else:
            updateMessage("You WIN")
            updateUserScore()
    else: 
        pass    

#update choices
choices=["rock","paper","scissors"]
def updateChoice(x):
#for computer
    compChoice= choices[randint(0,2)]
    if compChoice=="rock":
        comp_label.configure(image=rock_img_c)
    elif compChoice=="paper":
        comp_label.configure(image=paper_img_c)
    else:
        comp_label.configure(image=scissors_img_c)

 #for user   
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissors_img)

    checkWinner(x,compChoice)

#buttons
rock=Button(width=20,height=2,text="ROCK",bg="red",fg="white",command= lambda: updateChoice("rock")).grid(row=2,column=1)
paper=Button(width=20,height=2,text="PAPER",bg="green",fg="white",command= lambda: updateChoice("paper")).grid(row=2,column=2)
scissors=Button(width=20,height=2,text="SCISSORS",bg="blue",fg="white",command= lambda: updateChoice("scissors")).grid(row=2,column=3)

root.mainloop()