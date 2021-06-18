import tkinter
from tkinter import *
import random


questions=[
    "Which cricketer has scored the fastest hundred in the IPL ?",
    "Which cricketer has won the most number of IPL titles ?",
    "Who scored the first century in the first IPL ?",
    "Who is the costliest player in the IPL auction history ?",
    "When was first IPL started ?",
    "Which player has made highest numbers of runs in IPL history ?",
    "Which player has taken most number of wickets in IPL so far ?",
    "Which team has never won the IPL tournament ?",
    "Maximum how many foreign players can play in the playing eleven of the IPL match ?",
    "Which player has taken most numbers of hat-tricks in the IPL so far ?",
    "Which team won IPL title in the year 2012?",
    "Why was the second season of the IPL moved to South Africa?",
    "What is the name of the format in league matches of IPL?",
    "Who became the first batsman to score 5000 runs in IPL?",
    "___________ and Jonny Bairstow (Sunrisers Hyderabad) recorded the highest first-wicket partnership in the IPL (185 runs)"

]

answers_choice=[
    [
            "Virat Kohli",
            "David Warner",
            "AB de Villiers",
            "Chris Gayle"
        ],
    [
            "Rohit Sharma",
            "MS Dhoni",
            "Virat Kohli",
            "Gautam Gambhir"
        ],
[
            "Michael Hussey",
            "Brendon McCullum",
            "Rohit Sharma",
            "Suresh Raina"
        ],
[
            "Yuvraj Singh",
            "Jaydev Unadkat",
            "Glenn Maxwell",
            "Ben Stokes"
        ],
[
            "2006",
            "2007",
            "2009",
            "2008"
        ],
[
            "David Warner",
            "Chris Gayle",
            "Virat Kohli",
            "Suresh Raina"
        ],
[
            "Dwayne Bravo",
            "Zaheer Khan",
            "Ravindra Jadeja",
            "Lasith Malinga"
        ],
[
            "Royal Challengers Bangalore",
            "Rajasthan Royals",
            "Sunrisers Hyderabad",
            "Deccan Chargers"
        ],
[
            "3",
            "5",
            "4",
            "Not fixed, depends on the decision of captain of the team"
        ],
[
            "Yuvraj Singh",
            "Praveen Kumar",
            "Amit Mishra",
            "Dwayne Bravo"
        ],
[
            "CSk",
            "RR",
            "KKR",
            "DC"
        ],
[
            "Better facilities",
            "India’s national elections",
            "Weather issues",
            "Sponsor demands"
        ],
[
            "Double Round-Jules",
            "Double Round-Ethan",
            "Double Round-Robin",
            "Double Round-Lewis"
        ],
[
            "David warner",
            "Suresh Raina",
            "Virat kohli",
            "Rohit Sharma"
        ],
[
            "David Warner",
            "Kane Williamson",
            "Martin Guptill",
            "Deepak Hooda"
        ],


]


answers = [3,0,1,0,3,2,3,0,2,2,2,1,2,1,0]

user_answer=[]


randomlist=[]
def randomlistgen():
    global randomlist
    while(len(randomlist)<10):
        x=random.randint(0,14)
        if x in randomlist:
            continue
        else:
            randomlist.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage=Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext=Label(
        root,
        font=("Consolas",20),
        background="#ffffff",

    )
    labelresulttext.pack()
    if score>=90:
        img=PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You Are Excellent !!")
    elif (score>=20 and score<90):
        img=PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You Can be Better !!")
    else:
        img=PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You Should Work Hard !!")


def calc():
    global randomlist,user_answer,answers
    x=0
    score=0
    for i in randomlist:
        if user_answer[x]==answers[i]:
            score=score+10
        x+=1
    print(score)
    showresult(score)


ques=1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x=radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques<10:
        lblQuestion.config(text=questions[randomlist[ques]])
        r1["text"]=answers_choice[randomlist[ques]][0]
        r2["text"]=answers_choice[randomlist[ques]][1]
        r3["text"]=answers_choice[randomlist[ques]][2]
        r4["text"]=answers_choice[randomlist[ques]][3]
        ques+=1
    else:
        print(randomlist)
        print(user_answer)
        calc()


def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion=Label(
        root,
        text=questions[randomlist[0]],
        font=("Times New Roman",16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff"
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)

    r1=Radiobutton(
        root,
        text=answers_choice[randomlist[0]][0],
        font=("Perpetua",12),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r1.pack(pady=5)

    r2=Radiobutton(
        root,
        text=answers_choice[randomlist[0]][1],
        font=("Perpetua",12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r2.pack(pady=5)

    r3=Radiobutton(
        root,
        text=answers_choice[randomlist[0]][2],
        font=("Perpetua",12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r3.pack(pady=5)

    r4=Radiobutton(
        root,
        text=answers_choice[randomlist[0]][3],
        font=("Perpetua",12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    randomlistgen()
    startquiz()


root=tkinter.Tk()
root.title("IPL_quiz")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)

img1=PhotoImage(file="ipl_logo.png")

labelimage=Label(
    root,
    image=img1,
    background="#ffffff",
)
labelimage.pack()

labeltext=Label(
    root,
    text="IPL_quiz",
    font=("Segoe UI",24,"bold"),
    background="#ffffff",
)
labeltext.pack(pady=(0,20))


img2=PhotoImage(file="button.png")
btnStart=Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command=startIspressed,
)
btnStart.pack()

lblInstruction=Label(
    root,
    text="Read The Rules And\nClick Start Once You Are Ready",
    background="#ffffff",
    font=("Cambria",12),
    justify="center",
)
lblInstruction.pack(pady=(60,16))

lblRules=Label(
    root,
    text="This Quiz Contains 10 Questions\nOnce You Select a Radio Button That Will be a Final Choice\nHence Think Before You Select",
    width=100,
    font=("Bookman Old Style",14),
    background="#000000",
    foreground="#FACA2F",
)
lblRules.pack()


root.mainloop()
