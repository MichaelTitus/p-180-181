from tkinter import*
from tkinter import ttk
from googletrans import Translators,LANGUAGES

root=Tk()
root.geometry("600x700")
root.title("Google+Alexa+Siri")

language=list(LANGUAGES.value())

lblTitle=Label(root,text="Language translator")
lblTitle.place(relx=0.5,rely=0.1,anchor=CENTER)

input_label=Label(root,text="Select language")
input_label.place(relx=0.02,rely=0.2,anchor=W)

srclanguage=ttk.Combobox(root,values=language,width=22,state="readonly")
srclanguage.place(relx=0.13,rely=0.2,anchor=W)
srclanguage.set("english")

output_label=Label(root,text="Select output")
output_label.place(relx=0.81,rely=0.2,anchor=E)

destlanguage=ttk.Combobox(root,values=language,width=22,state="readonly")
destlanguage.place(relx=0.98,rely=0.2,anchor=E)
destlanguage.set("Choose output language")

inputText=Text(root,width=60,height=10)
inputText.place(relx=0.02,rely=0.5,anchor=W)

outputText=Text(root,width=60,height=10)
outputText.place(relx=0.98,rely=0.5,anchor=E)