from cgitb import text
import tkinter as tk
from tkinter.messagebox import *
from PyQt5 import QtGui
import pandas as pd

import get_info_from_webpage as getData
import delete_everything_from_db as delData
import check_db_info as checkInfo
import create_csv as createCSVs
import setup_db as sDB


class Table:
    # Initialize a constructor
    def __init__(self, gui, a, df):
        # Creating the table
        for i in range(total_rows):
            for j in range(total_columns):
                if i == 0:
                    self.entry = tk.Entry(gui, width=20, bg='LightSteelBlue', fg='Black',
                                          font=('Arial', 11, 'bold'))
                else:
                    self.entry = tk.Entry(gui, width=20, fg='blue',
                                          font=('Arial', 11, ''))

                self.entry.grid(row=i+a, column=j)
                self.entry.insert(tk.END, df.iat[i, j])

# make function for buttons


def get_info_from_webpage():
    showwarning("Program Is Running!",
                "Please don't close, don't be afraid the program, it is trying to get information from server")
    getData.main()
    showinfo("Success!", "Data has successfully inserted into database")


def delete_data():
    MsgBox = askquestion(
        'Deleting Data', 'Are you sure you want to delete all data from database?', icon='warning')
    if MsgBox == 'yes':
        delData.main()
        showinfo("Success!", "Data has successfully deleted")


def check_db_info():
    global df1, df2, df3, df4, total_rows, total_columns
    df1, df2, df3, df4 = checkInfo.main()

    total_rows = len(df1.axes[0])
    total_columns = len(df1.axes[1])
    # check if there are data in database
    if total_rows == 0 or total_columns == 0:
        showerror("No Data in Database!",
                  'There are no data stored in the database. Please press the button "Retrieve data from Web" to insert data')
    else:
        info = tk.Toplevel(root)
        info.title("Saved data")
        title1 = tk.Label(
            info, text="Nights spent at tourist accommodation establishments - monthly data",
            fg='Black', font=('Arial', 11, 'bold')).grid(row=0, column=0, columnspan=3, sticky='ws', pady=(10, 0))
        table1 = Table(info, 1, df1)

        title2 = tk.Label(
            info, text="Nights spent by non-residents at tourist accommodation establishments - 1990-2011 - world geographical breakdown - monthly data",
            fg='Black', font=('Arial', 11, 'bold')).grid(row=5, column=0, columnspan=7, sticky='ws', pady=(10, 0))
        table2 = Table(info, 6, df2)

        title3 = tk.Label(
            info, text="Arrivals at tourist accommodation establishments - monthly data",
            fg='Black', font=('Arial', 11, 'bold')).grid(row=8, column=0, columnspan=7, sticky='ws', pady=(10, 0))
        table3 = Table(info, 9, df3)

        title4 = tk.Label(
            info, text="Arrivals of non-residents at tourist accommodation establishments - 1990-2011 - world geographical breakdown - monthly data",
            fg='Black', font=('Arial', 11, 'bold')).grid(row=11, column=0, columnspan=7, sticky='ws', pady=(10, 0))
        table4 = Table(info, 12, df4)


def create_CSV():
    createCSVs.main()
    showinfo("CSV Files Created!",
             """CSV Files have been successfuly created. They are lockated in the folder named "csv files" """)


def setUpDB():
    MsgBox = askquestion(
        'Create Database', 'Are you sure you want to create the database? It will not be created if it already exists!')
    if MsgBox == 'yes':
        sDB.main()
        showinfo('Database Created',
                 'Database is successfully created. Please press the button "Retrieve data from Web" to insert data')


# start program
root = tk.Tk()
root.title("Tourist in Greece and Spain")
root.eval('tk::PlaceWindow . center')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

window_height = 270
window_width = 530

btnWidth = 25
btnHeight = 2

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width,
              window_height, x_cordinate, y_cordinate))

# make buttons
dataBtn = tk.Button(root, text="Retrieve data from Web", font=('Arial', 11, ''), height=btnHeight, width=btnWidth,
                    command=get_info_from_webpage).grid(column=0, row=1, padx=10, pady=(0, 10), columnspan=2)

chkInfo = tk.Button(root, text="Check Saved Info", font=('Arial', 11, ''), height=btnHeight, width=btnWidth,
                    command=check_db_info).grid(column=0, row=2, padx=10, pady=10, columnspan=2)

crtCsv = tk.Button(root, text="Create CSVs", font=('Arial', 11, ''), height=btnHeight, width=btnWidth,
                   command=create_CSV).grid(column=0, row=3, padx=10, pady=10)

setDB = tk.Button(root, text="Create database", font=('Arial', 11, ''), height=btnHeight, width=btnWidth,
                  command=setUpDB).grid(column=1, row=3, padx=10, pady=10)

delBtn = tk.Button(root, text="Delete all data from database", fg='red', font=('Arial', 11, ''), height=btnHeight, width=btnWidth,
                   command=delete_data).grid(column=0, row=4, padx=10, pady=10, columnspan=2)

root.mainloop()
