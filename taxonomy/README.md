# Defect Taxonomy

A versioned, **append-only** catalogue of defects found in practitioner
enquiry-to-booking paths, each with a standard fix and a regression guard. It is
the reusable asset underneath the Business Diagnostic: the same checklist,
applied to every practitioner, accumulating over time (blueprint §6.2, D-005).

**Current version: [v0.0](v0.0.md)** — 7 entries, all from one archived,
undeployed reference build. Governed by decision D-011.

## What this is not

- **Not evidence of how common any defect is.** A defect seen in one build is a
  hypothesis about a class, not a measurement of the market. No entry states or
  implies a frequency.
- **Not evidence of impact.** No entry claims lost bookings, revenue or
  conversion. The reference build was never deployed (C-001). Severity describes
  *mechanism*, not measured loss.
- **Not a case study.** Entries are anonymised patterns. They identify no
  person, business, site or audience (D-010).
- **Not validated.** Severity ratings are one assessor's provisional judgement
  and are uncalibrated.

## Evidence-quality scale (`EQ`)

Every observation carries one label. State the **lowest** label that is honestly
true; upgrade only with new evidence, as a new version.

| Label | Meaning |
|---|---|
| **EQ0 — Asserted** | Claimed in a document; not independently observed by the author of the entry |
| **EQ1 — Observed (static)** | Seen in source code or a static artefact by the author of the entry |
| **EQ2 — Reproduced** | Failure demonstrated, or the defect is guarded by an automated test that fails when it returns |
| **EQ3 — Observed live** | Seen in a deployed funnel a real visitor could reach |
| **EQ4 — Impact measured** | A before/after from a **named, consenting** client (CLAUDE.md rule 2). Count today: **zero** |

## Sample size (`n`)

State `n` as a count of **distinct builds or funnels** in which the defect was
observed, with the unit written out ("n = 1 build"). Also state occurrences
within a build if useful, but never use occurrences as `n`. Entries at `n = 1`
must say so.

## Fields

| Field | Meaning |
|---|---|
| **ID** | `TX-<CLASS>-<NNN>`; never reused, never renumbered |
| **Class** | `ROUTE` enquiry routing · `STATE` false or unsupported state shown to a visitor · `DATA` collecting more than needed · `WIRE` built but unreachable · `ASSET` asset integrity · `QA` verification gaps |
| **Pattern** | The defect, described generically |
| **Mechanism** | Why it harms, without asserting measured loss |
| **Detection** | How it was or would be found in a diagnostic |
| **Standard fix** | The reusable remedy |
| **Regression guard** | The test or check that keeps it fixed |
| **Evidence** | `EQ` label, `n`, source type |
| **Severity (provisional)** | `S1` falsifies, misroutes or over-collects · `S2` degrades or dead-ends the path · `S3` hygiene |
| **Frequency** | Always `unknown` until an owner-set threshold of evidence exists (unset) |
| **Measured impact** | Always `none` until an EQ4 observation exists |

## How to add or change an entry

1. A defect found in a real engagement is recorded first in that engagement's
   **private** record, not here.
2. Pass it through the deposit gate in `docs/00-canonical/ARCHITECTURE.md` §3
   (sanitise, no identity, evidence label, `n`).
3. Add it as a **new entry** or a **new version note** on an existing one. Do not
   edit history: if an `EQ` label or `n` changes, add a dated line beneath the
   entry and bump the file version.
4. Run `python3 scripts/check-docs.py`.
5. An engagement is not closed until it has deposited something (D-005).

## Informal crosswalk to historical doctrine

The parent methodology's 14-Point Bleed Map describes business-level areas
(attention, conversion, follow-up, and so on). This taxonomy is finer-grained
and technical. The crosswalk in each entry is **informal**: that doctrine has not
been adopted into this repository's decision log.
