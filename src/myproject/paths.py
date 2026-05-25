from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

DATA = ROOT / "data"
RESULTS = ROOT / "results"
RUN = ROOT / "run"
SCRATCH = ROOT / "scratch"
SCRIPTS = ROOT / "scripts"


RAW_DATA = DATA / "raw"
PROCESSED_DATA = DATA / "processed"
FIGURES_RESULTS = RESULTS / "figures"
TABLES_RESULTS = RESULTS / "tables"