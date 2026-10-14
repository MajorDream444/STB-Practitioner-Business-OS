# Human Context — Deletion and Retention Protocol

> **DRAFT — INACTIVE.** Not approved for use. See [the index](README.md) and
> D-035. **The 30-day default (D-034) is PROVISIONAL**: an operating default, not
> a legal determination, and it requires jurisdiction-specific privacy review
> before it is relied on. Items marked **[DECISION]** or **[LEGAL REVIEW]** are
> unresolved.

## Proposed default

Delete identifiable Human Context notes **within 30 days after engagement
completion**, unless the practitioner:

- asks for **earlier** deletion, or
- separately agrees a **defined extension** (written, with a purpose and an end
  date).

## Definitions that must be fixed before use

| Term | Proposal | Status |
|---|---|---|
| "Engagement completion" | The later of handover accepted and final debrief held | **[DECISION]** |
| "Within 30 days" | Calendar days from completion, deletion actually finished (not merely scheduled) | **[DECISION]** |
| "Identifiable" | Anything that could be linked to the practitioner, including pseudonymous records while the identity map exists | **[LEGAL REVIEW]** |

## What is deleted

All Human Context content for the engagement, including **derived** copies:
facilitator notes, drafted accommodations awaiting review, exports, summaries,
working files and any copy a software assistant produced. Accommodations the
practitioner chose to receive in **their own handover document** are theirs to
keep; HAMAL's copy follows this protocol.

## What may be kept, and why

| Item | Kept? | Notes |
|---|---|---|
| Consent record (pathway, notice version, consent and withdrawal timestamps) | Yes, for a period to be set | Contains **no content**. Evidences that consent was obtained and honoured. **[LEGAL REVIEW]** period |
| Access log (who, when; no content) | Yes, for a period to be set | **[LEGAL REVIEW]** |
| Aggregate, de-identified learning (for example a non-adoption reason code) | Yes | Must pass the deposit gate; no Human Context content |
| Anything else | No | |

## Triggers

| Trigger | Action | Timing |
|---|---|---|
| Engagement completes | Standard deletion | Within 30 days (provisional) |
| Practitioner asks for earlier deletion | Delete | Promptly. **[DECISION]** target, for example within a small number of days |
| Practitioner withdraws consent | Stop using the data at once; delete on request or by the standard clock, practitioner's choice | Stop immediately |
| Agreed extension | Retain only for the stated purpose | Until the agreed end date, then delete |
| Engagement stops without completion | Treat as completion on the last contact date | **[DECISION]** inactivity period |
| Legal hold or other legal obligation | Retain only what the obligation requires | **[LEGAL REVIEW]** |

## Backups, logs and tools

1. Backup retention must not silently outlast the deletion window. Either backups
   expire within a documented, short period, or the practitioner is told the
   period in the notice.
2. Deleting in a tool is not deletion until the tool's own recycle, trash, version
   history and sync copies are cleared. **Each tool's behaviour is unverified and
   must be checked before it is used.**
3. A software assistant's working files and any cached context are included.

## Verification and confirmation

- [ ] Primary record deleted
- [ ] Derived copies deleted (notes, drafts, exports, summaries)
- [ ] Recycle/trash and version history cleared
- [ ] Backups: expiry date recorded
- [ ] Access removed for all named accounts
- [ ] Identity-map link removed or tombstoned as appropriate
- [ ] Written confirmation sent to the practitioner stating what was deleted,
      when, and what is retained (consent and access records) and why
- [ ] Completed entry recorded in the private index (no content)

## Before activation

A **deletion drill** with synthetic data must pass end to end, including backups
and a tool's trash. No real record is created until it does.
