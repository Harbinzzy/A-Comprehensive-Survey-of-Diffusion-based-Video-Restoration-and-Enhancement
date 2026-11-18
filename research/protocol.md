# Evidence and scope protocol

Search date and evidence cutoff: 17 November 2026.

This is a critical, taxonomy-led technical survey, not a registered systematic review or meta-analysis. The title's “comprehensive” refers to the dimensions of analysis; the paper does not claim exhaustive retrieval of every publication.

## Questions

1. How do generative priors alter fidelity, perceptual realism and temporal coherence in video restoration?
2. Which architectural, conditioning and sampling mechanisms constrain temporal errors?
3. Which task and deployment settings are supported by verified primary literature?
4. What would fair model comparison and perceptually valid video evaluation require?

## Retrieval

The user's three literature tables and supplementary 81-record spreadsheet supplied candidate titles. The supplementary list is fully reconciled in spreadsheet_coverage.csv; primary papers supply the technical evidence. Exact-title and method-name searches are supplemented by searches for diffusion video restoration, diffusion video super-resolution, video enhancement, underwater, infrared, turbulence, adverse weather, face restoration, video inpainting, compression, zero-shot, streaming, one-step, flow matching, and video quality assessment. Primary sources include arXiv, CVF Open Access, publisher records, OpenReview and official project repositories. Related-survey bibliographies provide backward citation leads.

Google Scholar was attempted but returned a JavaScript verification page. BibTeX is exported from primary sources where available or constructed from retrieved primary bibliographic metadata. No claim is made that entries were exported from Scholar.

## Inclusion and boundaries

- Core: a diffusion, score-based, rectified-flow or flow-matching prior used to restore or enhance an observed video, with video-specific inference, learning or evaluation.
- Context: image inverse-problem priors, discriminative video baselines, backbone papers, datasets, metrics and neighboring surveys.
- Boundary: generation enhancement, compression reconstruction, interpolation/inpainting and agentic orchestration when they clarify the observed-video problem. These are labeled, not silently treated as identical tasks.
- Excluded from factual method comparisons: unverified titles and unretrievable claims; image-only work represented as if it validated video performance; pure unconstrained generation without restoration relevance.

## Extraction and verification

Records retain canonical title, author list, year/version, source URL, DOI/arXiv identifier where available, source reading depth and a concise claim-to-source locator. Conference status is stated only when supported by official metadata. Abstract-only records support broad scope claims, not unreported architecture details or numerical conclusions. A missing result is not proof that a research area is empty.

## Synthesis rules

- Supervision, knowledge of degradation and test-time adaptation are separate axes.
- Original conceptual diagrams are schematic; they contain no invented experimental measurements.
- No new model experiments or cross-paper numerical leaderboard are claimed.
- The benchmark design is a proposal, not a benchmark release or empirical finding.
- Preprints are explicitly distinguished from verified archival publications.
- Candidate corrections and retrieval limits are kept in the evidence notes.

## Workflow provenance

The source-verification, literature-synthesis and writing-quality principles of [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills) informed this work. The workflow is adapted to an English IEEE-style computer-vision survey and the user's authorization to rewrite and push. It is not a certified run of that package's complete pipeline, clinical evidence hierarchy, calibration framework or journal-submission checks.
