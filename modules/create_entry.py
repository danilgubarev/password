import customtkinter as ctk
import modules.main_app as m_app
import modules.create_data_frame as m_data_frame

width_input = 420
height_input = 50

font_size = ctk.CTkFont(
    family= "Arial",
    size= 20,
    # weight= "bold"
)


text = ctk.StringVar()
text2 = ctk.StringVar()

text_input = ctk.CTkEntry(
    master= m_data_frame.message_frame,
    width= width_input,
    height= height_input,
    fg_color= "white",
    text_color= "black",
    font= font_size,
    textvariable= text
)

text_input2 = ctk.CTkEntry(
    master= m_data_frame.message_frame,
    width= width_input,
    height= height_input,
    fg_color= "white",
    text_color= "black",
    font= font_size,
    textvariable= text2
)

text_input.place(x = m_data_frame.message_frame._current_width // 2 - 60, y = m_data_frame.message_frame._current_height // 2 - 100, anchor = ctk.CENTER)

text_input2.place(x = m_data_frame.message_frame._current_width // 2 - 60, y = m_data_frame.message_frame._current_height // 2 + 50, anchor = ctk.CENTER)