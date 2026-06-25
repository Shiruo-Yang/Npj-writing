# PaperLocus derived NPJ writing standards

This file condenses whole-paper reading of representative `npj Computational Materials` papers into reusable writing standards.

## Scope

Use journal-style corpus papers for writing structure, not as evidence for domain-specific scientific facts.

For a mechanism-aware photoinitiator manuscript, keep these roles separate:

- writing corpus: style, structure, claim scale
- 2PI corpus: photochemistry and two-photon polymerization facts
- ML/QM corpus: methods, benchmark, dataset, uncertainty, applicability domain, and reproducibility positioning

## Core narrative

The manuscript should read as a method-led scientific Article:

1. Define a discovery bottleneck.
2. Show why raw ML ranking is insufficient.
3. Add reliability, applicability-domain, disagreement, and mechanism controls.
4. Screen a large accessible space.
5. Separate incompatible initiation modes.
6. Use QM as lane-specific triage.
7. Conclude with computational priorities pending experimental validation.

## Section standards for a 2PI manuscript

Introduction:

1. 2PP bottleneck and the role of radical photoinitiators.
2. Mechanism ambiguity across Type-I, Type-II, SET/PET, cationic, mixed-mode, and unresolved systems.
3. ML opportunity and the risk of property-only ranking.
4. Large purchasable chemical space as a mechanism-annotation problem.
5. Contribution statement with conservative computational claims.

Results:

- Define a mechanism-aware screening problem.
- Show scaffold-disjoint model behavior and audit constraints.
- Show large-space screening and mechanism heterogeneity.
- Separate radical initiation routes with role-aware taxonomy.
- Use family-balanced portfolios to avoid cross-mechanism ranking.
- Assign lane-specific quantum-mechanical validation routes.

Discussion:

Use no subheadings. Explain why separating optical prediction from mechanism qualification changes screening practice. State what QM supports and what still requires synthesis, 2PA measurement, radical generation, and photopolymerization tests.

Methods:

Minimum subheadings should cover data standardization, endpoint definitions, model training, scaffold split, disagreement, applicability domain, screening database construction, mechanism taxonomy, portfolio selection, QM calculations, and reproducibility.

## Claim language

Supported operations:

- `trained`
- `screened`
- `classified`
- `excluded`
- `selected`
- `calculated`
- `observed`

Moderate interpretations:

- `indicates`
- `prioritizes`
- `supports`
- `identifies`
- `constrains`

Unresolved or future-facing:

- `may`
- `could`
- `requires validation`
- `remains unresolved`

Avoid without experiments:

- `discovered photoinitiators`
- `validated 2PI performance`
- `mechanistically confirmed`
- `ready for application`
- `superior initiators`

