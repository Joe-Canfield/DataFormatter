# Spaces to tsv converter
# This script takes a file arbitrarily formatted with spaces
# and converts to a new file with Tab Separated Values (TSV)
# This makes importing to Excel convenient
# Joe Canfield, Last Updated 3 Jan, 2023

import re
import numpy as np
import matplotlib.pyplot as plt
import math

NumParams = 9
fileName = 'Noise_Test_Data'
txtExt = '.txt'
csvExt = '.csv'

gain_value = np.empty(shape=(NumParams, 1))
gain_value[0] = 80000000    # 5m, 16
gain_value[1] = 80000000    # 5m, 16
gain_value[2] = 32000000    # 1m, 32
gain_value[3] = 2000000     # 1m, 2
gain_value[4] = 80000000    # 5m, 16
gain_value[5] = 20000000    # 5m, 4
gain_value[6] = 20000000    # 2.5m, 8
gain_value[7] = 80000000    # 5m, 16
gain_value[8] = 80000000    # 5m, 16

def convert_to_csv(file):   # Converts .txt file with CRLF separation to CSV

    with open(file) as f:
        with open(fileName + '.csv', 'w') as newfile:
            for line in f:
                content = re.sub("[\r\n]", ",", line)   # Replace CRLF with commas
                newfile.write(content)


convert_to_csv(fileName + txtExt)

name = ["0v15_5M_16_60Khz_WMDM_1k", "0v15_5M_16_60Khz_WMDM", "0v15_1M_32_60Khz_WMDM_1k", "0v15_1M_2_60Khz_WMDM", "0v15_5M_16_100Khz_WMDM", "0v15_5M_4_60Khz_WMDM", "0v15_2M5_8_60Khz_WMDM", "0v15_5M_16_60Khz_WMDM", "0v15_5M_16_100Khz_DSC24Khz"]

with open(fileName + csvExt, 'r') as csvfile:
    data = np.genfromtxt(csvfile, dtype=int, delimiter=",")
    temp_array = np.empty(shape=(NumParams, math.floor(len(data)/NumParams)))
    for i in range(math.floor(len(data)/NumParams)):
        for j in range(NumParams):
            temp_array[j, i] = data[i*NumParams+j]
    np.savetxt("outputfile.csv", temp_array, delimiter=",")

    for i in range(NumParams):
        plt.figure(num=i+1)
        plt.plot(temp_array[i] * ((2 ^ -23) * 2.3 * math.pi) / gain_value[i])
        plt.ylabel('pA')
        plt.xlabel('sample')
        plt.title(name[i])
        plt.grid(visible=True)

    plt.show()
