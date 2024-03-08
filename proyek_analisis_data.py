import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
import streamlit as st

# Membaca data
df_day = pd.read_csv('day.csv')
df_hour = pd.read_csv('hour.csv')

#Overview Data 
st.write("Data Day")
st.write(df_day.describe())
st.write("Data Hour")
st.write(df_hour.describe())

# Merubah tipe data kolom dteday menjadi tipe data datetime
df_day['dteday'] = pd.to_datetime(df_day['dteday'])
df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])

warnings.filterwarnings("ignore")

# df_day
correlation_matrix = df_day.corr()
fig = px.imshow(correlation_matrix)
fig.update_layout(title="Korelasi antara Variabel Numerik")
st.plotly_chart(fig)

# categorical_cols = ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']
# for col in categorical_cols:
#     fig = px.bar(df_day[col].value_counts().reset_index().rename(columns={'index': 'value'}), x='value', y=0)
#     fig.update_layout(title=f'Distribusi {col}')
#     st.plotly_chart(fig)

fig = px.box(df_day, x='season', y='cnt')
fig.update_layout(title='Hubungan antara Musim dan Jumlah Sewa')
st.plotly_chart(fig)

fig = px.box(df_day, x='holiday', y='cnt')
fig.update_layout(title='Hubungan antara Hari Libur dan Jumlah Sewa')
st.plotly_chart(fig)

fig = px.box(df_day, x='weathersit', y='cnt')
fig.update_layout(title='Hubungan antara Cuaca dan Jumlah Sewa')
st.plotly_chart(fig)

fig = px.scatter(df_day, x='temp', y='cnt', title='Scatter Plot antara Suhu dan Jumlah Sewa')
st.plotly_chart(fig)

# Filter musim panas (season 2)
filtered_data = df_day[df_day["season"] == 2]

# Buat plot dengan Plotly untuk menganalisis pengaruh cuaca terhadap jumlah sewa sepeda
fig = px.bar(filtered_data, x="weathersit", y="cnt", title="Pengaruh Cuaca terhadap Jumlah Sewa Sepeda (Musim Panas)")
fig.update_xaxes(title="Cuaca (weathersit)")
fig.update_yaxes(title="Jumlah Sewa Sepeda (cnt)")

# Tampilkan plot
st.plotly_chart(fig)

# Filter tahun 2011 dan musim dingin (season 4)
filtered_data = df_day[(df_day["yr"] == 0) & (df_day["season"] == 4)]

# Hitung jumlah total sepeda sewaan
total_sepeda_sewaan = filtered_data["cnt"].sum()

st.write("Jumlah total sepeda sewaan yang digunakan pada tahun 2011 selama musim dingin", total_sepeda_sewaan)

"""## Conclusion

- Penyewa sepeda saat musim panas mayoritas menyewa sepeda saat cuaca cerah
- Total sepeda yang disewakan saat musim dingin tahun 2011 mencapai 326.137 penyewa sepeda
"""
