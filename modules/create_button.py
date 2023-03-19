import customtkinter as ctk
import modules.main_app as m_app
import modules.create_frame as m_frame
import modules.create_entry as m_entry
import modules.create_data_frame as m_data

def create_button(master, text, width=100, height=50, fg="black"):
    button = ctk.CTkButton(
        master= master,
        width= width,
        height= height,
        text= text,
        command= button_auto
)
    return button

def button_auto():
    m_entry.text_input.delete(0, ctk.END)
    send_button = ctk.CTkButton(
    master = m_data.message_frame, 
    text ="send",
    width = 90,
    height = 50,
    fg_color = 'green',
    command= m_data.write_text
)
    send_button.place(x = m_data.message_frame._current_width // 2, y = m_data.message_frame._current_height // 2 + 140, anchor = ctk.CENTER)

def create_button2(master, text, width=100, height=50, fg="black"):
    button2 = ctk.CTkButton(
        master= master,
        width= width,
        height= height,
        text= text,
        command= button_auto2
)
    return button2

def button_auto2():
    m_entry.text_input.delete(0, ctk.END)
    send_button2 = ctk.CTkButton(
    master = m_data.message_frame, 
    text ="sending",
    width = 90,
    height = 50,
    fg_color = 'green',
    command= m_data.generate_button
)
    send_button2.place(x = m_data.message_frame._current_width // 2, y = m_data.message_frame._current_height // 2 + 140, anchor = ctk.CENTER)
    
button1 = create_button(master=m_app.main_app.FRAME1, text= "Авторезуватися")
button1.place(x= m_app.main_app.FRAME1._current_width // 2 - 50, y= m_app.main_app.FRAME1._current_height // 2, anchor = ctk.CENTER)

button2 = create_button2(master = m_app.main_app.FRAME1,text = "Вхід")
button2.place(x = m_app.main_app.FRAME1._current_width // 2 + 60, y = m_app.main_app.FRAME1._current_height // 2, anchor = ctk.CENTER)
