import geopandas as gpd
from shapely.geometry import Point

# Data lokasi aset infrastruktur (Koordinat Longitude, Latitude)
data_aset = {
    'nama_aset': ['Gedung A', 'Gedung B', 'Jembatan C'],
    'latitude': [-3.795, -3.790, -3.800],
    'longitude': [102.265, 102.270, 102.260]
}

# Membuat GeoDataFrame (Data Spasial)
geometry = [Point(xy) for xy in zip(data_aset['longitude'], data_aset['latitude'])]
gdf = gpd.GeoDataFrame(data_aset, geometry=geometry)

print("--- SESI 3: Pemetaan Aset GIS ---")
print(gdf[['nama_aset', 'geometry']])