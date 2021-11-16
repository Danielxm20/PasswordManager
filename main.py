from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    gen_password = "".join(password_list)
    pass_entry.delete(0, 'end')
    pass_entry.insert(0, gen_password)
    pyperclip.copy(gen_password) # copia al porta papeles la contraseña

    # print(f"Your password is: {gen_password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # messagebox.showinfo("entry", user_entry.get())
    web_name = web_entry.get()
    user_name = user_entry.get()
    password = pass_entry.get()

    if web_name == "" or password == "":
        messagebox.showwarning("warning", "Please don't let any field empty")
    else:
        is_ok = messagebox.askokcancel(title=web_name, message=f"These are the detail entered: \nEmail: {user_name}"
                                                   f"\nPassword: {password} \n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a+") as file:
                file.write(f"{web_name} |   {user_name} |   {password}\n")
                web_entry.delete(0, 'end')
                pass_entry.delete(0, 'end')
            # file.write(web_entry.get() + "\t|" + user_entry.get() + "\t|" + pass_entry.get() + "\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#LABELS
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
user_label = Label(text="User/Email:")
user_label.grid(row=2, column=0, sticky="NSEW")
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0, sticky="NSEW")

#ENTRIES
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2, sticky="NSEW")
web_entry.focus()
user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2, sticky="NSEW")
user_entry.insert(0, "dany685044@gmail.com")
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1, sticky="NSEW")

# BUTTONS
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2, sticky="NSEW")
add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="NSEW")

window.mainloop()
