import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_unh = pd.read_csv('UNH Historical Data.csv', usecols=['Date', 'Price'], thousands=',', parse_dates=['Date'])
data_csgs = pd.read_csv('CSGS Historical Data.csv', usecols=['Date', 'Price'], thousands=',', parse_dates=['Date'])

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(data_unh['Date'], data_unh['Price'], label='UNH')
plt.title('Ціна акцій UNH')
plt.xlabel('Дата')
plt.ylabel('Ціна')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(data_csgs['Date'], data_csgs['Price'], label='CSGS')
plt.title('Ціна акцій CSGS')
plt.xlabel('Дата')
plt.ylabel('Ціна')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
