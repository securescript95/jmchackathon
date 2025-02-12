import customtkinter
import time

startTime=time.time()
def startButtonPressed():
    stopTime=time.time()
    with open('score.txt','wr')as f:
        read=f.readlines()
        read.append(startTime-StopTime)
        f.write(read)

def newgamePressed():
    tabview.set('tab1')

def highscorep():
    with open ('score.txt','r')as f:
        read=f.readlines()
        return min(read)
def start():
    tabview.set("tab2")
    startTime=time.time()

l=[['','',''],['','',''],['','','']]
def buttonPressed(row,coloumn):
    if l[row-1][coloumn-1]!='':
        l[row-1][column-1]= playerSymbol

app = customtkinter.CTk()
app.title("TIC-TAC-TOE")
app.geometry("800x600")
app.grid_rowconfigure((0,1,2),weight=1)
app.grid_columnconfigure((0,1,2),weight=1)

# INITIATING TAB VIEW
tabview=customtkinter.CTkTabview(app)
tabview.grid(
    row=0,
    column=0,
    padx=0,
    pady=0,
    sticky='nesw',
    rowspan=3,
    columnspan=3,
)


# ADDING TABS
tab1=tabview.add('tab1')
tab2=tabview.add('tab2')

tabview.set('tab1')

# TAB 1
tab1.grid_rowconfigure((1,3),weight=1)
tab1.grid_columnconfigure((0,2),weight=2)
tab1.grid_columnconfigure((0,1,2),weight=1)

# NAME
nameFont=customtkinter.CTkFont(family="Monoton",size=60,)
name = customtkinter.CTkLabel(tab1,
text="TIC-TAC-TOE",
height=40,
width=100,
font=nameFont,
)
name.grid(
    row=0,
    column=1,
    sticky='n',
    pady=(0,10),
    padx=10,
)

# HIGH SCORE LABLE
hs = f'High Score {highscorep}'
hichScoreFont=customtkinter.CTkFont(family="Monoton",size=18,weight='bold')
highscore=customtkinter.CTkLabel(tab1,
text=hs,
font=hichScoreFont,
)
highscore.grid(
    row=1,
    column=1,
    padx=10,
    pady=(0,10),
    ipadx=2,
    ipady=2,
    sticky='new',
)
# PICK SYMBOL LABLE
pickSymbolFont=customtkinter.CTkFont(family="helvatica",size=14,slant='italic')

pickSymbol = customtkinter.CTkLabel(tab1,
text='PICK A SYMBOL',
font=pickSymbolFont,
height=10,
width=20,
)
pickSymbol.grid(
    row=2,
    column=1,
    padx=10,
    pady=(0,100)
)

# PLAYING SYMBOL
options =['O',"X"]
symbol=customtkinter.CTkComboBox(tab1,
values=options,
)
symbol.grid(
    row =2,
    column=1,
    padx=10,
    pady=(20,0),
)
playerSymbol=symbol.get()
# START BUTTON
startButtonFont=customtkinter.CTkFont("Monoton",12,weight='bold',slant='italic')
start=customtkinter.CTkButton(tab1,
text="start",
font=startButtonFont,
command=start,
)
start.grid(
    row=3,
    column=1,
    padx=10,
    pady=10,
)

# TAB 2

tab2.grid_rowconfigure((0,2),weight=1)
tab2.grid_rowconfigure(1,weight=3)
tab2.grid_columnconfigure((0,2),weight=1)
tab2.grid_columnconfigure(1,weight=3)

# HIGH SCORE

highscore2=customtkinter.CTkLabel(tab2,
text=hs,
font=hichScoreFont,
)
highscore2.grid(
    row=0,
    column=1,
    padx=10,
    pady=(0,10),
    ipadx=2,
    ipady=2,
    sticky='ews'
)

# MID FRAME
frame1=customtkinter.CTkFrame(tab2,
)
frame1.grid(row=1,column=1,sticky='nesw')

frame1.grid_rowconfigure((0,1,2),weight=1)
frame1.grid_columnconfigure((0,1,2),weight=1)

startButtonFont=customtkinter.CTkFont(family="Monoton",size=16,weight='bold')

# BUTTONS

# BUTTON 1 1 
b11Text=''
b11=customtkinter.CTkComboBox(frame1,
corner_radius=0,
border_width=2,
border_color='white',
hover=False,
text_color='white',
values=['','O','X'],
font=startButtonFont,
height=100,
width=100,
fg_color='black',
command=buttonPressed(1,1),
)
b11.grid(
    row=0,
    column=0,
    
)

# BUTTON 12
b12Text=''
b12=customtkinter.CTkComboBox(frame1,
corner_radius=0,

border_width=2,
border_color='white',
hover=False,
text_color='white',
values=['','O','X'],
font=startButtonFont,
height=100,
width=100,
fg_color='black',
command=buttonPressed(1,2),
)
b12.grid(
    row=0,
    column=1,
    
)

# BUTTON 13
b13Text=''
b13=customtkinter.CTkComboBox(frame1,
corner_radius=0,

border_width=2,
border_color='white',
hover=False,
text_color='white',
values=['','O','X'],
font=startButtonFont,
height=100,
width=100,
fg_color='black',
command=buttonPressed(1,3),
)
b13.grid(
    row=0,
    column=2,
    
)

#BUTTON 21
b21Text=''
b21=customtkinter.CTkComboBox(frame1,
corner_radius=0,

border_width=2,
border_color='white',
hover=False,
text_color='white',
values=['','O','X'],
font=startButtonFont,
height=100,
width=100,
fg_color='black',
command=buttonPressed(2,1),
)
b21.grid(
    row=1,
    column=0,
    
)

# BUTTON 22
b22Text=''
b22=customtkinter.CTkComboBox(frame1,
corner_radius=0,

border_width=2,
border_color='white',
hover=False,
text_color='white',
values=['','O','X'],
font=startButtonFont,
height=100,
width=100,
fg_color='black',
command=buttonPressed(2,2),
)
b22.grid(
    row=1,
    column=1,
    
)

#BUTTON 23
b23Text=''
b23=customtkinter.CTkComboBox(frame1,
corner_radius=0,

border_width=2,
border_color='white',
hover=False,
text_color='white',
values=['','O','X'],
font=startButtonFont,
height=100,
width=100,
fg_color='black',
command=buttonPressed(2,3),
)
b23.grid(
    row=1,
    column=2,
    
)
# BUTTON 31
b31Text=''
b31=customtkinter.CTkComboBox(frame1,
corner_radius=0,

border_width=2,
border_color='white',
hover=False,
text_color='white',
values=['','O','X'],
font=startButtonFont,
height=100,
width=100,
fg_color='black',
command=buttonPressed(3,1),
)
b31.grid(
    row=2,
    column=0,
    
)
#BUTTON 32
b32Text=''
b32=customtkinter.CTkComboBox(frame1,
corner_radius=0,

border_width=2,
border_color='white',
hover=False,
text_color='white',
values=['','O','X'],
font=startButtonFont,
height=100,
width=100,
fg_color='black',
command=buttonPressed(3,2),
)
b32.grid(
    row=2,
    column=1,
)
#BUTTON 33
b33Text=''
b33=customtkinter.CTkComboBox(frame1,
corner_radius=0,

border_width=2,
border_color='white',
hover=False,
text_color='white',
values=['','O','X'],
font=startButtonFont,
height=100,
width=100,
fg_color='black',
command=buttonPressed(3,3),
)
b33.grid(
    row=2,
    column=2,
    
)


# BOTTOM FRAME
frame2=customtkinter.CTkFrame(tab2)
frame2.grid(
    row=2,
    column=1,
    sticky='news',
)
frame2.grid_rowconfigure(0,weight=1)
frame2.grid_rowconfigure(1,weight=2)
frame2.grid_columnconfigure((0,1),weight=1)

# TIME
TimeFont=customtkinter.CTkFont(family="Monoton", size=14,weight='bold')

timeText='Time'
timeLable=customtkinter.CTkLabel(frame2,
text=timeText,
font=TimeFont,
)
timeLable.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky='news'
)
#buttons

newgameFont=customtkinter.CTkFont(family='Monoton',size=14,weight='bold')
newgame=customtkinter.CTkButton(frame2,
text= 'New Game',
font=newgameFont,
command=newgamePressed
)
newgame.grid(
    row=1,
    column=0,
    pady=10,
    padx=10,
    sticky='n',
)

ssButton=customtkinter.CTkButton(frame2,
font=newgameFont,
text = 'Start/Stop',
command=startButtonPressed,
)
ssButton.grid(
    row=1,
    column=1,
    padx=10,
    pady=10,
    sticky='n',
    
)

app.mainloop()