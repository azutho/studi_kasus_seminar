import pandas as pd

# Data mentah transaksi bisnis
raw_data = {
    'transaksi_id': [101, 102, 103, 103, 104, 105],
    'pendapatan': [5000, 7000, None, 6000, 8000, None],
    'piutang': [1000, 2000, 1500, 1500, None, 3000]
}

df = pd.DataFrame(raw_data)

# 1. Hapus duplikat
df = df.drop_duplicates()

# 2. Isi nilai NaN dengan menampungnya kembali ke kolom
df['pendapatan'] = df['pendapatan'].fillna(df['pendapatan'].median())
df['piutang'] = df['piutang'].fillna(0)

# 3. Hitung total bersih
df['total_bersih'] = df['pendapatan'] - df['piutang']

print("--- SESI 1: Data Transaksi Bersih ---")
print(df)