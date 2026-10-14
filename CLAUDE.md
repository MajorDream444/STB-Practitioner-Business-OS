# CLAUDE.md — STB Practitioner Business OS

## What this repository is

The canonical home for the SPARK LAB–STB product. Commercial model, delivery
architecture, and reusable practitioner infrastructure.

## Read these before acting

| Question | Source |
|---|---|
| What is sold, how, at what price | `docs/00-canonical/PRACTITIONER-BUSINESS-OS-V1.md` |
| Is this approved or just suggested? | `docs/01-decisions/DECISION-LOG.md` |
| What may be reused or referenced | `docs/03-provenance/PROVENANCE.md` |
| Parent methodology | `SPARK-LAB-STB` repo |
| Historical reference implementation | `STB-Come-Back-To-Yourself` repo |

## Rules

1. **Recommended is not approved.** A council verdict, an audit finding, or an
   agent proposal is an *input*. It becomes a decision only when recorded as
   APPROVED in the decision log by the owner. Never implement a recommendation
   as though it were a decision.

2. **No outcome claims without measured evidence.** No conversion, booking or
   revenue improvement may appear in any document or client-facing material
   without a before/after from a named, consenting client. Current count: zero.

3. **Floortje de Liefde is not referenceable** — name, photographs,
   testimonials or recognisable description — without her written permission.
   Code components from her implementation are reusable; her identity is not.

4. **Never ship a fabricated state.** No invented scarcity, no confirmation of
   something the system cannot confirm, no "we have sent it" where nothing is
   sent. All three shipped in the reference build.

5. **No health data.** Special-category under GDPR Art. 9. Practitioners are in
   the EU/NL.

6. **Build nothing speculatively** that a paid engagement could produce as a
   side-effect. Multi-tenant templating is deliberately deferred until the third
   practitioner.

7. **Every engagement deposits something** — an intake question, a taxonomy
   entry, a component, or a test. That is the compounding rule (D-005), and it
   is approved.

8. **Append to the decision log; do not rewrite it.** Corrections go in as new
   entries under "Corrections to the record" so the history stays visible.

## Scope discipline

Do not widen a task beyond what was asked. If you find something outside scope,
report it with evidence and let the owner decide. State plainly when something
is unverified rather than presenting it as established.
