# Proposal — Where Intake and Blueprint Records Live

**Decision:** D-017 · **Status: PROPOSED — not approved, not implemented**
**Date:** 2026-10-14 · **Author:** Claude Code (input to the owner, per CLAUDE.md rule 1)
**Merge / build:** none. This proposal creates no storage, no repository, no automation.

## Problem

This repository is public and must stay so for reusable material (D-010). The
product nevertheless generates records that are personal and sensitive:
intake responses, written blueprints, audit findings that name a practitioner's
site, call notes, baseline numbers, consents. They need a home that is private,
access-controlled, erasable on request, and consistent with the practitioner
remaining the data controller (blueprint §4). Without a decision, the default
will be "wherever is convenient", which is how the reference build ended up with
personal data in a public repository.

## Constraints

- D-010: nothing identifying enters this repository.
- CLAUDE.md rule 5: no health data. Free-text intake invites it, so storage must
  not assume the data is clean.
- GDPR: practitioners are EU/NL. Right to erasure must be practicable. **Raw
  personal data in git history is effectively not erasable** — this rules out
  committing raw responses to any repository, public or private.
- Solo operator: the design must be simple enough to actually be followed.
- Existing tools already hold intake data (Notion databases, a Google Form/Sheet,
  a former Airtable sync). Their processor status and region are **unverified**.
- Rule 6: build nothing speculative. Whatever is chosen must be creatable by hand
  when the first paying engagement starts.

## Options

| | A. One private git repo for everything | B. HAMAL's own Notion workspace | C. Practitioner-controlled workspace + thin private index |
|---|---|---|---|
| Raw responses | In git (bad: not erasable) | In Notion | In the practitioner's own workspace, shared to HAMAL |
| Controller/processor clarity | Muddy: HAMAL becomes the holder | HAMAL is processor/holder under DPA | **Cleanest: practitioner stays controller** |
| Erasure | Poor | Good | Good (practitioner deletes, HAMAL revokes) |
| Versioning / review | Excellent | Weak | Weak for raw data; good for the index |
| Effort for a solo operator | Low | Low | Medium: needs a per-engagement setup step |
| Handover | Awkward | Export needed | **Built in: it is already theirs** |

## Recommendation (hybrid of C with a thin private repo)

1. **Raw records** (Layer A/B/C responses, call notes) live in a workspace the
   **practitioner owns**, shared to HAMAL with scoped, revocable access for the
   engagement. HAMAL keeps no standing copy beyond the retention period below.
2. **A private repository** (suggested name `STB-Engagements`, separate from this
   one) holds only a **thin, pseudonymous index** and the deposit log. It never
   holds narrative content, responses, or contact details.
3. **The identity map** (engagement ID to person) is a separate, restricted file
   or note, not stored alongside the index.
4. **Deposits** to this public repo pass the gate in `ARCHITECTURE.md` §3.

### What lives where

| Record | Class | Home | Notes |
|---|---|---|---|
| Intake template (question wording) | A | This repo (`intake/`, after D-018) | Public; no answers |
| Intake responses, Layers A/B/C | B | Practitioner-owned workspace | Layer C only collected when a Stage 2 is agreed |
| Booking-path facts, baseline numbers | B | Practitioner-owned workspace; copy of figures in index | Baseline recorded **before** work starts (blueprint §3.4) |
| Written blueprint and defect list | B | Delivered to the practitioner; private copy per retention | Naming their site, so never public |
| Engagement index (E-### , stage, dates, hours, consent flags) | B (pseudonymous) | Private repo | Hours logged for compounding (blueprint §7.4) |
| Identity map | B | Restricted store, separate | Re-identifies the index; protect accordingly |
| Consent register (per scope) | B | Private repo, per engagement | Scopes: diagnostic use, taxonomy deposit, named reference |
| Sanitised defect observation | A | This repo (`taxonomy/`) | Via deposit gate only |
| Credentials, tokens, form URLs | D | Secrets manager | Never in any repository |

### Suggested private-repo shape (illustrative, not created)

```
STB-Engagements/            (PRIVATE)
  index.csv                 E-ID, stage, start, handover, hours, consents
  engagements/E-001/
    consent.md              scopes granted, date, how withdrawn
    deposits.md             what was deposited to the public repo, when
    hours.csv               date, activity, minutes
  templates/                copies of public templates only
```

### Retention and erasure (starting positions for the owner and counsel)

- Raw responses: removed from HAMAL access at handover; any HAMAL-held copy
  deleted after a fixed period. **The period is a decision, not a fact** — a
  placeholder of 90 days after handover is offered only to have something to
  argue with.
- Index and consent register: kept as long as needed to evidence consent and
  compounding; contain no narrative content.
- Erasure request: delete in the practitioner's workspace, revoke HAMAL access,
  delete the identity-map row, tombstone the index row.

## Needs a human with legal standing before the first sale

- DPA between practitioner (controller) and HAMAL (processor) — D-022. **Not
  drafted.**
- Sub-processor and region review for any tool that holds responses (Notion,
  Google, Airtable, email). **Unverified.**
- Entity and invoicing position of a solo operator based outside the EU serving
  EU practitioners (blueprint §4). **Unresolved; not advised on here.**

## Not asking the owner to decide now

- Whether this repository should become private (owner's call under D-010).
- Tool brands. The proposal is tool-neutral apart from the suggested repo name.
- Anything about the Flo repository (tracked separately under D-013).

## Done looks like

- The owner records APPROVED / amended / rejected against D-017.
- If approved: the private repo and templates are created by hand at the first
  paid engagement, not before.
