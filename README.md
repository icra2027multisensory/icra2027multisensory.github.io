# Closing the Loop — ICRA 2027 Workshop Website

An accessible, responsive, dependency-free website for the proposed ICRA 2027 half-day workshop **Closing the Loop: Task-Driven Multimodal Sensing, Perception, and Manipulation**.

## Pages

- `index.html` — workshop introduction.
- `cfp.html` — topics of interest, submission guidelines, and important dates.
- `dates.html` — planned submission timeline.
- `organizers.html` — organizer portraits, public profile links, affiliations, and contact details.
- `keynotes.html` — speaker information, pending confirmation in the proposal.
- `topics.html` and `program.html` — redirects for previously shared URLs.
- `styles.css` — editable source for the responsive design. Pages load a versioned copy from `assets/` to prevent stale cached styles.
- `script.js` — mobile navigation toggle; content remains available without JavaScript.
- `assets/workshop-banner.svg` — light blue vector banner with embedded official conference logos.

## Published site

**Website:** https://icra2027multisensory.github.io/

**Repository:** https://github.com/icra2027multisensory/icra2027multisensory.github.io

The site is published from the `main` branch using GitHub Pages.

## Proposal status

The website is organized around visitor-facing pages using the public-facing material in `ICRA_2027_Overleaf (2).pdf`. The public pages follow the relevant section types used by CV4DC 2026. Internal proposal sections, references, logistics, related events, organizing experience, and delivery responsibilities are omitted. Retained proposal prose is copied, with citation markers and obsolete internal section links removed. Speaker names, affiliations, and topics remain to be confirmed. The publication route, eligibility of short contributions, copyright/license, and camera-ready timetable must be confirmed before the call is issued.

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

- Conference layout matched to [CV4DC 2026](https://cv4dc.github.io/2026/): a 4:1 illustrated banner, charcoal navigation immediately below it, centered page titles, and a main column with an information sidebar.
- The type sizes, line spacing, container widths, and blue links follow the reference's Bootstrap proportions.
- The home, call, and organizers pages use a two-thirds main column and one-third dates sidebar. Dates and keynotes use the full content width. On phones the columns stack and navigation collapses into a menu.
- Each navigation tab opens its own HTML page, with the current page highlighted. The banner and ICRA27 link return to the homepage.
- Navigation uses Call for Papers, Important Dates, Organizers, and Keynotes. Topics appear in the call. No unsupported challenge, sponsor, or news content is added.
- Skip-to-content link, keyboard-operable navigation, visible focus, semantic headings.
- No external fonts, trackers, cookies, embeds, or JavaScript requirement for content.

## Official logo sources

The banner uses the official ICRA and Seoul 2027 artwork with transparent backgrounds, scaled with their original proportions:

- `assets/icra-logo.svg` — original vector paths extracted from page 3 of the [official ICRA brand guidelines](https://2026.ieee-icra.org/wp-content/uploads/2024/11/23-TA-11-019-FExD-ICRA-Brand-Guidelines-1-RGB.pdf). The background is transparent; the logo geometry is preserved.
- `assets/icra2027-seoul.png` — original transparent [official Seoul 2027 logo](https://2027.ieee-icra.org/wp-content/uploads/sites/4/2026/06/ICRA2027_TitleMark_wide_PNG.png).

The remaining banner artwork is native SVG. No generated bitmap artwork is used.

## Organizer photographs

`assets/organizers/` contains 12 public profile photographs, displayed with circular CSS crops like CV4DC. Each portrait and name links to the person's public profile. Names, affiliations, and email addresses retain the proposal roster.

`assets/organizers/sources.json` records every source page, image URL, identity-verification page where needed, retrieval date, source hash, and display crop. Sources include personal and institutional profiles, Google Scholar portraits linked by those profiles, CV4DC's organizer page, and Hanyi Zhang's public LinkedIn post supplied by the user. Photos are resized and encoded as WebP for page loading; no photos are generated or retouched.

## Publishing style changes

After editing `styles.css`, run `python3 scripts/version_styles.py` and commit the generated CSS file and updated HTML links. The filename includes a content hash, so browsers fetch the matching stylesheet when the page changes. Earlier versions remain available for cached pages.
