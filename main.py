import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
GRAY = "#505050"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    iteration_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Break", font=(FONT_NAME, 45, "bold"), fg=RED, bg=GRAY)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Break", font=(FONT_NAME, 35, "bold"), fg=PINK, bg=GRAY)
    else:
        countdown(work_sec)
        title_label.config(text="Work", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=GRAY)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    if minutes < 1:
        minutes = "00"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        iteration_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GRAY)

# Centering Window on the Screen
window_width = 500
window_height = 450
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# Creating Background Image in Window using Canvas Widget
canvas = tk.Canvas(width=200, height=224, bg=GRAY, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Creating Title called title
title_label = tk.Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=GRAY)
title_label.grid(column=1, row=0)

# Creating an iteration label using a checkmark
iteration_label = tk.Label(fg=GREEN, bg=GRAY)
iteration_label.config(pady=10)
iteration_label.grid(column=1, row=3)

# Creating a start button to initiate the timer.
start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# Creating a reset button to reset the timer.
reset_button = tk.Button(text="Reset", command=timer_reset)
reset_button.grid(column=2, row=2)

window.mainloop()
