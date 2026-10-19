# ICRA 2027 Workshop Website — Draft v0.1

An accessible, responsive, dependency-free static website and draft Call for Papers for the **proposed** merged ICRA 2027 half-day workshop.

## Included files

- `index.html` — workshop overview, dates summary, and links to the dedicated pages.
- `cfp.html` — **draft only** CFP, topics, contribution types, and pending submission requirements.
- `topics.html` — research topics.
- `program.html` — tentative half-day program.
- `organizers.html` — organizing team.
- `dates.html` — workshop proposal and pending author submission dates.
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

- [ ] Choose the **final title**; currently an explicitly labeled working title.
- [ ] Confirm the workshop is **accepted**, and update status/banner language only after the conference decision.
- [ ] Confirm which day (May 24 **or** May 28) and actual half-day time slot; do not imply a specific room.
- [ ] Approve the merged abstract/topic descriptions with Hanyi and Jian.
- [ ] Finalize speaker names, institutions, talk titles **and acceptance** before replacing anonymous placeholders.
- [ ] Finalize organizing team roster and assigned roles (workshop co-chairs, faculty advisors, student organizers); add a separate PC section if appropriate.
- [ ] Set the final program format and timetable; the schedule on `program.html` is *tentative*.
- [ ] Decide which contribution types to accept, short/full paper lengths, whether recently published papers are welcome, archival or non-archival proceedings policy, reviewer criteria, and publication/hosting policies.
- [ ] Confirm submission platform, paper deadline, acceptance notification, camera-ready deadline (if applicable), and exact times/timezones.
- [ ] Approve a public organizer contact email or contact form; **do not expose private addresses** without permission.
- [ ] Publish the final CFP and submission link once author submissions can be received and the team approves release.
- [ ] Review all terms and logos if incorporating official IEEE/ICRA brand assets in a later revision (none are copied in this draft).

## Evidence and caveats

Based on the two organizer-provided pre-proposals:

- Proposal #95: *Robotic Manipulation Beyond Vision and Language: Learning to See, Hear, Smell, Feel, and Act like Humans*; proposes a half-day workshop with invited talks, spotlights, posters/demos, non-archival recent-work option, and early-career engagement.
- Proposal #3: *Closing the Loop: Task-Driven Multimodal Sensing, Perception, and Manipulation for Robotics*; proposes a half-day format with three talks, spotlights, poster/demos, panel, and explicit closed-loop perception/uncertainty framing.

The site paraphrases their compatible research directions; **the scientific merger text is not an officially approved abstract**. The proposed speaker names listed in one pre-proposal are **not** shown because their participation is not confirmed.

Official dates/source: https://2027.ieee-icra.org/contribute/call-for-workshop-and-tutorial/
- Full proposal due **November 2, 2026** via PaperPlaza.
- Workshop decisions announced **January 31, 2027**.
- Workshops/tutorials planned for **May 24 or May 28, 2027**.
- ICRA 2027 is in Seoul, South Korea.

**Do not confuse the November 2 deadline to submit the workshop proposal with a deadline for workshop *papers*.** No paper deadline has yet been set here.

## Design and accessibility

- Simple conference layout inspired by [CV4DC 2026](https://cv4dc.github.io/2026/): an illustrated SVG banner, dark navigation, and a white content area with a dates sidebar.
- Responsive single-column layouts on phones; main content and a sidebar on desktops.
- Each navigation item opens its own HTML page, with the current page highlighted.
- Skip-to-content, always-visible keyboard-operable navigation, visible focus, semantic sections and headings, reduced-motion support.
- No external fonts, trackers, cookies, embeds, or required JavaScript for content.
- All workshop content is a working draft for substantial revision. The header identifies the workshop as proposed, and the CFP states that submissions are not open yet.
- Speakers, organizers, contact details, the assigned workshop session, submission platform, paper dates, formats, review criteria, and publication policy use explicit `TBD` placeholders. Official ICRA conference dates remain listed separately.
