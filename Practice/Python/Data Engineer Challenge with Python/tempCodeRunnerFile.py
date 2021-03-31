#[Web Scraping](https://academy.dqlab.id/main/projectcode/170/333/1597)
#import library yang dibutuhkan
import pandas as pd
import requests
from bs4 import BeautifulSoup

#buatlah request ke website
website_url = requests.get('https://id.wikipedia.org/wiki/Demografi_Indonesia').text
soup = BeautifulSoup(website_url, 'lxml')

#ambil table dengan class 'wikitable sortable'
my_table = soup.find('table', {'class':'wikitable sortable'})

#cari data dengan tag 'td'
links = my_table.findAll('td')

#buatlah lists kosong
kode_bps = []
nama = []
ibu_kota = []
populasi = []
luas_km = []
pulau = []

#memasukkan data ke dalam list berdasarkan pola HTML
for i, link in enumerate(links):
  if i in range(0, len(links), 9):
  	kode_bps.append(link.get_text())
  if i in range(2, len(links), 9):
  	nama.append(link.get_text())
  if i in range(4, len(links), 9):
  	ibu_kota.append(link.get_text())
  if i in range(5, len(links), 9):
  	populasi.append(link.get_text())
  if i in range(6, len(links), 9):
  	luas_km.append(link.get_text())
  if i in range(8, len(links), 9):
  	pulau.append(link.get_text()[:-1])
#buatlah DatFrame dan masukkan ke CSV
df = pd.DataFrame()
df['Kode BPS'] = kode_bps
df['Nama'] = nama
df['Ibu Kota'] = ibu_kota
df['Populasi'] = populasi
df['Luas km'] = luas_km
df['Pulau'] = pulau
df.to_csv('Indonesia_Demography_by_Province.csv', index=False, encoding='utf-8', quoting=1)

df.head()

#[Function and Regular Expression](https://academy.dqlab.id/main/projectcode/170/333/1598)
import numpy as np

def sigmoid(x):
    return 1/ (1 + np.exp(-x))

training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

training_outputs = np.array([[0,1,1,0]]).T

np.random.seed(1)

synaptic_weights= 2* np.random.random((3,1)) - 1

print('Random starting synaptic weights: ')
print(synaptic_weights)

for iteration in range(1):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

print('Outputs after training: ')
print(outputs)
