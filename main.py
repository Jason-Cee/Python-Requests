from tkinter import *
from tkinter import messagebox
import requests

root = Tk()
root.title("Chuck Norris")
root.geometry("350x350")
root.resizable(False, False)
root.config(bg="aqua")


def joke():
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        data = response.json()
        messagebox.showinfo("Chuck", data["value"])
    except requests.exceptions.ConnectionError as x:
        messagebox.showerror("ERROR", "Please Get Better Wifi")


btn = Button(root, text="Click for a Chuck", command=joke, borderwidth=4)
btn.config(bg="crimson", fg="black")
btn.place(x=100, y=40)
root.mainloop()
