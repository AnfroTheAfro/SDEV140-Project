import tkinter as tk
import time
import tkinter.messagebox as messagebox

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0
        self.recorded_times = []  # List to store recorded times

        # Create UI elements for stopwatch
        self.time_display = tk.Label(root, text="00:00:00.000", font=("Arial", 24))
        self.time_display.grid(row=0, column=0, columnspan=2, pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_stopwatch)
        self.start_button.grid(row=1, column=0, padx=5, pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_stopwatch, state=tk.DISABLED)
        self.stop_button.grid(row=1, column=1, padx=5, pady=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_stopwatch)
        self.reset_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.leaderboard_label = tk.Label(root, text="Leaderboard:", font=("Arial", 18))
        self.leaderboard_label.grid(row=0, column=2, columnspan=2, sticky='w', padx=(50, 0))

        self.leaderboard_text = tk.Text(root, height=10, width=30, font=("Arial", 12))
        self.leaderboard_text.grid(row=1, column=2, rowspan=3, columnspan=2, padx=(50, 0), pady=5)

        self.update_time()

        # Bind spacebar to start and stop
        self.root.bind('<space>', lambda event: self.toggle_stopwatch())

    def toggle_stopwatch(self):
        if self.is_running:
            self.stop_stopwatch()
        else:
            self.start_stopwatch()

    def start_stopwatch(self):
        if not self.is_running:
            self.is_running = True
            if self.start_time is None:
                self.start_time = time.time()
            else:
                self.start_time = time.time() - self.elapsed_time
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.update_time()

    def stop_stopwatch(self):
        if self.is_running:
            self.is_running = False
            self.stop_button.config(state=tk.DISABLED)
            self.elapsed_time = time.time() - self.start_time
            self.display_time()
            self.prompt_save()
            self.start_time = None  # Reset start time to prevent further starts without reset

    def update_time(self):
        if self.is_running:
            current_time = time.time()
            self.elapsed_time = current_time - self.start_time
            self.display_time()
            self.root.after(50, self.update_time)

    def display_time(self):
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(self.elapsed_time))
        milliseconds = int((self.elapsed_time - int(self.elapsed_time)) * 1000)
        time_str = f"{formatted_time}.{milliseconds:03d}"
        self.time_display.config(text=time_str)

    def reset_stopwatch(self):
        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0
        self.start_button.config(state=tk.NORMAL)  # Enable the start button
        self.stop_button.config(state=tk.DISABLED)
        self.time_display.config(text="00:00:00.000")

    def prompt_save(self):
        answer = messagebox.askquestion("Save to Leaderboard", "Do you want to save this time to the leaderboard?")
        if answer == "yes":
            self.recorded_times.append(self.elapsed_time)
            self.update_leaderboard()

    def update_leaderboard(self):
        self.leaderboard_text.delete(1.0, tk.END)
        self.leaderboard_text.insert(tk.END, "Leaderboard Times\n")
        
        # Sort the recorded times
        sorted_times = sorted(self.recorded_times)
        
        for idx, recorded_time in enumerate(sorted_times, start=1):
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(recorded_time))
            milliseconds = int((recorded_time - int(recorded_time)) * 1000)
            time_str = f"{formatted_time}.{milliseconds:03d}"
            self.leaderboard_text.insert(tk.END, f"{idx}. {time_str}\n")

def main():
    root = tk.Tk()
    root.title("Stopwatch & Leaderboard")
    root.maxsize(1280, 720)
    root.config(bg="black")

    # Create an instance of Stopwatch
    stopwatch = Stopwatch(root)

    root.mainloop()

if __name__ == "__main__":
    main()
