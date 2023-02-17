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
WORK_REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_label.config(text="")
    global WORK_REPS
    WORK_REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global WORK_REPS
    WORK_REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if WORK_REPS % 2 == 0:
        title_label.config(text="Short break", fg=PINK)
        count_down(short_break_sec)
    elif WORK_REPS % 8 == 0:
        title_label.config(text="Long break", fg=RED)
        count_down(long_break_sec)
    else:
        title_label.config(text="Work time", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # to change canvas not config but itemconfig
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(WORK_REPS / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Productivity")
window.config(padx=100, pady=50, bg=YELLOW)

# label title
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW)
# Photo class from tkinter
tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

# buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)
# check label
check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12))
check_label.grid(column=1, row=3)

window.mainloop()
