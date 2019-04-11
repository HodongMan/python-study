import tkinter as tk
from PIL import ImageTk, Image

banana = r"banana.gif"
bordercolor = [('aliceblue', '#F0F8FF'), ('blue', '#0000EF'), ('biege', '#F5F5DC'), ('cornsilk', '#FFF8DC'), ('red', '#FF0000'), ('lightgreen', '#90EE90')]

class BgChange:

    def __init__(self, label, color):

        self.label = label
        self.color = color

    def __call__(self, event=None):

        self.label.configure(bg=self.color)

class MyWindow(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title("select bordercolor")
        f_button = tk.Frame(self)
        f_button.pack(side=tk.LEFT, padx=5, pady=1)
        self.banana = ImageTk.PhotoImage(Image.open(banana))
        label = tk.Label(self, image=self.banana, relief=tk.RAISED, bd=6)
        label.pack(side=tk.RIGHT, padx=7)

        for name, code in bordercolor:
            b = tk.Button(f_button, text=name, bg=code, command=BgChange(label, code) )
            b.pack(fill=tk.X)


if __name__ == "__main__":
    
    window = tk.Tk()
    frame = MyWindow(window)
    frame.pack()
    window.mainloop()