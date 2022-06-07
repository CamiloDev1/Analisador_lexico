from ctypes.wintypes import tagMSG
from hashlib import new
import re
from unicodedata import name
from Gram2 import gramatica
from tkinter import StringVar, ttk

import tkinter
import pandas as pd
window = tkinter.Tk()
pd.set_option("display.max_rows", None, "display.max_columns", None)
window.title("Analizador Lexico")
window.geometry("850x350")
window.configure(background='#51A7D5')
s = ttk.Style()
s.theme_use('clam')

# Configure the style of Heading in Treeview widget
s.configure('Treeview.Heading', background="#48FF23")
table = ttk.Treeview(window, columns=(
"#1", "#2", "#3"),show='headings') 
table.heading("#1", text="token") 
table.heading("#2", text="valor")
table.heading("#3", text="incidencias")
table.column("#1", width=100)  
table.column("#2", width=150)
table.column("#3", width=100)
table.place(x=450, y=30, height=290)
table.tag_configure('odd', background='#CDF1FB')
table.tag_configure('even', background='#CDF1FB')

newInput=""
def ObtenerCadena():
    table.delete(*table.get_children())
    x= entry.get()
    x=x.split(" ")
    evaluate(x)
def evaluate(input):
    for i in range(len(gram.reserved)):
        result = re.findall(r""+gram.reserved[i]+"\\b",input)
        if(i%2==0):
            table.insert('','end',values=(gram.tokens[i],result,len(result)),tags=('odd'))
        else:
            table.insert('','end',values=(gram.tokens[i],result,len(result)),tags=('even'))
    for i in range(len(gram.simbols)):
        result = re.findall(gram.simbols[i],newInput)
        if(i%2==0):
            table.insert('','end',values=(gram.tokens[i+8],result,len(result)),tags=('odd'))
        else:
            table.insert('','end',values=(gram.tokens[i+8],result,len(result)),tags=('even'))
    chain=""
    for i in range(len(gram.simbols2)):
        result = re.findall(gram.simbols2[i],input)
        if(len(result)>0):
            for j in range(len(result)):
                chain=chain+result[j]+", "
    print(chain)
    textTitle.set(chain)

if __name__ == "__main__":
    gram = gramatica()
    entry = ttk.Entry(window)

    entry.config(width=50)
    # Posicionarla en la ventana.
    entry.place(x=65, y=120)
    textTitle=StringVar()
    texto2 = tkinter.Label(window,text="TOKENS IRRECONOCIDOS:",font=12,background='#51A7D5').place(x=80,y=150) 
    texto1 = tkinter.Label(window,text="",font=12,textvariable= textTitle,background='#51A7D5').place(x=60,y=180) 
    T = tkinter.Text(window, height = 10, width = 52)
    boton = tkinter.Button(text="verificar tokens", command=ObtenerCadena)
    boton.place(x=150, y=300)
    window.mainloop()

