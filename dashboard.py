import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Muat data
order_df = pd.read_csv("../Data/orders_dataset.csv")
customers_df = pd.read_csv("../Data/customers_dataset.csv")

# Konversi kolom tanggal yang sesuai
order_df['order_purchase_timestamp'] = pd.to_datetime(order_df['order_purchase_timestamp'])

# Gabungkan data order dan customer untuk analisis kota
merged_df = pd.merge(order_df, customers_df, on='customer_id')

# Hitung jumlah order per pelanggan
order_counts = order_df.groupby('customer_id').size()

# Rata-rata jumlah order per pelanggan
avg_orders = order_counts.mean()

# Hitung distribusi jumlah pelanggan per segmen order
segment_distribution = order_counts.value_counts()

# Hitung jumlah pelanggan per kota
city_counts = merged_df['customer_city'].value_counts()
top_5_cities = city_counts.head(5)

# Sidebar
st.sidebar.title('Menu Dashboard')
option = st.sidebar.selectbox(
    'Pilih Analisis:',
    ['Rata-rata Jumlah Order per Pelanggan', 'Distribusi Jumlah Pelanggan per Segmen Order', '5 Kota dengan Jumlah Pelanggan Terbanyak']
)

# Judul Dashboard
st.title('Dashboard Analisis Order Pelanggan')

# Menampilkan konten sesuai pilihan di sidebar
if option == 'Rata-rata Jumlah Order per Pelanggan':
    st.subheader('Rata-rata Jumlah Order per Pelanggan')
    st.write(f'Rata-rata jumlah order per pelanggan adalah {avg_orders:.2f} kali.')

    # Pie chart untuk distribusi rata-rata jumlah order
    if not segment_distribution.empty:
        fig, ax = plt.subplots()
        ax.pie(segment_distribution, labels=segment_distribution.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
        ax.set_title('Distribusi Jumlah Order per Segmen Pelanggan')
        st.pyplot(fig)
    else:
        st.write("Data tidak tersedia untuk distribusi segmen order.")

elif option == 'Distribusi Jumlah Pelanggan per Segmen Order':
    st.subheader('Distribusi Jumlah Pelanggan per Segmen Order')
    
    if not segment_distribution.empty:
        fig, ax = plt.subplots()
        ax.pie(segment_distribution, labels=segment_distribution.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
        ax.set_title('Distribusi Jumlah Pelanggan per Segmen Order')
        st.pyplot(fig)
    else:
        st.write("Data tidak tersedia untuk distribusi segmen order.")

elif option == '5 Kota dengan Jumlah Pelanggan Terbanyak':
    st.subheader('5 Kota dengan Jumlah Pelanggan Terbanyak')
    
    if not top_5_cities.empty:
        fig, ax = plt.subplots()
        top_5_cities.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
        ax.set_xlabel('Kota')
        ax.set_ylabel('Jumlah Pelanggan')
        ax.set_title('5 Kota dengan Jumlah Pelanggan Terbanyak')
        st.pyplot(fig)
    else:
        st.write("Data tidak tersedia untuk jumlah pelanggan per kota.")
