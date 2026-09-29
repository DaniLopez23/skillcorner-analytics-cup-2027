"""Loaders for SkillCorner open data.

Raw files are expected under ``data/raw/`` (see README for how to obtain them from
https://github.com/SkillCorner/opendata). Nothing here assumes a specific layout yet — fill in the TODOs
once the raw data has actually been downloaded and its exact structure inspected.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"


def list_available_matches() -> list[str]:
    """Return the match ids present under ``data/raw/``."""
    if not RAW_DATA_DIR.exists():
        return []
    return sorted(p.name for p in RAW_DATA_DIR.iterdir() if p.is_dir())


def load_match_tracking(match_id: str):
    """Load tracking (and body-pose, if present) data for a single match."""
    raise NotImplementedError("TODO: implement once raw data layout is confirmed")


def load_match_physical(match_id: str):
    """Load physical metrics for a single match."""
    raise NotImplementedError("TODO: implement once raw data layout is confirmed")
