# STB Practitioner Business OS

Canonical repository for the SPARK LAB–STB product: a done-for-you client
acquisition, delivery and continuity system for coaches, facilitators, healers
and independent practitioners — delivered by HAMAL, methodology from SPARK LAB,
built to become reusable infrastructure.

**Not a SaaS platform first.** A repeatable, revenue-generating service that can
eventually become one.

---

## Where things live

| Repository | Role |
|---|---|
| **This one** | **Canonical for the product** — commercial model, delivery architecture, reusable infrastructure |
| `SPARK-LAB-STB` | Parent methodology and research system |
| `STB-Come-Back-To-Yourself` | Archived Flo reference implementation — historical only |

## Start here

| Document | What it is |
|---|---|
| [Canonical Product Blueprint V1](docs/00-canonical/PRACTITIONER-BUSINESS-OS-V1.md) | Single source of truth: what is sold, at what price, how delivered, under what gates, and what may not be claimed |
| [Decision Log](docs/01-decisions/DECISION-LOG.md) | What is **approved** vs merely **recommended** vs **open**. Read before acting on any proposal |
| [Provenance & Reuse Constraints](docs/03-provenance/PROVENANCE.md) | What exists, where it came from, what may legally be reused |
| [Council evidence](docs/02-evidence/council-20261014/) | The LLM Council that informed the model — open the `.html` |
| [Architecture — data boundaries](docs/00-canonical/ARCHITECTURE.md) | What may and may not live in this public repository, and how material moves from private to reusable |
| [Defect taxonomy v0.0](taxonomy/README.md) | The reusable defect catalogue, with evidence labels and sample sizes. No frequency or impact is claimed |
| [Intake reconciliation](docs/02-evidence/intake-reconciliation-20261014/RECONCILIATION.md) | What the existing intake structures contain and where they diverge |
| [Engagement storage proposal](docs/01-decisions/PROPOSAL-engagement-storage.md) | **Proposed, not approved** — where private records would live |
| [AGENTS.md](AGENTS.md) | Entry point for non-Claude agents; defers to `CLAUDE.md` |

Before committing, run `python3 scripts/check-docs.py`.

## Current state — honest summary

- **Approved:** product direction, repository architecture, three-stage model
  (structure), scope discipline, the compounding rule, claims discipline, the
  public-repository data boundary, the numbered documentation structure, and the
  rule that the defect taxonomy carries evidence labels and no frequency or
  impact claims.
- **Open:** pricing; required monthly revenue floor; outreach channel; where
  private engagement records live; which existing intake is the base schema;
  whether consent-before-extraction becomes binding doctrine; who drafts the DPA
  and refund policy (both are first-sale blockers); the consent route for the
  reference practitioner; and the scope of the privacy review of historical
  repositories. See the [decision log](docs/01-decisions/DECISION-LOG.md) for
  identifiers (D-007, D-008, D-017 to D-023).
- **Evidence of demand:** none. Zero practitioners have paid. No measured
  before/after exists for any engagement.
- **Built:** a handful of proven reusable components (see Provenance). No
  multi-tenant template, no payments, no analytics, no platform.

The 30-day pilot in the blueprint exists to convert the first of those from
assertion into evidence.

## Status

Draft for approval. Nothing here has been sold or deployed.
