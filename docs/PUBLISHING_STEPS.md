# GitHub + Zenodo: step by step

## Before you upload (checklist)

- [ ] Add the three missing Simulink models (H4 unipolar, HERIC unipolar, HERIC bipolar) to `models/` and fill the table in `models/README.md`.
- [ ] Add the missing 12 kHz row of the H4 bipolar sweep to `data/raw/thesis_data_all_sweeps.xlsx`, then run `python scripts/build_csv.py`.
- [ ] Decide which stop time (0.1 s or 0.08 s) produced the H4 bipolar data and say so in `data/README.md`.
- [ ] Confirm the author list, affiliations and add ORCIDs to `CITATION.cff` and `.zenodo.json` if the co-authors have them.
- [ ] Decide whether `manuscript/` should be public before submission. It can be deleted from the repository without affecting anything else.
- [ ] Replace `<your-username>` in `README.md` and `CITATION.cff`.

## 1. GitHub

1. github.com > New repository. Name: `h4-heric-leakage-current-resonance`. Public. Do not tick "add README" (this folder has one).
2. About box (gear icon). Description: *Simulink models, sweep data and scripts: switching-frequency-dependent leakage current in H4 and HERIC transformerless PV inverters (common-mode resonance).* Topics: `transformerless-inverter`, `photovoltaic`, `leakage-current`, `common-mode-voltage`, `heric`, `h4-inverter`, `simulink`, `power-electronics`.
3. From this folder:
   ```bash
   git init
   git add .
   git commit -m "Initial release: models, data, scripts"
   git branch -M main
   git remote add origin https://github.com/<your-username>/h4-heric-leakage-current-resonance.git
   git push -u origin main
   ```
   (No Git? Use the web upload: "Add file > Upload files". GitHub rejects single files over 100 MB; nothing here comes close.)

## 2. Connect Zenodo (do this before creating the release)

1. zenodo.org > log in with GitHub.
2. Account menu > GitHub. Press *Sync now*, then switch the toggle ON for `h4-heric-leakage-current-resonance`.

## 3. Release, which triggers the archive

1. GitHub repo > Releases > *Draft a new release*. Tag `v1.0.0`, title `v1.0.0`, short notes. Publish.
2. Within a few minutes Zenodo creates the record, using `.zenodo.json` for the metadata, and issues the DOIs.
3. Open the record on Zenodo and check title, authors, licence (CC BY 4.0) and files.

## 4. Put the DOI everywhere

Replace `10.5281/zenodo.XXXXXXX` in:

- `README.md` (badge)
- `CITATION.cff` (uncomment `doi:`)
- `manuscript/sections/11_declarations_elsevier.tex` and `11_acknowledgment_data.tex`
- the journal's Data availability field

Commit these edits. They do not alter the archived v1.0.0 snapshot, which is expected. If you want the DOI inside the archived files, cut `v1.0.1` after editing.

## 5. At submission

In the submission system's data-availability step, choose the option stating that data have been deposited in a repository, and paste statement A from `docs/DATA_AVAILABILITY.md`.
