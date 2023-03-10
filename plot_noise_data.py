# plot_noise_data.py
# Joe Canfield, 10 March 2023
# This script plots data in the local directory ./CSV folder. This data is created by parse_noise_data.py

import math
import os
import csv
import numpy as np
import matplotlib.pyplot as plt

WaferID = 'Wafer_ID_PS9097-02A1'
TestConfig = ['0v15_5M_16_60Khz_WMDM_1k', '0v15_1M_32_60Khz_WMDM_1k']
gain = [80000000, 32000000]     # Gain values for 5M_16 and 1M_32 tests respectively

os.chdir('./CSV')       # Change directory to folder containing CSV files

for filename in os.listdir(os.getcwd()):    # Find each file in CSV directory
    if WaferID in filename:                 # Find files matching specified Wafer ID

        for i in range(len(TestConfig)):    # Find files matching specified test names
            if TestConfig[i] in filename:
                with open(filename) as f:
                    reader = csv.reader(f, delimiter=',')
                    headers = next(reader)
                    data = np.genfromtxt(f, delimiter=',', dtype=int)
                    scaled_data = data * (math.pow(2, -23) * 2.3 * math.pi) / gain[i]

                    for j in range(len(headers)-1):
                        plt.figure(i*4+j)
                        plt.plot(scaled_data)
                        plt.xlabel("Sample #")
                        plt.ylabel("A")
                        plt.suptitle(TestConfig[i])
                        plt.title(headers[j+1])
    else:
        print("No files found")

plt.show()
