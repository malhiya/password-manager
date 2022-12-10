from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    p_letters = [choice(letters) for _ in range(nr_letters)]
    p_numbers = [choice(numbers) for _ in range(nr_numbers)]
    p_symbols = [choice(symbols) for _ in range(nr_symbols)]

    password_list = p_symbols + p_numbers + p_letters
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    password_entry.insert(0, password)
    # pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def copy_password():
    password = password_entry.get()

    if len(password) == 0:
        messagebox.showerror(title="⛔ Cannot Copy: Missing Password ⛔️", message="You do not have a password")
    else:
        pyperclip.copy(password)


# def check_password(current_password):
#     password = password_entry.get()
#     button_text = copy_button['text']
#     if button_text == "  ✅ " and current_password != password:
#         copy_button.config(text="  📋 ")
#     else:
#         window.after(1000, check_password(password))

def save():
    password = password_entry.get()
    website = website_entry.get()
    email = email_entry.get()
    if len(password) == 0 or len(website) == 0:
        messagebox.showerror(title="⚠️Missing Inofrmation!⚠️", message="You did not fill out all the information")
    else:
        ok = messagebox.askokcancel(title=website, message=f"Email: {email}\n"
                                                                           f"Password: {password}\n"
                                                                           f"Is it ok to save?")
        if ok:
            with open("pw_data.txt", "a") as data_file:
                account_info = f"{website} | {email} | {password} \n"
                data_file.write(account_info)
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0, columnspan=2)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=3)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.insert(0, "dummyemail@gmail.com") # END constant can also be used
email_entry.grid(column=1, row=2, columnspan=3)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)
password_entry = Entry(width=18)
password_entry.grid(column=1, row=3, columnspan=1)

copy_button = Button(text="  📋 ", width=2, command=copy_password)
copy_button.grid(column=2, row=3, columnspan=1)


generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=3, row=3, columnspan=1)


add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=3)


window.mainloop()