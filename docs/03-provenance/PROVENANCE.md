# Provenance & Reuse Constraints

What exists, where it came from, and what may legally and ethically be reused.

---

## Source material

| Source | Location | Status |
|---|---|---|
| Flo reference implementation | `MajorDream444/STB-Come-Back-To-Yourself` | Archived. Code source, **not a credential**. |
| ECC integration audit | same repo, `docs/ecc-audit/` | Engineering tooling evaluation. Referenced, not duplicated here. |
| Stage 0 remediation | same repo, `docs/ecc-audit/stage0/` | Completed; produced the reusable components below. |
| LLM Council 2026-10-14 | `docs/02-evidence/council-20261014/` | Copied here — product evidence. |
| Notion: Client Clarity Intake | Notion workspace | **Richest schema** — base for Universal Intake V1. |
| Notion: Theo — Business Telemetry intake | Notion workspace | Source of commercial-reality fields. |
| Notion: Sheetal — Shakti System intake | Notion workspace | Source of worldview-preservation fields. |
| Notion: SPARK LAB OS | Notion workspace | Documents the intended flow. |
| Notion: `CLIENT INTAKE - STB` | Notion workspace | **Blank.** A named page is not a working form. Fill or delete. |

---

## Reusable components already proven

Extracted from the Flo implementation and verified by passing tests
(64/64 at `STB-Come-Back-To-Yourself@220d831`). Carry no client identity.

| Component | What it does | Why it matters |
|---|---|---|
| `src/lib/intake.ts` | Single enquiry routing point to the approved intake form. **No `mailto:` path exists in it by design.** Returns a result object; never throws; exposes a copyable summary when routing is blocked. | Prevents the silent downgrade to email that bypasses the CRM |
| `no-untracked-submission.test.ts` | Fails the build if any component reintroduces a `mailto:` submission or advertises invented scarcity | Makes the defect unrepeatable rather than merely fixed |
| `asset-register.test.ts` | Fails if a declared approved asset is missing, or a referenced image would 404 | Catches the "approved image doesn't exist" class before deploy |
| Honest-state patterns | No confirmation without confirmation; blocked-popup fallback; preference ≠ booking | The reference build claimed bookings it had not made |

**Known trap, worth carrying forward:** on an SPA, a missing asset can return
**HTTP 200 with `content-type: text/html`** via the index fallback. Asset checks
must assert content-type, not status.

---

## Constraints — binding

1. **Floortje de Liefde may not be referenced** — name, photographs,
   testimonials, or recognisable description — in any public case study,
   marketing material or pitch **without her written permission**. She was an
   unpaid research participant, she has disengaged, her site was never publicly
   deployed, and no outcome data exists.
2. **No outcome claim from the Flo engagement.** No revenue, booking or
   conversion improvement. See `DECISION-LOG.md` C-001.
3. **Strip identity before reuse.** Photography, copy, testimonials, offers and
   prices are hers. The components are reusable; the identity is not.
4. **Two image files in the Flo repo are named `regenerated_image_*`**,
   suggesting generative output. Confirm against the "preserve original
   photographs" rule before any of them is ever reused.
5. **No health data at any stage.** Special-category under GDPR Art. 9.

---

## Deliberately deferred

- **Multi-tenant configuration.** Build the second practitioner site by copying
  and editing. Extract a template at the **third**, when real variation is known
  rather than guessed.
- **A diagnostic "engine" as software.** V1 is a prompt plus a fixed template.
  Resist building until ~10 diagnostics have shown what the output should contain.
- **Stage 3 pricing.** Until three Sprints have before/after data.

---

# Addendum — 2026-10-14 read-only reconciliation

Appended under decision D-012. Nothing above was edited. Historical repositories
and the Notion workspace were read, not modified. No client responses, contact
details, photographs or credentials were imported.

## Verification record

| Claim | Result |
|---|---|
| Blueprint V1 committed as `0f803e1` on `claude/magical-hopper-umi99c` in the reference repository | **Verified.** One file, 323 lines. The branch tip is `af04c8f`, which removed it and left a "moved" notice, so the original survives only in history |
| Blueprint here equals the original | **Verified.** Differs in three places only: the header placement note, the "intended/canonical home" line, and the BP-D3 row |
| Council transcript and report here equal the originals (`b185843`) | **Verified.** Byte-identical |
| Reference build passes 64/64 tests at `220d831` | **Reproduced** on a clean install. See the typecheck caveat in `taxonomy/v0.0.md` (TX-QA-001) |
| The reference build's defects (mail-client submission, invented scarcity, health checklist, unmounted booking component, false confirmation) | **Re-observed** in the pre-fix source, except where `taxonomy/v0.0.md` marks a lower evidence label |
| "HTTP 200 with HTML content type" asset trap | **Unverified** (EQ0). Stated above; not found demonstrated in the test code |
| Constraint 4 above: "two image files named `regenerated_image_*`" | **Correction:** the branch tree lists **four** in `src/assets/images/` (and copies in a nested folder). The constraint still stands; the count was wrong |

## Source inventory

Read-only shallow reads on 2026-10-14. "Reuse stance" is a proposal, not a decision.

| Source | Read at | Relevant content | Reuse stance |
|---|---|---|---|
| Reference implementation repository | branch tip `af04c8f`; `main` `cfc9d84` | Intake router and its tests; ECC audit and Stage 0 report | Code patterns only, identity-stripped (see constraints above) |
| `SPARK-LAB-STB` | `d6de649` (16 files) | `doctrine-upgrades/`: 14-Point Bleed Map, public-lexicon translation layer, worldview-extraction axiom; repo operations rules, including a "promotion standard" for bringing reference material in | Doctrine **inputs**. Not adopted. The bleed map is a business-level crosswalk target for the taxonomy; the lexicon is input to R-003 (naming) |
| `STB-COMMAND-CENTER` | `e60e1ea` (28 files) | Staged build plan; a data schema with tables for practitioners, daily entries, evidence logs, sprint tasks, offers, AI suggestions, and access policies (file and table names only; contents not reviewed); two short doctrine files (names only; not read) | Operational reference. The schema has **not** been reviewed for health or personal data and must be before any reuse |
| `business-pressure-test-scratch-off` | `699a3e5` | A scored self-assessment questionnaire (question and option wording with numeric scores); a submission endpoint | Question wording may inform Layer A. **Scores are unvalidated.** Do not present a score as a finding |
| `HAMAL_MOB_PLAYBOOKS` | `9291d06` (189 files) | Playbook, SOP and context templates; a client-onboarding payment/signature playbook; audit and rubric folders | Template structure only. Contains agent-framework artefacts that are **not imported** (instruction: no broad frameworks) |
| A practitioner-specific implementation repository (name and revision withheld) | n/a | A full single-client implementation with payments, expiring signed download links and scheduled sequences | **Client-specific. Not a template.** One pattern worth studying: expiring signed links instead of public paths. Identified in the owner-only record, not here |
| `hamal-agent-registry` | `96639f8` (2 files) | An agent-campus handover document | **Not assessed in depth.** Relevance unverified |
| Notion workspace | read 2026-10-14 | Four intake structures, one doctrine page on consent before extraction | See [the reconciliation](../02-evidence/intake-reconciliation-20261014/RECONCILIATION.md) |

**Privacy indicators.** The reads found indicators of the same class of exposure
as the reference repository in some of the public historical repositories. Per
D-013, specifics are **intentionally not recorded in this public repository**.
They are in an owner-only checklist delivered outside it. Scope extension is
D-023. Nothing was changed.

## Missing or unverified dependencies and skills

| Item | Referenced by | Status |
|---|---|---|
| `stb-doorkeeper`, `stb-offer-architect`, `stb-evidence-tracker` | Blueprint §6.4 delivery playbook | Exist as **user-level skills** in the owner's environment. **Not found in any repository read**, so they are unversioned, not reviewable, and not reproducible by another agent. Their contents were not inspected |
| `stb-continuity-keeper`, `stb-trip-wire-detector`, `stb-webinar-os`, `stb-gumroad-asset-builder` | Named in council and ECC materials | Same as above. Not needed for V0.1 |
| `hamal-learning-loop` | Blueprint §6.4 ("spec'd") | Mentioned in the ECC audit's skill specs and implementation plan. That spec file states its skills are **specified, not built**. Nothing exists to run |
| Notion workspace (processor) | Intake, doctrine | Plan, region and sub-processor terms **unknown**; relevant to D-017 and D-022 |
| Airtable | `Airtable Record ID` properties; a setup script in a historical repo | Whether any sync still runs is **unverified** |
| Google Forms and Sheets | The reference build's intake and CRM | Belong to the archived practitioner. Class D. Not reusable |
| Email, hosting, database and payment vendors | Several historical repos | **Not dependencies of this repository.** None are needed for V0.1 |
| Agent-framework artefacts | Two historical repos | **Not imported.** No hooks activated |

## Proposed next provenance actions (none taken)

1. Decide where the `stb-*` skills should live so they are versioned (candidate:
   a private repo; they may contain methodology). Until then the blueprint's
   delivery playbook rests on unversioned inputs.
2. Review the command-centre schema for personal and health data before reuse.
3. Record the outcome of D-023 (privacy scope) once decided.
