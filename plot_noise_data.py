# plot_noise_data.py
# Joe Canfield, 10 March 2023
# This script plots data in the local directory ./CSV folder. This data is created by parse_noise_data.py

import os
import csv
import numpy as np
import matplotlib.pyplot as plt

WaferID = 'Wafer_ID_PS9097-02A1'
TestConfig = ['0v15_5M_16_60Khz_WMDM_1k', '0v15_1M_32_60Khz_WMDM_1k']

os.chdir('./CSV')

# Find each file in CSV directory
for filename in os.listdir(os.getcwd()):
    # Find files matching specified Wafer ID
    if WaferID in filename:
        # Find files matching specified test names
        for i in range(len(TestConfig)):
            if TestConfig[i] in filename:
                plt.figure(i)
                # Open file
                with open(filename) as f:
                    reader = csv.reader(f, delimiter=',')
                    headers = next(reader)
                    data = np.genfromtxt(f, delimiter=',', dtype=int)
                    plt.plot(data[1:, 1])
    else:
        print("No files found")

plt.show()
