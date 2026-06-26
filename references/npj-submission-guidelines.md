# NPJ Computational Materials submission guidelines

Source: Nature `npj Computational Materials` submission guidelines.

URL: https://www.nature.com/npjcompumats/for-authors-and-referees/submission-guidelines

Accessed: 2026-06-26.

Use this reference for submission readiness. It summarizes current official requirements and must override corpus-derived style preferences when preparing a manuscript, cover letter, figures, supplementary information, data/code availability, statistics, chemical characterization, and computational-result reporting.

## Submission and policy gates

- Submit manuscripts through the journal online submission system.
- Do not submit a revision as a new manuscript.
- Review editorial policies before submission.
- Large language models do not satisfy authorship criteria. If an LLM was used, document the use in the Methods section, or another suitable section if there is no Methods section.
- The corresponding author is responsible for coauthor communication, author list/order agreement, and submission awareness.
- Corresponding authors must provide ORCID before final manuscript submission after acceptance; non-corresponding authors are encouraged to link ORCID.
- Submission implies no significant overlap with work by the same authors under consideration or in press elsewhere. Related manuscripts with overlapping authorship must be supplied or disclosed.
- If related work is submitted elsewhere during review, send a copy to the Editor.
- Permission is required for quoted personal communications.

## Cover letter

Require a cover letter with corresponding-author affiliation and contact information.

The cover letter should:

- explain the context, importance and journal fit of the work
- avoid repeating the abstract and Introduction
- disclose confidential information such as conflicts of interest
- declare related work in press or under consideration
- optionally suggest or exclude referees
- consider diversity in reviewer suggestions

## Initial manuscript format

- Initial submissions do not need to follow final formatting requirements.
- A single PDF or Word file containing manuscript text and figures is encouraged at initial submission.
- Figures may be inserted in the text or grouped at the end, provided they are legible.
- Figure legends should be on the same page as their figures for initial review when possible.
- LaTeX files may be accepted at the acceptance stage; before that, supply compiled PDFs.
- npj Series articles are not deeply copyedited or redrawn by production; submission-ready language and figure quality remain the authors' responsibility.

## Methods

Methods must be reproducible and sufficiently detailed for interpretation and replication.

Require:

- short Methods subheadings
- adequate experimental and characterization information
- standard protocols and experimental procedures
- suppliers of reagents, instrumentation and kits where applicable
- synthesis protocols for compounds when synthesis is reported
- reagent amounts in parentheses where possible
- safety hazards for reagents or protocols
- isolated mass and percent yield at the end of protocols when applicable
- specific sections for statistics and reproducibility where statistical testing is used
- no reliance on Supplementary Methods; all Methods must be in the main manuscript file

For the current 2PI computational manuscript, Methods should additionally include:

- molecule and dataset provenance
- standardization, deduplication and split construction
- target definitions and missing-label handling
- model architecture, hyperparameters and random seeds
- scaffold-disjoint split and leakage checks
- prediction disagreement and applicability-domain procedures
- ZINC22 snapshot, filtering, and watchlist construction
- mechanism taxonomy and exclusion rules
- candidate aggregation and fixed pre-QM portfolio rules
- Gaussian/QM settings, charge, spin, solvent model, functional, basis set, convergence policy and failure handling
- LLM-use disclosure if Codex or another LLM contributed to writing, analysis, code or decision support

## References

- References are numbered sequentially in the order they appear in text, Methods, tables and figure legends.
- Use one publication per reference number.
- Include only published work, accepted work, recognized preprints, published conference abstracts, numbered patents, research datasets, or other allowed source types.
- Papers in preparation and unpublished meeting abstracts should be mentioned in text, not listed as numbered references.
- Dataset citations should include DOI or accession code when available.
- Website URLs should usually be cited parenthetically in the text rather than added to the reference list, except for formal peer-reviewed online journals.
- Grant details and acknowledgments must not be numbered references.
- Footnotes are not used.
- Use standard Nature reference style.
- If a cited work has more than five authors, list first author followed by `et al.`.

## Author contributions acknowledgements and competing interests

- Author contributions statement is required and should specify individual contributions using author initials.
- Acknowledgements should be brief.
- Funding belongs in Acknowledgements, not in a separate Funding section.
- State the role of each funder in study design, data collection, analysis, interpretation and writing; if no role, state that.
- If no funding was received, state that.
- Competing interests statement is required for all accepted papers, including a no-competing-interests statement when applicable.

## Data availability

The manuscript must include a Data Availability section after Methods and before References.

The statement should identify the minimal dataset required to interpret, replicate and build on the methods or findings.

For the current 2PI manuscript, plan to specify availability of:

- training and validation datasets or their allowed derivatives
- DOI and metadata tables
- molecular identifiers, SMILES and standardization rules
- train/validation/test and scaffold-split assignments
- ZINC22 snapshot or query/filter definitions
- screened watchlist tables and candidate portfolios
- QM input/output summaries, coordinates and failure logs where shareable
- figure source data where applicable

If a dataset cannot be public, state the reason and access route.

## Code availability

Previously unreported custom code or scripts central to main claims must be available to Editors and referees on request.

At publication, code release that enables repeatability is considered best practice.

For studies using central custom code, include a `Code availability` statement in Methods, indicating access route and restrictions.

For the current 2PI manuscript, plan to identify:

- model training and inference code
- preprocessing and standardization scripts
- split construction scripts
- ZINC22 filtering and taxonomy code
- portfolio selection scripts
- QM parsing and audit scripts
- software versions and environment files

## Supplementary information

- Supplementary Information is sent to referees and published with accepted manuscripts.
- Avoid `data not shown`; data supporting claims should be deposited or supplied.
- Supplementary Information should be a separate, single merged PDF.
- The journal does not permit Supplementary Methods; all Methods must be reported in the main manuscript file.
- Remove tracked changes before final submission.
- Large supplementary tables or Excel files should be supplied as `Supplementary Data`, not `Supplementary Table`.
- Supplementary Data files need corresponding titles and legends in the Supplementary Information PDF and must be cited consistently.

## Figures and tables

Figures:

- Authors are responsible for permissions for reused or protected figures.
- Avoid unnecessary figures.
- Multi-panel figures should contain only logically connected panels.
- Number figures with Arabic numerals in order of text occurrence.
- Include error bars where appropriate and define the error treatment in legends.
- Chemical reactions and experimental sequences should be submitted as figures, not schemes.
- Use a consistent sans-serif typeface such as Arial or Helvetica.
- Use a white background and avoid decorative or low-resolution effects.
- Do not truncate histogram axes to exaggerate small differences.
- Use readable labels, SI units, scale bars where relevant, and defined abbreviations.
- Use colorblind-accessible palettes; avoid arbitrary red-green contrasts and rainbow scales.
- For publication, supply each complete figure as a separate file; multi-panel figures should be arranged as a single file, not uploaded panel-by-panel.
- Supply RGB color and at least 300 dpi for image files.
- Prefer editable vector or layered files where possible.
- ChemDraw `.cdx` is accepted for chemical structures.

Figure legends:

- Begin with a brief title for the whole figure.
- Then describe each panel and symbol.
- Emphasize what is shown rather than detailed Methods.
- Define error bars, abbreviations, symbols and colors.
- Cite figures in text order.
- Legend body is limited to 350 words.
- Add figure legends in the main manuscript file after References.
- Multi-panel labels use the `a), b), c)` convention and each panel should be described individually.

Tables:

- Submit tables at the end of the text document.
- Tables containing statistical analyses should describe error-analysis standards and ranges in the table legend.

## Figures for peer review and publication

- At initial submission, incorporate figures into the main article file when possible and keep them legible.
- If a combined manuscript file is not workable, submit separate high-resolution figure files or deposit image data in a suitable repository with private reviewer access.
- At final manuscript stage, upload all figures as separate files meeting publication quality requirements.
- Poor figure quality can delay publication.

## Video figures

- Video figures may be submitted to support the research.
- Individual video figure size limit is 150 MB.
- Total combined file size for all content should not exceed 1 GB.
- If a video is part of a multipart figure, the whole figure must be submitted as a video.

## Statistics and reproducibility

Methods must include a statistics and reproducibility section when statistical analysis is used.

Report:

- statistical test name
- n value for each analysis
- comparisons of interest
- justification for the test
- alpha level
- one-tailed or two-tailed status
- actual P value, not only thresholded significance
- descriptive statistics including n, centre and variability
- whether ± is standard error or standard deviation
- error-bar definitions in graphs
- treatment of multiple comparisons
- normality testing or non-parametric alternatives when assumptions fail
- small-sample justification when sample size is below about 10

Avoid using `significant` without a P value. Prefer `substantial` or similar language when no statistical test supports significance.

## Chemical and biomolecular characterization

The manuscript must provide adequate evidence for identity, purity and homogeneity of compounds and materials.

For known compounds or biomolecules central to the study, include a statement of source, identity and purity, even if purchased or resynthesized.

Chemical nomenclature:

- Identify molecular structures by bold Arabic numerals in order of presentation.
- Use systematic IUPAC name, defined standard abbreviation, or bold numeral consistently.
- Define unconventional or specialist abbreviations at first use.

For synthesized compounds:

- include synthesis protocols in Methods
- give commercial source of compounds
- identify safety hazards
- report isolated mass and percent yield
- quantify inseparable isomeric ratios where possible
- establish identity by appropriate spectroscopy
- provide purity evidence for each isolated compound
- report melting points for crystalline compounds where relevant
- state when species are not isolated or fully characterized

Spectroscopy and structure:

- Provide standard peak listings for proton and proton-decoupled carbon NMR.
- Include other NMR nuclei when appropriate.
- Provide UV or IR spectral data when relevant.
- Provide mass spectral evidence; HRMS is preferred for small molecules.
- For single-crystal XRD, provide CIF, structure factors, CheckCIF output, and explain serious alerts.
- Deposit crystallographic data in the appropriate database when required.
- For solid-state compounds, use appropriate solid-state characterization such as solid-state NMR or powder XRD.

## Computational results

For electronic-structure calculations:

- provide atomic coordinates of optimized computational models
- make codes and software available and cite them properly
- report input parameters, basis sets and coordinates of input and output structures
- if relative energies are reported, provide absolute energies in Supplementary Information

For molecular dynamics:

- supply at least initial and final configurations
- preferably deposit trajectories or structures in an appropriate data repository
- otherwise supply them as supplementary data, ideally plain text

For the current 2PI/QM manuscript, this means QM reporting must include enough information to reproduce lane-specific calculations, not only summarized energy or orbital values.

## Submission readiness checklist for the 2PI manuscript

Before submission, verify:

- LLM use is documented if applicable.
- Cover letter states journal fit without repeating Abstract or Introduction.
- Methods include all ML, ZINC22, taxonomy, portfolio and QM details in the main manuscript file.
- No Supplementary Methods are used.
- Data Availability section exists after Methods and before References.
- Code availability statement exists when custom code supports central claims.
- Figures use accessible colors, readable labels, 300 dpi or vector format, and text-order numbering.
- Figure legends appear after References and are no more than 350 words.
- Statistical claims include tests, n, P values, assumptions and error definitions where applicable.
- Chemical compounds and purchased molecules have source, identity and purity information where central.
- QM calculations provide software, basis sets, input/output coordinates and absolute energies where needed.
- References are sequentially numbered and follow Nature style.
