import pyautogui
import time
import tkinter as tk

def screenshot():
    root.withdraw()  # Hide the entire window
    time.sleep(0.5)  # Small delay to ensure the window is hidden
    name = int(round(time.time() * 1000))
    name = '{}.png'.format(name)
    img = pyautogui.screenshot(name)
    root.deiconify()  # Show the window again
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button( 
    frame,
    text="Take a Screenshot",
    command=screenshot
)
button.pack(side=tk.LEFT)

close = tk.Button(
    frame,
    text="Quit",
    command=root.quit
)
close.pack(side=tk.LEFT)

root.mainloop()
