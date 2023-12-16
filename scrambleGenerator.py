import tkinter as tk
import random
import sys

class ScramblerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Scrambler GUI")
        
        self.moves = ["L", "L2", "L'",
                      "R", "R2", "R'",
                      "F", "F2", "F'",
                      "B", "B2", "B'",
                      "U", "U2", "U'",
                      "D", "D2", "D'"]

        self.output_label = tk.Label(root, text="Scramble will appear here", font=("Arial", 14))
        self.output_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.generate_button = tk.Button(root, text="Generate Scramble", command=self.generate_scramble)
        self.generate_button.grid(row=1, column=0, padx=10, pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.grid(row=1, column=1, padx=10, pady=10)

    def generate_scramble(self):
        slen = random.randint(10, 15)
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
        self.output_label.config(text=scramble_text)


def main():
    root = tk.Tk() # Create main root window
    app = ScramblerGUI(root) 
    root.config(bg="black") # Background color
    left_frame = tk.Frame(root, bg='#272838')
    left_frame.grid(row=0, column=2, padx=10, pady=5)
    root.mainloop()

if __name__ == "__main__":
    main()
