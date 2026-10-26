# 附录：理想二元混合熵 ΔmixS/R 与 ln C(N,N/2) 的 Stirling 近似
import numpy as np, matplotlib.pyplot as plt
from math import lgamma, log
from style import PAL, corner, save, mixxlabel, mixylabel
fig,(a1,a2)=plt.subplots(1,2,figsize=(9,4))
x=np.linspace(1e-6,1-1e-6,2000)
a1.plot(x,-(x*np.log(x)+(1-x)*np.log(1-x)),color=PAL[0],lw=1.8)
a1.axhline(log(2),color="#999",ls=":",lw=1); a1.text(0.5,log(2)+0.02,"$\\ln 2$",ha="center",fontsize=9)
for x0 in [0.01,0.99]:   # 端点斜率 ln[(1-x)/x] → ±∞
    s=np.log((1-x0)/x0); y0=-(x0*np.log(x0)+(1-x0)*np.log(1-x0)); xx=np.array([x0-0.01,x0+0.05]) if x0<.5 else np.array([x0-0.05,x0+0.01])
    a1.plot(xx,y0+s*(xx-x0),color=PAL[3],lw=1.2,ls="--")
a1.text(0.1,0.08,"端点处斜率\n趋于无穷",fontsize=9,color=PAL[3])
a1.set_xlim(0,1);a1.set_ylim(0,0.8);a1.set_title("(a) 理想二元混合熵",loc="left",fontsize=10.5)
N=np.unique(np.logspace(1,6,60).astype(int)); N=N[N%2==0]
ex=np.array([lgamma(n+1)-2*lgamma(n/2+1) for n in N]); st=N*log(2)
a2.loglog(N,ex,color=PAL[0],lw=1.8,label="精确值")
a2.loglog(N,st,color=PAL[1],lw=1.5,ls="--",label="Stirling 近似（N ln 2）")
ax3=a2.inset_axes([0.55,0.12,0.4,0.33]); ax3.loglog(N,(st-ex)/ex,color=PAL[2],lw=1.4)
ax3.set_title("相对误差",fontsize=8); ax3.tick_params(labelsize=7)
a2.legend(frameon=False,fontsize=9,loc="upper left");a2.set_title("(b) 组合数的 Stirling 近似",loc="left",fontsize=10.5)
fig.tight_layout(rect=(0.02,0.07,1,1),w_pad=3)
mixxlabel(a1,["摩尔分数 ","$x$"],y=-0.11); mixylabel(a1,["$\\Delta_{\\mathrm{mix}}S/R$"],x=-0.13)
mixxlabel(a2,["粒子数 ","$N$"],y=-0.11); mixylabel(a2,["$\\ln C(N,N/2)$"],x=-0.13)
corner(fig);save(fig,"fig5_附录_混合熵")
