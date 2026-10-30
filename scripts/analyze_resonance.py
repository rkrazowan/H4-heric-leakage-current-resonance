"""Predicted CM resonance f_res = 1/(2*pi*sqrt(L_eq*C_pv)), L_eq = L/2 (L1 = L2 = L),
and comparison with the leakage-current peaks found in the sweeps.

Peak = local maximum of leakage vs f_sw that exceeds both neighbours and is at least
`MIN_PEAK_MA` mA. Deviation = |f_peak - f_pred| / f_pred, with f_pred the nearest of
f_res, f_res/2, f_res/3, 2 f_res (same definition as the manuscript).
"""
from math import pi, sqrt
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CPV = 150e-9
MIN_PEAK_MA = 100.0
CASES = {  # name: (L1 = L2 in H)
    "h4_unipolar": 90e-3,
    "h4_bipolar": 10e-3,
    "heric_unipolar": 10e-3,
    "heric_bipolar": 10e-3,
}

def f_res_khz(L):
    return 1 / (2 * pi * sqrt((L / 2) * CPV)) / 1000

def peaks(df, thr):
    out = []
    y = df["leakage_mA"].values; x = df["f_sw_kHz"].values
    for i in range(len(y)):
        left = y[i - 1] if i > 0 else -1
        right = y[i + 1] if i < len(y) - 1 else -1
        if y[i] >= thr and y[i] > left and y[i] > right:
            out.append((x[i], y[i]))
    return out

def main():
    rows = []
    for case, L in CASES.items():
        df = pd.read_csv(ROOT / "data" / f"{case}.csv")
        fr = f_res_khz(L)
        thr = 10.0 if case == "heric_bipolar" else MIN_PEAK_MA
        for fp, ip in peaks(df, thr):
            cands = {"f_res": fr, "f_res/2": fr / 2, "f_res/3": fr / 3, "2 f_res": 2 * fr}
            rel, fpred = min(cands.items(), key=lambda kv: abs(fp - kv[1]))
            rows.append(dict(case=case, f_res_kHz=round(fr, 2), peak_kHz=fp, peak_mA=ip,
                             nearest=rel, f_pred_kHz=round(fpred, 2),
                             deviation_pct=round(100 * abs(fp - fpred) / fpred, 1)))
        lim = df[df.leakage_mA > 300]
        print(f"{case}: f_res = {fr:.2f} kHz; samples above 300 mA: "
              f"{', '.join(f'{a:g} kHz' for a in lim.f_sw_kHz) or 'none'}")
    res = pd.DataFrame(rows)
    res.to_csv(ROOT / "results" / "resonance_table.csv", index=False)
    print(res.to_string(index=False))

if __name__ == "__main__":
    main()
