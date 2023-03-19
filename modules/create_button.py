import customtkinter as ctk
import random
import modules.main_app as m_app
import modules.create_frame as m_frame
import modules.create_entry as m_entry

def create_button(master, text, width=100, height=50, fg="black"):
    button = ctk.CTkButton(
        master= master,
        width= width,
        height= height,
        text= text,
        command= clear_text
)
    return button

# def entrance(master, text, width=100, height=50, fg="black"):
    # button1 = ctk.CTkButton(
        # master = master,
        # text = text,
        # width = width,
        # height = height
    # )
def clear_text():
    m_entry.text_input.delete(0, ctk.END)
    m_entry.text_input2.delete(0, ctk.END)
    
button1 = create_button(master=m_app.main_app.FRAME1, text= "Авторезуватися")
button1.place(x= m_app.main_app.FRAME1._current_width // 2 - 50, y= m_app.main_app.FRAME1._current_height // 2, anchor = ctk.CENTER)

button2 = create_button(master = m_app.main_app.FRAME1,text = "Вхід")
button2.place(x = m_app.main_app.FRAME1._current_width // 2 + 60, y = m_app.main_app.FRAME1._current_height // 2, anchor = ctk.CENTER)
