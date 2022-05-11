from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(1, 2))]
    password_number = [choice(numbers) for _ in range(randint(2, 3))]

    password_list = password_letters + password_symbols + password_number
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    # Replacing the upper 3 lines
    password = "".join(password_list)

    #print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_link_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_link_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# creating a new window and configurations
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=44, command=save)

generate_password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

# Labels
website_label = Label(text="Website:")
email_username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(row=1, column=0)
email_username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# Entries
website_link_entry = Entry(width=52)
website_link_entry.focus()
email_username_entry = Entry(width=52)
email_username_entry.insert(0, string="bilal@gmail.com")
password_entry = Entry(width=33)

website_link_entry.grid(row=1, column=1, columnspan=2)
email_username_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

window.mainloop()
