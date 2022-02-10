from cgitb import text
import tkinter as tk 

mainView = tk.Tk()
mainView.geometry("340x180")
mainView.configure(bg='gray')

lbl = tk.label(text='hello')
lbl.pack()

mainView.bind("<Control>", lambda event: print(event))

mainView.mainloop()