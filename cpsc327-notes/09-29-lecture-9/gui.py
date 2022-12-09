import tkinter as tk

# Example GUI program using tkinter

window = tk.Tk()                # top-level main window

first_frame = tk.Frame()        # create frames
second_frame = tk.Frame()

greeting = tk.Label(first_frame, text="Hello, Tkinter")             # create label
text_field = tk.Entry(text="Enter text", bg="yellow", fg="purple")  # create input entry
button1 = tk.Button(second_frame, text="Press me")                  # create button

# pack(): place this object somewhere in the window
# greeting.pack()
# text_field.pack()
# button1.pack()

# grid(): more specific way of placing this object, using grid format
# Note: cannot use pack and grid at the same time
text_field.grid(row=0, column=1)
button1.grid(row=1, column=2)
greeting.grid(row=0, column=3)

# where to put the frames
first_frame.grid(row=0, column=1)
second_frame.grid(row=2, column=0)

window.mainloop()
