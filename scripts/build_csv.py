"""Convert the raw sweep workbook into tidy CSV files (one per case).

Unit handling:
  * UnipolarH4 sheet stores f_sw in Hz and leakage in A  -> converted to kHz and mA
  * Bipolar H4 Load Varry stores leakage in A and has text such as '5.5 kH' -> cleaned
Output columns: f_sw_kHz, leakage_mA, efficiency_pct, thd_pct (blank = not recorded)
"""
import re
from pathlib import Path
import openpyxl
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "raw" / "thesis_data_all_sweeps.xlsx"
OUT = ROOT / "data"

# sheet -> (output name, f_sw unit, leakage unit, column order after f_sw)
SHEETS = {
    "UnipolarH4":              ("h4_unipolar",            "Hz",  "A",  ["eff", "leak", "thd"]),
    "Bipolar H4":              ("h4_bipolar",             "kHz", "mA", ["eff", "leak", "thd"]),
    "Unipolar Heric":          ("heric_unipolar",         "kHz", "mA", ["eff", "leak", "thd"]),
    "Bipolar Heric":           ("heric_bipolar",          "kHz", "mA", ["leak", "thd"]),
    "Bipolar H4 Load Varry":   ("h4_bipolar_load_variation_supplementary", "kHz", "A", ["eff", "leak", "thd"]),
}

def num(x):
    if x is None:
        return None
    if isinstance(x, (int, float)):
        return float(x)
    m = re.search(r"[-+]?\d*\.?\d+", str(x))
    return float(m.group()) if m else None

def main():
    wb = openpyxl.load_workbook(SRC, data_only=True)
    frames = []
    for sheet, (name, fu, lu, cols) in SHEETS.items():
        ws = wb[sheet]
        rows = []
        for r in ws.iter_rows(min_row=2, values_only=True):
            vals = r[4:4 + 1 + len(cols)]
            f = num(vals[0])
            if f is None:
                continue
            d = {"f_sw_kHz": f / 1000 if fu == "Hz" else f}
            for c, v in zip(cols, vals[1:]):
                d[c] = num(v)
            rows.append(d)
        df = pd.DataFrame(rows)
        df["leakage_mA"] = df["leak"] * (1000 if lu == "A" else 1)
        df["efficiency_pct"] = df["eff"] if "eff" in df else float("nan")
        df["thd_pct"] = df["thd"]
        df = df[["f_sw_kHz", "leakage_mA", "efficiency_pct", "thd_pct"]].sort_values("f_sw_kHz")
        df.to_csv(OUT / f"{name}.csv", index=False)
        d2 = df.copy(); d2.insert(0, "case", name)
        frames.append(d2[~d2["case"].str.contains("supplementary")])
        print(f"{name}.csv  {len(df)} points  f_sw {df.f_sw_kHz.min():g}-{df.f_sw_kHz.max():g} kHz")
    pd.concat(frames).to_csv(OUT / "all_cases_combined.csv", index=False)

if __name__ == "__main__":
    main()
