# Human Context — Access and Storage Protocol

> **DRAFT — INACTIVE.** Not approved for use. See [the index](README.md) and
> D-035. **Technology is deliberately not chosen** (D-017). **[LEGAL REVIEW]**
> items need someone with privacy-law standing.

Human Context records are a restricted sub-class of client-private records
(Class B, D-030). They never enter this or any repository.

## Roles

| Role | Access | Notes |
|---|---|---|
| Practitioner (the data subject) | Full access to their own record: view, correct, delete, export | Identity verified before any change |
| Named facilitator | Read and write during the engagement, for that practitioner only | One named person at a time (D-032) |
| Software assistants | Read **only** the structured accommodation fields the practitioner approved, to draft for human review | May not read notes, infer, interpret, summarise feelings, or retain anything (D-027) |
| Owner / administrator | No routine access. Break-glass only, logged and reported to the practitioner | |
| Everyone else, including delivery staff | None | |

## Storage requirements (technology-neutral)

1. **Separate store** from the core intake, CRM, proposals and delivery files.
2. **Never** in any repository, chat transcript, email thread, general-purpose
   agent memory, marketing or outreach system, analytics tool, or case study.
3. Access by **named individual accounts** with multi-factor authentication; no
   shared logins; access granted per engagement and revoked at the end.
4. **Encryption** in transit and at rest.
5. **Access log** recording who opened which record and when (not the content),
   reviewed on a schedule. [Log retention period: LEGAL REVIEW]
6. **Processor terms:** a data-processing agreement with every processor that
   holds the data, and a documented location. **[LEGAL REVIEW]**; the practitioner
   remains controller (blueprint §4) and the DPA is still undrafted (D-022).
7. **No local copies:** no downloads, screenshots, or notes on personal devices
   unless covered by the same controls.
8. **Backups documented**, with a known deletion horizon (see
   [DELETION-AND-RETENTION.md](DELETION-AND-RETENTION.md)).
9. **Tested with synthetic data only** before any real use.

## What may be stored

From the V1.2 schema, per dimension (decision friction, visibility and expression
comfort, capacity and self-regulation preferences, identity and readiness):
`observed_or_reported`, `practitioner_interpretation` (verbatim, optional),
`business_implications` (linked defect IDs, stated as hypotheses the practitioner
can reject), `accommodations`, `evidence_code`; plus `pathway`, `consent_status`,
`consent_timestamp`, `frameworks_requested` (free text, optional), `retention_until`.

## What must never be stored

Diagnoses, trauma history or narratives, medication, clinical treatment, other
people's personal data, or any text the practitioner has not approved recording.
The form has **no field** for these. If a free-text field receives such content,
the facilitator removes it and tells the practitioner.

## Practitioner rights (operational)

| Request | Handling |
|---|---|
| See what is held | Provide a readable export. [Response time: LEGAL REVIEW] |
| Correct | Practitioner edits or dictates; the original wording is replaced, not annotated |
| Delete | See the deletion protocol; confirm in writing when done |
| Withdraw consent | Stops use immediately; deletion per the deletion protocol |
| Complain or ask who holds it | Provide the controller and processor details |

## Suspected exposure

1. Contain: revoke access, preserve the access log.
2. Tell the owner immediately.
3. Tell the affected practitioner promptly and plainly.
4. Assess notification duties and deadlines. **[LEGAL REVIEW]** — these can be
   short; decide the contact person in advance.
5. Record what happened and what changed, without personal content.

## Not decided

Storage tool and location (D-017), log retention, response times, and the DPA
(D-022).
