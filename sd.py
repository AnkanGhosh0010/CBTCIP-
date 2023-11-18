#PROJECT Voice Recorder
#Author: Ankan Ghosh
#Assigned by: Cipherbyte Technologies
#date: 18.11.23 

import sounddevice as sd
from scipy.io.wavfile import write
from tkinter import *
from tkinter.messagebox import showinfo,showwarning
from tkinter.filedialog import askdirectory

add=""

#to specify path to save
def file_path():
    global add
    add= askdirectory()


#function to record data
def record():
    global add
    try:
        time=int(sec.get())
        address=add+"/"+"recordedAudio.wav"
        showinfo(title="START",message="Recording Started")
        audio_data= sd.rec((time*44100),samplerate=44100,channels=2)
        sd.wait()

        print("Recording finished.")
        write(address, 44100, audio_data)

        showinfo(title="END",message="Recording STOPPED")

    except:
        showwarning(title="ERROR TIME",message="Invalid Time Format")


def mainWindow():
    global sec
    #window specifications
    root=Tk()
    root.geometry("600x400")
    root.title("VOICE RECORDER")
    root.config(bg="yellow")
    root.resizable(False,False)
    
    #project title
    titlelabel= Label(root,text="VOICE RECORDER",font=("Helvetica",20,"bold"),bg="yellow",fg="black")
    titlelabel.place(x=190,y=10)

    #record button
    mic_img=PhotoImage(file="mic.png")
    micButton=Button(root,image=mic_img,bg="yellow",command=record)
    micButton.place(x=250,y=50)

    #duration entry place
    sec= Entry(root,font=("Helvetica",15))
    sec.place(x=190,y=190)
    timelabel=Label(root,text="Time in sec",font=("Helvetica",10,"bold"),bg="yellow")
    timelabel.place(x=260,y=220)

    #path button
    pathbutton= Button(root,text="Path",font=("Helvetica",10,"bold"),bg="black",fg="white",command= file_path)
    pathbutton.place(x=250,y=245,width=100)

    root.mainloop()

mainWindow()

