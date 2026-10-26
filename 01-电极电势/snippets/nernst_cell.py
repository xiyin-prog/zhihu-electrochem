# Cu|CuSO4 浓差电池的电动势：E = (RT/nF) ln(a_浓 / a_稀)
from math import log
R, F = 8.314462618, 96485.33212      # 气体常数 J/(mol·K)、法拉第常数 C/mol
T, n, ratio = 298.15, 2, 100         # 25 °C、Cu2+ 两电子、活度比 100
E = R * T / (n * F) * log(ratio)
print(f"E = {E*1e3:.1f} mV")
