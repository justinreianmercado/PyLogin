import tkinter as tk
from tkinter import filedialog, Text
import os
from Account import Account

# Root is the window that allows a canvas to be placed on top
root = tk.Tk()

# Canvas is the background that allows frame to be placed on top
canvas = tk.Canvas(root, height=300, width=300, bg="black")
canvas.pack()

# Frame is the element on top of background, allows for buttons and text boxes to be placed on top
frame = tk.Frame(root, bg="white")
frame.place(relheight=1, relwidth=1)


def dispEntry():
    print(usernameEntry.get())
    print(passwordEntry.get())


def createAccountWindow():
    cAccountWindow = tk.Toplevel(root)
    cAccountCanvas = tk.Canvas(cAccountWindow, height=400, width=300, bg="black")
    cAccountCanvas.pack()
    cAccountFrame = tk.Frame(cAccountWindow, bg="white")
    cAccountFrame.place(relheight=1, relwidth=1)

    # First Name Label
    cAccFName = tk.Label(cAccountFrame, text="First Name")
    cAccFName.pack()
    cAccFName.place(relx=.2, rely=.1)
    # First Name Entry Widget
    cAccFNameEntry = tk.Entry(cAccountFrame, bg="white")
    cAccFNameEntry.pack()
    cAccFNameEntry.place(relx=.42, rely=.1)

    # Last Name Label
    cAccLName = tk.Label(cAccountFrame, text="Last Name")
    cAccLName.pack()
    cAccLName.place(relx=.2, rely=.16)
    # Last Name Entry Widget
    cAccLNameEntry = tk.Entry(cAccountFrame, bg="white")
    cAccLNameEntry.pack()
    cAccLNameEntry.place(relx=.42, rely=.16)

    # Username Label
    cAccUsername = tk.Label(cAccountFrame, text="Username")
    cAccUsername.pack()
    cAccUsername.place(relx=.2, rely=.22)
    # Username Entry Widget
    cAccUsernameEntry = tk.Entry(cAccountFrame, bg="white")
    cAccUsernameEntry.pack()
    cAccUsernameEntry.place(relx=.42, rely=.22)

    # Password Label
    cAccP1 = tk.Label(cAccountFrame, text="Password")
    cAccP1.pack()
    cAccP1.place(relx=.2, rely=.28)
    # Password Entry Widget
    cAccP1Entry = tk.Entry(cAccountFrame, bg="white", show="*")
    cAccP1Entry.pack()
    cAccP1Entry.place(relx=.42, rely=.28)

    # Validate Password Label
    cAccP2 = tk.Label(cAccountFrame, text="Re-enter Password")
    cAccP2.pack()
    cAccP2.place(relx=.07, rely=.34)
    # Validate Password Entry Widget
    cAccP2Entry = tk.Entry(cAccountFrame, bg="white", show="*")
    cAccP2Entry.pack()
    cAccP2Entry.place(relx=.42, rely=.34)

    # Phone Number Label
    cAccPhone = tk.Label(cAccountFrame, text="Phone number (optional)")
    cAccPhone.pack()
    cAccPhone.place(relx=.01, rely=.4)
    # Phone Number Entry Widget
    cAccPhoneEntry = tk.Entry(cAccountFrame, bg="white")
    cAccPhoneEntry.pack()
    cAccPhoneEntry.place(relx=.48, rely=.4)

    # Recovery Email Address Label
    cAccRecoveryEmail = tk.Label(cAccountFrame, text="Recovery Email (optional)")
    cAccRecoveryEmail.pack()
    cAccRecoveryEmail.place(relx=.01, rely=.46)
    # Recovery Email Address Entry Widget
    cAccRecoveryEmailEntry = tk.Entry(cAccountFrame, bg="white")
    cAccRecoveryEmailEntry.pack()
    cAccRecoveryEmailEntry.place(relx=.48, rely=.46)


# Login Button
loginButton = tk.Button(frame, padx=5, pady=5, bg="#42f5b6", text="Login", command=dispEntry)
loginButton.pack()
loginButton.place(relx=.6, rely=.8)

# Create Account Button
cAccountButton = tk.Button(frame, padx=5, pady=5, bg="#42f5b6", text="Create Account", command=createAccountWindow)
cAccountButton.pack()
cAccountButton.place(relx=.2, rely=.8)

# Username Label
usernameLabel = tk.Label(frame, text="Username")
usernameLabel.pack()
usernameLabel.place(relx=.2, rely=.3)
# Username Entry Widget
usernameEntry = tk.Entry(frame, bg="white")
usernameEntry.pack()
usernameEntry.place(relx=.4, rely=.3)

# Password Label
passwordLabel = tk.Label(frame, text="Password")
passwordLabel.pack()
passwordLabel.place(relx=.2, rely=.38)
# Password Entry Widget
passwordEntry = tk.Entry(frame, bg="white", show="*")
passwordEntry.pack()
passwordEntry.place(relx=.4, rely=.38)

root.mainloop()
