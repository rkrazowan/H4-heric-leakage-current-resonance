"""Redraw leakage / efficiency / THD versus switching frequency from the CSV files."""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "h4_unipolar": "H4, unipolar SPWM (Vdc=220 V, L1=L2=90 mH, RL=50 ohm)",
    "h4_bipolar": "H4, bipolar SPWM (Vdc=460 V, L1=L2=10 mH, RL=10 ohm)",
    "heric_unipolar": "HERIC, unipolar SPWM (Vdc=220 V, L1=L2=10 mH, RL=10.68 ohm)",
    "heric_bipolar": "HERIC, bipolar SPWM (Vdc=220 V, L1=L2=10 mH, RL=10.68 ohm)",
}

for case, title in CASES.items():
    df = pd.read_csv(ROOT / "data" / f"{case}.csv")
    cols = [("leakage_mA", "Leakage current (mA)"),
            ("efficiency_pct", "Efficiency (%)"),
            ("thd_pct", "Low-order THD (%)")]
    cols = [c for c in cols if df[c[0]].notna().any()]
    fig, axs = plt.subplots(len(cols), 1, figsize=(6.5, 2.2 * len(cols)), sharex=True)
    axs = [axs] if len(cols) == 1 else axs
    for ax, (c, lab) in zip(axs, cols):
        ax.plot(df.f_sw_kHz, df[c], "o-", ms=3)
        ax.set_ylabel(lab); ax.grid(alpha=.3)
    axs[0].axhline(300, color="r", ls="--", lw=.8)
    axs[0].set_title(title, fontsize=9)
    axs[-1].set_xlabel("Switching frequency (kHz)")
    fig.tight_layout()
    fig.savefig(ROOT / "results" / f"sweep_{case}.png", dpi=200)
    plt.close(fig)
    print("saved", case)
