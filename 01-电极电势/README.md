# 01 电极电势：配图与代码

| 图 | 脚本 | 输出 |
|---|---|---|
| 图0 装置示意 | `fig_apparatus.py` | `figures/fig0_装置示意.png/.svg` |
| 图1 双电层电势分布 | `fig_edl.py` | `figures/fig1_双电层电势分布.png/.svg` |
| 图2 溶解/沉积速率交点 | `fig_bv_cross.py` | `figures/fig2_溶解沉积速率交点.png/.svg` |
| 图3 能斯特方程 | `fig_nernst.py` | `figures/fig3_能斯特方程.png/.svg` |
| 图4 CuSO4 活度系数 | `fig_activity.py` | `figures/fig4_CuSO4活度系数.png/.svg` |
| 图5 附录：混合熵 | `fig_mixing_entropy.py` | `figures/fig5_附录_混合熵.png/.svg` |

运行：在本目录下 `python fig_xxx.py`（依赖 numpy、scipy、matplotlib、Pillow；共用样式 `style.py`）。参数、假设与来源见 `params.md`；正文代码片段见 `snippets/`。

**关于图0**：图0 是示意图，其底图（`assets/apparatus_original.png`）未包含在本仓库中，`fig_apparatus.py` 在缺少底图时会提示并跳过。`figures/` 中带标注的 `fig0_装置示意.png` / `.svg` 为发布版本。

许可：代码 MIT，图片 CC BY 4.0（见仓库根目录 README 与 LICENSE）。
