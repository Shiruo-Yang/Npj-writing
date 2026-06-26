---
name: npj-writing
description: "NPJ Computational Materials writing and revision guidance for materials-informatics, machine-learning materials discovery, high-throughput screening, applicability-domain/OOD validation, and 2PI photoinitiator manuscripts. Use when drafting, restructuring, polishing, or auditing manuscript sections, cover letters, Methods, figures, supplementary information, data/code availability, statistics, computational reporting, or submission readiness."
---

# NPJ Writing

Use this skill to draft, restructure, polish, or audit manuscripts intended to resemble the argumentative style and evidentiary discipline of `npj Computational Materials`.

The skill is about target-journal writing structure and evidentiary scale. It must not substitute for domain facts, photochemistry mechanism evidence, 2PA measurement literature, quantum-chemical outputs, or experimental validation.

## Required Reading Order

1. `references/npj-official-rules-summary.md`
2. `references/npj-submission-guidelines.md`
3. `references/writing-playbook.md`
4. `references/paperlocus-derived-npj-writing-standards.md`

Official journal rules and current submission guidelines override corpus-derived style observations. Use the corpus to learn argument scale and section rhythm, not to relax submission requirements.

## Workflow

1. Identify the writing task: title, abstract, introduction, Results, Discussion, Methods, figure legends, limitations, or full-paper positioning.
2. Separate evidence roles:
   - writing-style corpus
   - domain fact corpus
   - ML/QM method corpus
3. Build the manuscript around a restrained discovery chain:
   - large-space candidate screening
   - model confidence and applicability-domain control
   - mechanism-aware filtering
   - physics-based or quantum-mechanical triage
   - candidate positioning without unsupported experimental claims
4. Produce a concrete output: revised text, section outline, claim-evidence table, or submission-readiness checklist.

## Defaults

- Title: state the object, method, and claim level without promising deployment.
- Abstract: for an NPJ Article, use one unheaded paragraph of no more than 150 words.
- Introduction: no subheadings; move from domain bottleneck to mechanism-aware validation need.
- Results: use subheadings and organize by evidence modules.
- Discussion: no subheadings; do not create separate Limitations or Conclusions sections.
- Methods: use subheadings and provide reproducible data, model, screening, and QM details in the main manuscript file.

## Submission Readiness

For submission-readiness audits, apply `references/npj-submission-guidelines.md` and check at minimum:

- LLM use is disclosed in Methods or another suitable section when applicable.
- The cover letter gives journal fit, corresponding-author information, related-work disclosures, conflicts, and reviewer suggestions or exclusions if used.
- Data Availability appears after Methods and before References.
- Code availability is included when central custom code or scripts support the claims.
- Supplementary Information is a single merged PDF where possible; do not create Supplementary Methods.
- Methods include statistics and reproducibility details where statistical testing is used.
- Central compounds have source, identity, purity, nomenclature and characterization support.
- Computational results include software, input parameters, basis sets, input/output coordinates, optimized-model coordinates, and absolute energies where relative energies are reported.
- Figures are legible, accessible, permission-clean, numbered in text order, and supplied as complete figure files; legends are no more than 350 words and placed after References.

## Guardrails

- Do not mix style-corpus papers with domain-evidence papers.
- Do not present model scores as chemical truth.
- Do not collapse Type-I, Type-II, SET/PET, cationic, mixed-mode, and unresolved systems into a single photoinitiator ranking.
- Do not describe computational candidates as validated leads without synthesis and photopolymerization evidence.
- Do not leave central Methods details only in Supplementary Information.
- Do not omit Data Availability, Code availability, author contributions, acknowledgements/funding role, competing interests, or LLM-use disclosure when applicable.
- Preserve conservative language when evidence is computational-only.
