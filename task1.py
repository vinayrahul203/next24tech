import tkinter as tk
from tkinter import ttk, messagebox
def SubmitRegistrationForm():
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    gender = gender_combobox.get()
    phonenum=phonenum_entry.get()
    address=address_entry.get()

    # Validation
    if not firstname or not lastname or not phonenum or not email or not age or not gender:
        messagebox.showerror("Error", "Please ensure that you have filled in all fields")
        return
    
    if len(phonenum)<10 or len(phonenum)>10:
            messagebox.showerror("Error","Phone number should be 10 digits")
            return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for Age")
        return
    
    try:
        phonenum = int(phonenum)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid Phone Number")
        return

    # Upon Successful Validation, Display the details
    messagebox.showinfo("Success", "!!Registration Completed!!\nFirst Name: {}\nLast Name: {}\nEmail: {}\nAge: {}\nGender: {}\nPhone Number: {}\nAddress: {}".format(firstname, lastname, email, age, gender, phonenum, address))

# Creating the Main Window
window = tk.Tk()
window.title("Simple Registration Form")

# Creating Labels and Entries for each field
firstname_label = tk.Label(window, text="First Name:",bg="green",font=("Courier",15,"bold italic"))
firstname_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
firstname_entry = tk.Entry(window,font=("Courier",15,"italic"),foreground="black",justify="center")
firstname_entry.grid(row=0, column=1, padx=10, pady=5,ipadx=20,ipady=2)

lastname_label = tk.Label(window, text="Last Name:",bg="green",font=("Courier",15,"bold italic"))
lastname_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
lastname_entry = tk.Entry(window,font=("Courier",15,"italic"),foreground="black",justify="center")
lastname_entry.grid(row=1, column=1, padx=10, pady=5,ipadx=20,ipady=2)

email_label = tk.Label(window, text="Email:",bg="green",font=("Courier",15,"bold italic"))
email_label.grid(row=2, column=0, padx=10, pady=5,sticky=tk.W)
email_entry = tk.Entry(window,font=("Courier",15,"italic"),foreground="black",justify="center")
email_entry.grid(row=2, column=1, padx=10, pady=5,ipadx=20,ipady=2)

age_label = tk.Label(window, text="Age:",bg="green",font=("Courier",15,"bold italic"))
age_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
age_entry = tk.Entry(window,font=("Courier",15,"italic"),foreground="black",justify="center")
age_entry.grid(row=3, column=1, padx=10, pady=5,ipadx=20,ipady=2)

gender_label = tk.Label(window, text="Gender:",bg="green",font=("Courier",15,"bold italic"))
gender_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
gender_combobox = ttk.Combobox(window, values=["Male", "Female", "Other"],font=("Courier",15,"italic"),foreground="black",justify="center")
gender_combobox.grid(row=4, column=1, padx=10, pady=5,ipadx=10,ipady=2)

phonenum_label = tk.Label(window, text="Phone Number:",bg="green",font=("Courier",15,"bold italic"))
phonenum_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
phonenum_entry = tk.Entry(window,font=("Courier",15,"italic"),foreground="black",justify="center")
phonenum_entry.grid(row=5, column=1, padx=10, pady=5,ipadx=20,ipady=2)

address_label = tk.Label(window, text="Address:",bg="green",font=("Courier",15,"bold italic"))
address_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
address_entry = tk.Entry(window,font=("Courier",15,"italic"),foreground="black",justify="center")
address_entry.grid(row=6, column=1, padx=10, pady=5,ipadx=20,ipady=2)

# Creating a Submit button to click after filling all the fields
submit_button = tk.Button(window, text="Submit", command=SubmitRegistrationForm,fg="red",font=("Courier",15,"bold italic"),bg="black")
submit_button.grid(row=7, column=0, columnspan=2,padx=10, pady=5,sticky=tk.NSEW)

# To Run The Main Event Loop
window.configure(bg="green")
window.mainloop()
