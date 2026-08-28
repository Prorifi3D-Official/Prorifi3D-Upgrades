from pathlib import Path
import os
import subprocess
import sys


root: Path = Path(__file__).resolve().parents[1]
environment: dict[str, str] = os.environ.copy()
environment["PYTHONPATH"] = str(root / "tmp" / "mkdocs-deps")
command: list[str] = [
    sys.executable,
    "-m",
    "mkdocs",
    "build",
    "--strict",
    "--site-dir",
    str(root / "tmp" / "site"),
]
result: subprocess.CompletedProcess[str] = subprocess.run(
    command,
    cwd=root,
    env=environment,
    check=False,
    text=True,
)
raise SystemExit(result.returncode)
