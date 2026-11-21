"""make.fun entry: news-image-20261120.

Writes the entry image to /output/entry.png (or $MAKEFUN_OUTPUT_DIR).
The image beside this file (entry.png) is the finished front page that
sums up the world news of 20 November 2026; this program copies it
byte-for-byte so two runs always produce identical output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"entry image missing beside entrypoint: {SOURCE}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    # Determinism guard: the copy must be byte-identical to the source.
    if dest.read_bytes() != SOURCE.read_bytes():
        raise SystemExit("copied entry.png differs from the bundled image")


if __name__ == "__main__":
    main()
