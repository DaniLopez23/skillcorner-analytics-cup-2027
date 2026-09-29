# Skillcorner Analytics Cup 2.0

Entry for the SkillCorner Analytics Cup 2027, using SkillCorner's open data (tracking + body-pose).

## Idea

Player environment awareness: how does scanning the pitch (checking surroundings via head/body
orientation before receiving the ball) relate to a player's physical output and the pressure they face
from opponents at the moment of reception?

## Structure

The analysis is written as a [Quarto](https://quarto.org) book, one chapter per stage, in `notebooks/`:

- `01-data-overview.qmd` — sourcing and loading the SkillCorner open data
- `02-scanning-detection.qmd` — deriving scan events from body-pose/orientation data
- `03-physical-metrics.qmd` — scans vs. physical output around ball reception
- `04-pressure-analysis.qmd` — scans vs. opponent pressure at reception
- `05-conclusions.qmd` — findings and next steps

Reusable Python code lives in `src/skillcorner_cup/`, imported from the notebooks.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -e .
```

Install [Quarto](https://quarto.org/docs/get-started/) separately (not a Python package).

Download the SkillCorner open data from <https://github.com/SkillCorner/opendata> into `data/raw/`
(git-ignored).

## Rendering

```bash
quarto render          # build the full book into _book/
quarto preview          # live preview while editing
```
