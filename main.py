from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)


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

reset = Button(text="Reset",  highlightthickness=0)
reset.grid(column=2, row=2)

check_marks = Label(text='✓', fg = GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2)







window.mainloop()