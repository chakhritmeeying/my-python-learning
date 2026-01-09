import tkinter as tk


def submit_show_info():
    name = en_name.get()
    phone = en_phone.get()
    if not name or not phone:
        show_contact.set("Please enter name and phone!!")

    else:
        show_contact.set(f"Name : {name} | Phone : {phone}")
        en_name.delete(0, tk.END)
        en_phone.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Book")
root.geometry("400x300")


label = tk.Label(root, text="Contact Book")
label.pack()

name_frame = tk.Frame(root)
name_frame.pack(pady=20)
lb_name = tk.Label(name_frame, text="Name : ")
en_name = tk.Entry(name_frame, width=20)
lb_name.pack(side="left", padx=5)
en_name.pack(side="left")

phone_frame = tk.Frame(root)
phone_frame.pack()
lb_phone = tk.Label(phone_frame, text="Phone : ")
en_phone = tk.Entry(phone_frame, width=20)
lb_phone.pack(side="left", padx=5)
en_phone.pack(side="left")


btn_submit_show_info = tk.Button(
    root,
    text="Submit",
    command=submit_show_info,
    bg="blue",
    fg="white"
)
btn_submit_show_info.pack(pady=10)

show_contact = tk.StringVar()
tk.Label(root, textvariable=show_contact, ).pack(pady=10)


root.mainloop()
