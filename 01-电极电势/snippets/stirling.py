# 比较 ln C(N, N/2) 的精确值与 Stirling 近似 N ln 2
from math import lgamma, log
for N in [10, 100, 1000, 10**4]:
    exact = lgamma(N + 1) - 2 * lgamma(N / 2 + 1)   # 精确的 ln C(N, N/2)
    approx = N * log(2)                              # Stirling 一阶近似
    rel = (approx - exact) / exact                   # 相对误差
    print(f"N = {N:>5}: 精确 = {exact:10.3f}, 近似 = {approx:10.3f}, 相对误差 = {rel:.2%}")
