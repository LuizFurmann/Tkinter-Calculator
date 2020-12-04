from tkinter import *

window = Tk()

class Calculator():
    window = window

    def __init__(self):
        self.display()
        window.mainloop()

    def display(self):

        def click_plus():
            first_number = visor.get()
            global f_number
            global math
            math = "plus"
            f_number = float(first_number)
            visor.delete(0, END)

        def click_less():
            first_number = visor.get()
            global f_number
            global math
            math = "less"
            f_number = float(first_number)
            visor.delete(0, END)

        def click_div():
            first_number = visor.get()
            global f_number
            global math
            math = "div"
            f_number = float(first_number)
            visor.delete(0, END)
            
        def click_mult():
            first_number = visor.get()
            global f_number
            global math
            math = "mult"
            f_number = float(first_number)
            visor.delete(0, END)

        def click_iqual():
            second_number = visor.get()
            visor.delete(0, END)
            if math == "plus":
                visor.insert(0, f_number + float(second_number))
            elif math == "less":
                visor.insert(0, f_number - float(second_number))
            elif math == "div":
                visor.insert(0, f_number / float(second_number))
            elif math == "mult":
                visor.insert(0, f_number * float(second_number))

        def deletar():
            visor.delete(0, END)

        def click_point():
            visor.insert(END, ".")

        def click_button(number):
            recent = visor.get()
            visor.delete(0, END)
            visor.insert(END, str(recent) + str(number))

        visor = Entry(window, background="lightgreen")
        visor.pack()

        bt7 = Button(window, text="7", background="lightblue", pady=14, padx=14, bd=4, command=lambda: click_button(7))
        bt7.place(x=10, y=100)
        bt4 = Button(window, text="4", background="lightblue", pady=14, padx=14, bd=4, command=lambda: click_button(4))
        bt4.place(x=10, y=155)
        bt1 = Button(window, text="1", background="lightblue", pady=14, padx=14, bd=4, command=lambda: click_button(1))
        bt1.place(x=10, y=210)
        bt0 = Button(window, text="0", background="lightblue", pady=14, padx=14, bd=4, command=lambda: click_button(0))
        bt0.place(x=60, y=267)
        bt8 = Button(window, text="8", background="lightblue", pady=14, padx=14, bd=4, command=lambda: click_button(8))
        bt8.place(x=60, y=100)
        bt5 = Button(window, text="5", background="lightblue", pady=14, padx=14, bd=4, command=lambda: click_button(5))
        bt5.place(x=60, y=155)
        bt2 = Button(window, text="2", background="lightblue", pady=14, padx=14, bd=4, command=lambda: click_button(2))
        bt2.place(x=60, y=210)
        btd = Button(window, text=".", background="lightblue", pady=14, padx=14, bd=4, command=lambda: click_button("."))
        btd.place(x=10, y=267)
        bt9 = Button(window, text="9", background="lightblue", pady=14, padx=14, bd=4, command=lambda: click_button(9))
        bt9.place(x=110, y=100)
        bt6 = Button(window, text="6", background="lightblue", pady=14, padx=14, bd=4, command=lambda: click_button(6))
        bt6.place(x=110, y=155)
        bt3 = Button(window, text="3", background="lightblue", pady=14, padx=14, bd=4, command=lambda: click_button(3))
        bt3.place(x=110, y=210)
        btp = Button(window, text="+", background="lightblue", pady=14, padx=13, bd=4, command=click_plus)
        btp.place(x=160, y=100)
        btl = Button(window, text="-", background="lightblue", pady=14, padx=14, bd=4, command=click_less)
        btl.place(x=160, y=155)
        btm = Button(window, text="*", background="lightblue", pady=14, padx=14, bd=4, command=click_mult)
        btm.place(x=160, y=210)
        btd = Button(window, text="/", background="lightblue", pady=14, padx=14, bd=4, command=click_div)
        btd.place(x=160, y=265)
        btc = Button(window, text="C", background="lightblue", pady=14, padx=14, bd=4, command=deletar)
        btc.place(x=110, y=267)
        bti = Button(window, text="=", background="lightblue", pady=14, padx=88, bd=4, command=click_iqual)
        bti.place(x=10, y=325)

        self.window.title("Python")
        self.window.geometry("220x400")
        self.window.resizable(False, False)


Calculator()