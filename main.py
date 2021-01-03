from tkinter import *

#create main window
main = Tk()
# main window Title & dimensions
main.title("welcome screen")
main.geometry('700x400')


#adding widgets
username_lbl = Label(main, text = "Enter your Username:")
password_lbl = Label(main, text = "Enter your password:")
username_lbl.grid()
password_lbl.grid()
def clicked():
    login_btn.configure(text = "done")
login_btn = Button(main, text = "login", fg = 'red', command = clicked)

login_btn.grid(column = 1, row = 0)

# main loop
main.mainloop()