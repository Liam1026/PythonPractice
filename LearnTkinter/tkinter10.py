import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('400x400')

tk.Label(window, text='On the window').pack()

frame = tk.Frame(window)
frame.pack()

frame_l = tk.Frame(frame)
frame_r = tk.Frame(frame)

frame_l.pack(side='left')
frame_r.pack(side='right')

tk.Label(frame_l, text='On the Frame_l1').pack()
tk.Label(frame_l, text='On the Frame_l2').pack()
tk.Label(frame_r, text='On the Frame_r1').pack()

window.mainloop()
