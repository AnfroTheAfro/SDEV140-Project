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
        top_frame1 = tk.Frame(root, bg='#272838') # Create a frame for the title and logo
        top_frame1.grid(row=0, column=1, padx=10, pady=5)
        
        tool_bar_top1 = tk.Frame(top_frame1, width=450, height=100, bg='#14203e')
        tool_bar_top1.pack(side="right", padx=5, pady=5)
        
        self.logo = Image.open("media/logo.png") # Load the image file (media/logo.png)

        self.logo = self.logo.resize((70, 70), Image.BILINEAR) # Resize the image (media/logo.png)

        self.logo_image = ImageTk.PhotoImage(self.logo)
        
        self.title_label = tk.Label(tool_bar_top1, text="Anthony Manzo's Program", font=("Arial", 18, "bold"), bg='#14203e', fg='white')
        self.title_label.pack()
        
        self.logo_label = tk.Label(tool_bar_top1, image=self.logo_image, bg='#14203e')
        self.logo_label.pack()
        
        

        # Create UI elements for left_frame1
        left_frame1 = tk.Frame(root, bg='#272838') # Create a frame for the scrambler
        left_frame1.grid(row=1, column=0, padx=10, pady=5)

        tool_bar_left1 = tk.Frame(left_frame1, width=450, height=100, bg='#14203e')
        tool_bar_left1.grid(row=0, column=0, padx=5, pady=5)
        
        self.scrambler = ScramblerGUI(tool_bar_left1, self)  # Create ScramblerGUI instance passing Stopwatch reference
        
        
        
        #create UI elements for left_frame2
        left_frame2 = tk.Frame(root, bg='#272838') # Create a frame for the stopwatch
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
        right_frame1 = tk.Frame(root, bg='#272838') # Create a frame for the top times scoreboard
        right_frame1.grid(row=1, column=1, rowspan=2, padx=10, pady=5)

        tool_bar_right1 = tk.Frame(right_frame1, width=450, height=100, bg='#14203e')
        tool_bar_right1.grid(row=0, column=1, padx=5, pady=5)
        
        self.leaderboard_label = tk.Label(tool_bar_right1, text="Leaderboard:", font=("Arial", 18, "bold"), bg='#14203e', fg='white')
        self.leaderboard_label.pack()

        self.leaderboard_text = tk.Text(tool_bar_right1, height=15, width=40, font=("Arial", 12, "bold"), bg='#14203e', fg='#ffffff', bd=5)
        self.leaderboard_text.pack()
        
        
        
        # Create UI elements for right_frame2
        right_frame2 = tk.Frame(root, bg='#272838') # Create a frame for the recent times scoreboard
        right_frame2.grid(row=1, column=3, rowspan=2, padx=10, pady=5)

        tool_bar_right2 = tk.Frame(right_frame2, width=450, height=100, bg='#14203e')
        tool_bar_right2.grid(row=0, column=0, padx=5, pady=5)
        
        self.times_label = tk.Label(tool_bar_right2, text="Recent Times:", font=("Arial", 18, "bold"), bg='#14203e', fg='white')
        self.times_label.pack()

        self.times_text = tk.Text(tool_bar_right2, height=15, width=40, font=("Arial", 12, "bold"), bg='#14203e', fg='#ffffff', bd=5)
        self.times_text.pack()



        self.update_time()
        self.root.bind('<space>', lambda event: self.toggle_stopwatch()) # Bind the spacebar to toggle the stopwatch


    # Toggles the stopwatch between running and stopped with the spacebar
    def toggle_stopwatch(self):
        if self.is_running: # This checks if the stopwatch is running
            self.stop_stopwatch() # This stops the stopwatch if the stopwatch is running
        else:
            self.start_stopwatch() # This starts the stopwatch if the stopwatch is not running
            

    # Programs the start button to start the stopwatch and disable the start button once the stopwatch is running
    def start_stopwatch(self):
        if not self.is_running: # This checks if the stopwatch is not running
            self.is_running = True # This starts the stopwatch if the stopwatch is not running
            if self.start_time is None: # This checks if the stopwatch has not been started before
                self.start_time = time.time() # This starts the stopwatch if the stopwatch has not been started before
            else:
                self.start_time = time.time() - self.elapsed_time # This resumes the stopwatch if the stopwatch has been started before
            self.start_button.config(state=tk.DISABLED) # This disables the start button once the stopwatch is running
            self.stop_button.config(state=tk.NORMAL) # This enables the stop button once the stopwatch is running
            self.update_time() # This updates the stopwatch
            

    # Programs the stop button to stop the stopwatch and disable the stop button once the stopwatch is not running
    def stop_stopwatch(self):
        if self.is_running: # This checks if the stopwatch is running
            self.is_running = False # This stops the stopwatch if the stopwatch is running
            self.stop_button.config(state=tk.DISABLED) # This disables the stop button once the stopwatch is not running
            self.elapsed_time = time.time() - self.start_time # This calculates the elapsed time
            self.display_time() # This displays the stopwatch
            self.prompt_save() # This prompts the user to save the time to the leaderboard
            self.start_time = None # This resets the start time to 0 or None

    # Updates the stopwatch after a certain amount of time and displays it
    def update_time(self):
        if self.is_running: # This checks if the stopwatch is running
            current_time = time.time() # This gets the current time
            self.elapsed_time = current_time - self.start_time # This calculates the elapsed time
            self.display_time() # This displays the stopwatch
            self.root.after(50, self.update_time) # This updates the stopwatch every 50 milliseconds

    # Displays the stopwatch
    def display_time(self):
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(self.elapsed_time)) # This formats the time. The time is formatted as hours:minutes:seconds with time.strftime
        milliseconds = int((self.elapsed_time - int(self.elapsed_time)) * 1000) # This calculates the milliseconds
        time_str = f"{formatted_time}.{milliseconds:03d}" # This helps format the time with milliseconds
        self.time_display.config(text=time_str) # This displays the time
        
    # Resets the stopwatch to 0 and enables the start button
    def reset_stopwatch(self):
        self.is_running = False # This stops the stopwatch if the stopwatch is running
        self.start_time = None # This resets the start time to 0 or None
        self.elapsed_time = 0 # This resets the elapsed time to 0
        self.start_button.config(state=tk.NORMAL) # This enables the start button
        self.stop_button.config(state=tk.DISABLED) # This disables the stop button
        self.time_display.config(text="00:00:00.000") # This resets the time display to 00:00:00.000

    # Prompts the user to save the time to the leaderboard
    def prompt_save(self):
        answer = messagebox.askquestion("Save to Leaderboard", "Do you want to save this time to the leaderboard?") # This prompts the user to save the time to the leaderboard with a messagebox
        if answer == "yes": 
            self.recorded_times.append(self.elapsed_time) # This appends the recorded time to the recorded times list if user selects yes
            self.update_leaderboard() # This updates the leaderboard

    # Updates the "Top Times" scoreboard
    def update_leaderboard(self):
        self.leaderboard_text.delete(1.0, tk.END) # This deletes the old leaderboard
        self.leaderboard_text.insert(tk.END, "Top Times\n\n") # This inserts the title of "Top Times" to the leaderboard
        sorted_times = sorted(self.recorded_times) # This sorts the recorded times from least to greatest
        for idx, recorded_time in enumerate(sorted_times, start=1): # This gets the index and recorded time from the sorted times list
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(recorded_time)) # This formats the time. The time is formatted as hours:minutes:seconds with time.strftime
            milliseconds = int((recorded_time - int(recorded_time)) * 1000) # This calculates the milliseconds
            time_str = f"{formatted_time}.{milliseconds:03d}" # This helps format the time with milliseconds
            self.leaderboard_text.insert(tk.END, f"{idx}. {time_str}\n") # This inserts the index and time to the leaderboard
        self.update_recent_times() # This updates the recent times scoreboard

    # Updates the "Recent Times" scoreboard        
    def update_recent_times(self):
        self.times_text.delete(1.0, tk.END) # Clears the old recent times
        self.times_text.insert(tk.END, "Recent Times\n\n") # Inserts the title of "Recent Times" to the recent times scoreboard
    
        num_recent_times = 5  # Only records the last 5 recorded times to the recent times scoreboard
        recent_times = self.recorded_times[-num_recent_times:] # Get the last 5 recorded times from num_recent_times
    
        if len(recent_times) >= 5: 
            # Calculate the average time excluding the best and worst times
            recent_times_sorted = sorted(recent_times) # Sort the recent times from least to greatest
            middle_three_times = recent_times_sorted[1:4]  # Exclude the best and worst times
            average_time = sum(middle_three_times) / len(middle_three_times) # Calculate the average for the middle three times
        
            formatted_avg_time = time.strftime("%H:%M:%S", time.gmtime(average_time)) # This formats the time. The time is formatted as hours:minutes:seconds with time.strftime 
            avg_milliseconds = int((average_time - int(average_time)) * 1000) # This calculates the milliseconds for the average time
            avg_time_str = f"Average of 5: {formatted_avg_time}.{avg_milliseconds:03d}\n\n" # This displays the average time with milliseconds
            self.times_text.insert(tk.END, avg_time_str) # This inserts the average time to the recent times scoreboard

        # Display recent times after the average time
        for idx, recorded_time in enumerate(recent_times, start=1): # This gets the index and recorded time from the recent times list
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(recorded_time)) # This formats the time. The time is formatted as hours:minutes:seconds with time.strftime
            milliseconds = int((recorded_time - int(recorded_time)) * 1000) # This calculates the milliseconds
            time_str = f"{formatted_time}.{milliseconds:03d}" # This helps format the time with milliseconds
            self.times_text.insert(tk.END, f"{idx}. {time_str}\n") # This inserts the index and time to the recent times scoreboard
                
                
            
class ScramblerGUI:
    def __init__(self, root, stopwatch):
        self.root = root # Reference to the root window
        self.stopwatch = stopwatch # Reference to the Stopwatch instance

        self.moves = ["L", "L2", "L'", 
                      "R", "R2", "R'", 
                      "F", "F2", "F'", 
                      "B", "B2", "B'", 
                      "U", "U2", "U'", 
                      "D", "D2", "D'"] # Listing all possible moves for the scrambler

        # Create UI elements for the scrambler
        self.output_label = tk.Label(root, text="Scramble will appear here", font=("Arial", 14, "bold"), bg='#14203e', fg='white')
        self.output_label.grid(row=0, column=0, columnspan=2, pady=5)
        
        self.scramble = Image.open("media/scramble.png") # Load the image file (media/scramble.png)

        self.scramble = self.scramble.resize((70, 70), Image.BILINEAR) # Resize the image (media/scramble.png)
        
        self.scramble_image = ImageTk.PhotoImage(self.scramble)
        
        self.scramble_label = tk.Label(root, image=self.scramble_image, bg='#14203e', pady = 0)
        self.scramble_label.grid(row=1, column=0, columnspan=2, pady=20)

        self.generate_button = tk.Button(root, text="Generate Scramble", command=self.generate_scramble)
        self.generate_button.grid(row=2, column=0, padx=10, pady=15)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.grid(row=2, column=1, padx=10, pady=10)

    # Generates a random scramble and displays it
    def generate_scramble(self):
        slen = random.randint(15, 20) # Random scramble length between 15 and 20 moves
        
        # Keeps track of the number of moves generated
        cnt = 0
        output = []
        prev = 'ZZ'

        while cnt < slen:
            pos = random.randrange(len(self.moves)) # Randomly select a move from the self.moves list
            if self.moves[pos][0] != prev[0]: # Check if the move is not the same as the previous move
                output.append(self.moves[pos]) # Added to scramble sequence if the move is not the same as the previous move
                prev = self.moves[pos] 
                cnt += 1 # Increment the move counter
                
        scramble_text = ' '.join(output) + " [" + str(slen) + " Moves]" # Join the scramble sequence and add the number of moves to the scramble as a string
        self.output_label.config(text=scramble_text)  # Update only the output_label with the generated scramble
        

def main():
    root = tk.Tk() # Create the root window
    root.maxsize(1920, 1080) # Set the maximum size of the window
    root.config(bg="black") # Set the background color of the window
    root.iconbitmap('media/logo.png') # Set the icon of the window

    stopwatch = Stopwatch(root) # Create the Stopwatch instance passing the root window reference

    root.mainloop() 

if __name__ == "__main__":
    main()
