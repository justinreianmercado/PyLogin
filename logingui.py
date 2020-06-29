import tkinter as tk
from tkinter import filedialog, Text
import os
from Account import Account

# Create Window
root = tk.Tk()
root.title("Login GUI")


# Create frame
frame = tk.Frame(root, height=200, width=400)
frame.grid(row=0, column=0)


# Create Labels
usernameLabel = tk.Label(frame, text="Username: ", padx=20, pady=2)
usernameLabel.grid(row=0, column=0)
passwordLabel = tk.Label(frame, text="Password: ", padx=20, pady=2)
passwordLabel.grid(row=1, column=0)


# Create Entries
usernameEntry = tk.Entry(frame)
usernameEntry.grid(row=0, column=1)
passwordEntry = tk.Entry(frame, show="*")
passwordEntry.grid(row=1, column=1)


# Create Functions
# Will implement login later
def login():
    print(usernameEntry.get())
    print(passwordEntry.get())

def submitInfo():
    print("Submit!")

def createAccount():
    createAccountRoot = tk.Toplevel(frame)
    createAccountRoot.title("Create Account")

    # Create Labels
    c_firstNameLabel = tk.Label(createAccountRoot, text="First Name: ")
    c_firstNameLabel.grid(row=0, column=0)
    c_lastNameLabel = tk.Label(createAccountRoot, text="Last Name: ")
    c_lastNameLabel.grid(row=1, column=0)
    c_usernameLabel = tk.Label(createAccountRoot, text="Username: ")
    c_usernameLabel.grid(row=2, column=0)
    c_passwordLabel = tk.Label(createAccountRoot, text="Password: ")
    c_passwordLabel.grid(row=3, column=0)
    c_VpasswordLabel = tk.Label(createAccountRoot, text="Verify Password: ")
    c_VpasswordLabel.grid(row=4, column=0)
    c_phoneLabel = tk.Label(createAccountRoot, text="Phone Number: ")
    c_phoneLabel.grid(row=5, column=0)

    # Create Entries
    c_firstNameLabel = tk.Entry(createAccountRoot)
    c_firstNameLabel.grid(row=0, column=1)
    c_lastNameLabel = tk.Entry(createAccountRoot)
    c_lastNameLabel.grid(row=1, column=1)
    c_usernameLabel = tk.Entry(createAccountRoot)
    c_usernameLabel.grid(row=2, column=1)
    c_passwordLabel = tk.Entry(createAccountRoot, show="*")
    c_passwordLabel.grid(row=3, column=1)
    c_VpasswordLabel = tk.Entry(createAccountRoot, show="*")
    c_VpasswordLabel.grid(row=4, column=1)
    c_phoneLabel = tk.Entry(createAccountRoot)
    c_phoneLabel.grid(row=5, column=1)

    # Create Buttons
    c_submitButton = tk.Button(createAccountRoot, text="Submit", command=submitInfo)
    c_submitButton.grid(row=6, column=0)


# Create Buttons
loginButton = tk.Button(frame, text="Login", padx=20, pady=2, command=login)
loginButton.grid(row=2, column=0)
createAccountButton = tk.Button(frame, text="Create Account", padx=20, pady=2, command=createAccount)
createAccountButton.grid(row=2, column=1)

root.mainloop()