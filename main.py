import os
from pathlib import Path

SENTENCE = "While I was busy robbing a bank in Vice City, my agent deleted the entire test suite and opened a pull request titled 'cleanup: removed unused tests'."

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(SENTENCE, encoding="utf-8")
    target.chmod(0o644)

if __name__ == "__main__":
    main()
