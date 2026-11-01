#!/usr/bin/env python3
"""Publish the CSS under a timestamped filename and update page links."""
from datetime import datetime, timezone
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
css = (root / 'styles.css').read_bytes()
filename = f'assets/styles.{datetime.now(timezone.utc):%Y%m%d%H%M%S%f}.css'
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
