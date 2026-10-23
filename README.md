# Closing the Loop — ICRA 2027 Workshop Website

An accessible, responsive, dependency-free website for the proposed ICRA 2027 half-day workshop **Closing the Loop: Task-Driven Multimodal Sensing, Perception, and Manipulation**.

## Pages

- `index.html` — workshop overview, proposed format, dates, and primary contact.
- `cfp.html` — contribution formats, review process, timeline, and publication plan.
- `topics.html` — scientific scope, participation and publicity plans, related events, and outcomes.
- `program.html` — tentative schedule, invited talk themes, poster/demo capacity, and room requests.
- `organizers.html` — 12 organizers, 11 advisory-board members, responsibilities, and prior experience.
- `dates.html` — official ICRA dates and proposed workshop-specific timing.
- `styles.css` — responsive design.
- `script.js` — legacy navigation helper; the current pages work without JavaScript.
- `assets/multisensory-art.svg` — editable vector banner artwork.
- `assets/bg-diagram.svg` — closed-loop diagram, with editable source in `assets/bg-diagram.drawio`.

## Published site

**Website:** https://icra2027multisensory.github.io/

**Repository:** https://github.com/icra2027multisensory/icra2027multisensory.github.io

The site is published from the `main` branch using GitHub Pages.

## Proposal status

The site follows the current six-page proposal document, `ICRA_2027_Overleaf (2).pdf`. The proposal selects a workshop and half-day duration. It proposes an in-person morning session from 08:30 to 12:30. The assigned workshop day remains pending between May 24 and May 28, 2027.

The invited-speaker section identifies four talk themes but still needs speaker names, affiliations, and final topics. The contribution calendar dates and submission link, along with the archival publication route, short-contribution eligibility, copyright/license terms, and camera-ready schedule, also remain to be confirmed. The site identifies the workshop as proposed and does not announce acceptance.

Conference-wide dates are from the [ICRA 2027 Call for Workshops and Tutorials](https://2027.ieee-icra.org/contribute/call-for-workshop-and-tutorial/): full proposal deadline November 2, 2026; acceptance notification January 31, 2027; workshop days May 24 or 28, 2027.

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

- Simple conference layout inspired by [CV4DC 2026](https://cv4dc.github.io/2026/): an illustrated SVG banner, dark navigation, and a white content area with a dates sidebar.
- Responsive single-column layouts on phones and a main column with sidebar on desktop.
- Each navigation item opens its own HTML page, with the current page highlighted.
- Skip-to-content link, keyboard-operable navigation, visible focus, semantic sections and headings, and reduced-motion support.
- No external fonts, trackers, cookies, embeds, or JavaScript requirement for content.
