from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# Pandas
try:
    data = pd.read_csv("data/words_to_learn.csv")
except:
    original_data = pd.read_csv("data/words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------------- DEF ------------------------------- #


def next_card():
    global current_card, flip_timer
    windown.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Inglês", fill="black")
    canvas.itemconfig(card_word, text=current_card["Inglês"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = windown.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="Português", fill="white")
    canvas.itemconfig(card_word, text=current_card["Português"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #

windown = Tk()
windown.title("Flashy")
windown.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = windown.after(3000, func=flip_card)
# Images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=520)
card_background = canvas.create_image(400, 260, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 260, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)
known_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=0)

next_card()
windown.mainloop()
