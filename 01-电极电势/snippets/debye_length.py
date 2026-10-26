# 计算 CuSO4（2:2 电解质）在 25 °C 水中的德拜长度
import numpy as np
e, kB, NA, eps0 = 1.602176634e-19, 1.380649e-23, 6.02214076e23, 8.8541878128e-12
T, er, z = 298.15, 78.30, 2           # 温度 K、水的相对介电常数、离子价数
for c in [0.001, 0.01, 0.1]:          # 浓度 mol/L
    n0 = c * 1000 * NA                # 每种离子的数密度 /m^3
    lam = np.sqrt(er * eps0 * kB * T / (2 * n0 * z**2 * e**2))  # 对称 z:z 电解质
    print(f"c = {c:<6} mol/L  ->  λ_D = {lam*1e9:.3f} nm")
