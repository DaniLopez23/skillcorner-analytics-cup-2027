# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Entry for the SkillCorner Analytics Cup 2027, built on SkillCorner's open tracking + body-pose data
(https://github.com/SkillCorner/opendata). Research question: does a player's environment awareness —
scanning the pitch via head/body orientation before receiving the ball — relate to their physical output
and the pressure they face from opponents at reception?

The deliverable is a single Quarto book compiled from chapters in `notebooks/`, each documenting one
stage of the analysis in prose + executable Python code cells.

## Commands

```bash
# environment
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -e .                # installs src/skillcorner_cup in editable mode + deps

# render/preview the book (requires Quarto CLI installed separately — not on PATH yet on this machine)
quarto render                   # builds all chapters into _book/
quarto preview                  # live-reloading preview
quarto render notebooks/02-scanning-detection.qmd   # render a single chapter
```

There are no tests or linters configured yet.

## Architecture

- `_quarto.yml` — book config; `book.chapters` lists the `.qmd` files in build order. Add new stages of
  analysis here as a new chapter file, not as a loose notebook.
- `notebooks/*.qmd` — one file per analysis stage (data loading → scan detection → physical metrics →
  pressure analysis → conclusions). Each later chapter builds on outputs/tables produced by earlier ones,
  so keep the numeric prefix order meaningful — it's both the narrative order and the execution order.
- `src/skillcorner_cup/` — reusable Python (data loading, feature engineering) imported from notebooks via
  `from skillcorner_cup import data`. Put logic that's reused across chapters here rather than duplicating
  it in `.qmd` code cells; keep the `.qmd` cells focused on orchestration/analysis/plots.
- `data/raw/` — untouched SkillCorner open data, git-ignored. Populate manually from
  https://github.com/SkillCorner/opendata; layout is not yet fixed in code (see TODOs in
  `src/skillcorner_cup/data.py`).
- `data/processed/` — derived tables (e.g. per-reception scan/physical/pressure features) written by
  notebooks for reuse by later chapters, git-ignored.

## Notes for future work

`src/skillcorner_cup/data.py` has loader stubs (`load_match_tracking`, `load_match_physical`) that raise
`NotImplementedError` — implement them against the actual raw data layout once it has been downloaded and
inspected, since the open-data file structure isn't confirmed in this repo yet.
