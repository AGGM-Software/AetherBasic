import tkinter as tk
from AetherUI import AetherUI

def start_click():
    print("Start button clicked!")

def settings_click():
    print("Settings button clicked!")
    

root = tk.Tk()
root.title("AetherUI")
root.geometry("420x700")
root.configure(bg="white")
ui = AetherUI(root)
ui.create_navbar("AetherUI")
ui.create_header("Welcome!")
ui.create_button("Start", start_click)
ui.create_button("Settings", settings_click)
ui.create_footer("Your footer text here")
root.mainloop()
