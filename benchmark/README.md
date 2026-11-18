# Proposed evaluation protocol

This folder is a specification and empty reporting template, not a released video dataset, an executed experiment, or a model leaderboard.

## Tracks

- **Controlled method:** match the exact prior checkpoint or explicitly matched pretraining, data access, degradation, context, resolution and inference budget; isolate the restoration mechanism through matched comparisons.
- **Open system:** allow each system's intended backbone and recipe; use identical test material and report all information access and resources. This compares complete systems, not causal contributions of individual modules.

## Data strata

1. Paired synthetic, with a frozen degradation manifest.
2. Paired real, with documented alignment and acquisition.
3. Unpaired real, with human evaluation and explicitly limited fidelity claims.
4. Specialized domain, including sensor/identity/radiometric metadata where needed.
5. Generated video, with a contract specifying which attributes may change.
6. Long and streaming sequences, including motion, occlusion and cuts.

Split by source scene/identity and acquisition or generator pipeline; do not leak neighboring frames across splits. Publish fixed seeds for stochastic restorers. Bootstrap at sequence/content level instead of treating adjacent frames as independent observations. Use separate held-out content for metric calibration.

## Reporting

`protocol.example.json` lists the required configuration fields. `null` means that the field must be filled before a run; it does not encode an actual measurement. `results.template.csv` intentionally has a header and no result rows. For nonapplicable metrics, use an explicit reason rather than an invented zero. Preserve per-sequence, per-seed results; publish aggregates separately.

Timing must state whether capture/file decode, transfers, conditioning/flow, denoising, VAE decoding, stitching and output encoding are included. Report look-ahead, first-output latency, sustained FPS and peak memory separately. Human assessment should distinguish viewing quality, content fidelity and temporal artifacts and document the display and presentation protocol.
