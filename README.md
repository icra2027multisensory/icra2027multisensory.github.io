# ICRA 2027 Workshop Website — Draft v0.1

An accessible, responsive, dependency-free static website and draft Call for Papers for the **proposed** merged ICRA 2027 half-day workshop.

## Included files

- `index.html` — homepage: scientific framing, research topics, tentative program, speaker placeholders, organizing team.
- `cfp.html` — **draft only** CFP, topics, contribution types, and pending submission requirements.
- `styles.css` — responsive design.
- `script.js` — accessible mobile navigation.
- `assets/favicon.svg` — abstract loop mark.
- `.nojekyll` — GitHub Pages compatibility.

## Preview locally

Run `python3 -m http.server 8000` in this folder, then open `http://localhost:8000`.

## Publish through GitHub Pages

1. Create a **new, separate** public GitHub repository, e.g. `icra2027-multisensory-workshop` (do not place this under an unrelated research repository).
2. Upload everything in this folder to its `main` branch, preserving the directory structure.
3. Go to repository **Settings → Pages → Build and deployment**. Choose **Deploy from a branch**, **main**, **/(root)**, then save.
4. Open the URL GitHub shows. HTTPS may take some time to become available.
5. Once officially accepted and approved for public advertising, update all draft text and remove the `noindex, nofollow` tags from **both** HTML pages so search engines can find it.

The project uses plain HTML/CSS/JS and requires no npm install, build, framework, hosting plan, or API key.

## REQUIRED APPROVALS BEFORE ANNOUNCEMENT

- [ ] Choose the **final title**; currently an explicitly labeled working title.
- [ ] Confirm the workshop is **accepted**, and update status/banner language only after the conference decision.
- [ ] Confirm which day (May 24 **or** May 28) and actual half-day time slot; do not imply a specific room.
- [ ] Approve the merged abstract/topic descriptions with Hanyi and Jian.
- [ ] Finalize speaker names, institutions, talk titles **and acceptance** before replacing anonymous placeholders.
- [ ] Finalize organizing team roster and assigned roles (workshop co-chairs, faculty advisors, student organizers); add a separate PC section if appropriate.
- [ ] Set the final program format and timetable; the 240-minute allocation on the homepage is *illustrative*.
- [ ] Decide which contribution types to accept, short/full paper lengths, whether recently published papers are welcome, archival or non-archival proceedings policy, reviewer criteria, and publication/hosting policies.
- [ ] Confirm submission platform, paper deadline, acceptance notification, camera-ready deadline (if applicable), and exact times/timezones.
- [ ] Approve a public organizer contact email or contact form; **do not expose private addresses** without permission.
- [ ] Replace the CFP warning and noindex only once author submissions can be received and team approves release.
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

- Responsive single-column layouts on phones; four-column grids on desktops.
- Skip-to-content, keyboard-operable nav, visible focus, semantic sections and headings, reduced-motion support.
- No external fonts, trackers, cookies, embeds, or required JavaScript for content.
- Provisional-status text is deliberately prominent, including on the CFP page.