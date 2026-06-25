# NPJ writing playbook

## Core manuscript logic

Frame a computational materials-discovery manuscript as a constrained evidence chain, not as a generic AI screening story.

Preferred chain:

1. Candidate space is large and chemically heterogeneous.
2. Direct experimental or high-level quantum-mechanical evaluation of every candidate is infeasible.
3. A model narrows the space, but raw model scores are not enough.
4. Applicability-domain, OOD, model disagreement, family balance, and mechanistic filters prevent overconfident extrapolation.
5. Quantum-mechanical or physics-based calculations evaluate a small, defensible subset.
6. The output is a prioritized candidate map, not final experimental proof.

## Title

Respect the 15-word Article limit. Prefer literal titles that name:

- the discovery object
- the method
- the claim level

Avoid titles that imply experimental deployment if the evidence is computational.

## Abstract

Use one paragraph of no more than 150 words for a final NPJ Article abstract.

Five moves:

1. Problem
2. Gap
3. Approach
4. Strongest evidence
5. Scoped implication

## Introduction

Use no subheadings.

Build a funnel:

1. Domain bottleneck.
2. Why a simple property target is insufficient.
3. Why ML helps but can mislead outside its domain.
4. Why prior work leaves a specific gap.
5. What this study contributes, stated conservatively.

## Results

Use informative subheadings. Organize by evidence modules:

- Data and task definition
- Model performance and calibration
- Applicability domain or OOD behavior
- High-throughput screening and family distribution
- Rule-based or mechanistic filtering
- Quantum-mechanical validation and candidate prioritization
- Representative molecules and controls

Each module should state the question, evidence, justified claim, and unresolved point.

## Discussion

Use no subheadings. Do not create separate Limitations or Conclusions sections.

Use Discussion to calibrate:

- why the workflow is credible for prioritization
- where extrapolation is still risky
- which candidate families are robust versus tentative
- what QM validates and what it does not validate
- what experiments are required before application claims
- how the workflow generalizes to related discovery tasks

## Methods

Use subheadings and write reproducible details in the main manuscript file:

- dataset provenance, cleaning, deduplication, splits, and target definitions
- molecular representation and model choices
- training, validation, uncertainty, and applicability-domain procedures
- screening database and filtering criteria
- taxonomy or mechanism rules
- quantum-mechanical settings and failure criteria
- candidate selection logic and controls
- code, data, and environment availability

