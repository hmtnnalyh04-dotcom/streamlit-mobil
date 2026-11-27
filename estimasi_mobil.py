import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('🚗 Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil', step=1, format='%d')
mileage = st.number_input('Input Km Mobil', step=100, format='%d')
tax = st.number_input('Input Pajak Mobil', step=5, format='%d')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size')


def format_id(nilai: float, desimal: int = 2) -> str:
  """Mengubah angka float menjadi format Indonesia: titik ribuan, koma desimal."""
  teks = f"{nilai:,.{desimal}f}"
  # Tukar sementara koma dan titik menggunakan placeholder agar tidak saling timpa
  return teks.replace(",", "X").replace(".", ",").replace("X", ".")


if st.button('Estimasi Harga'):
  prediksi = model.predict([[year, mileage, tax, mpg, engineSize]])
  price_pounds = float(prediksi[0])
  price_idr = price_pounds * 19000

  formatted_pounds = format_id(price_pounds, desimal=2)
  formatted_idr = format_id(price_idr, desimal=2)

  st.success(f"Estimasi harga mobil bekas dalam Ponds : £ {formatted_pounds}")
  st.success(f"Estimasi harga mobil bekas dalam IDR : Rp. {formatted_idr}")
