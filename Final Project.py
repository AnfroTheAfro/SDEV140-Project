from tkinter import *



root = Tk()  # create root window
root.title("Basic GUI Layout")  # title of the GUI window
root.maxsize(1280, 720)  # specify the max size the window can expand to
root.config(bg="black")  # specify background color

# Create left frame
left_frame = Frame(root, bg='#272838')
left_frame.grid(row=0, column=0, padx=10, pady=5)

# Create tool bar frame (left)
tool_bar = Frame(left_frame, width=500, height=600, bg='#14203e')
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# Create right frame
right_frame = Frame(root, bg='#272838')
right_frame.grid(row=0, column=2, padx=10, pady=5)

# Create tool bar frame (right)
tool_bar = Frame(right_frame, width=200, height=600, bg='#14203e')
tool_bar.grid(row=2, column=0, padx=5, pady=5)








root.mainloop()




