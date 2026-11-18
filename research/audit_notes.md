# Evidence audit and revision notes

Cutoff: **17 November 2026**. The ledger contains **118 sources**, of which **117 are cited** in the paper. The remaining WAM survey was used to study organization, not as evidence for video-restoration claims.

## Scientific revisions

- The fidelity/realism/temporal triangle is an organizing design tension, not a proved three-way impossibility theorem. Diversity across whole samples is distinguished from flicker within a sample.
- Existing video diffusion surveys do cover restoration as a subtopic, and video restoration surveys do cover motion and temporal consistency. The new manuscript claims integrated analysis, not absolute first coverage.
- Video adverse-weather removal, including fog-related work, is already represented by verified papers. The research agenda concerns precise remaining conditions and validation gaps.
- UnDIVE uses a diffusion-derived encoder with mixed supervision: unlabeled pretraining, paired spatial enhancement, and an unsupervised temporal term. It is not labeled a wholly unsupervised reverse-diffusion video sampler.
- DiQP is codec/cold-diffusion-inspired and does not use ordinary Gaussian corruption in the same way as DDPM.
- The original GDP conference paper is image-focused; video claims cite the IJCV 2026 extension. HDR image/event work is labeled adjacent rather than claimed as video consistency evidence.
- STAR's default prior is distinguished from its separate scaling variant; SeedVR2's restoration-trained teacher is distinguished from public video-foundation adaptation.
- Sampling steps, function evaluations, future look-ahead, throughput and first-output latency are kept separate. Training-only teacher supervision is separated from inference in the pipeline diagram.
- The proposed controlled track matches an exact checkpoint or explicitly matched pretraining. Merely matching the model family does not remove pretraining confounding.

## Requested quality-assessment study

The QoMEX 2026 study by Herb et al. was checked at full-text level. The manuscript reproduces five pairs of Table I SRCC values and records the six source clips, 360p/720p input conditions, codecs, 32 recruited/28 retained observers and display setting. The **222 test sequences include original UHD references** and are not all attributed to generated upscaler outputs. Within-source and overall correlations are kept separate. Implementation changes needed for the study's memory budget are disclosed as an interpretation limit.

## Candidate-list corrections

Several supplied method acronyms differ from official paper titles, including StableVSR, DLoRAL, DiQP, UnDIVE, FlashVSR, InfVSR, HATIR, StableBFVR and EVDiffuser. The bibliography uses the verified titles. The low-light wavelet paper is CVMP 2024. The weather test-time adaptation title is *Genuine Knowledge from Practice: Diffusion Test-Time Adaptation for Video Adverse Weather Removal*, not the unrelated generative-feedback Diff-TTA title.

The HATIR full text contains inconsistent dataset arithmetic; those counts are not repeated. Late arXiv posting alone was not treated as evidence against conference publication (PatchVSR illustrates this distinction).

## Supplementary-list revision

All 81 records in the supplementary Excel list now map to manuscript citations. Of these, 47 were already included and 34 were newly verified and added. The earlier unresolved leads TurboVSR, SimpleGVR, FastVSR, SeTe-VSR, PS-SR, OSDEnhancer, DiffST and DGAF-VSR are resolved in this revision. See `spreadsheet_coverage.csv` for row-level mapping and the expanded source ledger for primary evidence.

Thirty-two additions address restoration/enhancement directly. Two clarify adjacent roles: generative coding (`stdpevc`) and diffusion-assisted degradation synthesis for adaptation (`dadeblur`). Vivid-VR, InfVSR and ZSVD now use verified 2026 conference identities. The all-in-one survey is also cited as a related survey.

The six figures were redrawn as original taxonomy, sequence, architecture, temporal-mechanism, context and evaluation diagrams. The manuscript follows seven main sections; retrieval/process declarations have been removed from its technical body. Source verification, AI-assisted drafting and figure programming remain documented here.

## Retrieval limits

Google Scholar and some OpenReview pages returned verification challenges. Primary CVF/NeurIPS exports, publisher/Crossref exports and arXiv metadata were used instead. Some sources have abstract-level scope verification; stronger architecture claims use full-text anchors. No full retraction audit, blind human peer review, independent code replication or model rerun is claimed.

## Review and reproducibility

Three parallel evidence passes covered (1) VSR and the requested metric study, (2) specialized/general restoration, and (3) foundations and related surveys. Cross-reading checked the manuscript's factual scope, backbone distinctions, supervision, equations, metrics and benchmark logic. This was AI-assisted technical review, not journal peer review. Corrections included posterior-conditioning notation, missing LaTeX symbols, an overbroad conventional-baseline sentence, and training/inference diagram semantics.

The deterministic validator checks citation keys, bibliography completeness, source records, labels and figure existence. Successful compilation and visual inspection verify rendering; neither establishes independent experimental reproducibility. Raw downloaded papers and supplied source PDFs are retained outside the repository and are not redistributed here.

## Before journal submission

The supplied author order and affiliation remain in the manuscript. Contributions, funding, competing interests and venue-specific AI statements require confirmation by the actual authors. No grants, contribution assignments, ethics approvals or new experimental results have been invented. The manuscript and repository can be revised without losing the evidence trail.

### Final bibliographic normalization

Final issue dates were used for Rota et al. (June 2023) and Xing et al. (February 2025), replacing online-first dates attached to final volume/issue metadata. DISTS was corrected to TPAMI 44(5), 2567--2581, May 2022 using NLM PubMed PMID 33338012 and Europe PMC, replacing early-access 1--1 pagination. The corporate author Team Wan is brace-protected. Preprint status is explicit in the bibliography. These are metadata corrections, not changes to scientific claims.

DDIM and Score-SDE use their ICLR 2021 archival identity; DPS uses ICLR 2023. Their original arXiv export revision years are not treated as publication years. FVD uses first-publication year 2018. FAST-VQA is typed as a conference paper so the ECCV booktitle is retained.

## Final technical review of the revision

Cross-reading of the new method paragraphs corrected heterogeneous base/draft costs in the inference equation, distinguished DTG-Restore conditioning from its reconstruction target, clarified PixRevive feature conditioning, and separated DADeblur test-time adaptation from subsequent deblurring. ZVRV's selection is described as optimizing perceptual/temporal proxy scores, not directly establishing source fidelity. HDR overview coverage now includes DiffHDR. The public manuscript does not include the working review files or downloaded full texts.
