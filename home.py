from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk

class myApp(object):
    def __init__(self, **kw):
        self.window = Tk()
        self.window.title("Pizzaria Luigi")
        self.window.iconbitmap('C:\\Users\\vitor\\OneDrive\\Área de Trabalho\\devVitor\\pizzariaLuigi (2).ico')
        self.window.geometry("{}x{}" .format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        
        my_font = Font(family="Comic Sans MS",size=16, weight="bold")

        img = Image.open('backgroundPizza.jpg')
        img = img.resize((1380, 600), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(img)
        self.window.img = image
        background_image = Label(self.window, image=image, background="grey")
        background_image.place(x=0, y=-200, relwidth=1, relheight=1)
        self.window.wm_attributes("-transparentcolor", 'grey')

        background_white = Label(self.window, background="#FFFFFF")
        background_white.place(x=0, y=430, relwidth=1, relheight=1)

        nameStore = Label(background_image, text="Pizzaria Luigi", foreground="#F02036")
        nameStore.configure(font=Font(family="Comic Sans MS",size=60, weight="bold"))
        nameStore.place(x=430, y=300)

        buttonLogin = Button(self.window, width=21, text="ENTRAR", relief=SOLID, font=my_font)
        buttonLogin.configure(background="#FFFFFF", foreground="#2D2119")
        buttonLogin.place(x=530, y=525)

        buttonCreateAccount = Button(self.window, width=21, text="CADASTRAR", relief=SOLID,font=my_font)
        buttonCreateAccount.configure(background="#2D2119", foreground="#FFFFFF")
        buttonCreateAccount.place(x=530, y=600)

        nameCreator = Label(self.window, text="Software criado e mantido por José Vitor G. de Melo")
        nameCreator.configure(foreground="#2D2119", background="#FFFFFF")
        nameCreator.config(font=Font(family="Comic Sans MS",size=10, weight="bold"))
        nameCreator.place(x=1000, y=680)

    def execute(self):
        self.window.mainloop()

def main(args):
    app_proc = myApp()
    app_proc.execute()
    return 0
 
if __name__ == '__main__':
    sys.exit(main(sys.argv))