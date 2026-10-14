# Implementation Adoption — Data Model

**Status: PROPOSED schema.** The *concept* (track built, activated, in use after
30 days) is APPROVED as D-029. This model is a proposal for the owner to approve.
**Contains schema only — no engagement data.** Records themselves are Class B
(client-private) and live in the private store (D-017), never in this repository.
**Open parameter:** the 30-day clock start (D-043) is a configurable field below,
not an assumption.

## Purpose

Learn whether what HAMAL built is something the practitioner can adopt and
sustain (the Implementation Reality, D-024). It is a **delivery-learning signal
for HAMAL**. It is never recorded as a practitioner failing, and it is not an
outcome claim: adoption is not conversion, booking lift or revenue
(CLAUDE.md rule 2).

## Entities

```
Engagement 1 ──< DeliveredItem 1 ──< AdoptionCheck
                      │
                      ├──< AccommodationRef   (by ID only; no content)
                      └──0..1 NonAdoptionReview
```

### Engagement (pseudonymous)

| Field | Type | Notes |
|---|---|---|
| `engagement_id` | `E-###` | Pseudonymous. The identity map is held separately and restricted (D-017) |
| `stage` | enum | `diagnostic`, `sprint`, `continuity` |
| `handover_date` | date | Used by the open clock-start rule |
| `adoption_clock_start` | enum | `activation` or `handover`. **Not decided (D-043)**; stored per engagement so either result can be recomputed |

### DeliveredItem

| Field | Type | Notes |
|---|---|---|
| `item_id` | string | Unique within the engagement |
| `engagement_id` | ref | |
| `taxonomy_ref` | string | The defect or dimension it addresses (for example `A1`), or `none` |
| `resolution_route` | enum | `self_serve`, `sprint`, `ama_custom`, `no_action`, `refer_out` (V1.2). `ama_custom` is undefined in the blueprint and log (D-044) |
| `item_type` | enum | For example `booking_link`, `intake_form`, `followup_sequence`, `payment_request`, `template`, `other` |
| `use_definition` | text | **Written at build time, before delivery**: what observable event counts as "in use" for this item. Prevents defining success after the fact |
| `use_evidence_type` | enum | `system_signal`, `practitioner_report`, `none_available` |
| `built_at` | date | |
| `activated_at` | date, nullable | The practitioner switched it on or began using it live |
| `state` | enum | `built`, `activated`, `in_use_30d`, `not_activated`, `retired_by_choice`, `declined_by_practitioner`, `blocked_external` |
| `use_check_due` | date | Computed: `adoption_clock_start` + 30 days. If never activated, due 30 days after handover and the outcome is `not_activated` |

### AdoptionCheck

| Field | Type | Notes |
|---|---|---|
| `check_id` | string | |
| `item_id` | ref | |
| `checked_on` | date | |
| `result` | enum | `in_use`, `partially_in_use`, `not_in_use`, `cannot_tell` |
| `evidence_note` | text | What was observed. **No personal detail** |
| `low_volume_caveat` | bool | True when the item sees too little traffic for "no signal" to mean "not used" |

### AccommodationRef

| Field | Type | Notes |
|---|---|---|
| `item_id` | ref | |
| `accommodation_id` | string | An identifier only. **The content of an accommodation lives in the Human Context store, never here** |

### NonAdoptionReview (only when `built` but not `activated`, or `not_in_use`)

| Field | Type | Notes |
|---|---|---|
| `reason_code` | enum | `design_fit`, `pacing`, `skill_gap`, `tool_friction`, `scope_changed`, `practitioner_chose_not_to`, `external_dependency`, `unknown` |
| `reason_source` | enum | `practitioner_stated`, `observed_by_hamal`. **Cause attributed to a person's inner state is not permitted** (D-026); only the practitioner can state it |
| `design_learning` | text | What HAMAL would change in design, pacing or fit. **No personal detail** |
| `taxonomy_feedback` | bool | Whether this should feed an accommodation template or a taxonomy note |

## Rules

1. **Pre-register `use_definition`.** No item is delivered without one.
2. **Human Context never explains non-adoption in HAMAL's voice.** Reasons come from
   the enumerated list or the practitioner's own statement.
3. **No Human Context content crosses in.** `AccommodationRef` carries IDs only.
   Agents may read these structured fields and draft for human review; they may
   not infer causes (D-027).
4. **Low traffic is not non-use.** If `low_volume_caveat` is true, `cannot_tell` is
   the honest result.
5. **Cash and shadow cost** stay separate from this model; adoption is not a
   margin figure.
6. **Aggregate before publishing.** Counts may enter the public repository only as
   aggregates across multiple named, consenting engagements (CLAUDE.md rule 2),
   and never as an outcome claim.
7. **Each engagement deposits something** (D-005): a closed `NonAdoptionReview`
   with a `taxonomy_feedback` flag is a valid deposit, passed through the deposit
   gate in `ARCHITECTURE.md` §3.

## Metrics this supports (definitions only; no thresholds)

- **Activation rate:** items `activated` ÷ items `built`.
- **30-day use rate:** items `in_use_30d` ÷ items `activated`.
- **Not-activated share by reason code.**
- **Effect of accommodations on activation:** to be examined only with enough
  engagements to say anything, and reported with `n` and evidence labels like the
  taxonomy. V1.2's open question — "does Human Context improve adoption?" — cannot
  be answered at small `n`, and no claim should be made until it can.

## Not decided here

| Question | Tracked as |
|---|---|
| Clock start for "30 days" | D-043 |
| Where records live | D-017 |
| Whether `ama_custom` is a real route | D-044 |
| Any numeric target for adoption | Not proposed |
