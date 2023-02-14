# Verify that ImageTK images are valid to pass to TK code.
import tkinter

from PIL import ImageTk

photo = ImageTk.PhotoImage()
bitmap = ImageTk.BitmapImage()

tkinter.Label(image=photo)
tkinter.Label(image=bitmap)

tkinter.Label().configure(image=photo)
tkinter.Label().configure(image=bitmap)
