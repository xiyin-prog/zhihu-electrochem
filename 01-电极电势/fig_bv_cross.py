import numpy as np, matplotlib.pyplot as plt
from scipy.optimize import brentq
from style import PAL, corner, save, mixxlabel
R=8.314462618;F=96485.33212;T=298.15;n=2;al=0.5;k0=1.0  # k0 illustrative (arb. units), E vs E°
f=n*F/(R*T); E=np.linspace(-0.25,0.15,800)
ia=lambda E:k0*np.exp((1-al)*f*E)
ic=lambda E,a:k0*a*np.exp(-al*f*E)
fig,ax=plt.subplots(figsize=(6.4,4.6)); Eq=[]
for a,col,nm in [(0.001,PAL[0],"稀溶液"),(0.1,PAL[1],"浓溶液（×100）")]:
    ax.semilogy(E*1e3,ic(E,a),color=col,lw=1.8,label=f"还原分电流（沉积），{nm} a={a:g}")
    e=brentq(lambda x:ia(x)-ic(x,a),-1,1); Eq.append(e)
    ax.plot(e*1e3,ia(e),"o",color=col,ms=6,zorder=5)
    ax.axvline(e*1e3,color=col,ls=":",lw=1)
ax.semilogy(E*1e3,ia(E),color=PAL[2],lw=1.8,label="氧化分电流（溶解），与浓度无关")
s=(Eq[1]-Eq[0])*1e3; print("Eeq (mV vs E°):",[x*1e3 for x in Eq],"shift",s,"theory",R*T/(n*F)*np.log(100)*1e3)
y=ia(Eq[1])*30
ax.annotate("",xy=(Eq[1]*1e3,y),xytext=(Eq[0]*1e3,y),arrowprops=dict(arrowstyle="<->",lw=1))
ax.text(np.mean(Eq)*1e3,y*1.6,f"$\\Delta E$ = {s:.1f} mV",ha="center",fontsize=10)
ax.set_ylabel("分电流大小（任意单位，对数）")
ax.legend(frameon=False,fontsize=8.5,loc="upper center");ax.set_ylim(1e-5,1e3)
fig.tight_layout(rect=(0,0.05,1,1));mixxlabel(ax,["电极电势 ","$E-E^{\\ominus}$"," / mV"],y=-0.08);corner(fig);save(fig,"fig2_溶解沉积速率交点")
