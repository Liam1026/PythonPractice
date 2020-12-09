import tkinter as tk

window = tk.Tk()
window.title('My windows')
window.geometry('400x400')

l = tk.Label(window, bg='yellow', width=20, text='Empty')
l.pack()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I only love Python')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I only love C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I love either')
    else:
        l.config(text='I love both')


var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(window,
                    text='Python',
                    variable=var1,
                    onvalue=1,
                    offvalue=0,
                    command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window,
                    text='C++',
                    variable=var2,
                    onvalue=1,
                    offvalue=0,
                    command=print_selection)

c2.pack()

window.mainloop()
