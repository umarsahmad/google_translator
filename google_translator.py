# google trasnlator with gui

pip install google translator and tkinter

from tkinter import *
from tkinter import ttk # combo box 

from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
	
	text1=text
	src1=src
	dest1=dest

	trans = Translator() # creating object

	trans1 = trans.translate(text,src1,dest1)

	return(trans1.text) # to only sned the text data otherwise see what it'll send

def data():
	s = comn_sor.get()
	d = comb_dest.get()
	msg = sor_txt.get(1.0,END) # starting to end all data
	textget = change(text = msg, src=s, dest=d)

	dest_txt.delete(1.0,END) # delete all data inside dest box
	dest_txt.insert(END,textget) 

#########################################################################

root = Tk()

root.title("Translator")
root.geometry("500x700")
root.config(bg= 'Red')

lab_txt = Label(root, text="Translator", font=("Time New Roman", 40, "bold")) # for creating label
lab_txt.place(x=100, y=40, height=50,width=300)

frame = Frame(root).pack(side=BOTTOM) # creating frame


lab_txt = Label(root, text="Source Text", font=("Time New Roman", 20, "bold"),bg='Red',fg= 'Blue') # for creating label
lab_txt.place(x=100, y=100, height=20,width=300)



sor_txt = Text(frame,font=("Time New Roman", 20, "bold"),wrap=WORD) 
sor_txt.place(x=10, y=120, height=150,width=480) # for placement

#list_text = [1,2,3,4]
list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value=list_text) # combo box 1 source ka
comb_sor.place(x=10, y=300, height=40,width=100)
comb_sor.set("english")

button_change = Button(frame,text = 'Translate',relief=RAISED,command=data) # calling the data function
button_change.place(x=170, y=300, height=40,width=100)

comb_dest = ttk.Combobox(frame,value=list_text) # combo box 1 source ka
comb_dest.place(x=330, y=300, height=40,width=150)
comb_dest.set("english")


dest_txt = Label(root, text="Destination Text", font=("Time New Roman", 20, "bold"),bg='Red',fg= 'Blue') # for creating label
dest_txt.place(x=100, y=100, height=20,width=300)

dest_txt = Text(frame,font=("Time New Roman", 20, "bold"),wrap=WORD)  # for destination
dest_txt.place(x=10, y=400, height=150,width=480) # for placement


root.mainloop() # for creating graphics

