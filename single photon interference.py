import matplotlib.pyplot as plt
from numpy import linspace
import math

# slit positions
x = linspace(0, 7.8, num = 79)
# counts
y = [204, 262, 279, 383, 417, 436, 433, 545, 676, 807, 1018, 1699, 2251, 447, 2030, 1400, 2017, 4015, 6004, 6416, 4486, 2277, 2356, 6024, 9786, 10958, 7580, 2972, 2251, 6794, 12971, 14641, 10074, 3479, 1663, 6152, 13028, 15237, 10886, 3937, 1160, 4778, 10462, 12905, 9286, 3733, 974, 3263, 6825, 8544, 6521, 2975, 994, 1868, 3692, 4338, 3410, 1879, 1166, 1176, 1601, 1550, 1282, 994, 1025, 915, 684, 347, 273, 485, 680, 574, 370, 216, 186, 260, 354, 358, 282]
plt.scatter(x, y)

# manual fit according to Io sinc^2(alpha) cos^2(beta) numbers are arbitrarily chosen until it fit
x = linspace(0,7.8, 7900)
y = []
I = 16000
a = 0.14
b = 0.9
l =500 * 10 ** -3
c = 3.635
for i in x:
    y.append(I * (math.sin(math.pi * a * (i - c) / l) / math.pi / a / (i - c) * l) ** 2 * math.cos(math.pi * b * (i - c) / l) ** 2)
plt.plot(x, y)
plt.show()