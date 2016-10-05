from socket import *
import Tkinter

def main():
    top = Tkinter.Tk()
    textbox = Tkinter.Text(top, width=50, height=5, bg="black", fg="magenta", font=("Arial", 16))
    textbox.grid(row=0, column=0, sticky="NSWE")

    scrollbar = Tkinter.Scrollbar(top, cursor="spraycan", bg="#00ffff")
    scrollbar.grid(row=0, column=1, sticky="NSWE")

    scrollbar.config(command=textbox.yview)
    textbox.config(yscrollcommand=scrollbar.set)

    chatbox = Tkinter.Text(top, width=50, height=2, bg="white", fg="black", font=("Arial", 16))
    chatbox.grid(row=1, column=0, columnspan=2, sticky="WE")

    top.grid_columnconfigure(0,weight=1)
    top.grid_rowconfigure(0,weight=1)

    
    #textbox.insert(Tkinter.INSERT, )
    #textbox.configure(state=Tkinter.DISABLED)

    top.title('ICQ 2')
    top.mainloop()
    

if __name__== "__main__":
    main()
