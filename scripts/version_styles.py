#!/usr/bin/env python3
"""Publish the CSS under a content-based filename and update page links."""
from hashlib import sha256
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
css = (root / 'styles.css').read_bytes()
filename = f'assets/styles.{sha256(css).hexdigest()[:12]}.css'
(root / filename).write_bytes(css)
pattern = re.compile(r'href="(?:styles\.css(?:\?[^"\s]*)?|assets/styles\.[0-9a-f]+\.css)"')
updated = 0
for page in root.glob('*.html'):
    before = page.read_text()
    after = pattern.sub(f'href="{filename}"', before)
    if after != before:
        page.write_text(after)
        updated += 1
# Keep earlier versions so cached HTML can still load its matching stylesheet.
print(f'{filename} — updated {updated} pages')
