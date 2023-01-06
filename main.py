# Spaces to tsv converter
# This script takes a file arbitrarily formatted with spaces
# and converts to a new file with Tab Separated Values (TSV)
# This makes importing to Excel convenient
# Joe Canfield, Last Updated 3 Jan, 2023

import tkinter as tk
import re


def convert_to_tsv(filepath):

    with open(filepath) as f:
        with open('RX_AC_LIN_DATA.csv', 'w') as tsv:
            for line in f:
                content = re.sub(" {2,}", "\t", line)   # Replace 2 or more spaces with tabs
                content = re.sub(" ", "", content)   # Remove single spaces
                tsv.write(content)
        tsv.close()
    f.close()


window = tk.Tk()
greeting = tk.Label(text="Hello!")
greeting.pack()


window.mainloop()


convert_to_tsv('RX_AC_LIN_DATA.txt')
