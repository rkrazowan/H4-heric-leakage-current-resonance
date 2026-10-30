# h4-heric-leakage-current-resonance

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

**Simulink models, sweep data and analysis scripts for: "Switching-frequency-dependent leakage current in H4 and HERIC transformerless PV inverters: a common-mode resonance perspective"**

Transformerless single-phase PV inverters have no galvanic isolation, so the switching common-mode voltage can drive a leakage current through the parasitic capacitance between the PV array and ground. This repository holds the data behind a study of how the **switching frequency interacts with the common-mode resonance** formed by the output-filter inductance and the parasitic capacitance (150 nF), for four cases: H4 and HERIC, each with unipolar and bipolar SPWM, swept from 1 to 40 kHz.

> Replace `XXXXXXX` in the badge above and in the files listed in `docs/PUBLISHING_STEPS.md` once Zenodo has issued the DOI.

## Repository layout

| Path | Content |
|---|---|
| `data/*.csv` | Cleaned sweep results, one file per case: `f_sw_kHz, leakage_mA, efficiency_pct, thd_pct` |
| `data/all_cases_combined.csv` | The four manuscript cases in one long table |
| `data/raw/` | Original Excel workbooks with the simulation settings recorded in each sheet |
| `data/README.md` | Data dictionary, units, per-case parameters, known gaps |
| `models/` | MATLAB/Simulink models (H4 bipolar). See `models/README.md` |
| `scripts/build_csv.py` | Raw workbook -> CSV (unit conversion Hz->kHz, A->mA) |
| `scripts/analyze_resonance.py` | Predicted f_res = 1/(2π√(L_eq·C_pv)), peak detection, deviation table, 300 mA check |
| `scripts/plot_sweeps.py` | Redraws leakage / efficiency / THD versus switching frequency |
| `results/` | Output of the scripts (resonance table and sweep plots) |
| `manuscript/` | LaTeX source of the paper (preprint; see licence note) |
| `docs/` | Data availability statement, Zenodo/GitHub publishing steps, reproducibility notes |

## Cases and parameters

| Case | Vdc (V) | L1 = L2 | RL (Ω) | Cpv | Sweep (kHz) | f_res (kHz) |
|---|---|---|---|---|---|---|
| H4, unipolar SPWM | 220 | 90 mH | 50 | 150 nF | 1–25 | 1.94 |
| H4, bipolar SPWM | 460 | 10 mH | 10 | 150 nF | 1–40 | 5.81 |
| HERIC, unipolar SPWM | 220 | 10 mH | 10.68 | 150 nF | 5–30 | 5.81 |
| HERIC, bipolar SPWM | 220 | 10 mH | 10.68 | 150 nF | 5–35 | 5.81 |

Common to all cases: DC-link 0.94 F with 0.049 Ω series resistance, continuous Powergui solver, parasitic capacitance between the negative DC rail and ground.

## Quick start

```bash
git clone https://github.com/<your-username>/h4-heric-leakage-current-resonance.git
cd h4-heric-leakage-current-resonance
pip install -r requirements.txt
python scripts/build_csv.py          # regenerate data/*.csv from data/raw/
python scripts/analyze_resonance.py  # writes results/resonance_table.csv
python scripts/plot_sweeps.py        # writes results/sweep_*.png
```

To rerun a simulation, open a model from `models/` in MATLAB/Simulink with Simscape Electrical, set the carrier frequency, run, and read the RMS current through the 150 nF capacitor. Details are in `models/README.md`.

## Licence

* Scripts: MIT (`LICENSE`).
* Data, models and figures in `data/`, `models/`, `results/`: CC BY 4.0 (`LICENSE-DATA.md`).
* `manuscript/`: the authors' preprint source, all rights reserved; it is provided for transparency and is not covered by the licences above. Class and style files keep their own licences.

## How to cite

Cite the Zenodo record (DOI above) and, once published, the journal article. See `CITATION.cff`.

## Authors

Razowan Kabir (corresponding author; Khulna University of Engineering and Technology), Mridha Raju (KUET), Mursida Khatun, Pantho Mondal, Tanzim Khan, Rabiul Islam, A.T.M. Saiful Islam (Gopalganj Science and Technology University). Contact: rkrazowan@gmail.com.
