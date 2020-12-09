import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('My window')
window.geometry('400x400')


def hit_me():
    tk.messagebox.showinfo(title='Hi', message='Hahahaha')
    tk.messagebox.showwarning(title='Hi', message='Nononono')
    tk.messagebox.showerror(title='Hi', message='No, Never')
    print(tk.messagebox.askquestion(title='Hi', message='hahahaha'))
    print(tk.messagebox.askyesno(title='Hi', message='hahahaha'))
    print(tk.messagebox.askretrycancel(title='Hi', message='hahahaha'))
    print(tk.messagebox.askokcancel(title='Hi', message='hahahaha'))
    print(tk.messagebox.askyesnocancel(title="Hi", message="haha"))


tk.Button(window, text='Hit me', command=hit_me).pack()

window.mainloop()
