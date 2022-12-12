from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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

   
    password = "".join(password_list)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def copy_password():
    password = password_entry.get()

    if len(password) == 0:
        messagebox.showerror(title="⛔ Cannot Copy: Missing Password ⛔️", message="You do not have a password to copy")
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
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.showerror(title="⚠️Missing Inofrmation!⚠️", message="You did not fill out all the information")
    else:
        try:
            with open("/Users/malihya/PycharmProjects/Udemy/password-manager/pw_data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open("/Users/malihya/PycharmProjects/Udemy/password-manager/pw_data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("/Users/malihya/PycharmProjects/Udemy/password-manager/pw_data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message=f"No Data Dile Found")
    else:
        if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
                messagebox.showerror(title="Website Not Found", message=f"There is no account information"
                                                                        f" for the website: {website}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="/Users/malihya/PycharmProjects/Udemy/password-manager/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0, columnspan=2)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
website_entry = Entry(width=20)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.insert(0, "dummyemail@gmail.com") # END constant can also be used
email_entry.grid(column=1, row=2, columnspan=3)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)
password_entry = Entry(width=18)
password_entry.grid(column=1, row=3, columnspan=1)

copy_button = Button(text="   📋 ", width=2, command=copy_password)
copy_button.grid(column=2, row=3, columnspan=1)


generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=3, row=3, columnspan=1)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=3, row=1, columnspan=1)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=3)


window.mainloop()
