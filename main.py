import tkinter as tk
import requests
from tkinter.font import Font
import time

# Get paragraphs
r = requests.get("http://metaphorpsum.com/paragraphs/1")
sentence = r.text



start_time = None
elapsed_time = 0


def start_timer():
    global start_time
    start_time = time.time()


def stop_timer():
    global start_time, elapsed_time
    if start_time is not None:
        elapsed_time = time.time() - start_time
        start_time = None
        return elapsed_time


def start_test():
    title_label.config(text="")
    text_label.config(text=sentence)
    input_box.delete('1.0', 'end')
    input_box.bind("<KeyRelease>", check_typing)
    start_timer()


def check_typing(event):
    user_text = input_box.get('1.0', 'end').strip()
    if user_text == sentence:
        # Stop the clock and get the time taken
        test_time = round(stop_timer(), 2)
        # Calculate the number of words in the paragraph and length of the paragraph.
        p_length = len(sentence)
        p_words = len(sentence.split())
        cpm = round(p_length / (test_time / 60), 2)
        wpm = round(p_words / (test_time / 60), 2)
        results_label.config(text=f"Test Completed in {test_time} seconds. {p_length} characters, {p_words} words.")
        results_label_2.config(text=f"You scored {cpm} CPM, and {wpm} WPM.")
    elif user_text in sentence:
        results_label.config(text="Keep going!")
    else:
        results_label.config(text="Spelling Error!")


# Window config
window = tk.Tk()
window.title("Errol's tkTyper")
window.geometry("800x600")

FONT = Font(size=14, family="Helvetica")

# Widgets
title_label = tk.Label(window, text="Press Start to start the test.", font=FONT)
start_button = tk.Button(window, text="Start", command=start_test, font=FONT)
text_label = tk.Label(window, text="", wraplength=400, font=FONT)
input_box = tk.Text(window, width=50, height=8, font=FONT)
results_label = tk.Label(window, text="", font=FONT)
results_label_2 = tk.Label(window, text="", font=FONT)

title_label.place(relx=0.5, rely=0.1, anchor="center")
start_button.place(relx=0.5, rely=0.4, anchor="center")
text_label.place(relx=0.5, rely=0.2, anchor="center")
input_box.place(relx=0.5, rely=0.7, anchor="center")
results_label.place(relx=0.5, rely=0.9, anchor="center")
results_label_2.place(relx=0.5, rely=0.95, anchor="center")

if __name__ == "__main__":
    window.mainloop()
