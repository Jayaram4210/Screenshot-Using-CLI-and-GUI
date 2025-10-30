import pyautogui
import datetime
import os
import tkinter as tk
from tkinter import messagebox

folder = "../screenshots"
os.makedirs(folder, exist_ok=True)

def take_screenshot():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(folder, f"screenshot_{timestamp}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    messagebox.showinfo("Success", f"Screenshot saved as:\n{filename}")

root = tk.Tk()
root.title("Screenshot App")
root.geometry("500x250")

label = tk.Label(root, text="Click to take a screenshot", font=("Arial", 16))
label.pack(pady=20)

btn = tk.Button(root, text="Take Screenshot", command=take_screenshot, bg="blue", fg="white")
btn.pack(pady=10)

root.mainloop()
