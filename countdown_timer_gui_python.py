# ╔═════════════════╗
# ║ Count-downcula  ║
# ╠═════════════════╣
# ║ by: mysticality ║
# ╚═════════════════╝

# This script creates a simple GUI countdown timer using Tkinter.
# Users can enter a time in seconds and start the countdown.

import tkinter as tk
from tkinter import messagebox


class CountdownTimer:
    
    def __init__(self, root):
        
        # Initialize the CountdownTimer application.
        # Sets up the GUI elements including labels, entry field, and button.
        
        self.root = root
        self.root.title("Count-downcula")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.time_left = 0
        self.running = False
        self.paused = False

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

        # Button frame to hold control buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        self.start_button = tk.Button(
            button_frame,
            text="Start",
            command=self.start_timer,
            font=("Courier New", 10)
        )
        self.start_button.pack(side=tk.LEFT, padx=3)

        self.pause_button = tk.Button(
            button_frame,
            text="Pause",
            command=self.pause_timer,
            font=("Courier New", 10),
            state=tk.DISABLED
        )
        self.pause_button.pack(side=tk.LEFT, padx=3)

        self.resume_button = tk.Button(
            button_frame,
            text="Resume",
            command=self.resume_timer,
            font=("Courier New", 10),
            state=tk.DISABLED
        )
        self.resume_button.pack(side=tk.LEFT, padx=3)

        self.cancel_button = tk.Button(
            button_frame,
            text="Cancel",
            command=self.cancel_timer,
            font=("Courier New", 10),
            state=tk.DISABLED
        )
        self.cancel_button.pack(side=tk.LEFT, padx=3)
    
    def start_timer(self):
        
        # Start the countdown timer.
        # Validates the input, sets the time_left, and begins the countdown if valid.
        
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
        self.paused = False
        # Update button states
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.resume_button.config(state=tk.DISABLED)
        self.cancel_button.config(state=tk.NORMAL)
        self.entry.config(state=tk.DISABLED)
        self.countdown()

    def pause_timer(self):
        # Pause the countdown timer.
        # The timer can be resumed from this point.
        self.paused = True
        self.pause_button.config(state=tk.DISABLED)
        self.resume_button.config(state=tk.NORMAL)

    def resume_timer(self):
        # Resume the countdown timer from where it was paused.
        self.paused = False
        self.pause_button.config(state=tk.NORMAL)
        self.resume_button.config(state=tk.DISABLED)
        self.countdown()

    def cancel_timer(self):
        # Cancel the countdown timer and reset to initial state.
        self.running = False
        self.paused = False
        self.time_left = 0
        self.label.config(text="0")
        # Reset button states
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.resume_button.config(state=tk.DISABLED)
        self.cancel_button.config(state=tk.DISABLED)
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "60")

    def countdown(self):
        
        # Update the countdown display every second.
        # Decrements time_left and schedules the next update.
        # When time reaches zero, stops the timer and shows a message.
        self.label.config(text=str(self.time_left))

        if self.time_left > 0 and not self.paused:
            self.time_left -= 1
            self.root.after(1000, self.countdown)
        elif self.time_left > 0 and self.paused:
            # Timer is paused, don't schedule next update
            pass
        else:
            self.running = False
            self.paused = False
            self.label.config(text="Time is up!")
            # Reset button states when timer finishes
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            self.resume_button.config(state=tk.DISABLED)
            self.cancel_button.config(state=tk.DISABLED)
            self.entry.config(state=tk.NORMAL)
            messagebox.showinfo("Done", "Time is up!")


# Create the main window and start the application
root = tk.Tk()
app = CountdownTimer(root)
root.mainloop()
