# AGENTS.md

Guidance for any coding or research agent working in this repository (Claude
Code, Codex, or other). This file adds no doctrine of its own.

**The operating rules are in [CLAUDE.md](CLAUDE.md). Read it first and follow
it exactly.** If this file and `CLAUDE.md` ever differ, `CLAUDE.md` wins.

## Order of authority

1. The owner's explicit instruction, once recorded in the decision log.
2. APPROVED entries in [the decision log](docs/01-decisions/DECISION-LOG.md).
3. [CLAUDE.md](CLAUDE.md) and the binding constraints in
   [Provenance](docs/03-provenance/PROVENANCE.md).
4. The [canonical blueprint](docs/00-canonical/PRACTITIONER-BUSINESS-OS-V1.md).
   Where it disagrees with the log on status, the log governs.
5. Evidence and audits (`docs/02-evidence/`): inputs only, never decisions.
6. Historical repositories: read-only reference, never modified from here.

## Agent-specific reminders

- This repository is **public**. Before adding any file, check it against the
  boundary in [ARCHITECTURE.md](docs/00-canonical/ARCHITECTURE.md). Client
  records, intake responses, contact details, credentials and photographs do not
  belong here.
- Before committing, run `python3 scripts/check-docs.py`. It must print `OK`.
- The Human Context protocols under `docs/04-protocols/` are **INACTIVE drafts**.
  Never collect, request, infer or store Human Context information, and never
  generate psychological interpretations of a practitioner (D-027, D-035).
- Cite blueprint §9 open decisions as `BP-D1`…`BP-D6`, never bare `D-1`…`D-6`.
- Do not install agent frameworks, add hooks, merge, deploy, or open pull
  requests unless the owner has asked for it in the current phase.
- When something is unverified, say so. Do not present a recommendation as a
  decision.
