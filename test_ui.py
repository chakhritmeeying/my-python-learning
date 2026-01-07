import tkinter as tk

root = tk.Tk()
root.title("My Fist UI")
root.geometry("600x400")


def show_label():
    # label_text.set("Hello! You clicked the button to show label😊")
    label_text.set(entry.get())


def show_entry():
    entry_text.set("Hello! You clicked the button to show text in entry😊")


entry_text = tk.StringVar()
label_text = tk.StringVar()

label = tk.Label(root, text="Hello")
label.pack()

label = tk.Label(root, textvariable=label_text)
label.pack(pady=20)
entry = tk.Entry(root, textvariable=entry_text, width=50)
entry.pack(pady=10)
tk.Button(root, text="Show label", command=show_label).pack(pady=10)

tk.Button(root, text="Show entry", command=show_entry).pack(pady=10)


root.mainloop()
