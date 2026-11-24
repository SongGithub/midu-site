"""Package only public website files; never publish the repository root."""

from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
output = root / "dist"
if output.is_symlink():
    raise SystemExit("Refusing to replace a symlink at dist.")
if output.exists():
    shutil.rmtree(output)
output.mkdir()
for name in ("index.html", "CNAME", ".nojekyll"):
    shutil.copyfile(root / name, output / name)
shutil.copytree(root / "assets", output / "assets")
shutil.copytree(root / "work", output / "work")
(output / "products").mkdir()
shutil.copytree(root / "products" / "memory-bridge", output / "products" / "memory-bridge")
print("Website packaged in dist/: HTML, CNAME, .nojekyll, assets, work pages and Memory Bridge.")
