import matplotlib.pyplot as plt

# Data hasil analisis untuk ditampilkan ke pengguna
kategori = ['Kategori A', 'Kategori B', 'Kategori C']
nilai = [45, 88, 20]

# Fitur Visual Preattentive: Memberi warna menonjol pada nilai tertinggi
warna = ['lightgray', 'red', 'lightgray'] 

plt.figure(figsize=(6, 4))
plt.bar(kategori, nilai, color=warna)
plt.title("Dashboard Pengambilan Keputusan (HCI)", fontsize=12)
plt.xlabel("Kategori Aset")
plt.ylabel("Tingkat Risiko")
plt.savefig("dashboard_hci.png")

print("--- SESI 5: Dashboard HCI berhasil disimpan sebagai 'dashboard_hci.png' ---")