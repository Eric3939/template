from pathlib import Path
from myproject.paths import RESULTS
from myproject.utils.utils import helloworld

experiment_name = "run20260524"
run_dir = RESULTS / experiment_name
run_dir.mkdir(exist_ok=True)
output_file = run_dir / "results.csv"

print(helloworld())