from tkinter import  *

'''Miles to KM converter'''

screen = Tk()
screen.minsize(200, 200)
screen.title('Converter')

# Label
label = Label(text="Converter",font=('Arial', 24),fg='blue')
label.grid(column=2, row=1)

entry = Entry()
entry.grid(column=2, row=3)

label2 = Label(text="Miles",font=('Arial', 14),fg='red')
label2.grid(column=3, row=3)

label3 = Label(text='0',font=('Arial', 14),fg='red')
label3.grid(column=2, row=4)


label4 = Label(text="KM",font=('Arial', 14),fg='red')
label4.grid(column=3, row=4)


def calculate():
    input = int(entry.get())
    converted_val = round((input * 1.609),2)
    label3.config(text=converted_val)


btn = Button(text='Calculate', command=calculate)
btn.grid(column=2,row=5)

screen.mainloop()
