import tkinter as tk
import time
import random
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Final Project SDEV 140")
        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0
        self.recorded_times = []  # List to store recorded times
        
        # Create UI elements for top_frame1
        top_frame1 = tk.Frame(root, bg='#272838')
        top_frame1.grid(row=0, column=1, padx=10, pady=5)
        
        tool_bar_top1 = tk.Frame(top_frame1, width=450, height=100, bg='#14203e')
        tool_bar_top1.pack(side="right", padx=5, pady=5)
        
        # Load the image file (media/logo.png)
        self.logo = Image.open("media/logo.png")

        # Resize the image (media/logo.png)
        self.logo = self.logo.resize((70, 70), Image.BILINEAR) 

        self.logo_image = ImageTk.PhotoImage(self.logo)
        
        self.title_label = tk.Label(tool_bar_top1, text="Anthony Manzo's Program", font=("Arial", 18, "bold"), bg='#14203e', fg='white')
        self.title_label.pack()
        
        self.logo_label = tk.Label(tool_bar_top1, image=self.logo_image, bg='#14203e')
        self.logo_label.pack()
        
        

        # Create UI elements for left_frame1
        left_frame1 = tk.Frame(root, bg='#272838')
        left_frame1.grid(row=1, column=0, padx=10, pady=5)

        tool_bar_left1 = tk.Frame(left_frame1, width=450, height=100, bg='#14203e')
        tool_bar_left1.grid(row=0, column=0, padx=5, pady=5)
        
        self.scrambler = ScramblerGUI(tool_bar_left1, self)  # Create ScramblerGUI instance passing Stopwatch reference
        
        
        
        #create UI elements for left_frame2
        left_frame2 = tk.Frame(root, bg='#272838')
        left_frame2.grid(row=2, column=0, padx=10, pady=5)
        
        tool_bar_left2 = tk.Frame(left_frame2, width=450, height=100, bg='#14203e')
        tool_bar_left2.grid(row=2, column=0, padx=5, pady=5)
        
        self.time_display = tk.Label(tool_bar_left2, text="00:00:00.000", font=("Arial", 24, "bold"), bg='#14203e', fg='white')
        self.time_display.pack()

        self.start_button = tk.Button(tool_bar_left2, text="Start", command=self.start_stopwatch)
        self.start_button.pack(side=tk.LEFT, padx=15, pady=10)

        self.stop_button = tk.Button(tool_bar_left2, text="Stop", command=self.stop_stopwatch, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=15, pady=10)

        self.reset_button = tk.Button(tool_bar_left2, text="Reset", command=self.reset_stopwatch)
        self.reset_button.pack(side=tk.LEFT, padx=15, pady=10)
        
        
        
        # Create UI elements for right_frame1
        right_frame1 = tk.Frame(root, bg='#272838')
        right_frame1.grid(row=1, column=1, rowspan=2, padx=10, pady=5)

        tool_bar_right1 = tk.Frame(right_frame1, width=450, height=100, bg='#14203e')
        tool_bar_right1.grid(row=0, column=1, padx=5, pady=5)
        
        self.leaderboard_label = tk.Label(tool_bar_right1, text="Leaderboard:", font=("Arial", 18, "bold"), bg='#14203e', fg='white')
        self.leaderboard_label.pack()

        self.leaderboard_text = tk.Text(tool_bar_right1, height=15, width=40, font=("Arial", 12, "bold"), bg='#14203e', fg='#ffffff', bd=5)
        self.leaderboard_text.pack()
        
        
        
        # Create UI elements for right_frame2
        right_frame2 = tk.Frame(root, bg='#272838')
        right_frame2.grid(row=1, column=3, rowspan=2, padx=10, pady=5)

        tool_bar_right2 = tk.Frame(right_frame2, width=450, height=100, bg='#14203e')
        tool_bar_right2.grid(row=0, column=0, padx=5, pady=5)
        
        self.times_label = tk.Label(tool_bar_right2, text="Recent Times:", font=("Arial", 18, "bold"), bg='#14203e', fg='white')
        self.times_label.pack()

        self.times_text = tk.Text(tool_bar_right2, height=15, width=40, font=("Arial", 12, "bold"), bg='#14203e', fg='#ffffff', bd=5)
        self.times_text.pack()



        self.update_time()
        self.root.bind('<space>', lambda event: self.toggle_stopwatch()) # Bind the spacebar to toggle the stopwatch

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
            self.start_time = None

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
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.time_display.config(text="00:00:00.000")

    def prompt_save(self):
        answer = messagebox.askquestion("Save to Leaderboard", "Do you want to save this time to the leaderboard?")
        if answer == "yes":
            self.recorded_times.append(self.elapsed_time)
            self.update_leaderboard()

    def update_leaderboard(self):
        self.leaderboard_text.delete(1.0, tk.END)
        self.leaderboard_text.insert(tk.END, "Top Times\n\n")
        sorted_times = sorted(self.recorded_times)
        for idx, recorded_time in enumerate(sorted_times, start=1):
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(recorded_time))
            milliseconds = int((recorded_time - int(recorded_time)) * 1000)
            time_str = f"{formatted_time}.{milliseconds:03d}"
            self.leaderboard_text.insert(tk.END, f"{idx}. {time_str}\n")

        self.update_recent_times()

            
    def update_recent_times(self):
        self.times_text.delete(1.0, tk.END)
        self.times_text.insert(tk.END, "Recent Times\n\n")
    
        num_recent_times = 5  # Only records the last 5 recorded times
        recent_times = self.recorded_times[-num_recent_times:]
    
        if len(recent_times) >= 5:
            # Calculate the average time excluding the best and worst times
            recent_times_sorted = sorted(recent_times)
            middle_three_times = recent_times_sorted[1:4]  # Exclude the best and worst times
            average_time = sum(middle_three_times) / len(middle_three_times)
        
            formatted_avg_time = time.strftime("%H:%M:%S", time.gmtime(average_time))
            avg_milliseconds = int((average_time - int(average_time)) * 1000)
            avg_time_str = f"Average of 5: {formatted_avg_time}.{avg_milliseconds:03d}\n\n"
            self.times_text.insert(tk.END, avg_time_str)

        # Display recent times after the average time
        for idx, recorded_time in enumerate(recent_times, start=1):
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(recorded_time))
            milliseconds = int((recorded_time - int(recorded_time)) * 1000)
            time_str = f"{formatted_time}.{milliseconds:03d}"
            self.times_text.insert(tk.END, f"{idx}. {time_str}\n")
                
                
            
class ScramblerGUI:
    def __init__(self, root, stopwatch):
        self.root = root
        self.stopwatch = stopwatch

        self.moves = ["L", "L2", "L'", 
                      "R", "R2", "R'", 
                      "F", "F2", "F'", 
                      "B", "B2", "B'", 
                      "U", "U2", "U'", 
                      "D", "D2", "D'"]

        self.output_label = tk.Label(root, text="Scramble will appear here", font=("Arial", 14, "bold"), bg='#14203e', fg='white')
        self.output_label.grid(row=0, column=0, columnspan=2, pady=5)
        
        # Load the image file (media/scramble.png)
        self.scramble = Image.open("media/scramble.png")

        # Resize the image (media/scramble.png)
        self.scramble = self.scramble.resize((70, 70), Image.BILINEAR) 
        
        self.scramble_image = ImageTk.PhotoImage(self.scramble)
        
        self.scramble_label = tk.Label(root, image=self.scramble_image, bg='#14203e', pady = 0)
        self.scramble_label.grid(row=1, column=0, columnspan=2, pady=20)

        self.generate_button = tk.Button(root, text="Generate Scramble", command=self.generate_scramble)
        self.generate_button.grid(row=2, column=0, padx=10, pady=15)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.grid(row=2, column=1, padx=10, pady=10)

    def generate_scramble(self):
        slen = random.randint(15, 20)
        cnt = 0
        output = []
        prev = 'ZZ'

        while cnt < slen:
            pos = random.randrange(len(self.moves))
            if self.moves[pos][0] != prev[0]:
                output.append(self.moves[pos])
                prev = self.moves[pos]
                cnt += 1
                
        scramble_text = ' '.join(output) + " [" + str(slen) + " Moves]"
        self.output_label.config(text=scramble_text)  # Update only the output_label with the generated scramble
        

def main():
    root = tk.Tk()
    root.maxsize(1920, 1080)
    root.config(bg="black")
    root.iconbitmap('media/logo.png')

    stopwatch = Stopwatch(root)

    root.mainloop()

if __name__ == "__main__":
    main()
