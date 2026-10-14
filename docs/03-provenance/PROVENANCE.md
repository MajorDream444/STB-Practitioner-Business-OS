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
