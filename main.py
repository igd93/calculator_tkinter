import tkinter as tk

window = tk.Tk()
window.geometry("640x480")
window.title("Calcualtor app")

num1 = tk.Label(text = "Enter the 1st number: ")
num1.grid(column = 0, row = 0)
num1Entry = tk.Entry()
num1Entry.grid(column = 1, row = 0)

num2 = tk.Label(text = "ENter 2nd Number: ")
num2.grid(column = 0, row = 1)
num2Entry = tk.Entry()
num2Entry.grid(column = 1, row = 1)

def addNumbers():
    a = int(num1Entry.get())
    b = int(num2Entry.get())
    s = a + b
    result = f"The sum is {s}"
    textArea = tk.Text(master = window, height = 2, width = 15)
    textArea.grid(column = 1, row = 3)
    textArea.insert(tk.END, result)

button = tk.Button(window, text = "Calculate Sum", command = addNumbers, bg = "lightgreen")
button.grid(column = 1, row = 2)

window.mainloop()