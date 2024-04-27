import numpy as np
import matplotlib.pyplot as plt

k = 0.03
prev = 0

def my_filter(val):
    return prev + (val - prev) * k

# Задание частот дискретизации и диапазона частот
fs = 5000  # Частота дискретизации
frequencies = np.arange(1, 1000, 1)  # Диапазон частот

# Функция для вычисления частотной характеристики
def calculate_frequency_response(frequencies, fs, k):
    frequency_response = []
    for f in frequencies:
        t = np.arange(0, 1, 1/fs)
        x = np.sin(2 * np.pi * f * t)  # Входной сигнал
        y = np.zeros(len(t))  # Выходной сигнал

        # Применение фильтра к входному сигналу
        for i in range(len(t)):
            y[i] = my_filter(x[i])

        # Вычисление амплитуды выходного сигнала после применения фильтра
        amplitude = np.abs(np.fft.fft(y))
        frequency_response.append(amplitude[int(len(amplitude)/2)])  # Берем только половину сигнала (симметричный)

    return frequency_response

# Получение частотной характеристики
frequency_response = calculate_frequency_response(frequencies, fs, k)

# Построение графика частотной характеристики
plt.plot(frequencies, frequency_response)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Response')
plt.show()
