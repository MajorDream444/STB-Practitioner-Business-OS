# Human Context — Consent Protocol

> **DRAFT — INACTIVE.** Not approved for use. See [the index](README.md) and
> D-035. Items marked **[LEGAL REVIEW]** need someone with privacy-law standing.

## Pathways and consent states

| Pathway | Included | `consent_status` |
|---|---|---|
| 1. Business diagnostic only (default) | Core intake and audit; no personal exploration | `business` |
| 2. Plus decision-making reflection | Adds the four human-context dimensions and an Implementation Fit section | `human_context` |
| 3. Plus personal frameworks | Adds practitioner-chosen frameworks as reflective language | `human_context_frameworks` |
| Withdrawn | Any pathway ended by the practitioner | `withdrawn` |

## Rules

1. **Separate consent.** Never bundled with the business intake, the proposal, a
   payment, or terms of service.
2. **Not a condition.** Declining changes neither price, scope, quality nor
   timing. The core service is complete without it.
3. **Not in a sales moment.** Not requested in the same conversation or message
   as a price, a proposal or a payment request. [Timing relative to Stage 1 vs
   Stage 2 is open: D-042.]
4. **Specific and granular.** Each pathway is consented to separately. The
   frameworks pathway is a further, separate step.
5. **Plain language, the practitioner's language.** Any translation is reviewed by
   a fluent speaker before use. **[LEGAL REVIEW]** for the lawful-basis wording
   (explicit consent for special-category data may be needed; not a legal
   determination).
6. **Informed.** The practitioner is told what will be asked, what will never be
   asked, who sees it, where it is kept, for how long, and how to stop.
7. **No pre-ticked boxes, no silence-as-consent.**
8. **Before any question.** No Human Context question is asked until consent is
   recorded.
9. **Re-checked each conversation.** At the start of every Human Context
   conversation the facilitator asks: still comfortable? what pace? what should we
   skip?
10. **Withdrawable at any time**, by any channel the practitioner uses, with
    immediate effect on future use. See
    [DELETION-AND-RETENTION.md](DELETION-AND-RETENTION.md).
11. **Re-consent when scope changes** (new question types, a new framework, a new
    use, a new retention period).

## What is recorded about consent (and nothing else)

`engagement_id` (pseudonymous) · `pathway` · `consent_status` · `consent_timestamp`
· `notice_version` · `withdrawal_timestamp` (if any). **No content.** This record
may be retained on a different schedule from the notes (see the deletion
protocol).

## Plain-language notice — skeleton (to be written and reviewed; do not use as is)

1. **What this is.** An optional conversation about how running your business feels
   and what helps you act on it, so we can pace and design the work to fit you.
2. **What this is not.** Not therapy, counselling, or any kind of assessment of
   you. We will not label or interpret you.
3. **What we might ask.** [Example style only, open and skippable: "Which business
   decisions tend to stall for you?" · "What helps when a decision feels heavy?" ·
   "What pace of change feels workable right now?"]
4. **What we will not ask.** About trauma history, diagnoses, medication, or
   clinical treatment. If you choose to share something, we will write down only
   the practical adjustments you approve.
5. **Frameworks.** If you want us to use Human Design, Gene Keys or something
   similar, we will use your language as a reflection tool. It is not evidence
   about you and never affects what we recommend or charge. [Birth details are
   requested only if you choose a framework that needs them and only what it needs.
   **LEGAL REVIEW**]
6. **Who sees it.** [Named facilitator]. Software assistants may only handle the
   adjustments you approved, to draft for a person to review. They do not interpret
   anything.
7. **Where it is kept and for how long.** [Storage description and period: D-017,
   D-034. **LEGAL REVIEW**]
8. **Your rights.** See what we hold, correct it, delete it, change your mind at
   any time. [Contact route.]
9. **Saying no or stopping.** Saying no changes nothing about your service.
10. **If something comes up.** We can share information about qualified
    professionals if you would like it. You choose.

## Not decided

Timing in the engagement (D-042); lawful basis and notice wording (D-034 review);
storage (D-017).
