from tkinter import *
import random

root = Tk()

root.geometry("1280x720")
lb = Label(text="Password Generator", font=20)
lb.pack(pady=20)

lb2 = Label(root, text="Length", font=('calibre',10, 'bold'))

length = IntVar()
en2 = Entry(root, textvariable = length, font=('calibre',10,'normal'))

# variables area
Uppercase = IntVar()
Lowercase = IntVar()
Special_chars = IntVar()
Numbers = IntVar()

# Checkbox area
Upper = Checkbutton(root, text = "Uppercase", variable = Uppercase, onvalue = 1, offvalue = 0,height = 2, width = 10)
Lower = Checkbutton(root, text = "Lowercase", variable = Lowercase, onvalue = 1, offvalue = 0,height = 2, width = 10)
NumbersX = Checkbutton(root, text = "Numbers", variable = Numbers, onvalue = 1, offvalue = 0,height = 2, width = 10)
Special_charsX = Checkbutton(root, text = "Special chars", variable = Special_chars, onvalue = 1, offvalue = 0,height = 2, width = 10)

# generating password area
def Generate(Uppercase, Lowercase, Number, Special_char, length):
    gen = ""
    if Uppercase == 1:
        gen = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if Lowercase == 1:
        gen += "abcdefghijklmnopqrstuvwxyz"
    if Number == 1:
        gen += "1234567890"
    if Special_char == 1:
        gen += "!@#$%^&*()-_=+{[}]|\;:'*<>.,?/"
            
    password = "".join(random.sample(gen, length))
    passwd.set(password)

# password printing area
passwd = StringVar()
printing_tab = Entry(root, textvariable=passwd, justify=CENTER)

#button
button = Button(root, text = "Generate", command = lambda : Generate(Uppercase.get(), Lowercase.get(),  Numbers.get(), Special_chars.get(), length.get()))

# packing area
lb2.pack()
en2.pack()
Upper.pack()
Lower.pack()
NumbersX.pack()
Special_charsX.pack()
printing_tab.pack(pady=8)
button.pack()

root.mainloop()