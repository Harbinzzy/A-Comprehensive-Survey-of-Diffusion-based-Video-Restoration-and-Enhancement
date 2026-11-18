# Figure sources and reuse

Figs. 1 and 4 contain published artwork and results. Fig. 6 is an original plot of published numerical results. Figs. 2, 3 and 5 are survey-authored vector diagrams. No restoration outputs were generated for these illustrations.

## Fig. 1: published spatial and temporal comparisons

**Panel (a):** Shangchen Zhou, Peiqing Yang, Jianyi Wang, Yihang Luo, and Chen Change Loy, *Upscale-A-Video: Temporal-Consistent Diffusion Model for Real-World Video Super-Resolution*, CVPR 2024, Fig. 4, upper REDS30 example. [Paper figure](https://arxiv.org/html/2312.06640v1#S4.F4), [archival PDF](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhou_Upscale-A-Video_Temporal-Consistent_Diffusion_Model_for_Real-World_Video_Super-Resolution_CVPR_2024_paper.pdf).

- The six `source_assets/upscale_reds30_wall_*.png` method/detail crops are original 114 × 114 embedded images from PDF page 7. They show Bicubic, StableSR, SD x4 Upscaler, RealBasicVSR, Upscale-A-Video and the reference for the same region.
- The context image preserves the original yellow ROI, cropped from `upscale_reds30_wall_labeled_group.png`. That group is a rendered page-7 crop at `(150,210,1630,438)` from an 1836 × 2376 rendering; the script takes `(7,8,334,193)` within the group.
- Changes: select the upper example, rearrange it at publication size, and replace the original labels with consistent typography. “Ours” becomes “Upscale-A-Video”; “GT” becomes “Reference”. The context frame is not labeled as a degraded input. No reconstruction detail is retouched or synthesized.

**Panel (b):** Claudio Rota, Marco Buzzelli, and Joost van de Weijer, *Enhancing Perceptual Quality in Video Super-Resolution through Temporally-Consistent Detail Synthesis using Diffusion Models*, ECCV 2024, Fig. 6, first example (REDS4 sequence 000). [Paper figure](https://arxiv.org/html/2311.15908v2#S5.F6), [original image](https://arxiv.org/html/2311.15908v2/images/main/TemporalProfiles/temporal_profile.jpg).

- Asset: `source_assets/stablevsr_S5_F6_0.jpg`, 1280 × 809.
- Changes: resized as a complete panel, with a new panel heading. The original scanline, time/position axes, profiles and labels are preserved. “Ours” in this source image means StableVSR, as stated in the manuscript caption.
- The two panels come from different published experiments. Only comparisons within each panel share a source setting.

Both source papers' cited arXiv versions are released under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), as linked on the [Upscale-A-Video](https://arxiv.org/abs/2312.06640v1) and [StableVSR](https://arxiv.org/abs/2311.15908v2) abstract pages. The underlying REDS examples are credited to Seungjun Nah and collaborators, *NTIRE 2019 Challenge on Video Deblurring and Super-Resolution: Dataset and Study*, CVPR Workshops 2019. The [official REDS dataset page](https://seungjunnah.github.io/Datasets/reds.html) also specifies CC BY 4.0. The software repositories' licenses are not used as permission for these paper figures.

## Fig. 4: original method architectures

**Panel (a):** Rota, Buzzelli, and van de Weijer, StableVSR, Fig. 2. [Paper figure](https://arxiv.org/html/2311.15908v2#S4.F2), [original asset](https://arxiv.org/html/2311.15908v2/images/main/network.png). File: `source_assets/stablevsr_S4_F2_0.png`, 2561 × 946.

**Panel (b):** Zhou, Yang, Wang, Luo, and Loy, Upscale-A-Video, Fig. 2. [Paper figure](https://arxiv.org/html/2312.06640v1#S3.F2), [official GitHub image](https://raw.githubusercontent.com/sczhou/Upscale-A-Video/master/assets/pipeline.png). File: `source_assets/upscale_pipeline_github.png`, 2962 × 1232.

These complete diagrams are reproduced under the papers' CC BY 4.0 licenses linked above. Changes: proportional resizing, two panel headings and a separator. Network blocks, arrows, illustrative frames, legends, and frozen/trainable annotations are unchanged. No author endorsement is implied.

## Fig. 6: reported metric correlations

Data: Benjamin Herb, Steve Göring, Alexander Raake, and Rakesh Rao Ramachandra Rao, *How Accurate are Video Quality Models for Diffusion-Based Video Super-Resolution?*, QoMEX 2026, [Table I](https://arxiv.org/html/2605.25940v1#S4.T1).

The plot uses all 30 published SRCC pairs from `research/metric_study_table1.csv`, retaining original table order. The source distinguishes Fisher-aggregated within-source correlations and pooled overall correlations. It reports no SRCC confidence intervals. Colors, marker shapes and paired-point layout are new; no source artwork is reproduced. Display names normalize PIEAPP/Dover/Cover to PieAPP/DOVER/COVER.

`research/metric_study_evidence.md` records extraction, PDF cross-checking and a separate audit against the released raw data. The latter identifies sign-handling ambiguity for Q-Align and a DOVER mismatch; the plot preserves the published Table I values and is labeled **Reported SRCC**. It is not presented as an independent replication.

## Rebuilding

Run `python scripts/make_figures.py` to rebuild all six figures or `python scripts/make_evidence_figures.py` for Figs. 1, 4 and 6. Dependencies are in `scripts/requirements-figures.txt`. Source assets are retained at their downloaded resolution; enlarging a crop cannot add visual evidence. SHA-256 hashes and source locators are recorded in `source_assets/manifest.json`.
