import tkinter as tk
import guess as g
import bot as bt

label_style = {"bg": "#111111", "fg": "white", "font": ("Arial", 10)}
entry_style = {"width": 5}

rounds = 0


import tkinter as tk
import guess as g

label_style = {"bg": "#111111", "fg": "white", "font": ("Arial", 10)}
entry_style = {"width": 5}

rounds = 0

def create_window(correct_code, num_digits):
    global rounds, canvas, scroll_frame, scroll_window
    rounds = 0

    # Create NEW window properly
    win = tk.Toplevel()
    win.title("Mastermind Tkinter Window")
    win.configure(bg="#111111")
    win.geometry("450x500")

    # --- TOP STATIC AREA ---
    top_frame = tk.Frame(win, bg="#111111")
    top_frame.pack(side="top", fill="x")

    tk.Label(top_frame, text="Mastermind Game",
             bg="#111111", fg="white",
             font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(top_frame, text="Please enter your guess:",
             bg="#111111", fg="white",
             font=("Arial", 11)).pack(pady=5)

    input_row = tk.Frame(top_frame, bg="#111111")
    input_row.pack(pady=5)

    entries = []

    for i in range(1, num_digits + 1):
        cell = tk.Frame(input_row, bg="#111111")
        cell.pack(side="left", padx=5)

        tk.Label(cell, text=i, **label_style).pack()

        entry = tk.Entry(cell, **entry_style)
        entry.pack()
        entries.append(entry)

    submit_button = tk.Button(top_frame, text="Submit")
    submit_button.pack(pady=10)

    # --- SCROLL AREA ---
    scroll_container = tk.Frame(win, bg="#111111")
    scroll_container.pack(side="top", fill="both", expand=True)

    canvas = tk.Canvas(scroll_container, bg="#111111", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(scroll_container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    scroll_frame = tk.Frame(canvas, bg="#111111")
    scroll_window = canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>", lambda e: canvas.itemconfig(scroll_window, width=e.width))

    # --- SUBMIT LOGIC ---
    def on_submit():
        global rounds
        guess = "".join(e.get() for e in entries)
        score = g.guess_score(correct_code, guess)

        if score["black"] == num_digits:
            tk.Label(
                top_frame,
                text="Congratulations! You've guessed the code!",
                bg="#111111", fg="lightgreen",
                font=("Arial", 12, "bold")
            ).pack(pady=10)
            submit_button.config(state="disabled")
            for e in entries:
                e.config(state="disabled")
        else:
            rounds += 1
            addGuess(guess, scroll_frame, score, rounds)

            for e in entries:
                e.delete(0, tk.END)

        if rounds >= 10:
            tk.Label(
                top_frame,
                text=f"Game Over! The correct code was {correct_code}.",
                bg="#111111", fg="red",
                font=("Arial", 12, "bold")
            ).pack(pady=10)
            submit_button.config(state="disabled")
            for e in entries:
                e.config(state="disabled")

    submit_button.config(command=on_submit)



def addGuess(guess, container, score, round):
    row = tk.Frame(container, bg="#111111")
    row.pack(fill="x", pady=5)

    # CENTERED wrapper
    inner = tk.Frame(row, bg="#111111")
    inner.pack(anchor="center")  # stays centered because scroll_frame now stretches

    # Score
    score_frame = tk.Frame(inner, bg="#111111")
    score_frame.pack(side="left", padx=10)
    for k, v in score.items():
        tk.Label(score_frame, text=f"{k}: {v}", **label_style).pack(anchor="w")

    # Guess numbers
    guess_frame = tk.Frame(inner, bg="#111111")
    guess_frame.pack(side="left", padx=20)
    for g in guess:
        cell = tk.Frame(guess_frame, bg="#111111")
        cell.pack(side="left", padx=5)
        tk.Label(cell, text=g, **label_style).pack()

    round_label = tk.Label(inner, text=f"Round {round}", **label_style)
    round_label.pack(side="left", padx=10)


def random_code(length):
    import random
    digits = [str(i) for i in range(10)]
    return "".join(random.choices(digits, k=length))

def addbotGuess(guess, container, score, round):
    # Yellow label style override
    bot_label_style = label_style.copy()
    bot_label_style["fg"] = "yellow"

    row = tk.Frame(container, bg="#111111")
    row.pack(fill="x", pady=5)

    # CENTERED wrapper
    inner = tk.Frame(row, bg="#111111")
    inner.pack(anchor="center")  # stays centered because scroll_frame now stretches

    # Score
    score_frame = tk.Frame(inner, bg="#111111")
    score_frame.pack(side="left", padx=10)
    for k, v in score.items():
        tk.Label(score_frame, text=f"{k}: {v}", **bot_label_style).pack(anchor="w")

    # Guess numbers
    guess_frame = tk.Frame(inner, bg="#111111")
    guess_frame.pack(side="left", padx=20)
    for g in guess:
        cell = tk.Frame(guess_frame, bg="#111111")
        cell.pack(side="left", padx=5)
        tk.Label(cell, text=g, **bot_label_style).pack()

    # Round number
    round_label = tk.Label(inner, text=f"Round {round}", **bot_label_style)
    round_label.pack(side="left", padx=10)


def create_botwindow(correct_code, num_digits):
    global rounds, canvas, scroll_frame, scroll_window
    rounds = 0

    # Create NEW window properly
    win = tk.Toplevel()
    win.title("Mastermind Tkinter Window")
    win.configure(bg="#111111")
    win.geometry("450x500")

    # --- TOP STATIC AREA ---
    top_frame = tk.Frame(win, bg="#111111")
    top_frame.pack(side="top", fill="x")

    tk.Label(top_frame, text="Mastermind Game",
             bg="#111111", fg="white",
             font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(top_frame, text="Please enter your guess:",
             bg="#111111", fg="white",
             font=("Arial", 11)).pack(pady=5)

    input_row = tk.Frame(top_frame, bg="#111111")
    input_row.pack(pady=5)

    entries = []

    for i in range(1, num_digits + 1):
        cell = tk.Frame(input_row, bg="#111111")
        cell.pack(side="left", padx=5)

        tk.Label(cell, text=i, **label_style).pack()

        entry = tk.Entry(cell, **entry_style)
        entry.pack()
        entries.append(entry)

    # Bot guesses
    # Explicit conversion to integers
    bot_guess = bt.bot_guessing_game([int(s) for s in correct_code])
    
    # Explicit conversion back to strings
    bot_guess_str = ["".join([str(num) for num in round_guess]) for round_guess in bot_guess]
    print ("Bot Guess: ", bot_guess_str, "\n")

    submit_button = tk.Button(top_frame, text="Submit")
    submit_button.pack(pady=10)

    # --- SCROLL AREA ---
    scroll_container = tk.Frame(win, bg="#111111")
    scroll_container.pack(side="top", fill="both", expand=True)

    canvas = tk.Canvas(scroll_container, bg="#111111", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(scroll_container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    scroll_frame = tk.Frame(canvas, bg="#111111")
    scroll_window = canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>", lambda e: canvas.itemconfig(scroll_window, width=e.width))

    # --- SUBMIT LOGIC ---
    def on_submit():
        global rounds
        guess = "".join(e.get() for e in entries)
        score = g.guess_score(correct_code, guess)

        if score["black"] == num_digits:
            tk.Label(
                top_frame,
                text="Congratulations! You've guessed the code!",
                bg="#111111", fg="lightgreen",
                font=("Arial", 12, "bold")
            ).pack(pady=10)
            submit_button.config(state="disabled")
            for e in entries:
                e.config(state="disabled")
        else:
            rounds += 1
            addGuess(guess, scroll_frame, score, rounds)
            addbotGuess(bot_guess_str[rounds-1], scroll_frame, score, rounds)
            
            if bot_guess_str[rounds-1] == correct_code:
                tk.Label(
                    top_frame,
                    text="Bot has guessed the code!",
                    bg="#111111", fg="lightgreen",
                    font=("Arial", 12, "bold")
                ).pack(pady=10)
                submit_button.config(state="disabled")
                for e in entries:
                    e.config(state="disabled")

            for e in entries:
                e.delete(0, tk.END)

        if rounds >= 10:
            tk.Label(
                top_frame,
                text=f"Game Over! The correct code was {correct_code}.",
                bg="#111111", fg="red",
                font=("Arial", 12, "bold")
            ).pack(pady=10)
            submit_button.config(state="disabled")
            for e in entries:
                e.config(state="disabled")

    submit_button.config(command=on_submit)



