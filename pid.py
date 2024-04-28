import numpy as np
import matplotlib.pyplot as plt

# Параметры системы
kp = 0.001   # Пропорциональный коэффициент
ki = 0.0001   # Интегральный коэффициент
kd = 2.0   # Дифференциальный коэффициент

i = 0.0
d = 0.0
prev_err = 0.0

# настоящее значение
input = 0.0
# входной 'сигнал'
out = 0.0

# нужное значение
setpoint = 1000.0

# ваты
w = 0.0

setpoint_list = list()
for _ in range(7000):
    setpoint_list.append(setpoint)
plt.plot(setpoint_list)

real_data = list()
for _ in range(7000):
    input = out

    err = setpoint - input

    p = err * kp
    i = err * ki + i
    d = d + (err - prev_err) * kd

    pid = p + i + d

    out = input + pid / 60

    prev_err = err

    real_data.append(out)
plt.plot(real_data)



plt.show()
