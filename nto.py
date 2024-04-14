import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Загрузка данных
x, y = np.loadtxt('C1_00000.txt', delimiter=',', unpack=True, skiprows=5)

# Определение частоты колебаний зеркала
peaks, _ = find_peaks(-y, height=-1, distance=30, prominence=0.001, width=100)
T = (x[peaks[-1]] - x[peaks[0]]) / (len(peaks) - 1)
frequency = 1 / T

# Определение амплитуды колебаний зеркала
x_period = x[peaks[0]:peaks[1]]
y_period = y[peaks[0]:peaks[1]]
wavelength = 532
peaks_a, _ = find_peaks(y_period, height=-1, distance=30, prominence=0.001, width=10)
stripes = peaks_a[1:len(peaks_a) // 2 - 1]
amplitude = (len(stripes) - 1) * wavelength

# Определение средней скорости движения зеркала
speed = 4 * amplitude / (1000 * T)

# Расчет погрешностей
oscilloscope_error = 0.02
wavelength_error = 0.001

# T_error = T * oscilloscope_error
frequency_error = frequency * oscilloscope_error
amplitude_error = amplitude * wavelength_error
speed_error = speed * (oscilloscope_error + 2 * wavelength_error)  # Сумма погрешностей для скорости

# Вывод результатов с округлением

print(f'Частота колебаний: {frequency:.1f} ± {frequency_error:.1f# print(f'Период колебаний: {T*1000:.1f} ± {T_error*1000:.1f} мкс')} Гц')
print(f'Амплитуда колебаний зеркала: {amplitude:.1f} ± {amplitude_error:.1f} нм')
print(f'Средняя скорость зеркала за период: {speed:.0f} ± {speed_error:.0f} мкм/c')

