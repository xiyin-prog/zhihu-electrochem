# CuSO4 平均活度系数 γ± 随质量摩尔浓度 m：Debye–Hückel 极限律 vs 文献值（25 °C）
import numpy as np, matplotlib.pyplot as plt
from style import PAL, corner, save, mixxlabel, mixylabel
A=0.509; z=2                     # 25 °C 水中 A（kg^1/2 mol^-1/2），2:2 电解质
m=np.logspace(-4,0,300); I=0.5*m*(z**2+z**2)   # 离子强度 I = 4m
g_dh=10**(-A*z*z*np.sqrt(I))
# 文献值：CRC Handbook 97th ed. (2016), "Activity Coefficients of Acids, Bases, and Salts" (P. Vanýsek), p. 5-98, CuSO4 行
m_exp=np.round(np.arange(0.1,1.01,0.1),1)
g_exp=np.array([0.150,0.104,0.0829,0.0704,0.0620,0.0559,0.0512,0.0475,0.0446,0.0423])
for mm,ge in zip(m_exp,g_exp): print(f"m={mm:.1f}: exp {ge:.4f}, DH {10**(-A*z*z*np.sqrt(4*mm)):.4f}")
for mm in [0.001,0.01]: print(f"DH m={mm}: {10**(-A*z*z*np.sqrt(4*mm)):.3f}")
fig,ax=plt.subplots(figsize=(6.4,4.6))
ax.loglog(m,g_dh,color=PAL[0],lw=1.8,label="Debye–Hückel 极限律")
ax.loglog(m_exp,g_exp,"o",color=PAL[1],ms=6,label="文献值（CRC Handbook，25 °C）")
ax.set_ylim(1e-3,1.2);ax.legend(frameon=False,fontsize=9,loc="lower left")
fig.tight_layout(rect=(0.03,0.05,1,1))
mixxlabel(ax,["质量摩尔浓度 ","$m$"," / (mol·kg⁻¹)"],y=-0.09)
mixylabel(ax,["平均活度系数 ","$\\gamma_\\pm$"],x=-0.1)
corner(fig);save(fig,"fig4_CuSO4活度系数")
