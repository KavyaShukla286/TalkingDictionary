from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3

engine=pyttsx3.init()
voice=engine.getProperty('voices')
# engine.setProperty('voice',voice[0].id)
engine.setProperty('voice',voice[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 118)
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

root =Tk() # root is object of tkinter class
root.geometry('728x628')
root.resizable(0,0)
root.iconbitmap('r.ico')
root.title('Talking Dictionary')

root.configure(bg='papaya whip')

def search():
    data=json.load(open('data.json'))
    word=enterwordEntry.get()
    word=word.lower()
    if word in data:
        meaning=data[word]
        textarea.delete(1.0,END)
        for item in meaning:
            textarea.insert(END,u'\u2022'+''+item+'\n\n')
    elif len(get_close_matches(word, data.keys())) > 0: #some similar word is serached
        close_match = get_close_matches(word, data.keys())[0]
        res=messagebox.askyesno('confirm','Did you mean '+close_match+' instead?')
        if res==True:#is clicked yes
            enterwordEntry.delete(0,END) #wrong spelling gets deletd
            enterwordEntry.insert(END,close_match)
            meaning=data[close_match]
            textarea.delete(1.0, END)
            for item in meaning:
                textarea.insert(END, u'\u2022' + '' + item + '\n\n')
        else:
            messagebox.showerror('Error','Please check the word')
            enterwordEntry.delete(0,END)
            textarea.delete(1.0,END)
    else:
        messagebox.showinfo("Information","The word doesnt exist")
        enterwordEntry.delete(0,END)
        textarea.delete(1.0,END)

def clear():
    enterwordEntry.delete(0,END)
    textarea.delete(1.0,END)

def exit():
    res=messagebox.askyesno('Confirm','Do you want to exit?')
    if res==True:
        root.destroy()
    else:
        pass

def wordaudio():
    engine.say(enterwordEntry.get())
    engine.runAndWait()

def meaningaudio():
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()

enterwordlabel=Label(root,text='Enter Word',font=('castellar','29','bold'),fg='red3',bg='papaya whip')
enterwordlabel.place(x=215,y=21)

enterwordEntry=Entry(root,font=('arial','23','bold'),bg='ivory',justify=CENTER,bd=8,relief=GROOVE)
enterwordEntry.place(x=190,y=80)

searchimage=PhotoImage(file='search.png')
searchButton=Button(root,image=searchimage,bd=0,bg='papaya whip',cursor='hand2',activebackground='papaya whip',comman=search)
searchButton.place(x=273,y=150)

micimage=PhotoImage(file='mic.png')
micButton=Button(root,image=micimage,bd=0,bg='papaya whip',cursor='hand2',activebackground='papaya whip',command=wordaudio)
micButton.place(x=379,y=153)

meaninglabel=Label(root,text='Meaning',font=('castellar','29','bold'),fg='red3',bg='papaya whip')
meaninglabel.place(x=250,y=241)

textarea=Text(root,width=39,height=8,font=('arial',16,'bold'),bg='ivory',bd=8,wrap='word',relief=GROOVE)
textarea.place(x=123,y=300)

audioimage=PhotoImage(file='microphone.png')
audioButton=Button(root,image=audioimage,bd=0,bg='papaya whip',cursor='hand2',activebackground='papaya whip',command=meaningaudio)
audioButton.place(x=215,y=535)

clearimage=PhotoImage(file='clear.png')
clearButton=Button(root,image=clearimage,bd=0,bg='papaya whip',cursor='hand2',activebackground='papaya whip',command=clear)
clearButton.place(x=325,y=535)

exitimage=PhotoImage(file='exit.png')
exitButton=Button(root,image=exitimage,bd=0,bg='papaya whip',cursor='hand2',activebackground='papaya whip',command=exit)
exitButton.place(x=445,y=535)

def enter_function(e):
    searchButton.invoke()

root.bind('<Return>',enter_function) #when pressing enter key

root.mainloop()
