# STB Practitioner Business OS — Handover for Visualization

> **Status: derived summary for engineering and prospective-business explainers.
> Not a decision source.** If anything here differs from the
> [decision log](../01-decisions/DECISION-LOG.md) or the
> [canonical blueprint](../00-canonical/PRACTITIONER-BUSINESS-OS-V1.md), those
> govern. Written 2026-11-03. Contains no client data, prices, or outcome claims.
> Before showing to businesses, the owner must decide the external name, the price,
> and whether Human Context is shown at all (see section 8).

## 1. What it is (one paragraph)

A done-for-you business system for independent practitioners (coaches,
facilitators, educators). HAMAL delivers the work and SPARK LAB supplies the
diagnostic method. It starts small: a written Business Diagnostic that finds where
a practitioner's enquiries are being lost. Fixes are built only if the diagnostic
shows they are needed. Everything learned makes the next engagement faster. It is
**not** self-service software today.

## 2. The flow (the main animation)

FRONT DOOR → INTAKE → DIAGNOSTIC → DECISION → BUILD (optional) → HANDOVER → LEARNING LOOP

1. **Front door.** A visitor enquires through ONE routing point that lands in the
   practitioner's own tracked intake. There is no silent fallback to email, no
   fake "you're booked" message, and no invented scarcity. The system only
   confirms what it can really confirm.
2. **Intake.** Business facts first (offers, how clients find and book, tools in
   use, goals, capacity). Optional "Human Context" is a separate, consented step
   (section 4).
3. **Diagnostic (about 5 working days, human time-boxed).** The path from enquiry
   to booked call is checked against a standard defect checklist in four areas:
   Booking & Discovery, Follow-up & Retention, Offer Clarity, Infrastructure. Each
   finding gets a severity.
4. **Report.** A written blueprint: a severity-ranked defect list, the single
   highest-value bottleneck named, and a scoped fix plan. Each finding is routed to
   one of: do it yourself, HAMAL Sprint, refer out, or no action needed.
5. **Decision.** The practitioner chooses. A Sprint is offered only after a
   diagnostic, never cold. "You don't need to buy more" is a legitimate, honest
   outcome.
6. **Build (only if chosen).** Scope is written down, including what is out of
   scope. Reusable components are assembled. Done means the practitioner's OWN test
   enquiry arrives in THEIR CRM, witnessed by them.
7. **Handover.** The practitioner can run it without us. Each delivered item is
   tracked: built → activated → still in use after 30 days. If an item is not
   adopted, that is a lesson for HAMAL's design, not a failure on the
   practitioner's part.
8. **Learning loop.** Every engagement must deposit one reusable thing (an intake
   question, a defect-checklist entry, a component, or a test). The checklist grows
   and each engagement gets faster.

## 3. What the agents do

Agents assist. People decide, and people lead any sensitive conversation.

| Role | Does | Human gate |
|---|---|---|
| Doorkeeper | Routes a new lead to the right lane and first step | Founder reviews |
| Offer Architect | Applies the defect checklist to the intake and drafts the report | Founder edits and signs off |
| Evidence Tracker | Records the baseline before work starts, and before/after afterwards | Only with the practitioner's consent |
| Learning loop | Checks the engagement deposited something reusable | Not built yet (specified only) |

Agents never diagnose a person, interpret feelings, or lead Human Context
conversations. **Note for engineering:** these roles come from the blueprint
(§6.4). The skill implementations are not in any repository yet, so they are
unversioned and their contents have not been reviewed (see
[Provenance](../03-provenance/PROVENANCE.md)).

## 4. Two layers on top: the three "realities"

1. **Business Reality.** Observable evidence, scored by severity.
2. **Human Reality (optional).** How the practitioner experiences running the
   business. It is never scored and never changes a recommendation or price. It only
   shapes pacing and design. Separate consent, restricted storage, and a human
   facilitator. **Draft only: not live, collects nothing today**
   ([protocols](../04-protocols/human-context/README.md)).
3. **Implementation Reality.** Did the thing we built actually get used?
   ([data model](../00-canonical/ADOPTION-DATA-MODEL.md), proposed)

## 5. The back-end boundary (a key visual)

A wall splits two sides:

- **Public / reusable:** the defect checklist, intake question wording, templates,
  tests. No client identity, ever.
- **Private / per client:** their answers, reports, call notes, access. These live
  in a separate private store, and the practitioner stays in control of their data
  ([architecture](../00-canonical/ARCHITECTURE.md);
  [storage proposal](../01-decisions/PROPOSAL-engagement-storage.md), not yet
  approved).

Learning crosses the wall in one direction only: private → sanitize → review →
public. Nothing flows back.

## 6. Status legend (use as colour or badge on every box)

- **Approved:** product direction, three stages, the boundary, the compounding
  rule, the three realities, adoption tracking.
- **Proposed:** private storage design, adoption data model, gate metrics.
- **Draft, inactive:** Human Context protocols.
- **Not built:** multi-practitioner template, payments, analytics, any platform.
  Defect checklist: 7 observed examples from one build
  ([taxonomy](../../taxonomy/README.md)), plus about 18 candidate checks being
  finalised.

## 7. Motion and graphics brief for the visualization

Tone: calm, clear, premium. Use soft light, not alarm colours, and none of the
emergency-room metaphors.

- Scene 1: enquiries as small lights entering one door and landing in one tray.
- Scene 2: the report assembles as a ranked list, with the top item glowing.
- Scene 3: a fork into four paths (self-serve, Sprint, refer, no action).
- Scene 4: a test enquiry travels to the practitioner's CRM and gets a "witnessed"
  tick.
- Scene 5: a 30-day ring fills as an item moves to "in use".
- Scene 6: a private/public wall, with a sanitized glow passing through one way.
- Scene 7: the checklist grows each cycle and the next cycle gets visibly shorter.
- Two cuts from the same storyboard: **Engineering view** (names, statuses, data
  boundary) and **Business view** (plain language, no jargon).
- Include captions and a reduced-motion option.

## 8. Must NOT appear on screen (client-facing)

- Any result numbers, "more bookings", revenue, or conversion claims. There is zero
  measured evidence so far.
- Prices or "Stop the Bleed" branding. Pricing and external naming are not
  approved, so lead with the symptom, for example "People message me and I lose
  them."
- Names, photos, or testimonials of any practitioner.
- Health or therapy language ("healing", "treatment"). Human Context is shown only
  as optional and not yet live.
- Fake urgency or scarcity.

## Open decisions that affect this brief

External name and positioning (D-015, R-003); price (D-007); whether Human Context
appears at all (D-035, D-038); final defect count (D-040).
