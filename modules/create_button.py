import customtkinter as ctk
import random
import modules.main_app as m_app
 


# buton_with = 100
# buton_height = 50

def create_button(master, text, width=100, height=50, fg="black"):
    button = ctk.CTkButton(
        master= master,
        width= width,
        height= height,
        text= text
)
    return button

button1 = create_button(master=m_app.main_app,
                        text= "Авторигестрироваться")

button1.place(
    x= m_app.app_width // 2, 
    y= m_app.app_height // 2 - 5,
    anchor = ctk.CENTER
)

button2 = create_button(master = m_app.main_app,
                        text = "Вхід")

button2.place(
    x = m_app.app_width // 2 ,
    y = m_app.app_height // 2 - 40,
    anchor = ctk.CENTER
)
