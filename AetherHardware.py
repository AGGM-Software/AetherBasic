# AetherHardware.py
# This module is used to control the hardware of the device.

import os
import time
import tkinter as tk

def currentTime():
    return time.time()

class LaserModule:
    def __init__(self, root):
        self.root = root
        self.root.title("laser diode")
        
        self.brightness = 255

        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='black')
        self.canvas.pack()

        self.circle = self.canvas.create_oval(150, 150, 250, 250, fill=self._brightness_to_color())

    def _brightness_to_color(self):
        red_value = int(self.brightness)
        return f'#{red_value:02x}0000'

    def LaserDiodeOn(self, brightness):
        self.brightness = brightness
        self.canvas.itemconfig(self.circle, fill=self._brightness_to_color())

    def LaserDiodeOff(self):
        self.brightness = 0
        self.canvas.itemconfig(self.circle, fill=self._brightness_to_color())

class FlashlightModule:
    def __init__(self, root):
        self.root = root
        self.root.title("flashlight")
        
        self.brightness = 255

        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='black')
        self.canvas.pack()

        self.canvas.create_rectangle(0, 0, 400, 400, fill=self._brightness_to_color())

    def _brightness_to_color(self):
        white_value = int(self.brightness)
        return f'#{white_value:02x}{white_value:02x}{white_value:02x}'

    def FlashlightOn(self, brightness):
        self.brightness = brightness
        self.canvas.itemconfig(self.canvas.find_all(), fill=self._brightness_to_color())

    def FlashlightOff(self):
        self.brightness = 0
        self.canvas.itemconfig(self.canvas.find_all(), fill=self._brightness_to_color())


