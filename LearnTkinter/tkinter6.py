import tkinter as tk

window = tk.Tk()
window.title('My windows')
window.geometry('400x400')

l = tk.Label(window, bg='yellow', width=50, text='Empty')
l.pack()


def print_selection(v):
    l.config(text='You have selected ' + v)


s = tk.Scale(window,
             label='Try me',
             from_=5,
             to=11,
             orient=tk.HORIZONTAL,
             length=200,
             showvalue=0,
             tickinterval=2,
             resolution=0.01,
             command=print_selection)
s.pack()

window.mainloop()
