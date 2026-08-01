# Skrip Automasi Preprocessing Data
import pandas as pd
import numpy as np

def run_preprocessing():
    print("Memuat dataset mentah...")
    df = pd.read_csv('household_power_consumption.txt', sep=';', low_memory=False)

    print("Melakukan preprocessing...")
    df['Timestamp'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d/%m/%Y %H:%M:%S')
    df = df.drop(columns=['Date', 'Time'])
    df = df.sort_values('Timestamp').reset_index(drop=True)

    df.replace('?', np.nan, inplace=True)
    for col in df.columns:
        if col != 'Timestamp':
            df[col] = df[col].astype(float)
    df = df.ffill()

    # Menyimpan hasil preprocessing
    output_filename = 'household_power_consumption_preprocessing.csv'
    df.to_csv(output_filename, index=False)
    print(f"Preprocessing selesai! File disimpan sebagai {output_filename}")

if __name__ == "__main__":
    run_preprocessing()
