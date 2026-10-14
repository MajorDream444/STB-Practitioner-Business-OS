# Intake Reconciliation — Existing Notion Structures

**Date:** 2026-10-14 · **Authority:** D-012 (read-only) · **Feeds:** D-018
**Status:** Evidence and analysis. **Input, not a decision** (CLAUDE.md rule 1).
**Method:** database definitions (property names, types, option lists, form
prompts) read through the Notion connector. **No responses were imported or are
recorded here.** Property counts were taken from the schemas as read on this date.

> **Handling note.** Reading a database definition also returns a few sample
> rows. Those samples included personal contact details and health-related
> narrative about identifiable people. None of it is recorded in this repository.
> Future reads should use a schema-only method or a restricted integration.

## 1. What actually exists

The blueprint (§6.1) and provenance describe "three Notion questionnaires". The
read found **four structures plus one record-level artefact**:

| # | Structure | Kind | Properties | Shape |
|---|---|---|---|---|
| 1 | `Client Clarity Intake` | Database | 22 | 13 free-text, 2 selects, 2 checkboxes, plus email/URL/phone/date. 9-state pipeline. Has `Template Type` (4 values) and `Consent to Process` |
| 2 | `SPARK LAB-STB Intake` | Database | 34 | **11 structured fields** (selects, multi-selects, status) plus free text. Has `Client Type` (7), `Main Pressure Points` (12), `Support Needed Most` (9), `Visibility Comfort` (5), `Desired Business Model` (9), `Preferred Delivery` (7), `Communication Style` (7), `Source / Origin` (7). 6-state intake status incl. `Archived`. Has `Consent to Process` |
| 3 | Business telemetry intake for the second early practitioner | Database + form view | 40 | 10 required narrative prompts in a form view; commercial-reality fields (revenue ranges, price point, lead sources, referral dependence, measurement readiness, baseline numbers, 90-day targets, capacity, budget, software sensitivity, assets, handover, approvals, support). 3-state status. **No consent field** |
| 4 | `CLIENT CLARITY-STB` | Database | 1 (`Name`) | Contains one blank template named `CLIENT INTAKE - STB`. Confirms the blueprint's "blank" finding, with the correction that it is a database, not a page |
| 5 | The third practitioner's intake | **A record** in structure 1 (`Template Type` = the third practitioner's system, status "Sent") | n/a | Not a separate schema. Contents not read |

The early reference practitioner's intake is likewise **records** in structure 2,
not a separate questionnaire.

## 2. Overlap and divergence

The narrative core is shared. Structures 1 and 3 both ask for the same nine or
ten topics: origin, the work, the people served, resistance and boundaries,
expression/delivery, vision, reality check, final reflection; structure 3 adds
philosophy. This is the "worldview preservation" layer (blueprint Layer C).

| Topic | S1 Clarity | S2 STB | S3 Telemetry |
|---|---|---|---|
| Identity / contact | name, email, phone | name, email, phone, location, time zone, links | name only (respondent captured by system) |
| Narrative core (origin, work, people, vision…) | ✅ free text | partial (`Your Work / Gift`, `People You Serve`, `What Brings You Here`) | ✅ 10 prompts |
| Offers and revenue | `Offer / Revenue` (one free-text field) | `Current Offers`, `Current Revenue Range` | revenue range ×2 (duplicate), price point, best month, most profitable offer |
| Lead sources, conversion, baseline numbers | ❌ | `Source / Origin` (how *they* found us, not their leads) | ✅ lead sources, conversion reality, referral dependence, baseline-numbers prompt, measurement readiness |
| Pressure points / support wanted | ❌ | ✅ structured multi-selects | free text (bottlenecks, 90-day improvement) |
| Capacity and boundaries | `Resistance / Boundaries` | `Visibility Comfort`, `Avoidance Pattern` | ✅ 90-day volume prompt, capacity |
| Delivery model | ❌ | `Preferred Delivery`, `Desired Business Model` | support/handover/approval expectations |
| Assets and access | `Asset Links`, `Drive / Data Room URL` | same | assets/access prompt |
| Consent | ✅ checkbox | ✅ checkbox | ❌ |
| Pipeline status | 9 states | 6 states | 3 states |
| Birth date, place, time | ❌ | ✅ (3 fields) | ❌ |

## 3. Findings

**F1 — The blueprint's "richest schema" claim is contestable.** Blueprint §6.1
names `Client Clarity Intake` as source of truth because it is "richest". By
structured-field count, `SPARK LAB-STB Intake` (34 properties, 11 structured) is
richer in Layer A material; `Client Clarity Intake` is richer in its pipeline and
narrative fields only. This is a choice for the owner (D-018), not a
correction to the blueprint.

**F2 — Nothing captures the booking path.** None of the structures records what
the Business Diagnostic needs: where enquiries arrive and land; which site,
booking tool, form and CRM are in use; who answers and how fast; the steps from
enquiry to booked call; whether read access to site, booking tool and inbox is
granted; enquiry and booking counts for a baseline period. Structure 3's
baseline-numbers prompt and measurement-readiness field come closest. These are
**new fields** that the first paid diagnostics should produce (D-005), not
something to invent speculatively.

**F3 — Consent is partial and unscoped.** Two of the three populated structures
have a consent checkbox; the third does not. No structure records *what* was
consented to (use in a diagnostic, deposit into the taxonomy, naming as a
reference), nor that the practitioner reviewed the framing. In the sample
records returned, the flag was unchecked on records containing substantive
narrative. That is three samples of unknown population, not a rate.

**F4 — Data minimisation.** Fields that the Business Diagnostic does not need:

- `Birth Date`, `Birth Place`, `Birth Time` (structure 2) — drop for the
  diagnostic; if a later worldview layer needs them, collect only at Layer C with
  an explicit purpose.
- Open narrative prompts invite health content (CLAUDE.md rule 5). Each needs a
  "do not include health details" instruction, as the reference build's
  replacement booking note already does (TX-DATA-001).
- `Internal Review Notes` and similar fields hold the assessor's inferences about
  a person; they are Class B and must not be reused as templates.
- The 14-Point Bleed Map's "rate your energy 1–10" diagnostic question sits close
  to wellbeing data. Prefer a business-capacity framing (sessions per week the
  practitioner can sustain).

**F5 — Client identity is embedded in the schema.** Three property labels in
structure 3 contain the client's brand name, so it is not reusable as a template
without parameterising. This is the practical meaning of Class C configuration
in `ARCHITECTURE.md`.

**F6 — Duplicates and legacy.** Structure 3 has two near-identical "Business /
Revenue Reality" properties (one with a trailing space) and two revenue-range
properties (one select, one multi-select). Structures 1 and 2 carry an
`Airtable Record ID` property, implying a former Airtable sync whose state is
**unverified**.

**F7 — Typing the practitioner too early.** `Template Type` (4) and `Client Type`
(7) overlap and pre-sort practitioners into categories. This pulls toward
multi-tenant templating, which is deferred until the third practitioner
(CLAUDE.md rule 6). Treat as a free tag until real variation is known.

**F8 — Three status vocabularies.** 9, 6 and 3 states with different names for
equivalent stages. A unified lifecycle is needed before any tooling.

## 4. The doctrine the owner already wrote: consent before extraction

The workspace contains a doctrine page that says, in summary: the system must
never extract faster than the practitioner can consent, integrate and
understand; the sequence is **experience, consent, document, build, publish**; no
private material becomes public by default; no transcript becomes marketing copy
and no spontaneous phrase becomes a hook until the client reviews and approves.
It closes with a seven-question safety check before turning client material into
an asset. It directly supplies the rule F3 is missing.

**Not adopted.** Whether and how to make it binding is D-019. The source page also
contains a boundary layer specific to one named practitioner; that part must not be
carried into any reusable document.

## 5. Proposed path (for the owner; nothing built)

1. Owner decides the base schema (D-018). Defensible options: (a) structure 2 for
   Layer A, structure 3 as donor for Layer B, structure 1 for Layer C and
   lifecycle; or (b) start from structure 1 and import from the others.
2. Write the universal intake as a **field catalogue** in `intake/` with a
   provenance column (which structure each field came from), a keep/drop/add
   decision per field, a health-data guard note on every free-text field, and the
   F2 booking-path fields marked "to be validated in diagnostics 1–3".
3. Do **not** create or change anything in Notion until D-017 (storage) is decided.
4. Fill or delete the blank `CLIENT INTAKE - STB` template. An empty
   canonical-looking template is worse than none (blueprint §6.1).

`intake/` is deliberately **not created** in this phase (requirement 5, D-018).
