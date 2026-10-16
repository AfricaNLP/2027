# AfricaNLP 2027

Website for the 8th Workshop on African Natural Language Processing, accepted as a
one-day hybrid workshop at EACL 2027 in Athens, Greece (9-14 March 2027).

Repo: https://github.com/AfricaNLP/2027 (private during review)
Pages URL once public: https://africanlp.github.io/2027/

Plain static HTML. No build step, no dependencies, no JavaScript. Edit a file,
commit, and GitHub Pages republishes.

## Pages

| File | Page |
| --- | --- |
| `home.html` | Home: news, about, at a glance, previous editions |
| `index.html` | Redirect to `home`, so the bare directory URL works |
| `cfp.html` | Call for papers |
| `dates.html` | Important dates |
| `speakers.html` | Invited speakers |
| `shared-task.html` | Shared task |
| `mentorship.html` | Mentorship and participation support |
| `attending.html` | Registration, visas, joining remotely |
| `organizers.html` | Organizers |
| `committee.html` | Programme committee |
| `volunteers.html` | Student volunteers |
| `sponsors.html` | Sponsors |
| `contact.html` | Contact |

Shared files: `styles.css`, `assets/band.webp` (the header frieze),
`assets/people/` (organizer photos), `assets/logo.webp`, `favicon.png`.

## Editing

- **Deadlines**: fill the table in `dates.html` as EACL confirms the workshop timeline.
- **News**: add a row to the table at the top of `index.html`, newest first.
- **Committee**: add `<li>Name, Affiliation</li>` to the list in `committee.html`.
- **Organizer photos**: `assets/people/` holds one 400x400 JPG per organizer, reused
  from the AfricaNLP 2026 site, except Seid Muhie Yimam, whose photo is his GitHub
  profile picture. To replace any of them, overwrite the file keeping the same name.
- **Adding a page**: copy an existing file, change the title and body, then add the
  link to the `<p class="nav">` block in every page. The nav is duplicated in each
  file on purpose, so that the site needs no build tooling.
- **Accepted papers and schedule**: add `schedule.html`, `papers-archival.html` and
  `papers-non-archival.html` the same way once review is complete.

## Local preview

    python3 serve.py

Then open http://127.0.0.1:4027

`serve.py` resolves `/cfp` to `cfp.html`, which is what GitHub Pages does. Plain
`python3 -m http.server` will 404 on the extensionless links.

## Credits

Logo and favicon: the Africa panel cropped from the same pattern illustration.
Organizer photographs: reused from the AfricaNLP 2026 workshop site.

Header frieze cropped from a flat African pattern illustration. Confirm the licence
terms of the source and add attribution here before publishing if it requires it.
