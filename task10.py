from tkinter import *
from tkinter import scrolledtext, messagebox, ttk, filedialog, Menu
from tkinter.ttk import Combobox, Checkbutton, Progressbar
from os import path

window = Tk()
window.title("Шапошников Александр Дмитриевич")

window.geometry("400x300")

def exitOnClick():
    exit()

def uploadFileOnClick():
    with filedialog.askopenfile(filetypes = (("Text files","*.txt"),("all files","*.*")),initialdir=path.dirname(__file__)) as file:
        txtField.delete(1.0,END)
        txtField.insert(1.0,file.read())
    

menu = Menu(window)
window.config(menu=menu)
new_item = Menu(menu, tearoff=0) 
new_item.add_command(label='Загрузить файл', command = uploadFileOnClick)
new_item.add_command(label='Выход', command = exitOnClick)
menu.add_cascade(label='Файл', menu=new_item)

tab_control = ttk.Notebook(window) 

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control) 
tab3 = ttk.Frame(tab_control,padding=5) 
tab_control.add(tab1, text='Калькулятор') 
tab_control.add(tab2, text='Чекбоксы') 
tab_control.add(tab3, text='Текст') 

# 1 вкладка
subFr1 = ttk.Frame(tab1)
subFr1.place(anchor='c',relx=0.5,rely=0.5)

inputNum1=Entry(subFr1,width=15,justify=RIGHT)
inputNum1.grid(row= 0, column=0, padx=5, pady=5)


operation = Combobox(subFr1,width=2)
operation['values'] = ('+', '-', '*', '/') 
operation.current(0)
operation.grid(row= 0, column=1, padx=5, pady=5)


inputNum2=Entry(subFr1,width=15, justify=RIGHT)
inputNum2.grid(row= 0, column=2, padx=5, pady=5)


def calc(a,b,oper):
    try:
        a=float(a)
        b=float(b)        
        resField.configure(state='normal')
        resField.delete(0,END)
        if oper == '+':
            resField.insert(0, str(a+b))
        elif oper == "-":
            resField.insert(0, str(a-b))
        elif oper == "*":
            resField.insert(0, str(a*b))
        elif oper == "/":
            if b != 0:
                resField.insert(0, str(a/b))
        resField.configure(state='disabled')
    except ValueError:
        messagebox.showerror("Ошибка","Числа введены неверно")
        resField.configure(state='disabled')
        return

def equalsOnClick():
    calc(inputNum1.get(),inputNum2.get(),operation.get())

equals = Button(subFr1, text="=", command=equalsOnClick)
equals.grid(row= 0, column=3, padx=5, pady=5)


resField=Entry(subFr1,width=15, state='disabled')
resField.grid(row= 0, column=4, padx=5, pady=5)


# 2 вкладка
def chkBoxResBtnOnClick():
    arrStr = []
    if chk1_state.get():
        arrStr.append("первый")
    if chk2_state.get():
        arrStr.append("второй")
    if chk3_state.get():
        arrStr.append("третий")  
    if len(arrStr)==0:
        messagebox.showinfo("Информация","Вы не выбрали ни одного варианта")
        return
    resStr=", ".join(arrStr)     
    messagebox.showinfo("Информация","Вы выбрали "+ resStr + (" вариант" if len(arrStr)==1 else " варианты"))


subFr2 = ttk.Frame(tab2)
subFr2.place(anchor='c',relx=0.5,rely=0.5)

chk1_state = BooleanVar() 
chk1_state.set(False)
chk2_state = BooleanVar() 
chk2_state.set(False)
chk3_state = BooleanVar() 
chk3_state.set(False)
chk1 = Checkbutton(subFr2, text='Первый', var=chk1_state) 
chk1.grid(column=0, row=0) 
chk2 = Checkbutton(subFr2, text='Второй', var=chk2_state) 
chk2.grid(column=1, row=0) 
chk3 = Checkbutton(subFr2, text='Третий', var=chk3_state) 
chk3.grid(column=2, row=0) 

chkBoxResBtn = Button(subFr2, text="Информация", command=chkBoxResBtnOnClick)
chkBoxResBtn.grid(row= 0, column=3)


# 3 вкладка
txtField = scrolledtext.ScrolledText(tab3,width=40,height=10)
txtField.pack(expand=1, fill=BOTH)

tab_control.pack(expand=1, fill=BOTH)

window.mainloop()