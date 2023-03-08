# Spaces to tsv converter
# This script takes a file arbitrarily formatted with spaces
# and converts to a new file with Tab Separated Values (TSV)
# This makes importing to Excel convenient
# Joe Canfield, Last Updated 3 Jan, 2023

import re
import numpy as np
import pandas as pd
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

numSamples = np.empty(shape=(NumParams, 1))
numSamples[0] = 4000
numSamples[1] = 600
numSamples[2] = 4000
numSamples[3] = 600
numSamples[4] = 600
numSamples[5] = 600
numSamples[6] = 600
numSamples[7] = 600
numSamples[8] = 600

totalSamples = sum(numSamples)

def convert_to_csv(file):   # Converts .txt file with CRLF separation to CSV

    with open(file) as f:
        with open(fileName + '.csv', 'w') as newfile:
            for line in f:
                content = re.sub("[\r\n]", ",", line)   # Replace CRLF with commas
                newfile.write(content)


convert_to_csv(fileName + txtExt)

testname = ["0v15_5M_16_60Khz_WMDM_1k", "0v15_5M_16_60Khz_WMDM", "0v15_1M_32_60Khz_WMDM_1k", "0v15_1M_2_60Khz_WMDM",
        "0v15_5M_16_100Khz_WMDM", "0v15_5M_4_60Khz_WMDM", "0v15_2M5_8_60Khz_WMDM", "0v15_5M_16_60Khz_WMDM_reverse",
        "0v15_5M_16_100Khz_DSC24Khz"]

samplename = ["MainData_5k", "MainData_30k", "RefData", "RefDataQ", "ADC0", "ADC1"]

with open(fileName + csvExt, 'r') as csvfile:
    data = np.genfromtxt(csvfile, dtype=int, delimiter=",")                     # Get raw data from csv
    for i in range(NumParams):
        # For 1000 scan tests
        if numSamples[i] == 4000:
            temp = data[(i*2300):(4000+(i*2300))]
            temp2 = np.empty(shape=(1000, 4))
            for j in range(999):
                temp2[j, 0] = temp[j*4]
                temp2[j, 1] = temp[(j*4)+1]
                temp2[j, 2] = temp[(j*4)+2]
                temp2[j, 3] = temp[(j*4)+3]
            df = pd.DataFrame(temp2, columns=samplename[0:4])
        # For 1st 100 scan test
        elif i == 1:
            temp = data[4000:4600]
            temp2 = np.empty(shape=(600, 4))
            for j in range(99):
                temp2[j, 0] = temp[j*6]
                temp2[j, 1] = temp[(j*6)+1]
                temp2[j, 2] = temp[(j*6)+2]
                temp2[j, 3] = temp[(j*6)+3]
            df = pd.DataFrame(temp2, columns=samplename[0:4])
        # For all other 100 scan tests
        else:
            temp = data[(6800+(i*600)):(7400+(i*600))]
            temp2 = np.empty(shape=(600, 4))
            for j in range(99):
                temp2[j, 0] = temp[j*6]
                temp2[j, 1] = temp[(j*6)+1]
                temp2[j, 2] = temp[(j*6)+2]
                temp2[j, 3] = temp[(j*6)+3]
            df = pd.DataFrame(temp2, columns=samplename[0:4])
        df.to_csv(path_or_buf=testname[i]+'.csv')

    #
    # for i in range(NumParams):
    #     plt.figure(num=i+1)
    #     plt.plot(temp_array[i] * ((2 ^ -23) * 2.3 * math.pi) / gain_value[i])
    #     plt.ylabel('pA')
    #     plt.xlabel('sample')
    #     plt.title(testname[i])
    #     plt.grid(visible=True)
    #
    # plt.show()
