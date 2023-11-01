from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generater(length=12):
    c = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(c) for _ in range(length))
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    web=web_entry.get()
    pswd=password_entry.get()
    eml=email_entry.get()

    if len(web)==0 or len(pswd)==0:
        messagebox.showinfo(title="Oops",message="Please dont leave any field empty !")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"The Details Entered are:\nWebsite:{web}\n"
                                                          f"Email:{eml}\nPassword:{pswd}")
        if is_ok:
            with open("password_manager.txt",'a') as file:
                file.write(f"{web} | {pswd} | {eml} \n")
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, "ashadeep@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #
FONT_NAME = "Courier"
# window setup
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50)
# canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)
# label
website_label = Label(text="Website:", font=(FONT_NAME, 16, "bold"))
website_label.grid(row=1, column=0)
username_label = Label(text="Username/EMail:", font=(FONT_NAME, 16, "bold"))
username_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=(FONT_NAME, 16, "bold"))
password_label.grid(row=3, column=0)
# entries
web_entry = Entry(width=50)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"ashadeep@gmail.com")
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)
# buttons
generate_button = Button(text="Generate Password",command=password_generater)
generate_button.grid(row=3, column=2)
add_button = Button(text="ADD", width=42,command=add)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
