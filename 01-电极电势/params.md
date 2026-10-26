# 配图参数、假设与来源

运行方式：在本目录下 `python3 fig_apparatus.py / fig_edl.py / fig_bv_cross.py / fig_nernst.py / fig_activity.py / fig_mixing_entropy.py`（依赖 numpy、scipy、matplotlib、Pillow；共用样式在 `style.py`），输出到 `figures/`（PNG 300 dpi + SVG）。
所有图右下角注明“仿真，参数见图注”。标为 **示意** 的参数是为了作图选定的，不是文献测量值。

## 通用物理常数（CODATA 2018，SI 精确值或推荐值）
e = 1.602176634e-19 C，k_B = 1.380649e-23 J/K，N_A = 6.02214076e23 /mol，
ε0 = 8.8541878128e-12 F/m，R = 8.314462618 J/(mol·K)，F = 96485.33212 C/mol。
来源：Tiesinga et al., *Rev. Mod. Phys.* 93, 025010 (2021)（CODATA 2018）。
T = 298.15 K（25 °C）。

## 图1 双电层电势分布（fig_edl.py → figures/fig1_双电层电势分布）
- 模型：Gouy–Chapman–Stern。Stern 层内电势线性下降；扩散层采用 z:z 电解质 Gouy–Chapman 精确解
  φ(x) = (2kT/ze)·ln[(1+γe^{-(x-d)/λ_D})/(1-γe^{-(x-d)/λ_D})]，γ = tanh(zeφ_d/4kT)。
- φ_d 由界面电荷连续条件求得：ε_S ε0 (φ0−φ_d)/d = √(8 εr ε0 kT n0)·sinh(zeφ_d/2kT)。
- 电解质：CuSO4 当作理想的 2:2 对称电解质（z = 2），c = 0.001 / 0.01 / 0.1 mol/L；忽略离子缔合与活度系数（实际 CuSO4 有明显离子对缔合）。
- 水的相对介电常数 εr = 78.30（25 °C），出处：C. G. Malmberg, A. A. Maryott, “Dielectric Constant of Water from 0° to 100° C”, *J. Res. Natl. Bur. Stand.* 56(1), 1–8 (1956), RP2641, doi:10.6028/jres.056.001（表 2 拟合值 78.304）。
- **示意**：Stern 层厚度 d = 0.4 nm；Stern 层相对介电常数 ε_S = 10；总电势降 φ0 = 100 mV（三种浓度用同一值，便于比较）。
- 离子浓度：Boltzmann 分布 c_±(x) = c·exp(∓zeφ/kT)，只画扩散层。
- 图注说明：(a) 中竖直点线标出各浓度下 x = d + λ_D 的位置（Stern 层外缘再加一个德拜长度）；灰色带为 Stern 层。
- 计算结果：λ_D = 4.804 / 1.519 / 0.480 nm；φ_d = 47.7 / 28.5 / 12.8 mV。

## 图2 溶解/沉积速率交点（fig_bv_cross.py → figures/fig2_溶解沉积速率交点）
- 模型：Butler–Volmer 分电流，以 E° 为参考：
  溶解 i_a = k0·exp[(1−α)nFE/RT]（Cu 金属活度取 1，与溶液浓度无关）；
  沉积 i_c = k0·a(Cu²⁺)·exp[−αnFE/RT]。
- n = 2，α = 0.5（**示意**），k0 = 1（**示意**，任意单位）。动力学只用来说明平衡电势的位置，不代表 Cu 电极的真实电流大小。
- 活度 a = 0.001（稀）与 0.1（浓，×100），活度近似等于浓度（理想假设）。
- 数值求解交点：E_eq = −88.74 mV 与 −29.58 mV（相对 E°），偏移 59.159 mV；
  与 (RT/2F)ln100 = 59.159 mV 一致（差值 < 1e-9 mV）。

## 样式
中文 Noto Serif CJK SC，西文 Liberation Serif（Times New Roman 的度量兼容替代），数学 STIX；调色板见 style.py。

## 图0 装置示意（fig_apparatus.py → figures/fig0_装置示意）
- 底图：assets/apparatus_original.png（示意插图底图，**未包含在本仓库中**；`figures/` 中带标注的 PNG/SVG 为发布版本，没有底图时脚本会提示并跳过）。脚本按颜色阈值交换导线颜色：红线/红表笔/红端子 → 右侧（浓溶液）电极，黑线 → 左侧（稀溶液）电极；加中文标注。读数 59.2 mV 为理论值，不是实测值。右下角标“示意”。

## 图3 能斯特方程（fig_nernst.py → figures/fig3_能斯特方程）
- E = (RT/nF)·ln10·lg(a浓/a稀)，n = 1、2；T = 273.15、298.15、333.15 K。理想能斯特行为，忽略液接电势。
- 标记点：lg = 2、n = 2、25 °C → E = 59.16 mV（显示为 59.2 mV）。

## 图4 CuSO4 平均活度系数（fig_activity.py → figures/fig4_CuSO4活度系数）
- Debye–Hückel 极限律：lg γ± = −A|z₊z₋|√I，A = 0.509 kg^½·mol^−½（25 °C 水，常用值），z = 2，I = 4m。计算值：m = 0.001 → 0.743；0.01 → 0.392；0.1 → 0.052。
- 文献值（25 °C，质量摩尔浓度标度）：*CRC Handbook of Chemistry and Physics*, 97th ed. (2016), W. M. Haynes 主编, CRC Press, 第 5 节 “Activity Coefficients of Acids, Bases, and Salts”（P. Vanýsek），p. 5-98，CuSO4 行：
  m = 0.1…1.0 mol/kg：0.150, 0.104, 0.0829, 0.0704, 0.0620, 0.0559, 0.0512, 0.0475, 0.0446, 0.0423。
  获取方式：archive.org 上该版手册的全文 OCR 文本（并与 muni.cz 上 93rd ed. 同表摘录一致）。该表只给 0.1–1.0 mol/kg；同书 “Mean Activity Coefficients of Electrolytes as a Function of Concentration” 表中没有 CuSO4，因此低浓度段没有画文献点。
- 极限律只在极稀溶液（I ≲ 0.001–0.01）下成立；在 0.1 mol/kg 时已经比文献值低约 3 倍，图中两者不重叠，这是预期结果。

## 图5 附录：混合熵与 Stirling 近似（fig_mixing_entropy.py → figures/fig5_附录_混合熵）
- (a) 理想二元混合：Δ_mix S/R = −[x ln x + (1−x) ln(1−x)]，最大值 ln 2（x = 0.5）；斜率 d/dx = ln[(1−x)/x]，在 x→0、1 时发散（虚线为 x = 0.01、0.99 处的切线）。
- (b) ln C(N, N/2) 精确值（lgamma 计算）与 Stirling 一阶近似 N ln 2 的对比，N = 10…10⁶（偶数）；插图为相对误差：N = 10 → 25.4 %，100 → 3.8 %，1000 → 0.53 %，10⁴ → 0.07 %。

## 中西文混排
mathtext 不能渲染中文，所以含符号的中文坐标轴标签由 style.mixtext 拼接：中文用普通文本，符号用 $...$（STIX）。
