import customtkinter as ctk
import modules.create_frame as m_frame 
app_width = 600
app_height = 700

class App(ctk.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()
        self.geometry(f"{self.APP_HEIGHT}x{self.APP_WIDTH}+{0}+{0}")
        self.title("Вікно")
        self.resizable(False,False)
        
        self.FRAME1 = m_frame.Mains_Frame(text = '',master = self, width = app_width, height = 80,border_width=5)
        self.FRAME2 = m_frame.Mains_Frame(text='', master = self, width = app_width, height=350, border_width=5)
        # self.FRAME1.place(x = app_width // 2 + 50, y = app_height // 2 + 200, anchor = ctk.CENTER)
        self.FRAME1.pack(side='bottom', anchor='s', padx=10, pady=10)
        # self.FRAME2.place( x = app_width // 2 + 50, y = app_height // 2 - 20, anchor = ctk.CENTER)
        

main_app = App(app_width, app_height)

