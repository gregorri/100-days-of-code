from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# Labels
label = Label(text="is equal to", font=("Arial", 19, "bold"))
label.grid(column=0, row=2)

label_km = Label(text="0", font=("Arial", 19, "bold"))
label_km.grid(column=1, row=2)

label = Label(text="Miles", font=("Arial", 19, "bold"))
label.grid(column=4, row=1)

label = Label(text="Km", font=("Arial", 19, "bold"))
label.grid(column=4, row=2)

# Entries
entry = Entry(width=10)
entry.grid(column=1, row=1)


def calculate_miles_to_km():
	miles = entry.get()
	km = round(int(miles) * 1.609)
	label_km.config(text=km)


# Buttons
button = Button(text="Calculate", command=calculate_miles_to_km)
button.grid(column=1, row=3)

window.mainloop()
