# Spaces to tsv converter
# This script takes a file arbitrarily formatted with spaces
# and converts to a new file with Tab Separated Values (TSV)
# This makes importing to Excel convenient
# Joe Canfield, Last Updated 3 Jan, 2023

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import re

""" Conversion Function Definition """


def convert():

    with open(path) as f:
        with open('RX_AC_LIN_DATA.csv', 'w') as tsv:
            for line in f:
                content = re.sub(" {2,}", "\t", line)   # Replace 2 or more spaces with tabs
                content = re.sub(" ", "", content)   # Remove single spaces
                tsv.write(content)
        tsv.close()
    f.close()


def browse_clicked():
    """ Callback when browse button is clicked """
    global path
    path = filedialog.askopenfilename(initialdir="/",
                                      title="Select a File",
                                      filetypes=(("Text files", "*.txt"),
                                                 ("Comma Separated Values", "*.csv"),
                                                 ("All Files", "*.*")))


def print_filepath():
    print(path)


""" GUI """

window = tk.Tk()
window.title('Data Formatter')

filepath_label = ttk.Label(text="File Path:")
filepath_label.pack(padx=10, pady=10)

path = ""   # Global variable

# File browser button
ttk.Button(window, text="Browse Files", command=browse_clicked).pack()

# File Conversion button
ttk.Button(window, text="Convert file", command=convert).pack()

ttk.Label(text="Export Format:").pack()
ttk.Combobox(values="CSV TSV txt").pack()

window.geometry("600x300")

window.mainloop()
