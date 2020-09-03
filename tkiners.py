try:
    import tkinter
except ImportError as error:
    print(error)

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
# tkinter._test()

mainwindow=tkinter.Tk()
mainwindow.title("This is Sparta")
mainwindow.geometry("400x400")
mainwindow.mainloop()
