from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

	password_entry.delete(0, END)  # delete the content of the entry
	letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] # list comprehension
	symbols = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)] + [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]
	numbers = [str(i) for i in range(10)]
	password_list = [random.choice(letters) for _ in range(random.randint(8, 10))] + [random.choice(symbols) for _ in range(random.randint(2, 4))] + [random.choice(numbers) for _ in range(random.randint(2, 4))]
	random.shuffle(password_list)   # shuffle the list to mix the characters and symbols in a random order
	password = "".join(password_list)
	password_entry.insert(0, password)  # insert the password in the entry
	pyperclip.copy(password)  # copy the password to the clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()
	new_data = f"{website} | {email} | {password}"

	# Check if the user has entered a website and a password
	if len(website) == 0 or len(password) == 0:
		messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")    # showinfo is a messagebox
	else:
		is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: " f"\nEmail: {email} " f"\nPassword: {password} "f"\nIs it ok to save?")
		if is_ok:
			with open("data.txt", "a") as data_file:
				data_file.write(f"{new_data}" + "\n")

				website_entry.delete(0, END)
				email_entry.delete(0, END)
				password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)  # adding padding to the window

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=45)
website_entry.grid(column=1, row=1, columnspan=2)  # columnspan is used to span the entry over multiple columns
website_entry.focus()  # focus on the entry when the window opens
email_entry = Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "ursachi.g@mail.ru")  # insert a default value in the entry
password_entry = Entry(width=26)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
