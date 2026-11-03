# SPARK LAB Interactive Architecture — Prototype

**Status:** Concept demonstration for review. Not deployed, not published, not a product.
**Branch:** `prototype/spark-lab-map` (isolated from canonical methodology work).

A single, self-contained `index.html` showing what a practitioner experiences in
SPARK LAB, and the proposed HAMAL engine behind it.

## Preview

Open `index.html` in any modern browser. No build step, server, network access
or external dependency is needed.

Optional URL parameters, for review and screenshots:

| Parameter | Values | Effect |
|---|---|---|
| `mode` | `practitioner`, `school`, `eng` | Opens in that viewing mode |
| `scope` | `vision`, `today` | Full future vision, or what exists today |
| `view` | `engine` | Opens directly in the engine view |
| `stage` | `0`–`6` | With `view=engine`, jumps to that task stage |

## What it shows

1. **Maya's dashboard (hero).** A welcoming product screen with Bookings, Clients,
   Offers, Tasks and the business companion prompt. Maya is fictional; the screen is
   labelled as illustrative.
2. **The signature pass-through.** "See how it was prepared" lifts the cards,
   brightens the companion prompt, then zooms the camera through the dashboard
   glass into the HAMAL engine. Gold threads draw backwards from the finished
   booking page to the original request, showing who prepared it. The example
   task then plays from the start.
3. **One complete example task.** "Help me launch private sessions" moves
   through seven stages: request → Business Architect → Creative Studio and
   Systems Engineer in parallel → practitioner approval gate → authorized
   execution → verification → back to the dashboard. Handoff labels show what
   passes between agents. Dotted edges are drafts; solid edges are authorized
   actions.
4. **Three viewing modes on one architecture.** Practitioner (plain language),
   School partner (graduate support, the school never approves on a graduate's
   behalf) and Engineering (agent names, permissions, status badges, data
   boundaries). Only the level of detail changes.
5. **Around the engine.** Eighteen candidate business checks (A1–A5, B1–B5,
   C1–C4, E1–E4) with an example scan. Four separate Human Context dimensions,
   shown as inactive, optional and unscored. Four equal outcomes. Local versus
   cloud execution. A one-way private-to-shared knowledge boundary. Built →
   Activated → In use at 30 days. The school partnership model.

## Current versus future

Every element carries one of five labels:

| Label | Meaning |
|---|---|
| Exists today | Real and usable now: the human-led diagnostic method, the 18-check candidate list, the intake structure, a few proven components |
| Approved | A decided direction or principle; tooling may not exist yet |
| Proposed | A designed concept, not decided or built: the six agent groups, the orchestrator, adoption tracking, the school model |
| Inactive | Drafted and switched off: Human Context |
| Not built | Future capability shown for explanation: the dashboard, execution, the local runtime, cloud integrations |

The **What exists today** switch dims everything proposed or unbuilt. It states
that the steps are currently done by the HAMAL team by hand.

Some "Approved" labels (the approval gate and verification) reflect owner
direction in the build brief and the claims rules in `CLAUDE.md` and D-006. They
do not yet have their own decision-log entries.

## Interaction and animation system

- **State.** `body` data attributes drive everything: `data-mode`, `data-view`
  (`dash` or `engine`), `data-scope` and `data-expanded`. CSS reacts to them, so
  each mode and view is one attribute change.
- **Transition.** Dashboard and engine are two layers stacked in one grid cell
  with a 3D perspective. Entering the engine scales the dashboard past the
  viewer (2.35×) with an ease-in fade and blur, while the engine settles in after
  a short delay. Returning reverses it.
- **Task playback.** Each stage lists the nodes it lights and the edges a gold
  pulse travels, animated along the SVG path geometry. Play advances every
  ~2.8 s; selecting a stage or a node stops autoplay.
- **Engine expansion.** Collapsed shows the task path only. Expanded adds the
  orchestrator layer and the cloud and local execution zones, and is the default
  in Engineering mode.
- **Reduced motion.** It follows the operating-system setting and has its own
  toggle. Animations become instant, the pass-through becomes a cut, and
  autoplay stays off.
- **Keyboard.** Every control and node is focusable. Enter or Space selects a
  node, and Escape returns to the dashboard.

## Content safeguards

- No client-identifying information. Maya, the example school and the graduates
  are fictional.
- No prices, outcome numbers or performance claims. No "Stop the Bleed" branding
  on screen.
- No booking is ever shown as confirmed; the booking card reads "awaiting
  confirmation".
- No external requests: system fonts and inline SVG only.

## Not in scope

No pull request, merge, deployment or external publishing. The canonical
methodology documents and PR #1 are untouched.
