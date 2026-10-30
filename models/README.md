# Simulink models

MATLAB/Simulink with Simscape Electrical (Powergui, continuous). Parameters below were read from the model files.

| File | Case | Saved with | Original file name |
|---|---|---|---|
| `h4_bipolar_R2018a.slx` | H4, bipolar SPWM | R2018a | `bipolarh4....slx` |
| `h4_bipolar_R2018a_export.slx.zip` | same model, R2018a export | R2018a | `bipolarh4.slx.r2018a.zip` |
| `h4_bipolar_R2023a.slx` | H4, bipolar SPWM | R2023a | `bipolarh41.slx` |
| *(to add)* `h4_unipolar_*.slx` | H4, unipolar SPWM | | |
| *(to add)* `heric_unipolar_*.slx` | HERIC, unipolar SPWM | | |
| *(to add)* `heric_bipolar_*.slx` | HERIC, bipolar SPWM | | |

**Only the H4 bipolar models were available when this repository was assembled.** The other three cases are in the paper, so add their `.slx` files here before publishing, otherwise the Data Availability statement overstates what is deposited.

## Parameters of the H4 bipolar model (read from the files)

* DC source 460 V; DC-link branch 0.049 Ω with 0.94 F
* Four `Mosfet` blocks: Ron 0.1 Ω, Lon 0, Rd 0.01 Ω, Rs 1e5 Ω, Cs inf
* Filter inductors 10 mH each; load 10 Ω; parasitic capacitor 150 nF
* Powergui: Continuous; solver `VariableStepAuto`, max step `auto`
* Stop time: 0.1 s (R2018a file), 0.08 s (R2023a file)

## Running a sweep

1. Open the model; set the carrier frequency in the triangular/pulse generator.
2. Run to the stop time; read the RMS current through the 150 nF capacitor, the DC and AC powers, and the Powergui FFT of the load voltage.
3. Repeat for each frequency and compare with `data/h4_bipolar.csv`.
