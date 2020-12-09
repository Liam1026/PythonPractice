import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('400x400')

# canvas = tk.Canvas(window, height=200, width=500)
# canvas.grid(row=1, column=1)
# image_file = tk.PhotoImage(
#     file='/home/ohh/ohhPythonProject/LearnTkinter/2020-12-0800:11:51.png')
# image = canvas.create_image(0, 0, anchor='nw', image=image_file)

# tk.Label(window, text='2').pack(side='top')
# tk.Label(window, text='2').pack(side='bottom')
# tk.Label(window, text='2').pack(side='left')
# tk.Label(window, text='2').pack(side='right')

for i in range(4):
    for j in range(3):
        tk.Label(window, text=3).grid(row=i, column=j, padx=20, pady=20)

tk.Label(window, text=1).place(x=200, y=200, anchor='nw')

window.mainloop()
