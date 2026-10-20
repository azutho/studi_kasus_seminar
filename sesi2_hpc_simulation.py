import multiprocessing as mp
import time

# Fungsi simulasi komputasi berat (misal: analisis sensor cuaca lokal)
def hitung_beban_sensor(sensor_id):
    total = sum(i * i for i in range(1000000))
    return f"Sensor {sensor_id} selesai diproses."

if __name__ == '__main__':
    print("--- SESI 2: Simulasi Komputasi Paralel (HPC) ---")
    start_time = time.time()
    
    # Menjalankan komputasi di beberapa core CPU secara bersamaan
    with mp.Pool(processes=4) as pool:
        results = pool.map(hitung_beban_sensor, range(4))
        
    for res in results:
        print(res)
    print(f"Waktu Eksekusi: {time.time() - start_time:.4f} detik")