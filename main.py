# Spaces to tsv converter
# This script takes a file arbitrarily formatted with spaces
# and converts to a new file with Tab Separated Values (TSV)
# This makes importing to Excel convenient
# Joe Canfield, Last Updated 3 Jan, 2023

import tkinter as tk
from tkinter import ttk

import re

""" Conversion Function Definition """


def convert_to_tsv(filepath):

    with open(filepath) as f:
        with open('RX_AC_LIN_DATA.csv', 'w') as tsv:
            for line in f:
                content = re.sub(" {2,}", "\t", line)   # Replace 2 or more spaces with tabs
                content = re.sub(" ", "", content)   # Remove single spaces
                tsv.write(content)
        tsv.close()
    f.close()


def browse_clicked():
    """ Callback when browse button is clicked """


""" GUI """

window = tk.Tk()
path = tk.StringVar()

filepath_label = ttk.Label(text="File Path:")
filepath_label.pack(padx=10, pady=10)

filepath_field = ttk.Entry(window, textvariable=path)
filepath_field.pack(padx=10, pady=10)
filepath_field.focus()

browse = ttk.Button(window, text="Browse", command=browse_clicked)
browse.pack()


window.geometry("600x300")

window.mainloop()


# convert_to_tsv('RX_AC_LIN_DATA.txt')
