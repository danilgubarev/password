import customtkinter as ctk
import modules.main_app as m_app
import modules.create_entry as m_entry
import modules.search_path as m_path
email_font = ctk.CTkFont(family= 'Calibri', size= 15, weight= 'bold')
password_font = ctk.CTkFont(family= 'Calibri', size= 15, weight= 'normal')

class MessageFrame(ctk.CTkFrame):
    def __init__(self, email, password, width, height, master, border_width, fg_color, bg_color, **kwargs):
        super().__init__(master= master, width= width, height= height, border_width= border_width, fg_color= fg_color, bg_color= bg_color, **kwargs)
        
        self.EMAIL = self.message_name_label(text= email, text_color= 'white', fg_color= 'transparent')
        self.PASSWORD = self.message_text_label(text= password, text_color= 'white', fg_color= 'transparent')
        
        self.EMAIL.place(x = 20, y = 10)
        self.PASSWORD.place(x = 20, y = 150)
    def message_name_label(self, text, text_color, fg_color):
        return ctk.CTkLabel(
            master= self,
            text= text,
            font= email_font,
            text_color= text_color,
            fg_color= fg_color,
            bg_color= 'transparent',
            # image= m_img_frame.image_message
            )
    #
    def message_text_label(self, text, text_color, fg_color):
        return ctk.CTkLabel(
            master= self,
            text= text,
            font= password_font,
            text_color= text_color,
            fg_color= fg_color,
            bg_color= 'transparent'
        )

        
        
        
message_frame = MessageFrame(
    email= 'E-MAIL:',
    password= 'PASSWORD:',
    width= m_app.app_width,
    height= 350,
    master= m_app.main_app,
    border_width= 5,
    fg_color= 'transparent',
    bg_color= 'transparent'
)
message_frame.pack()
dict1 = {
    "email":"",
    "password":""
}
def write_text():
    dict1["email"] = m_entry.text_input.get()
    dict1["password"] = m_entry.text_input2.get()
    m_path.create_json("json/abc.json", dict1) 
    m_app.main_app.FRAME1.pack_forget()
    message_frame.pack_forget()
    button_image = ctk.CTkButton(
        master= m_app.main_app,
        text='generate',
        width = 100,
        height=50,
        fg_color='green'
    )
    # mentry.text_input.delete(0, ctk.END)
    button_image.place(x = m_app.app_width // 2, y = m_app.app_height // 2, anchor = ctk.CENTER)
send_button = ctk.CTkButton(
    master = message_frame, 
    text ="send",
    width = 90,
    height = 50,
    fg_color = 'green',
    command= write_text
)
send_button.place(x = message_frame._current_width // 2, y = message_frame._current_height // 2 + 140, anchor = ctk.CENTER)
message_frame.pack(side='top', anchor='s', padx=10, pady=50)
