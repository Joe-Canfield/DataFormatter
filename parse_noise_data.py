# Spaces to tsv converter
# This script takes a file arbitrarily formatted with spaces
# and converts to a new file with Tab Separated Values (TSV)
# This makes importing to Excel convenient
# Joe Canfield, Last Updated 3 Jan, 2023

import re
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import math

PLOT = False

NumParams = 9
numfiles = 0        # Initialize to 0

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

testname = ["0v15_5M_16_60Khz_WMDM_1k", "0v15_5M_16_60Khz_WMDM", "0v15_1M_32_60Khz_WMDM_1k", "0v15_1M_2_60Khz_WMDM",
        "0v15_5M_16_100Khz_WMDM", "0v15_5M_4_60Khz_WMDM", "0v15_2M5_8_60Khz_WMDM", "0v15_5M_16_60Khz_WMDM_reverse",
        "0v15_5M_16_100Khz_DSC24Khz"]

samplename = ["MainData_5k", "MainData_30k", "RefData", "RefDataQ", "ADC0", "ADC1"]

csvPath = '../CSV/'

### Program start

os.chdir("./TXT")

for filename in os.listdir(os.getcwd()):
    if "Wafer_ID_PS9097-02A1" in filename:  # Only use files from this Wafer ID
        numfiles += 1

        with open(filename) as f:
            csvname = os.path.splitext(filename)[0] + '.csv'
            with open(csvPath + csvname, 'w') as newfile:
                for line in f:
                    content = re.sub("[\r\n]", ",", line)   # Replace CRLF with commas
                    newfile.write(content)

        with open(csvPath + csvname, 'r') as csvfile:
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
                df.to_csv(path_or_buf=csvPath + testname[i]+'_'+csvname)

if numfiles == 0:
    print("No Files found matching contents")