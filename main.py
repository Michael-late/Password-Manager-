from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def GeneratePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    let = [random.choice(letters) for x in range(nr_letters)]
    sym = [random.choice(numbers) for x in range(nr_numbers)]
    num = [random.choice(symbols) for x in range(nr_symbols)]
    password_list = let + sym + num
    random.shuffle(password_list)

    password = "".join(password_list)
    passwordENTRY.delete(0,END)
    pyperclip.copy(password)
    passwordENTRY.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def SaveData():
    web = websiteENTRY.get()
    login = loginENTRY.get()
    password = passwordENTRY.get()

    details = {web: (login,password)}

    if (len(web) == 0) or (len(password) == 0):
        messagebox.showinfo(title="Warning", message="Entry must not be empty")
    else:
        isok = messagebox.askokcancel(title=web, message=f"Details Enter Are: \nEmail: {login} \nPassword: {password}")
        if isok:
            with open("data.txt","a") as file:
                file.write(str(details) + "\n")
            websiteENTRY.delete(0,END)
            passwordENTRY.delete(0,END)


# def confirmation():
#     confirm = Toplevel(window)
#     confirm.geometry("200x200")
#     confirm.title("Confirmation")
#     confirmLabel = Label(confirm,text="Save Confirmed")
#     confirmLabel.pack()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20,pady=20)

canvas = Canvas(window, width=200,height=200)
logoIMG = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logoIMG)
canvas.grid(row=0,column=1)

#website part
websiteLabel = Label(text="Website:")
websiteLabel.grid(row=1,column=0)
websiteENTRY = Entry(width=35)
websiteENTRY.focus()
websiteENTRY.grid(row=1,column=1,columnspan=2,sticky=EW)

#email/username 
loginLabel = Label(text="Email/Username:")
loginLabel.grid(row=2,column=0)
loginENTRY = Entry(width=35)
loginENTRY.insert(0,"abc@z.com")
loginENTRY.grid(row=2,column=1,columnspan=2,sticky=EW)

#Password
passwordLabel = Label(text="Password:")
passwordLabel.grid(row=3,column=0)
passwordENTRY = Entry(width=35)
passwordENTRY.grid(row=3,column=1)
passwordBTN = Button(text="Generate Password", command=GeneratePassword)
passwordBTN.grid(row=3,column=2,sticky=EW)

#Add
AddBTN = Button(text="ADD", width=36,command=SaveData)
AddBTN.grid(row=4,column=1,columnspan=2,sticky=EW)


window.mainloop()