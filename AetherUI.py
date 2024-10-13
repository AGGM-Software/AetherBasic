
# AetherUI.py

import tkinter as tk
from tkinter import font

class AetherUI:
    def __init__(self, root):
        self.root = root
        self.setup_fonts()

    def setup_fonts(self):
        self.font_header = font.Font(family="Helvetica Neue", size=22, weight="bold")
        self.font_button = font.Font(family="Helvetica Neue", size=16)
        self.font_navbar = font.Font(family="Helvetica Neue", size=18, weight="bold")

    def create_navbar(self, title_text):
        navbar = tk.Frame(self.root, bg="#1c1c1e", height=60)
        navbar.pack(side="top", fill="x")
        title = tk.Label(navbar, text=title_text, fg="white", bg="#1c1c1e", font=self.font_navbar)
        title.pack(side="left", padx=20, pady=15)

    def create_header(self, text):
        header = tk.Label(self.root, text=text, font=self.font_header, fg="#1c1c1e", bg="white")
        header.pack(pady=30)

    def create_button(self, text, command):
        button_canvas = tk.Canvas(self.root, width=360, height=55, bg="white", highlightthickness=0)
        button_canvas.pack(pady=15)
        button_canvas.create_rounded_rectangle(2, 2, 358, 53, radius=55, fill="black", outline="")
        button_text = button_canvas.create_text(180, 28, text=text, fill="white", font=self.font_button)
        button_canvas.tag_bind(button_text, "<Button-1>", lambda e: command())

    def create_footer(self, text):
        footer = tk.Frame(self.root, bg="#f2f2f2", height=30)
        footer.pack(side="bottom", fill="x")
        label = tk.Label(footer, text=text, fg="#333333", bg="#f2f2f2", font=self.font_button)
        label.pack(pady=5, padx=10)

    def create_image(self, image_path, width, height, radius=20):
        image_canvas = tk.Canvas(self.root, width=width, height=height, bg="white", highlightthickness=0)
        image_canvas.pack(pady=15)
        image_canvas.create_rounded_rectangle(0, 0, width, height, radius=radius, fill="white", outline="")
        img = tk.PhotoImage(file=image_path)
        image_canvas.create_image(0, 0, anchor="nw", image=img)
        image_canvas.image = img

def rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]
    return self.create_polygon(points, smooth=True, **kwargs)

tk.Canvas.create_rounded_rectangle = rounded_rectangle
