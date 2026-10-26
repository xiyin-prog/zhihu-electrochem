# 图0：装置示意。基于 assets/apparatus_original.png，交换导线颜色（红→右侧浓溶液电极，黑→左侧稀溶液电极）并加中文标注
import numpy as np, matplotlib.pyplot as plt, os
from PIL import Image
from style import save, mixtext
here=os.path.dirname(os.path.abspath(__file__))
_base=os.path.join(here,"assets/apparatus_original.png")
if not os.path.exists(_base):
    # 底图未随仓库发布；已发布版本见 figures/fig0_装置示意.png / .svg
    print("fig_apparatus.py: 底图 assets/apparatus_original.png 未包含在本仓库中，跳过。已发布的图0见 figures/fig0_装置示意.png/.svg")
    raise SystemExit(0)
a=np.array(Image.open(_base).convert("RGB")).astype(float)
H,W,_=a.shape; R,G,B=a[...,0],a[...,1],a[...,2]
yy,xx=np.mgrid[0:H,0:W]
# 原红色导线/表笔/端子（左侧）：红色相像素
red=(R>120)&(G<75)&(B<75)&(R-G>90)
# 原黑色导线/表笔/端子（右侧）：深色、低饱和，限定在右侧导线区域与右端子附近（避开表体 ~78 灰与外框）
dark=(a.max(-1)<62)&(a.max(-1)-a.min(-1)<20)
region=((xx>996)&(yy>140)&(yy<400)) | ((xx>=896)&(xx<=996)&(yy>=176)&(yy<=222)) | ((xx-923)**2+(yy-199)**2<26**2)
black=dark&region
out=a.copy()
lum=a.mean(-1,keepdims=True)
out[red]=(np.array([38,38,40])*(a[red].mean(-1,keepdims=True)/180).clip(0.4,1.4))
out[black]=(np.array([205,35,35])*(0.75+a[black].mean(-1,keepdims=True)/120)).clip(0,255)
fig=plt.figure(figsize=(W/300,H/300)); ax=fig.add_axes([0,0,1,1]); ax.imshow(out.astype(np.uint8)); ax.axis("off")
kw=dict(fontfamily=["Noto Serif CJK SC","DejaVu Serif"],ha="center",va="center")
ax.text(832,140,"59.2 mV",fontsize=13,fontfamily="Liberation Serif",ha="center",va="center",color="#1d2b1d")
T=ax.transData
mixtext(ax,415,880,["稀 CuSO","$_4$"],transform=T,fontsize=9)
mixtext(ax,1255,880,["浓 CuSO","$_4$","（活度 ×100）"],transform=T,fontsize=9)
ax.text(330,330,"阳极（−）\nCu",fontsize=8,ha="right",va="center",fontfamily="Noto Serif CJK SC")
ax.text(1385,330,"阴极（+）\nCu",fontsize=8,ha="left",va="center",fontfamily="Noto Serif CJK SC")
ax.text(836,395,"盐桥",fontsize=8.5,**kw)
ax.text(W-10,H-8,"示意",fontsize=6.5,color="#777",fontfamily="Noto Serif CJK SC",ha="right",va="bottom")
save(fig,"fig0_装置示意")
