# SPARK LAB Interactive Architecture — Prototype V0.1

**Status:** Concept demonstration for internal review. It is not deployed, not published and not a product. It is not yet cleared for partner demonstration.
**Branch:** `prototype/spark-lab-map`, kept isolated from canonical methodology work.

A single, self-contained `index.html` showing what a practitioner experiences in
SPARK LAB, and the proposed HAMAL engine behind it.

## Preview

Open `index.html` in any modern browser. No build step, server, network access
or external dependency is needed.

Optional URL parameters for review and screenshots. Invalid values are ignored.

| Parameter | Values | Effect |
|---|---|---|
| `mode` | `practitioner`, `school`, `eng` | Opens in that viewing mode |
| `scope` | `vision`, `today` | Full future vision, or only what exists today |
| `view` | `engine` | Opens directly in the engine view |
| `stage` | `0`–`7` | Used with `view=engine`; jumps to that journey stage |

## The journey

The main journey starts with the human-led Business Diagnostic. Implementation
is optional and only follows the practitioner's decision.

| # | Stage | What happens | Status |
|---|---|---|---|
| 1 | Diagnostic | The HAMAL team runs a human-led review against 18 candidate checks and writes a report | Method exists today (human-led); automated scoring not built |
| 2 | Decision | The practitioner picks one of four equal options: self-serve, implementation, referral or no action | Approved policy; decision capture not built |
| 3 | Architect | Only if implementation was chosen: the offer structure is drafted | Proposed |
| 4 | Prepare | Creative Studio and Systems Engineer prepare drafts in parallel | Proposed |
| 5 | Approve | The practitioner approves before anything consequential goes live | Human approval required: approved policy. Automated approval gate: not built |
| 6 | Execute | Approved actions run in the practitioner's own accounts | Not built |
| 7 | Verify | A test enquiry arrives in the practitioner's CRM, witnessed by them | End-to-end verification required: approved policy. Automated verification records: not built |
| 8 | Return | Back to the dashboard; adoption tracking begins | Adoption model proposed; dashboard not built |

The dashboard opens on "Your business diagnostic is ready". It changes to
"Your booking page is ready for review" only after the journey has reached
the final stage.

## Status labels

| Label | Meaning |
|---|---|
| Exists today | Real and usable now. Only the human-led diagnostic method, the candidate checklist and a few proven building blocks qualify |
| Approved policy | A founder-approved operating rule. Approved is not built: automated enforcement may not exist |
| Proposed | A designed concept, not decided or built: the agent groups, the orchestrator, adoption tracking, the school model |
| Inactive | Drafted and switched off: Human Context |
| Not built | A future capability shown for explanation: the dashboard, execution, the practitioner-side runtime, cloud integrations |

The **What exists today** switch dims everything proposed or unbuilt. It also
states that no paid engagements have been delivered yet. The practitioner-side
local runtime is labelled as a concept and as separate from HAMAL's own internal
team tooling.

## Interaction and animation

- **State.** Data attributes on `body` drive everything: `data-mode`,
  `data-view`, `data-scope` and `data-expanded`. Modes and scope are checked
  against whitelists before use.
- **Transition.** The dashboard and engine layers sit in one grid cell with a 3D
  perspective. Entering the engine scales the dashboard past the viewer with an
  ease-in fade, while the engine settles in behind it. Gold threads then draw
  along the whole journey. The layer that isn't showing is `inert` and
  `aria-hidden`.
- **Playback.** Each stage lists the nodes it lights and the edges a pulse
  travels along. Each stage change takes a fresh animation token, so earlier
  pulses stop and stale callbacks can't light the wrong node. Any manual
  selection stops autoplay and cancels pending intro timers.
- **Accessibility.**
  - Stage pills are buttons using `aria-pressed`.
  - SVG nodes are focusable buttons with labels that include their status, and they show a visible focus ring.
  - Only the short caption is a live region.
  - Escape returns to the dashboard.
- **Reduced motion.** It follows the operating-system setting, including changes
  made after the page has loaded, and has its own toggle. Animations become
  instant and autoplay stays off.
- **Mobile.** There is no page-level horizontal overflow at 360px. The engine
  diagram scrolls sideways inside its own panel, which the owner accepted for
  internal review.

## Content safeguards

- No client-identifying information. Maya, the example school and the graduates
  are fictional.
- No prices, outcome numbers or performance claims, and no therapy language.
- "STB" appears only in Engineering mode, as the internal method name.
- A booking is never shown as confirmed.
- The page makes no external requests: it uses system fonts and inline SVG only.

## Still required before a partner demonstration

- A vertical, simplified journey for the school-partner presentation, so the
  horizontal diagram isn't the partner-facing view.
- The 75-second partner cut, built around SPARK LAB as the bridge between
  certification and a sustainable independent practice.

## Not in scope

No pull request, merge, deployment or external publishing. The canonical
methodology documents and PR #1 are untouched.
