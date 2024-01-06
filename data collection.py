import os
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

#CODE WRITTEN AND MANAGED BY MSA 
#(MOHAMMED-SUHEM-AHMED)


root = Tk()
root.title("Data Collection")
root.geometry("450x450")
root.minsize(width=450, height=450)
root.maxsize(width=450, height=450)

company_name = "XYZ COMPANY"

def CODE():
    # Provide the path to the specific text file you want to open
    file_path = "/home/msa/Documents/INFO_DATA/data collection.py"  # Change this path to the desired text file

    try:
        # Open the text file with the default text editor
        os.system(f'xdg-open "{file_path}"')
    except FileNotFoundError:
        messagebox.showwarning("File Not Found", "The specified text file was not found.")



def button_upload_command():
    file_path = filedialog.askopenfilename(title="Select a File")
    file_uploaded.set(file_path)

def reset_screen():
    name_ent.delete(0, END)
    name_phone.delete(0, END)
    name_mail.delete(0, END)
    file_uploaded.set("")

def on_exit():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()

def view():
    # Provide the path to the folder you want to open
    folder_path = "/home/msa/Documents/INFO_DATA"  # Change this path to the desired folder

    # Open the file explorer at the specified folder
    os.system(f'xdg-open "{folder_path}"')

def button_save_command():
    # Get the user's input from the "Name" entry field
    user_name = name_ent.get()

    # Ensure the user has entered a name
    if not user_name:
        messagebox.showwarning("Warning", "Please enter a name.")
        return

    # Create the 'save_data' folder in the "Documents" directory if it doesn't exist
    save_folder = os.path.join(os.path.expanduser("~"), "Documents", "INFO_DATA")
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Create a folder with the user's name inside 'save_data'
    user_folder = os.path.join(save_folder, user_name)
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    # Save data to a text file inside the user's folder
    data_file_path = os.path.join(user_folder, "data.txt")
    with open(data_file_path, "w") as file:
        file.write(f"Name: {user_name}\n")
        file.write(f"Phone: {name_phone.get()}\n")
        file.write(f"Email: {name_mail.get()}\n")
        file.write(f"Uploaded File: {file_uploaded.get()}")

    # Copy the uploaded file to the user's folder
    if file_uploaded.get() and os.path.exists(file_uploaded.get()):
        shutil.copy(file_uploaded.get(), os.path.join(user_folder, "RESUME"))

    messagebox.showinfo("Success", "Data saved successfully.")
    reset_screen()

file_uploaded = StringVar()

font_size = 14
label_font = ("Helvetica", font_size, "bold")
label = Label(root, text=company_name, font=label_font, relief=SUNKEN)
label.grid(row=2, column=2)

label_name = Label(root, text='Name', font=label_font)
label_name.grid(row=5, column=0)
name_ent = Entry(root)
name_ent.grid(row=5, column=2)

label_phone = Label(root, text='Phone number', font=label_font)
label_phone.grid(row=6, column=0)
name_phone = Entry(root)
name_phone.grid(row=6, column=2)

label_non3 = Label(root)
label_non3.grid(row=3, column=0)

label_non1 = Label(root)
label_non1.grid(row=1, column=0)

label_mail = Label(root, text='Email', font=label_font)
label_mail.grid(row=7, column=0)
name_mail = Entry(root)
name_mail.grid(row=7, column=2)

label_non8 = Label(root)
label_non8.grid(row=8, column=0)

label_RESUME = Label(root, text='RESUME', font=label_font)
label_RESUME.grid(row=9, column=0)

button_upload = Button(text="UPLOAD FILE", font=label_font, command=button_upload_command)
button_upload.grid(row=9, column=2)

button_save = Button(text="--SAVE--", font=label_font, command=button_save_command)
button_save.grid(row=10, column=2, padx=40)

button_exit = Button(text="EXIT", font=label_font, command=on_exit)
button_exit.grid(row=12, column=2, padx=40)

button_view = Button(text="VIEW FILES", font=label_font, command= view)
button_view.grid(row=13, column=3, padx=0)

button_code = Button(text="VIEW CODE", font=label_font, command= CODE)
button_code.grid(row=14, column=3, padx=0)

root.mainloop()
