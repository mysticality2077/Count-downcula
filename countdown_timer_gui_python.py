# ╔═════════════════╗
# ║ Count-downcula  ║
# ╠═════════════════╣
# ║ by: mysticality ║
# ╚═════════════════╝

import tkinter as tk
from tkinter import messagebox


class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Count-downcula")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.time_left = 0
        self.running = False

        title = tk.Label(
            root,
            text="Count-downcula",
            font=("Courier New", 18, "bold")
        )
        title.pack(pady=10)

        self.entry = tk.Entry(root, justify="center", font=("Courier New", 14))
        self.entry.pack(pady=10)
        self.entry.insert(0, "60")

        self.label = tk.Label(
            root,
            text="0",
            font=("Courier New", 32, "bold")
        )
        self.label.pack(pady=10)

        self.start_button = tk.Button(
            root,
            text="Start Countdown",
            command=self.start_timer,
            font=("Courier New", 12)
        )
        self.start_button.pack(pady=5)
    def start_timer(self):
        if self.running:
            return

        try:
            self.time_left = int(self.entry.get())

            if self.time_left <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a positive number.")
            return

        self.running = True
        self.countdown()

    def countdown(self):
        self.label.config(text=str(self.time_left))

        if self.time_left > 0:
            self.time_left -= 1
            self.root.after(1000, self.countdown)
        else:
            self.running = False
            self.label.config(text="Time is up!")
            messagebox.showinfo("Done", "Time is up!")


root = tk.Tk()
app = CountdownTimer(root)
root.mainloop()
