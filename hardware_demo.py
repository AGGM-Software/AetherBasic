from AetherHardware import *

if __name__ == "__main__":
    root = tk.Tk()
    laser = LaserModule(root)
    laser.LaserDiodeOn(255)
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    flashlight = FlashlightModule(root)
    
    flashlight.FlashlightOn(255)  
    
    root.mainloop()