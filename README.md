# Closing the Loop — ICRA 2027 Workshop Website

An accessible, responsive, dependency-free website for the proposed ICRA 2027 half-day workshop **Closing the Loop: Task-Driven Multimodal Sensing, Perception, and Manipulation**.

## Pages

- `index.html` — proposal cover details and Sections 1.1–1.3, with references.
- `cfp.html` — Sections 3.4 and 5.2.
- `topics.html` — Sections 1.4–1.5, 4, and 5.1.
- `program.html` — Sections 3.1–3.3.
- `organizers.html` — Section 2.
- `dates.html` — Section 6, Organizer Requests.
- `styles.css` — responsive design.
- `script.js` — legacy navigation helper; the current pages work without JavaScript.
- `assets/multisensory-art.svg` — editable vector banner artwork.
- `assets/bg-diagram.svg` — closed-loop diagram, with editable source in `assets/bg-diagram.drawio`.

## Published site

**Website:** https://icra2027multisensory.github.io/

**Repository:** https://github.com/icra2027multisensory/icra2027multisensory.github.io

The site is published from the `main` branch using GitHub Pages.

## Proposal status

The website content follows the public-facing sections of `ICRA_2027_Overleaf (2).pdf` verbatim. The proposal's speaker details are marked “TO FILL.” Its publication route, eligibility of short contributions, copyright/license, and camera-ready timetable must be confirmed before the call is issued.

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

- Simple conference layout inspired by [CV4DC 2026](https://cv4dc.github.io/2026/): an illustrated SVG banner, dark navigation, and a white content area with a proposal-section sidebar.
- Responsive single-column layouts on phones and a main column with sidebar on desktop.
- Each navigation item opens its own HTML page, with the current page highlighted.
- Skip-to-content link, keyboard-operable navigation, visible focus, semantic sections and headings, and reduced-motion support.
- No external fonts, trackers, cookies, embeds, or JavaScript requirement for content.
