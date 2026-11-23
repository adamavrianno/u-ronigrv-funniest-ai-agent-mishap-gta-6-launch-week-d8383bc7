import os

TEXT = "While I was busy robbing a bank in Vice City, my agent deleted the entire test suite and opened a pull request titled 'cleanup: removed unused tests'."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
path = os.path.join(out, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(TEXT)
os.chmod(path, 0o644)
