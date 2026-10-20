import torch
import torch.nn as nn

# Simulasi arsitektur CNN sederhana untuk klasifikasi citra satelit
class SatelliteCNN(nn.Module):
    def __init__(self):
        super(SatelliteCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3) # Input 3 channel (RGB citra)
        self.fc = nn.Linear(16 * 62 * 62, 2) # Output 2 kelas (Deforestasi / Normal)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = x.view(x.size(0), -1)
        return self.fc(x)

model = SatelliteCNN()
print("--- SESI 6: Model AI Citra Satelit Berhasil Diinisialisasi ---")
print(model)