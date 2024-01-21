# Задание: даны самые популярные репозитории на github
# https://habr.com/ru/post/453444/, по последней цифре зачетки получить JSON
# для вашего варианта .
# Программа с графическим интерфейсом вводим в поле имя репозитория и по 
# нажатию кнопки получаем результат.
# Необходимо получить в новый файл следующую информацию:
# 'company': None,
# 'created_at': '2015-08-03T17:55:43Z',
# 'email': None,
# 'id': 13629408,
# 'name': 'Kubernetes',
# 'url': 'https://api.github.com/users/kubernetes'}
from tkinter import *
from tkinter import scrolledtext, messagebox, ttk, filedialog, Menu
from tkinter.ttk import Combobox, Checkbutton, Progressbar
from os import path
import json
import requests
from pprint import pprint

window = Tk()
window.title("Шапошников Александр Дмитриевич")
window.geometry("400x300")
window.resizable(False, False)

inputName=Entry(window,width=50)
inputName.grid(column=1, row=1, padx = 10, pady = 10)
inputName.focus()
inputName.insert(0,"Firehol")

def applyBtnOnClick():
    outputField.delete(1.0,END)
    response = requests.get('https://api.github.com/users/'+inputName.get())
    if not response:
        outputField.insert(1.0,'Ответ не получен')
        return
    info = json.loads(response.text)
    result = {
        "company": info["company"],
        "created_at": info["created_at"],
        "email": info["email"],
        "id": info["id"],
        "name": info["name"],
        "url": info["url"]}
    outputField.insert(1.0, json.dumps(result, indent=6))
    with open("task11_output.json", "w+") as write_file:
        json.dump(result, write_file, indent=2)

applyBtn = Button(window, text="Загрузить",command=applyBtnOnClick)
applyBtn.grid(column=2,row=1)

outputField = scrolledtext.ScrolledText(window,width=47,height=15)
outputField.grid(column=1, row=2, sticky='w', columnspan=2)


window.mainloop()