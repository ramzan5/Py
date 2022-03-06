# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def pasword_gen():
    nr_letters= random.randint(2,4)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)


    st = ""
    for i in range(0,nr_letters):
      st += letters[random.randint(0,25)]

    for j in range(0,nr_symbols):
      st += symbols[random.randint(0,8)]

    for j in range(0,nr_numbers):
      st += numbers[random.randint(0,9)]
    nstr = ""
    for i in range(0,len(st)-1):
       nstr += st[random.randint(0,len(st)-1)]
    placer2.insert(0,nstr)

# ---------------------------- SAVE PASSWORD ------------------------------- #
import json
def save_password():
    website_val = placer.get()
    email_val = placer1.get()
    pasword = placer2.get()
    my_dict = {
        website_val:{
            "email":email_val,
            "password":pasword
        }
    }
    if len(website_val)==0 or len(email_val)==0 or len(pasword)==0:
        messagebox.showinfo(title='Oops',message="Please Make sure that you have not left anything")
    else:
        try:
            with open("Data.json",'r') as file:
                data = json.load(file)

        except FileNotFoundError:
            with open('Data.json','w') as file:
                json.dump(my_dict, file, indent=4)
        else:
            data.update(my_dict)
            with open('Data.json','w') as file:
                json.dump(data, file, indent=4)
        finally:
            placer.delete(0, END)
            placer1.delete(0, END)
            placer2.delete(0, END)
# ----------------------------Search of Password-----------------------#


def search_password():
    web_name = placer.get()
    try:
        with open('Data.json','r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error',message="Data file does not exits")
    else:
        if web_name in data:
                email = data[web_name]['email']
                pasword = data[web_name]['password']
                messagebox.showinfo(title='Result',message=f'Email: {email}\n password: {pasword}')
        else:
            messagebox.showinfo(title='Error',message="Data does not exits in file")
        placer.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
screen = Tk()
screen.title("Password Manager")
# screen.minsize(width=500,height=400)
screen.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

website = Label(text='Website',font=('Arail',12))
website.grid(row=1,column=0)
placer = Entry(width=21)
placer.focus()

placer.grid(row=1,column=1)
email = Label(text='Email',font=('Arail',12))
email.grid(row=2,column=0)
placer1 = Entry(width=35)
placer1.grid(row=2, column=1, columnspan=2)
pasword = Label(text='Password',font=('Arail',12))
pasword.grid(row=3,column=0)

placer2 = Entry(width=21)

placer2.grid(row=3,column=1)
btn = Button(text='Generate',command=pasword_gen)
btn.grid(row=3,column=2)
btn1 = Button(text="Add",width=34, command=save_password)
btn1.grid(row=4,column=1,columnspan=2)

btn2 = Button(text="Search",command=search_password)
btn2.grid(row=1,column=2)
screen.mainloop()
