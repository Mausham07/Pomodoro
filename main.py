from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.25
SHORT_BREAK_MIN = 0.25
LONG_BREAK_MIN = 0.25
repition = 0
timer = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global repition
    repition = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global repition
    repition += 1

    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60

    if repition % 8 == 0:
        timer_label.config(text="Break", fg = RED)
        count_down(long)
        

    elif repition % 2 == 0:
        timer_label.config(text="Break", fg = PINK)
        count_down(short_break)

    else:
        timer_label.config(text="Work", fg = GREEN)
        count_down(work)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec  < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer =  window.after(1000, count_down, count-1)
       

    else:
        start_timer()
        marks = ""
        work_session = math.floor(repition/2)
        for _ in work_session:
            marks += "✓"

        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height = 224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", fg = GREEN, font=(FONT_NAME, 50), bg=YELLOW)
timer_label.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset",  highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

check_marks = Label(fg = GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2)







window.mainloop()