import tkinter as tk

root = tk.Tk()

text_widget = tk.Text(root)
text_widget.pack()

# Inserting a Label widget within the Text widget
label_widget = tk.Label(text_widget, text="Embedded Label")
text_widget.window_create(tk.END, window=label_widget)

root.mainloop()
