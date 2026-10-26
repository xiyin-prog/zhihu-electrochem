# 能斯特方程：浓差电池电动势 E = (RT/nF)·ln10·lg(a浓/a稀)，n=1,2；0/25/60 °C
import numpy as np, matplotlib.pyplot as plt
from style import PAL, corner, save, mixxlabel, mixylabel
R=8.314462618;F=96485.33212
x=np.linspace(0,3,200)
fig,ax=plt.subplots(figsize=(6.4,4.6))
for T_C,col in zip([0,25,60],PAL[:3]):
    T=T_C+273.15
    for n,ls in [(1,"-"),(2,"--")]:
        ax.plot(x,R*T/(n*F)*np.log(10)*x*1e3,color=col,ls=ls,lw=1.7,label=f"{T_C} °C,  $n$ = {n}")
E=R*298.15/(2*F)*np.log(100)*1e3; print(f"E(lg=2,n=2,25C) = {E:.2f} mV")
ax.plot(2,E,"o",color="k",ms=6,zorder=5)
ax.annotate(f"{E:.1f} mV",xy=(2,E),xytext=(2.2,E-25),fontsize=10,arrowprops=dict(arrowstyle="->",lw=0.8))
ax.text(2.2,E-29,"（25 °C，n = 2，活度比 100）",fontsize=8.5,va="top")
ax.set_xlim(0,3);ax.set_ylim(0,None);ax.legend(frameon=False,fontsize=9,ncol=2)
fig.tight_layout(rect=(0.03,0.05,1,1))
mixxlabel(ax,["活度比 ","$\\lg(a$","浓","$\\,/\\,a$","稀","$)$"],y=-0.09)
mixylabel(ax,["电动势 ","$E$"," / mV"],x=-0.1)
corner(fig);save(fig,"fig3_能斯特方程")
