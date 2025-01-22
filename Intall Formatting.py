#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:02:51 2025

@author: loganbrennan
"""

import pandas as pd
import numpy as np

# Define the start and step times !user input!
start_time = 0 #start time (minutes)
time_step = 5 #time between experiments (minutes)


# Initialize variables
data = {}
current_time_point = None

# Read and parse the file into a dictionary
with open('intall.txt', 'r') as file: #file must be in same folder as script and named intall.txt, if otherwise please use the filepath instead
    for line in file:
        line = line.strip()
        if line.startswith('/opt/NMR Data'):  # Header line
            current_time_point = line
            data[current_time_point] = []
        elif line:  # Data line
            parts = line.split()
            if current_time_point:
                # Add the integral value (last column) for the current time point
                data[current_time_point].append(float(parts[-1]))

# Reorganize data into a DataFrame
df = pd.DataFrame(data)

# Transpose and set the peak numbers as the index
df = df.T  # Transpose to have peaks as columns
df.columns = [f'Peak {i+1}' for i in range(df.shape[1])]
df.reset_index(drop=True, inplace=True)

# Create array of evenly spaces time points and add as a column to main df
num_experiments = df.shape[0]  # Number of rows (experiments)
time_points = np.arange(start_time, start_time + num_experiments * time_step, time_step)
df['Time (min)'] = time_points

df.to_csv('Formatted intall.csv', index=False)

print(df)