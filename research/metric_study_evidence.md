# Fig. 6 metric evidence and plotting notes

核证日期：2026-11-17。仅核对来源与提取数据；没有改主稿，没有运行新的恢复实验，没有估造置信区间。

## Quick integration note

- Plot `metric_study_table1.csv` exactly as Table I reports it: 30 metrics, 15 FR + 15 NR, two SRCC columns. No correlation CI is reported; leave out error bars.
- Label the graphic **Reported SRCC**, distinguishing Fisher-aggregated within-sequence values from pooled overall values.
- The source does not specify its sign handling. For Q-Align, the released data give a signed within-sequence Fisher mean of −0.121, whereas Table I prints +0.121. Preserve the published value; do not claim a signed reanalysis.
- Excluding six original source videos leaves 216 outputs and reproduces 29/30 published SRCC pairs in magnitude. DOVER remains discrepant (paper: 0.549/0.370; current data: 0.571/0.383). Preserve the paper values and record the limitation.
- This is a new visualization of published results, not a new restoration experiment. The local original crop comparison has no verified general reprint permission.

## 1. Sources and exact data product

- Benjamin Herb, Steve Göring, Alexander Raake, Rakesh Rao Ramachandra Rao. *How Accurate are Video Quality Models for Diffusion-Based Video Super-Resolution?* QoMEX 2026; arXiv:2605.25940v1, 25 May 2026.
- Original PDF: https://arxiv.org/pdf/2605.25940
- HTML/Table I: https://arxiv.org/html/2605.25940v1#S4.T1
- Local PDF: `work/research/vsr/metric.pdf`; Table I is on PDF page 5.
- Local complete HTML: `work/research/vsr/metric.html.html`.
- PDF SHA-256: `ae6b982deabdf3928fe3d3d35f1f4790a99da563cdebd9a59f0e3c7df0ba1ca3`.
- Visual verification of the entire original Table I: `work/figure_revision/metric-page-5.png`.
- Authors' dataset: https://github.com/Telecommunication-Telemedia-Assessment/AVT-VQDB-UHD-1-VSR
- Local clone: `work/figure_revision/metric_source`; inspected commit `d81eea1f0ef899390e9541b294e5973fb281e92c`.

**Plot-ready file: `research/metric_study_table1.csv`.** It contains all 30 Table I metric rows in the original order (15 FR, 15 NR), with all six published PLCC/SRCC/RMSE columns. Three-decimal values were extracted from the original HTML and visually checked against the PDF table. An additional independent PDF-text comparison confirms all 180 numeric cells exactly match the CSV. No original results have been corrected or replaced with recomputed values. Names retain the original table spelling, e.g. PIEAPP, Dover, Cover, LPIPS (Alex). Display typography may use PieAPP, DOVER and COVER, but retain a clear mapping to the source.

The CSV includes blank CI endpoints and the literal status `not_reported_in_Table_I`. These are missing values, not zero-width intervals. No CI is available for the table's correlations. The 95% intervals in original Fig. 5 and the `ci` field of the released dataset concern subjective MOS, not SRCC.

## 2. Exact caption and aggregation

Original Table I caption:

> Mean correlation for each source (within-sequence) and overall correlation across all videos. The evaluation is split into FR and NR metrics, with the top three results highlighted and the best result underlined.

Section IV states that, for within-sequence comparisons, correlations are calculated separately for all six source sequences and averaged using the Fisher z-transformation to reduce sampling bias. It also names the Meng–Rosenthal–Rubin test for comparing correlation coefficients. It supplies no per-metric correlation confidence intervals or numerical significance-test table.

The within-sequence SRCC aggregation is consistent with

`r_within = tanh(mean_s(atanh(r_s)))`,

where `r_s` is the Spearman correlation between metric predictions and MOS among versions of source `s`. This is not an arithmetic average of SRCC, and is not the correlation after pooling all scenes. Overall SRCC is the pooled rank association across evaluated outputs.

The text states Fisher aggregation for correlation coefficients. Do not apply it to RMSE. Table I gives the RMSE values, but the inspected paper does not fully specify the exact RMSE aggregation/calibration code.

Fig. 9 explicitly describes third-order mapping of each metric axis to the ACR scale per source and refers to ITU-T P.1401 (the caption prints “P.140”, while the bibliography names P.1401). That caption is evidence for the scatter plot's mapping. It is not sufficient to assert that every Table I statistic was computed after that mapping. A monotonic score reversal changes SRCC sign but not its magnitude; a non-monotonic fit can change ranks. Do not invent a mapping procedure for Table I.

## 3. Negative-direction metrics: what can and cannot be established

The original text does not explicitly explain its sign convention or whether/how it reverses lower-is-better metrics. The public repository contains raw metric outputs and MOS, but no correlation-analysis implementation was present in the inspected checkout. Therefore the following distinction is important:

1. **Published values:** All Table I SRCC values are printed as nonnegative. The figure can faithfully reproduce those values with the label “Reported SRCC” and a source citation.
2. **Raw-data cross-check:** Excluding `method == source` from the released 222-row dataset leaves 216 restored/upscaled outputs. Calculating signed Spearman correlations and the Fisher average reproduces the magnitudes of both reported SRCC columns to three decimals for 29 of the 30 metrics. The reproducibility record is `work/figure_revision/metric_study_crosscheck.json`.
3. **Lower-is-better outputs:** Butteraugli, PieAPP, LPIPS (Alex/VGG), DISTS, BRISQUE, and NIQE have negative raw correlations with MOS in this data. Their published positive values agree with reversing their quality direction (equivalently taking the absolute final statistic in these cases). Do not invert the CSV values again.
4. **Q-Align is a special warning:** Its raw within-source Fisher mean is **−0.1206614954**, while Table I reports **+0.121**. Its raw overall SRCC is **+0.1076212905**, reported as **+0.108**. Thus a single global direction reversal cannot explain both. The final aggregated magnitudes reproduce the table, but this does not establish the authors' exact code. The raw source correlations are mixed: approximately −0.247, −0.208, −0.052, +0.635, −0.589, −0.279. Taking absolute values separately for each source and *then* Fisher-averaging gives approximately 0.355, not 0.121. **Do not use per-source absolute values before aggregation.**
5. **DOVER data discrepancy:** Table I has within-source/overall SRCC **0.549/0.370**. The inspected released dataset's `dover` field on the 216 outputs gives **0.571357/0.383337**. Including the six sources instead gives approximately 0.548/0.368, still not the exact published pair. The technical/aesthetic components do not resolve it. No basis was found for changing the published values. Plot 0.549/0.370 as a reproduction of Table I, and retain this discrepancy in the provenance record. It may reflect a data/configuration/version difference, but that cause is unverified.

For the new figure, “Reported SRCC” is safer and more precise than presenting the values as an independently reproduced signed correlation leaderboard. Do not infer universal metric superiority or significance from visual point separation.

## 4. Sample design and interpretation

Paper Sections II-A/II-D:

- Six source clips from AVT-VQDB-UHD-1: BigBuckBunny, Daydreamer, Giftmord, Sparks15, Vegetables, Water.
- Approximately 8–10 s each; 3840×2160 UHD-1; 60 fps.
- Inputs at 360p and 720p, with uncompressed, AV1, and DCVC-RT conditions; outputs at 2160p, hence 6× and 3× scaling.
- AV1 encoder v3.12.0; DCVC-RT commit `9b7acf7`.
- Six upscalers: Lanczos (a=5), Topaz Rhea, SCST, DOVE, SeedVR2, Topaz Starlight Mini.
- 36 degraded inputs × 6 upscalers = 216 upscaled outputs, plus six unaltered originals = **222 rated sequences**. This decomposition is also explicit in the released dataset/README.
- The table caption describes “across all videos”, but the raw-data check shows that excluding the six source originals reproduces 29/30 table rows. Treat “216 outputs used for the correlation check” as a reconstruction from the released data, not a quoted explicit statement about the paper's analysis subset.
- 32 recruited participants, ages 23–36; 28 retained. Five-point ACR, each participant rates all 222 sequences in random order; 45–60 min with a break. FrACT10 vision test before rating.
- Outlier screening removes participants with correlation to MOS below 0.70, recalculating MOS after each removal; the paper explains that 0.70 is lower than the 0.75 recommendation because greater rating variance was expected.
- Asus XG43UQ, 43-inch UHD monitor; viewing distance 1.5 picture heights.
- IQA scores were sampled at two frames per second and averaged to adapt image metrics to videos. This does not make them measures of temporal consistency.

The exact condition identifiers in the released dataset are AV1 360p q54, AV1 720p q48, DCVC-RT 360p q34, DCVC-RT 720p q42, and uncompressed 360p/720p q0. Do not describe this as two independently varied compression levels at each resolution: the available released rows have the six listed resolution/codec combinations per source.

Limits: six source contents, selected compression settings, particular upscalers and implementation adaptations, one display/viewing arrangement, and a narrow observer age range. The experiment includes conventional/commercial comparators, so it is not a correlation analysis over only diffusion outputs. It establishes limitations in this tested VSR setting, not that all no-reference metrics are invalid for every diffusion restoration task.

## 5. Actual backbone and implementation comparison (optional inset/table)

These values come from Section II-B and describe this study's implementations, not necessarily original-paper defaults or a hardware-independent speed ranking.

| Upscaler | Prior/model used in this study | Steps | Temporal batch / overlap | Spatial/VAE configuration | Reported mean time |
|---|---|---:|---|---|---:|
| SCST | Stable Diffusion v2.1 image prior; Panda-70M captions | 20 | 8 / 1 frames | encoder tile 64; decoder tile 1024; process size 768 | 96 s/frame |
| DOVE | CogVideoX video prior | 1 | 128 / 64 frames | nine spatial tiles, 256-pixel overlap; modified tile blending, temporal overlap, prepend frames | 18 s/frame |
| SeedVR2 | SeedVR-based distilled generator; 7B, 16-bit model | 1 | 25 / 12 frames | nine 900×1460 tiles, 256-pixel overlap; added VAE tiling, temporal blending and prepend option | 11 s/frame |
| Rhea | Commercial Topaz model; architecture not fully specified here | Not reported | Not reported | Topaz v7.1.0; enhancement controls automatically set | Not reported |
| Starlight Mini | Commercial diffusion model | Not reported | Not reported | Topaz v7.1.0; 360p first resized to 540p with Lanczos, then 4× to 2160p | Not reported |
| Lanczos | Conventional resampling, a=5 | Not applicable | Not applicable | Direct scaling | Not reported |

Open models ran on a 40 GB A100, and the authors changed processing configurations to fit memory. SCST's small temporal batch is associated in the paper with visible temporal inconsistency; DOVE and SeedVR2 used larger batches and overlapping processing. The study's implementation differences prevent treating backbone identity as the sole causal explanation for quality differences. If space is limited, put this comparison in a supplementary table rather than mixing it into the metric correlation graphic.

## 6. Recommended publication-style figure

**Preferred: two aligned horizontal paired-dot panels, all 30 metrics.**

- Panel (a): 15 FR metrics. Panel (b): 15 NR metrics. Same x-axis 0–1, same panel width, identical tick spacing.
- One row per metric, with a filled blue circle for within-sequence and an orange square for overall. A thin light-gray segment connects the two values. Use shapes as well as color for grayscale/accessibility.
- Keep original Table I order to avoid an implied universal ranking; alternatively sort within each panel by published within-sequence SRCC and say so explicitly.
- Add two narrow aligned numeric columns (“Within” and “Overall”) to the right of each panel, with three decimal places. This is clearer than 60 floating numeric labels around close points.
- Directly label the x-axis **Reported SRCC with subjective MOS** and the legend **Within-sequence (Fisher aggregate)** / **Overall**.
- Use the same plot range for FR and NR. Avoid clipped axes, 3D bars, gradients, error bars, significance stars, and decorative model boxes.
- A two-column IEEE figure approximately 7.1 inches wide and 4.2–4.8 inches high can fit 15 rows per panel at readable font size. Use vector PDF/SVG.
- No error bars: Table I reports no correlation CIs. Do not transplant MOS CI to correlations.

Suggested caption:

> Reported agreement between objective quality models and subjective ratings in the diffusion-based VSR study of Herb et al. [metric], reproduced from their Table I. Panels separate full-reference (FR) and no-reference (NR) models. Within-sequence values aggregate correlations across six source contents using the authors' Fisher transformation, whereas overall values pool the evaluated material. Values follow the reporting convention of the source; correlation confidence intervals are not provided. The comparison describes the tested content, upscalers, degradations, and viewing conditions.

If a shorter caption is required, keep the source attribution, aggregation distinction, and absence of CIs. The negative-sign caveat can be a short footnote or surrounding prose if Q-Align is shown; do not silently relabel the values as signed recomputations. A compact subset can omit Q-Align for space, but must identify the selection as illustrative and retain the full CSV as evidence.

The central takeaway supported by the figure is that within-content ranking and across-content association differ materially, and that metric performance depends on the evaluated restoration setting. The figure does not prove that a single FR metric always works best.

## 7. Authentic image example and permission status

Original Fig. 2 is a seven-column crop comparison (Lanczos, Rhea, SCST, DOVE, SeedVR2, Starlight Mini, Original) from Daydreamer, 360p AV1 input. It visibly illustrates different edge/texture appearances and the paper discusses SCST oversharpening in this context.

- Local file: `work/figure_revision/metric_example_crops.png`.
- Exact source: https://arxiv.org/html/2605.25940v1/vsr_example_comparison_long.png
- Original caption: “Example crops from the Daydreamer sequence using 360p AV1 source encodings.”
- This is a real source figure, not an invented restoration example. It is a still crop and cannot on its own demonstrate temporal flicker.

**Permission status is not established for reprinting that bitmap.** The arXiv page displays its perpetual non-exclusive distribution license, which is not a CC reuse license. The inspected GitHub repository has no LICENSE file, and GitHub's repository API returns `license: null`. Its README requests citation and describes open data, but that does not supply an explicit figure-reprint license. The Hugging Face metadata request timed out, so no additional license claim is made. Keep the downloaded figure as internal source evidence; do not assume unrestricted permission for journal republication. The requested new metric diagram can instead be an original graphical presentation of the published numerical facts with a clear citation. If actual source imagery is desired, establish the publisher/author/underlying-content reuse conditions first.

Other useful original evidence: Fig. 7 shows correlation changes when removing a method or source, Fig. 8 visualizes prediction biases, and Fig. 9 contains MOS-versus-metric scatter plots. These can inform interpretation; a new schematic imitation or invented quantitative version would not be appropriate. Numerical data remain the most straightforward basis for the replacement Fig. 6.
