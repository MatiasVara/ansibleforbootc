# Copyright (C) 2024 Savoir-faire Linux, Inc
# SPDX-License-Identifier: Apache-2.0
#!/usr/bin/env python3

# remove panda warning
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt

def get_pcap_data(filename="data.csv"):
    data = pd.read_csv(filename)

    # remove the first line to remove the 0us value
    data = data[1:]

    # Mutiply the column Time by 1000000 to convert it to microseconds
    data['Time'] = data['Time'] * 1000000
    return data

def extract_values_array(df):

    a = {}
    a['max'] = df['Time'].max()
    a['min'] = df['Time'].min()
    a['avg'] = df['Time'].mean()
    a['std'] = df['Time'].std()
    a['occurrences_under_240'] = df['Time'][df['Time'] < 240].count()
    a['occurrences_under_200'] = df['Time'][df['Time'] < 200].count()
    a['occurrences_over_300'] = df['Time'][df['Time'] > 300].count()
    a['occurrences_over_280'] = df['Time'][df['Time'] > 280].count()
    return a


if __name__ == "__main__":
    df = get_pcap_data()

    a = extract_values_array(df)

    df = get_pcap_data()

    a = extract_values_array(df)
    for key in a:
        print(key, ': ', a[key])

    plt.plot(df['Time'])
    plt.show()
