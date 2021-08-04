import datetime
import tkinter as tk

window = tk.Tk()
window.geometry("400x470")
window.title(" Age Calculator ")
window['background']='#DCD0FF'
name = tk.Label(text=" Name ", bg="#FBFBF9")
name.grid(column=0, row=1)
year = tk.Label(text="  Year   ", bg="#FBFBF9")
year.grid(column=0, row=2)
month = tk.Label(text="Month", bg="#FBFBF9")
month.grid(column=0, row=3)
date = tk.Label(text="  Day   ", bg="#FBFBF9")
date.grid(column=0, row=4)
nameEntry = tk.Entry()
nameEntry.grid(column=1, row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1, row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1, row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1, row=4)


def getInput():
    name = nameEntry.get()
    person = Person(name, datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get())))

    textArea = tk.Text(master=window, height=10, width=35)
    textArea.grid(column=1, row=6)
    answer = "Hey {person}!.You are {age} years old. ".format(person=name, age=person.age())
    textArea.insert(tk.END, answer)


button = tk.Button(window, text="Calculate Age", command=getInput, bg="#00FA9A")
button.grid(column=1, row=5)


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age

window.mainloop()