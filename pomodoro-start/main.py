from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
COUNTER = ""
rep = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def rest_timer():
    screen.after_cancel(timer)
    canvas.itemconfig(can_var, text="00:00")
    label.config(text="Counter")
    global rep
    rep =0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_mech():
    global rep
    rep +=1
    if rep % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label.config(text="Break",fg=RED)
    elif rep % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN*60)
        label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(cnt):
    cnt_min = cnt // 60
    cnt_sec = cnt % 60
    global timer
    if cnt_sec == 0:
        cnt_sec='00'
    elif cnt_sec < 10 and cnt_sec > 0:
        cnt_sec =f"0{cnt_sec}"
    if cnt_min <10 and cnt_min>=0:
        cnt_min = f'0{cnt_min}'
    canvas.itemconfig(can_var,text=f"{cnt_min}:{cnt_sec}")
    if cnt >0:
       timer= screen.after(1000,count_down,cnt-1)
    else:
        timer_mech()
# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.minsize(500,400)
screen.title("Pomodoro")
screen.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)

can_var = canvas.create_text(100,112,text='00:00',font=("Courier", 24, 'bold'))
canvas.grid(column=1,row=1)


btn1 = Button(text='Start', command=timer_mech)
btn1.grid(row=3,column=0)
btn2 = Button(text='Reset',command=rest_timer)
btn2.grid(row=3,column=2)
label = Label(text="Counter",font=("Courier", 25, 'bold'),fg=GREEN,bg=YELLOW)
label.grid(row=0,column=1)

check = Label(text="✔",bg=YELLOW,fg=GREEN)
check.grid(row=3,column=1)
screen.mainloop()

