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

---

## 2026-10-14 · V0.1 foundation authorisation

Recorded from the owner's written authorisation following the Foundation Audit.
Entries below are **APPROVED** unless marked otherwise. The "Auth. ref" column
cites the owner's item label in that authorisation (D1–D8), which is a
different numbering from this log; the stable identifiers are the D-### ones.

### D-009 · Documentation structure — **APPROVED** · Auth. ref D1
The existing numbered documentation tree (`docs/00-canonical`, `01-decisions`,
`02-evidence`, `03-provenance`) is preserved. The canonical blueprint is not
reorganised or split. Additions are made only where something is missing.

### D-010 · Public-repository data boundary — **APPROVED** · Auth. ref D2
This repository stays **public** and holds reusable product documentation and
code only. The following must never enter it: client engagement records,
credentials, personal intake responses, identifiable photographs, private
contact details (including email addresses, phone numbers, and Google
Forms/Sheets links). `scripts/check-docs.py` enforces the mechanically
detectable parts. A separate private engagement-storage architecture is to be
proposed (see D-017).

### D-011 · Defect taxonomy v0.0 policy — **APPROVED** · Auth. ref D3
An initial taxonomy is created from anonymised, observed defects in the archived
reference implementation. Every observation carries an evidence-quality label and
a sample size. Nothing in it may imply a validated outcome or a recurring market
frequency. Location: `taxonomy/`.

### D-012 · Read-only reconciliation scope — **APPROVED** · Auth. ref D4
Notion intake schemas and historical repositories may be read, read-only, for
architectural reconciliation: schemas, prompts, reusable components,
non-sensitive patterns. No client responses are imported. Historical
repositories are not modified.

### D-013 · Privacy remediation of the reference implementation's public repository — **APPROVED as priority** · Auth. ref D5
The archived reference implementation's repository is public and contains
personal data requiring access-control remediation. **Specifics are intentionally
not recorded in this public repository.** A remediation checklist is prepared for
the owner. No repository visibility, sharing permission or file in that
repository is changed without the owner's explicit, separate authorisation.

### D-014 · Decision-ID collision corrected — **APPROVED** · Auth. ref D6
See "Decision-ID mapping" and C-003 below. Historical references are preserved.

### D-015 · Provisional internal offer name — **APPROVED (provisional)** · Auth. ref D7
"Business Diagnostic" is the provisional **internal** name for the Stage 1 offer.
Pricing, duration, scope and external positioning remain subject to validation
and remain governed by D-007. **$500–$750 is not approved.**

### D-016 · Working branch and phase limits — **APPROVED** · Auth. ref D8
Work continues on the designated review branch. During V0.1 foundation: no merge,
no deploy, no pull request, no practitioner website, no speculative automation,
no installation of broad agent frameworks.

---

## Open items added 2026-10-14

### D-017 · Engagement record storage architecture — **OPEN (proposal made)**
Where intake and blueprint records live, given D-010. Proposal:
`docs/01-decisions/PROPOSAL-engagement-storage.md`. Not implemented. Blocks
the first paid engagement, not V0.1.

### D-018 · Intake base schema — **OPEN**
Which existing structure is the base for the Universal Practitioner Intake.
Blueprint §6.1 names `Client Clarity Intake`; the reconciliation finds a
competing candidate. Evidence: `docs/02-evidence/intake-reconciliation-20261014/`.
No new universal intake is created until this is decided.

### D-019 · Consent-before-extraction doctrine — **OPEN**
Whether to adopt the owner's existing "experience, consent, document, build,
publish" sequence as approved doctrine for all engagements, in generalised form.
Recommended; not adopted. Source is summarised in the intake reconciliation.

### D-020 · Outreach channel — **OPEN** · was blueprint BP-D4
### D-021 · Consent route for any reference to the reference-implementation practitioner — **OPEN** · was blueprint BP-D5
Seek written consent, or exclude entirely. Until decided, CLAUDE.md rule 3 applies.
### D-022 · Authorship of the DPA and refund policy — **OPEN** · was blueprint BP-D6
Both are first-sale blockers per blueprint §4.

### D-023 · Privacy review of other public historical repositories — **OPEN**
The read-only reconciliation found indicators of the same class of exposure in
other public repositories (see `docs/03-provenance/PROVENANCE.md`, "Source
inventory"). Whether to extend D-013's remediation scope to them is the owner's
decision. Nothing has been changed.

---

## Decision-ID mapping (D-014)

The blueprint's §9 "Open decisions" table used labels `D-1`…`D-6`, which collide
with this log's `D-001`…`D-008` (for example blueprint "D-3" is not log D-003).
The blueprint is preserved unedited. **From now on, blueprint §9 labels are cited
as `BP-D1`…`BP-D6`.** Mapping:

| Blueprint label | Meaning | Log identifier | Status |
|---|---|---|---|
| BP-D1 | Required monthly revenue | D-008 | OPEN |
| BP-D2 | Stage 1 price band | D-007 | OPEN |
| BP-D3 | Canonical home for the blueprint | D-002 | Resolved |
| BP-D4 | Outreach channel | D-020 | OPEN |
| BP-D5 | Consent route for the reference practitioner | D-021 | OPEN |
| BP-D6 | Who drafts DPA and refund policy | D-022 | OPEN |

---

## Corrections to the record (continued)

### C-003 · Decision-ID collision
Blueprint §9 labels `D-1`…`D-6` were ambiguous against log IDs `D-001`…`D-008`.
Resolved by D-014 and the mapping above. No historical text was altered.

### C-004 · Attribution of the Stage 1 price band
The Foundation Audit handover described a five-day "Booking Path Audit" at
$500–$750 as the council's recommendation. It is not. The council chairman
named ~€450 (R-001); **$500–$750 is Claude's delivery-economics
recommendation in blueprint §1.1**, which the blueprint calls "adopted" but this
log records as **OPEN (D-007)**. Where the blueprint and this log differ on
status, this log governs. No price is approved.

---

## 2026-10-14 · Research Intelligence V1.2 — methodology approval

Recorded from the owner's written approval of Research Intelligence V1.2 as the
current research and methodology baseline. "Auth. ref" cites the owner's item
number in that approval. **This approval does not authorise commercial launch,
public claims of validated outcomes, or deployment of the optional Human Context
module.** V1.2 itself is supporting evidence; where it differs from this log or
the blueprint, this log governs.

### D-024 · Three-reality model — **APPROVED** · Auth. ref 1
Business Reality, Human Reality, Implementation Reality. (V1.2 calls these
"layers"; see D-042 for the terminology collision with the intake layers.)

### D-025 · Build While You Heal — **APPROVED** · Auth. ref 2
Foundational methodology, internally and as an opt-in journey. **No therapeutic
claims**: STB does not claim to heal, treat, regulate or resolve trauma or any
psychological condition.

### D-026 · Category D is unscored human context — **APPROVED** · Auth. ref 3
Unscored, optional, practitioner-interpreted. It never changes a severity, a
route, or a price, and observable signals alone never establish a human factor.

### D-027 · Human Context conditions — **APPROVED** · Auth. ref 4
Separate consent, restricted storage, human-led facilitation. AI agents may not
generate psychological interpretations or independently facilitate sensitive
conversations.

### D-028 · Reflective frameworks — **APPROVED** · Auth. ref 5
Human Design, Gene Keys and similar are optional, practitioner-requested
reflective language. They are not diagnostic or predictive evidence and are never
used to score, route, price, or explain a decision in HAMAL's own voice.

### D-029 · Implementation adoption tracking — **APPROVED** · Auth. ref 6
Per delivered item: built, activated, in use after 30 days. Non-adoption is a
delivery-learning signal, not a practitioner failing. Data model:
`docs/00-canonical/ADOPTION-DATA-MODEL.md` (PROPOSED). Clock start: D-043.

### D-030 · Client-private vs reusable IP, extended — **APPROVED** · Auth. ref 7
Reaffirms and extends D-010. Human Context data is a restricted sub-class of
client-private records and never enters any repository, public or private,
marketing system, outreach tool, or general-purpose agent memory.

### D-031 · V1.2 as baseline — **APPROVED**
Research Intelligence V1.2 is the current research and methodology baseline and
is preserved as supporting evidence (form of preservation: D-039). It is not a
decision source.

### D-032 · Initial Human Context facilitator — **PROVISIONAL**
The founder, after documented preparation (informed consent, supportive listening,
boundaries, handling distress, confidentiality, referral procedures). Future
facilitators complete the same preparation plus a supervised practice review.
Preparation does not qualify anyone to provide therapy. Draft:
`docs/04-protocols/human-context/FACILITATOR.md` (INACTIVE).

### D-033 · Referral network — **PROVISIONAL**
Verified qualified professionals in relevant jurisdictions (a Bali-based pathway
and an online pathway authorised for the client's physical location). The
directory structure and verification checklist exist; **the directory stays
empty until entries are verified**, and procedures are required before
activation. Draft: `docs/04-protocols/human-context/REFERRALS-AND-ESCALATION.md`
(INACTIVE).

### D-034 · Human Context retention — **PROVISIONAL, pending privacy and legal review**
Proposed default: delete identifiable Human Context notes within 30 days after
engagement completion, unless the practitioner asks for earlier deletion or
separately agrees a defined extension. The practitioner can access, correct and
request deletion. Administrative consent records may follow a different period.
Deletion must account for backups, access logs and legal obligations. Detailed
trauma narratives are not collected; only practical accommodations the
practitioner approves are recorded. **This is an operating default, not a legal
determination.** Draft: `docs/04-protocols/human-context/DELETION-AND-RETENTION.md`
(INACTIVE).

### D-035 · Human Context activation gate — **APPROVED**
No Human Context storage, collection or deployment until D-032, D-033 and D-034
are finalised, and D-038 is decided. All protocol documents are drafts marked
INACTIVE; `scripts/check-docs.py` enforces the marker.

### D-036 · Non-conversion is not automatically failure — **APPROVED in principle**
Appropriate, ethical non-conversion (for example a correct finding that needs no
paid implementation) must not be treated as a failed validation. Recommendation
appropriateness is measured alongside conversion. Metrics and thresholds are
OPEN (D-041).

### D-037 · Next milestone — **APPROVED as direction**
A working sample diagnostic using a fictional practitioner and invented data,
clearly marked synthetic, producing the report HAMAL would deliver. It counts as
zero evidence. Not started.

---

## Open items added by V1.2 reconciliation

### D-038 · Rule 5 and the Human Context exception — **OPEN (blocks any activation)**
CLAUDE.md rule 5 says "No health data." Self-reported experience of overwhelm,
self-regulation and identity, and the birth details reflective frameworks need,
are likely to be special-category data under GDPR Art. 9 even when framed as
non-clinical (not a legal determination). Proposal for the owner: reword rule 5 as
"No health data in the core service. Human Context is the sole consent-gated
exception, inactive until D-035 is lifted." CLAUDE.md is **not** edited until the
owner approves.

### D-039 · Form of V1.2 preservation — **OPEN**
V1.2 names individual practitioners and workspace identifiers, which conflicts
with D-010 if stored verbatim in this public repository. Proposal: a redacted copy
plus a manifest (hash and redaction list) here; the original stays in private
storage (see D-017). V1.0, V1.1 and Draft A were not provided and are unverified.

### D-040 · Taxonomy reconciliation — **OPEN**
(a) V1.2 lists 18 business defects (A:5, B:5, C:4, E:4) but states 16; which are
in scope? (b) V1.2 scores severity 3 = most severe; taxonomy v0.0 uses S1 = most
severe. One direction must be chosen before a v0.1 merge.

### D-041 · Validation-gate thresholds — **OPEN**
Blueprint §8 (stop above 12 average hours; fewer than 3 paid by day 21) and V1.2
(reprice above 8 hours; pause at 0 of 20 intakes) differ, and neither is approved.
D-036 sets the principle; thresholds are the owner's.

### D-042 · Human Context timing and terminology — **OPEN**
V1.2 reads Human Context on Day 1 of the paid diagnostic; blueprint §6.1 collects
its Layer C material only once Stage 2 is agreed. "Layer" also now means two
things (intake layers A–C vs the three realities). Until decided, new documents
say "intake tier" for A–C and "reality" for the V1.2 model.

### D-043 · Adoption clock start — **OPEN**
Whether "in use after 30 days" counts from activation or from handover.

### D-044 · The "AMA" tier and `ama_custom` route — **OPEN**
V1.2 uses an "AMA" tier and an `ama_custom` resolution route. Neither is defined
in the blueprint or this log. Until defined, `ama_custom` is treated as an
undefined placeholder and no document may present it as a product.

V1.2's five commercial "proposed decisions" (first ICP, diagnostic-led model,
three-client pilot, taxonomy as HAMAL IP, BPA/Sprint/AMA tiers) were **not part of
the owner's approval** and are not recorded as decisions. D-003, D-007 and D-015
continue to govern.

---

## Corrections to the record (continued)

### C-005 · Internal inconsistency in V1.2
V1.2 states "16 business defects" in several places; its tables list 18. Recorded
under D-040. V1.2's economics (margins, break-even, Month 1) were re-derived and
are arithmetically consistent; they remain unmeasured hypotheses, and V1.2's
$350 overhead is not the revenue floor required by D-008.

### C-006 · Wording of the hardcoded-address observation
The observation "booking submissions bypass the intended intake destination" is
imprecise. Source check of the reference build at `72a167e`: a hardcoded
mail-client address was used in two components (introduced in `3d6e922`,
2026-06-03; removed in `220d831`). The **reachable** instance was a guide-request
form mounted in the application root; the **booking-request** instance sat in a
component never mounted. The build was never publicly deployed. Supportable
wording: "enquiry submissions bypassed the intended intake destination in a build
never publicly deployed." Re-verified from source by a second session of the same
tool, not by an independent human reviewer.
