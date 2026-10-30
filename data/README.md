# Data dictionary

All CSV files have the same columns.

| Column | Unit | Meaning |
|---|---|---|
| `f_sw_kHz` | kHz | Carrier (switching) frequency of the run |
| `leakage_mA` | mA | RMS current through the parasitic capacitance Cpv |
| `efficiency_pct` | % | Pout / Pin from the DC input and AC output power (empty if not recorded) |
| `thd_pct` | % | Low-order THD of the load voltage from the Powergui FFT (harmonic orders up to the limit in the settings below) |

## Files

| File | Case | Points | Notes |
|---|---|---|---|
| `h4_unipolar.csv` | H4, unipolar SPWM | 27 | Vdc 220 V, L1=L2 90 mH, RL 50 Ω, MOSFET, stop time 0.08 s. Source sheet stores Hz and A; converted here. |
| `h4_bipolar.csv` | H4, bipolar SPWM | 25 | Vdc 460 V, L1=L2 10 mH, RL 10 Ω, MOSFET, THD window from 0.01 s to 4 cycles |
| `heric_unipolar.csv` | HERIC, unipolar SPWM | 25 | Vdc 220 V, L1=L2 10 mH, RL 10.68 Ω, IGBT, stop time 0.05 s, FFT max order 2000 Hz |
| `heric_bipolar.csv` | HERIC, bipolar SPWM | 40 | Same circuit; no efficiency recorded; FFT max frequency 10 kHz in the sheet header |
| `h4_bipolar_load_variation_supplementary.csv` | H4 bipolar, RLC load (R=100 Ω, C=1 µF, L=10 mH) | 39 | Supplementary run, not used in the manuscript. Efficiency collapses above 21 kHz and should be checked before anyone relies on it. |
| `all_cases_combined.csv` | the four manuscript cases | 117 | Long format with a `case` column |

Raw settings text for each case is kept in the header cell of the matching sheet in `raw/thesis_data_all_sweeps.xlsx`. `raw/unipolar_heric_data.xlsx` is the same HERIC unipolar series as a standalone file.

## Known gaps (fix before the Zenodo release)

1. **H4 bipolar, 12 kHz row missing.** The manuscript reports a leakage peak of about 440 mA at 12 kHz (Fig. 6 shows it), but the workbook has no 12 kHz row (rows jump from 11 to 13 kHz). Add the measured leakage, efficiency and THD for 12 kHz to `raw/thesis_data_all_sweeps.xlsx` and rerun `scripts/build_csv.py`.
2. **Sheet `Sheet1` of the workbook** is an early HERIC run labelled 200 µF with leakage of 3–5 mA. It does not match the 150 nF setup of the paper and is not converted. Delete it from the workbook or keep it with a note.
3. Stop time for H4 bipolar is 0.1 s in the workbook and in the R2018a model but 0.08 s in the manuscript (Appendix C) and in the R2023a model. State which one produced the data.
