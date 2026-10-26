import numpy as np, matplotlib.pyplot as plt
from scipy.optimize import brentq
from style import PAL, corner, save, mixylabel, mixxlabel
e=1.602176634e-19;kB=1.380649e-23;NA=6.02214076e23;eps0=8.8541878128e-12
T=298.15;er=78.30;z=2;d=0.4e-9;er_s=10.0;phi0=0.10  # Stern thickness, Stern εr, total drop (illustrative)
kT=kB*T; cs=[0.001,0.01,0.1]
fig,(a1,a2)=plt.subplots(2,1,figsize=(6.4,7),sharex=True)
for c,col in zip(cs,PAL):
    n0=c*1000*NA; lam=np.sqrt(er*eps0*kT/(2*n0*z**2*e**2))
    sig_d=lambda p:np.sqrt(8*er*eps0*kT*n0)*np.sinh(z*e*p/(2*kT))
    pd=brentq(lambda p:er_s*eps0*(phi0-p)/d-sig_d(p),0,phi0)
    x=np.linspace(0,12e-9,1500); g=np.tanh(z*e*pd/(4*kT))
    ed=g*np.exp(-(x-d)/lam)
    phi=np.where(x<d,phi0-(phi0-pd)*x/d,2*kT/(z*e)*np.log((1+ed)/(1-ed)))
    print(f"c={c}: Debye={lam*1e9:.3f} nm, phi_d={pd*1e3:.1f} mV")
    lab=f"{c:g} mol/L,  $\\lambda_D$ = {lam*1e9:.2f} nm"
    a1.plot(x*1e9,phi*1e3,color=col,lw=1.8,label=lab)
    a1.axvline((d+lam)*1e9,color=col,ls=":",lw=1)
    m=x>=d; xx=x[m]*1e9; f=np.exp(z*e*phi[m]/kT)
    a2.semilogy(xx,c/f,color=col,lw=1.8); a2.semilogy(xx,c*f,color=col,lw=1.4,ls="--")
for a in (a1,a2): a.axvspan(0,d*1e9,color="#ddd",alpha=.6,lw=0)
a1.text(d*1e9+0.1,103,"← Stern 层",ha="left",va="top",fontsize=9)
mixylabel(a1,["电势 ","$\\varphi$"," / mV（相对溶液本体）"]);a1.legend(frameon=False,fontsize=9)
a1.set_title("(a) 双电层电势分布",fontsize=10.5,loc="left")
a2.set_ylabel("离子浓度 / (mol·L⁻¹)");
a2.plot([],[],"k-",label="Cu²⁺（实线）");a2.plot([],[],"k--",label="SO₄²⁻（虚线）")
a2.legend(frameon=False,fontsize=9,loc="lower right",bbox_to_anchor=(1,0.08))
a2.set_title("(b) 扩散层离子浓度（Boltzmann 分布）",fontsize=10.5,loc="left");a2.set_xlim(0,12)
fig.tight_layout(rect=(0.03,0.04,1,1));mixxlabel(a2,["距电极表面距离 ","$x$"," / nm"],y=-0.11);corner(fig);save(fig,"fig1_双电层电势分布")
