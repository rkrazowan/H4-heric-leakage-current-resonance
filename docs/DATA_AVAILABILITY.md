# Data availability statement

Paste one of these into the journal's "Data availability" field and into the manuscript
(`manuscript/sections/11_declarations_elsevier.tex` already contains option A with a placeholder DOI).
Replace `10.5281/zenodo.XXXXXXX` and `<your-username>` first.

## A. Recommended (Zenodo DOI)

> The Simulink models, the switching-frequency sweep data (CSV files and the original Excel workbook) and the Python scripts used to analyse them are openly available in Zenodo at https://doi.org/10.5281/zenodo.XXXXXXX (development repository: https://github.com/<your-username>/h4-heric-leakage-current-resonance).

## B. Short form

> Data and models are available at https://doi.org/10.5281/zenodo.XXXXXXX.

## C. LaTeX (as used in the manuscript)

```latex
\section*{Data availability}
The Simulink models, the switching-frequency sweep data (CSV files and the original Excel workbook)
and the Python scripts used to analyse them are openly available in Zenodo at
https://doi.org/10.5281/zenodo.XXXXXXX (development repository:
https://github.com/<your-username>/h4-heric-leakage-current-resonance).
```

## D. Only if you cannot deposit everything

> The sweep data supporting the findings are openly available at https://doi.org/10.5281/zenodo.XXXXXXX. The Simulink models for <list cases> are available from the corresponding author on reasonable request.

Use D only if some models stay out of the repository. Do not use A while three of the four models are missing.

## Which DOI to cite

Zenodo issues two DOIs for a GitHub-archived repository: a *version* DOI (this exact release) and a *concept* DOI (always the latest version). For a statement tied to the published results, cite the **version DOI** of release v1.0.0.
