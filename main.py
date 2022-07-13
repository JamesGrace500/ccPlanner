# GUI imports
from tkinter import *
import customtkinter
import datetime

import database.db_table_creation as dtc

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('green')

date = datetime.datetime.now()

root = customtkinter.CTk()
root.title('ccPlanner')
root.geometry("1400x950+350+200")
root.resizable(True, True)

frame = customtkinter.CTkFrame(master=root,
                               width=200,
                               height=200,
                               corner_radius=10)
frame.pack(padx=20, pady=20, sticky="nsew")


def initalise_db():
    dtc.create_all_tables()


menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Create Database...')
file_menu.add_separator()

# add a submenu
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')

# add the File menu to the menubar
file_menu.add_cascade(
    label="Preferences",
    menu=sub_menu
)

menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu,
    underline=0
)

root.mainloop()
