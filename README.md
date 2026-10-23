# Closing the Loop — ICRA 2027 Workshop Website

An accessible, responsive, dependency-free website for the proposed ICRA 2027 half-day workshop **Closing the Loop: Task-Driven Multimodal Sensing, Perception, and Manipulation**.

## Pages

- `index.html` — workshop overview and references.
- `cfp.html` — call for contributions and dissemination information.
- `topics.html` — workshop topics, participant engagement, and related events.
- `program.html` — tentative program and speaker information.
- `organizers.html` — organizing team and responsibilities.
- `dates.html` — planned submission timeline and workshop logistics.
- `styles.css` — responsive design.
- `script.js` — legacy navigation helper; the current pages work without JavaScript.
- `assets/multisensory-art.svg` — editable vector banner artwork.
- `assets/bg-diagram.svg` — closed-loop diagram, with editable source in `assets/bg-diagram.drawio`.

## Published site

**Website:** https://icra2027multisensory.github.io/

**Repository:** https://github.com/icra2027multisensory/icra2027multisensory.github.io

The site is published from the `main` branch using GitHub Pages.

## Proposal status

The website is organized around visitor-facing pages using the public-facing material in `ICRA_2027_Overleaf (2).pdf`. Proposal form labels and internal section references are adapted for the site. Speaker names, affiliations, and topics remain to be confirmed. The publication route, eligibility of short contributions, copyright/license, and camera-ready timetable must be confirmed before the call is issued.

## Before publishing the final contribution call

- [ ] Update the site after the ICRA acceptance decision.
- [ ] Confirm the four invited speakers, affiliations, and final talk topics.
- [ ] Confirm the assigned workshop day.
- [ ] Confirm the submission portal and calendar dates for contributions, decisions, and final papers.
- [ ] Confirm the publication route, eligibility of short contributions, copyright/license terms, and camera-ready schedule.
- [ ] Publish the accessibility contact and approved final call details.

## Preview locally

Run `python3 -m http.server 8000` in this folder, then open `http://localhost:8000`.

The project uses plain HTML/CSS/JS and requires no package installation, build step, framework, hosting plan, or API key.

## Design and accessibility

- Simple conference layout inspired by [CV4DC 2026](https://cv4dc.github.io/2026/): an illustrated SVG banner, light page tabs, and a single white reading column.
- Single-column reading flow on desktop and phones.
- A short workshop introduction precedes a row of page tabs; each tab opens its own HTML page, with the current page highlighted.
- Proposal section numbering is removed from headings; site links connect related material across pages.
- Skip-to-content link, keyboard-operable navigation, visible focus, semantic headings, and reduced-motion support.
- No external fonts, trackers, cookies, embeds, or JavaScript requirement for content.
