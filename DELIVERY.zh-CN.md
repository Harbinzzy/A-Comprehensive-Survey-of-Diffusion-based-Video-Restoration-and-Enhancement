# 修订交付说明

题目：**A Comprehensive Survey of Diffusion-based Video Restoration and Enhancement**

## 本次修改

- 核对新增 Excel 的全部 81 条记录：原稿已有 47 篇，补入 34 篇；每条均能对应正文引用。
- 全文现有 117 条参考文献、6 幅图片和 8 张比较表，编译为 25 页 PDF。
- Fig.1 替换为 Upscale-A-Video 的同场景重建对比及 StableVSR 的真实时空切片；Fig.4 替换为两篇原论文的具体网络架构。图片来源、CC BY 4.0 许可和改动见 `figures/ATTRIBUTION.md`。
- Fig.6 改为指定质量评价论文中全部 30 个指标的实际 SRCC 配对图，区分同源场景内和跨场景相关性；删除原有五行重复小表。
- 整理为七章：引言、背景与分类、方法论、任务与应用、数据集与评价、挑战与未来方向、结论。
- 依据两篇指定综述调整分类层级、方法分析顺序和图形表达，重写摘要、引言、学习体系、评价及展望。
- 删除正文中的 Scope, Retrieval, and Evidence Boundaries、Limitations of This Survey、Data, Code, and Manuscript Preparation 等过程说明。
- 恢复原模板的 Journal of LaTeX Class Files 页眉。
- 补充 HDR 视频、任意倍率及空时超分、压缩增强、胶片恢复、内部学习、零样本组合和加速方法。

## 文献补充中的关键修正

- PS-SR 的默认配置为大模型 1 次加 draft 模型 3 次评估。
- FFF-VDI 需要微调；Warped Diffusion 无需视频训练，但需要图像任务训练。
- TC-VR 的 4 步为内部生成链，另有逐视频外层优化。
- ZVRV 和 ZVRD 是不同工作；ID-Blau 是 DADeblur 使用的模糊生成组件。
- DiffHDR 属于直接的 LDR-to-HDR 视频重建；扩散生成式 codec 与压缩视频后处理分别介绍。
- 新版 DiffCVE 的单步模型来自固定时间步训练，未直接归为教师蒸馏。

## 文件与核验

阅读 `paper.pdf`；编辑 `paper.tex`、`sections/`、`scripts/make_figures.py` 和 `scripts/make_evidence_figures.py`。`research/spreadsheet_coverage.csv` 提供 Excel 逐行对应，`research/method_matrix.csv` 提供 93 条方法记录；Fig.6 的原表数值和交叉核查分别位于 `research/metric_study_table1.csv` 和 `research/metric_study_evidence.md`。图中严格保留原论文 Table I 的刊载值，没有声称独立复现实验。

参考文献采用已核实的一手 BibTeX 或出版元数据，正式出版与预印本分别标记。正文没有新模型实验或虚构对比得分，公平评测部分保留为方法讨论和建议。
