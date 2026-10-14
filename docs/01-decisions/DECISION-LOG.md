# Decision Log

Append-only. Every entry records whether something is **APPROVED** (a decision
taken), **RECOMMENDED** (advice received, not yet decided), or **OPEN**.

This distinction is load-bearing. An LLM Council recommendation, a technical
audit finding, and an agent's proposal are all *inputs*. None of them is a
decision until it is recorded here as APPROVED by the owner.

---

## 2026-10-14

### D-001 · Product direction — **APPROVED**
Done-for-you service first; platform later. HAMAL delivers, SPARK LAB provides
methodology, the Practitioner Business OS becomes reusable product
infrastructure. Not a SaaS platform first: a repeatable, revenue-generating
service that can eventually become one.

### D-002 · Repository architecture — **APPROVED**
| Repo | Role |
|---|---|
| `STB-Practitioner-Business-OS` *(this one)* | **Canonical** for the product: commercial model, delivery architecture, reusable infrastructure |
| `SPARK-LAB-STB` | Parent methodology and research system |
| `STB-Come-Back-To-Yourself` | Archived Flo reference implementation — historical only |

Artifacts move here **directly**, not via the parent.

### D-003 · Three-stage commercial model — **APPROVED in structure, OPEN on price**
Stage 1 Business Diagnostic (entry) → Stage 2 Practitioner Launch & Conversion
Sprint (core) → Stage 3 Continuity & Growth (ongoing).

Structure approved. Specific prices remain hypotheses — see D-007.

### D-004 · Scope discipline — **APPROVED**
The Sprint's six components are a **menu, not a checklist**. The diagnostic
selects which are in scope for a given practitioner; the remainder are named
out-of-scope in writing before work starts.

### D-005 · The compounding rule — **APPROVED**
> Every practitioner implementation should improve the next implementation.

Operationalised in the blueprint §7: an engagement is not closed until it has
deposited a reusable artifact; the defect taxonomy is versioned and append-only;
nothing is rebuilt from memory; human hours per engagement are logged so
compounding can be measured rather than assumed.

### D-006 · Claims discipline — **APPROVED**
No conversion, booking or revenue improvement may be promised before a measured
before/after exists from a named, consenting client. Current count: **zero**.

### D-007 · Pricing — **OPEN**
Stage 1 proposed at $250–500 by the owner; $500–750 recommended by Claude Code
on delivery-economics grounds. Stage 2 proposed at $2,500–5,000. Stage 3
deliberately unpriced until three Sprints have before/after data.

Not blocking repository or structural work. Blocks going to market.

### D-008 · Required monthly revenue floor — **OPEN**
Needed to anchor pricing and capacity planning. Explicitly **not** a
precondition for organising the repository or preserving completed work.

---

## Recommendations received, not approved

Recorded so they are neither lost nor mistaken for decisions.

### R-001 · LLM Council, 2026-10-14 — *recommendation only*
Primary offer: a 5-day "Booking Path Audit" at ~€450–750; secondary: the fix
scoped off its own defect list; kill criteria at day 21.

**Status: a credible hypothesis, not an approved product identity.** It has not
been established that practitioners want a booking audit specifically, or will
pay that price. The diagnostic is adopted as the **commercial entry point**
(D-003) without becoming the product's identity.

Evidence: `docs/02-evidence/council-20261014/`.

### R-002 · Chairman's departure — *recommendation only*
A one-shot diagnostic is not repeatable; the audit is the wedge and the
**defect taxonomy** underneath it is the durable asset. Converges with D-005,
which is approved. The taxonomy itself is adopted; the "sell audits only"
framing is not.

### R-003 · Naming — *recommendation only*
"Stop the Bleed", "Business Pressure Test", "Trip Wire Detector", "Doorkeeper",
"Build While You Heal" read as emergency-room language to buyers whose
professional identity is calm. Suggested: keep internal, lead client-facing with
the symptom they would say aloud. **Not decided.**

### R-004 · ECC adoption — *recommendation only, deferred*
Adapt selectively; 8 capabilities; per-project install; hooks staged. Stage 0
remediation was authorised and completed; Stages 1–3 are not approved.
Evidence: `STB-Come-Back-To-Yourself/docs/ecc-audit/`.

---

## Corrections to the record

Kept visible rather than silently edited.

### C-001 · Overstated live impact — twice
A technical audit claimed Flo's booking flow was a live revenue leak. It was not:
`BookingSession.tsx` was never mounted, and the site was not deployed at all.
The code defects were real; the revenue consequence was **zero**. No booking,
conversion or revenue claim may be made from the Flo engagement.

### C-002 · Overstated a blocker
The required monthly revenue figure (D-008) was described as blocking
"everything." It gates pricing and capacity planning only, not repository
structure or preservation of completed work.
