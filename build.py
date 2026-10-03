"""Inline nand_lal_rahit_rules.json into the app. Run: python3 build.py"""
import json, pathlib
here = pathlib.Path(__file__).parent
data = json.loads((here / "nand_lal_rahit_rules.json").read_text(encoding="utf-8"))
blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
src = (here / "app.src.html").read_text(encoding="utf-8").replace("/*__DATA__*/null", blob)
(here / "rahit.html").write_text(src, encoding="utf-8")  # artifact body (skeleton added at publish)
(here / "index.html").write_text(
    '<!doctype html>\n<html lang="en"><head><meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>\n'
    + src.replace("<canvas", "</head><body>\n<canvas", 1) + "\n</body></html>\n", encoding="utf-8")
print(len(data["rules"]), "rules;", sum(1 for r in data["rules"] if r["needs_verification"]), "pending")
