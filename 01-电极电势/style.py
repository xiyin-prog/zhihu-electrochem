import matplotlib as mpl, matplotlib.font_manager as fm
mpl.rcParams.update({"font.family":["Liberation Serif","Noto Serif CJK SC","DejaVu Serif"],"mathtext.fontset":"stix",
 "axes.unicode_minus":False,"font.size":10.5,"axes.linewidth":0.8,"savefig.dpi":300,"svg.fonttype":"none"})
PAL=["#4C72B0","#DD8452","#55A868","#C44E52","#8172B3"]  # soft palette
def corner(fig): fig.text(0.99,0.005,"仿真，参数见图注",ha="right",va="bottom",fontsize=8,color="#777")
import os
def save(fig,name):
    d=os.path.join(os.path.dirname(os.path.abspath(__file__)),"figures"); os.makedirs(d,exist_ok=True)
    fig.savefig(os.path.join(d,name+".png"),dpi=300); fig.savefig(os.path.join(d,name+".svg"))

# ---- 中西混排：中文用普通文本，符号用 $...$ mathtext（stix）。mathtext 不能渲染中文，故拆成多个 Text 拼接 ----
from matplotlib.transforms import offset_copy
import matplotlib.pyplot as _plt
def mixtext(ax, x, y, parts, rotation=0, ha="center", va="center", transform=None, **kw):
    """parts: 字符串列表，依次拼接；含 $ 的片段走 mathtext。返回 Text 列表。"""
    fig = ax.figure; tr = transform or ax.transAxes
    ts = [ax.text(0, 0, p, transform=tr, rotation=rotation, va=va, ha="left", **kw) for p in parts]
    r = fig.canvas.get_renderer()
    ws = [(t.get_window_extent(r).height if rotation == 90 else t.get_window_extent(r).width) * 72 / fig.dpi for t in ts]
    tot = sum(ws); s = {"center": -tot / 2, "left": 0, "right": -tot}[ha]
    for t, w in zip(ts, ws):
        dx, dy = (0, s) if rotation == 90 else (s, 0)
        t.set_transform(offset_copy(tr, fig=fig, x=dx, y=dy, units="points")); t.set_position((x, y))
        if rotation == 90: t.set_va("bottom"); t.set_ha("center")
        s += w
    return ts
def mixylabel(ax, parts, x=-0.12, **kw): ax.set_ylabel(""); return mixtext(ax, x, 0.5, parts, rotation=90, **kw)
def mixxlabel(ax, parts, y=-0.13, **kw): ax.set_xlabel(""); return mixtext(ax, 0.5, y, parts, va="top", **kw)
