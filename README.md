# ICRA 2027 Workshop Website — Draft v0.1

An accessible, responsive, dependency-free website for an ICRA 2027 half-day workshop proposal. The uploaded proposal is an unfilled template, so its unconfirmed fields remain TBD on the site.

## Included files

- `index.html` — proposal summary; title, primary contact, and keywords are TBD.
- `cfp.html` — Call for Papers; scope and submission details are TBD.
- `topics.html` — proposal topic, scope, engagement, and prior-event fields are TBD.
- `program.html` — half-day program, format, and organizer-request fields are TBD.
- `organizers.html` — organizer roles and primary contact are TBD.
- `dates.html` — official conference dates and TBD workshop-specific dates.
- `styles.css` — responsive design.
- `script.js` — legacy navigation helper; the current navigation works without JavaScript.
- `assets/favicon.svg` — abstract loop mark.
- `assets/multisensory-art.svg` — hand-drawn vector header artwork with editable robot, sensing, and abstract background elements.
- `assets/bg-diagram.svg` — original closed-loop diagram; editable source in `assets/bg-diagram.drawio`.
- `.nojekyll` — GitHub Pages compatibility.

## Preview locally

Run `python3 -m http.server 8000` in this folder, then open `http://localhost:8000`.

## Dedicated GitHub Pages site

**Repository:** https://github.com/icra2027multisensory/icra2027multisensory.github.io

**Expected URL after GitHub Pages is enabled:** https://icra2027multisensory.github.io/

The website files are already on the `main` branch. To publish, open repository **Settings → Pages → Build and deployment**, select **Deploy from a branch**, choose **main** and **/(root)**, then save. Verify the published website in GitHub Pages settings. If the organization restricts Pages creation, its owner must permit public Pages sites in organization settings.

The website is a *draft*, not an announcement of workshop acceptance. After the conference accepts the workshop and the organizing team approves the final information, update provisional text and review search-indexing settings across all HTML pages.

The project uses plain HTML/CSS/JS and requires no npm install, build, framework, hosting plan, or API key.

## REQUIRED APPROVALS BEFORE ANNOUNCEMENT

- [ ] Set the proposal title (currently TBD).
- [ ] Add the response to pre-proposal feedback, if applicable.
- [ ] Add proposal keywords.
- [ ] Update workshop acceptance status only after the conference decision.
- [ ] Add the assigned workshop date and half-day time slot.
- [ ] Complete the scope, relevance, scientific questions, outcomes, and distinction from related workshops.
- [ ] Confirm invited speaker names, affiliations, and talk topics.
- [ ] Complete the co-chair, faculty-advisor, and student-organizer roster.
- [ ] Complete the tentative schedule and format, poster capacity, demonstration plans, and contribution-selection process.
- [ ] Describe audience engagement, inclusive participation, publicity, and any RAS Technical Committee collaboration.
- [ ] Provide previous-event venue, year, attendance, URL, and rationale, or state that this is a new workshop; add dissemination plans and other review information.
- [ ] Complete room, equipment, and remote/hybrid requests.
- [ ] Set contribution types, paper lengths, review criteria, and publication policy.
- [ ] Set the submission platform and all workshop-specific deadlines.
- [ ] Add the confirmed primary contact and public contact details.
- [ ] Complete the proposal fields and Call for Papers before inviting submissions.
- [ ] Review all terms and logos if incorporating official IEEE/ICRA brand assets in a later revision (none are copied in this draft).

## Source and proposal status

The uploaded PDF is the ICRA 2027 proposal template, not a completed proposal. It selects “Workshop” and “Half Day” and leaves the title, primary contact, keywords, scope, organizers, and program sections blank. Those fields are marked TBD on the website.

The [ICRA 2027 Call for Workshops and Tutorials](https://2027.ieee-icra.org/contribute/call-for-workshop-and-tutorial/) supplies the conference-wide proposal and event dates. The workshop’s assigned day, time, and paper deadlines are TBD.

## Design and accessibility

- Simple conference layout inspired by [CV4DC 2026](https://cv4dc.github.io/2026/): an illustrated SVG banner, dark navigation, and a white content area with a dates sidebar.
- Responsive single-column layouts on phones; main content and a sidebar on desktops.
- Each navigation item opens its own HTML page, with the current page highlighted.
- Skip-to-content, always-visible keyboard-operable navigation, visible focus, semantic sections and headings, reduced-motion support.
- No external fonts, trackers, cookies, embeds, or required JavaScript for content.
- The uploaded proposal is an unfilled template. The website marks unconfirmed proposal fields as TBD.
- Official conference dates are separated from workshop-specific dates, which remain TBD.
