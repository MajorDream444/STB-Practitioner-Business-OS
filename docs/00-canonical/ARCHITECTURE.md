# Architecture — Data and Asset Boundaries

**Status:** Boundary definitions APPROVED by decision D-010 and D-009.
Storage mechanics are **PROPOSED, not approved** — see D-017 and
[the proposal](../01-decisions/PROPOSAL-engagement-storage.md).
**Scope:** what kinds of thing exist in the Practitioner Business OS, where each
kind may live, and how anything moves between them. It does not design software;
no platform is being built (D-001, CLAUDE.md rule 6).

---

## 1. The four classes

Everything the business touches belongs to exactly one class. If it seems to
belong to two, split it.

| Class | What it is | Examples | Who controls it | May live in this public repo? |
|---|---|---|---|---|
| **A. Reusable product IP** | Knowledge and code that carries no client identity and improves with every engagement | Defect taxonomy entries, intake *question wording* (not answers), blueprint *templates*, test patterns, generic components, doctrine, decision log | The owner (SPARK LAB–STB / HAMAL) | **Yes — this is the only class that belongs here** |
| **B. Client-private records** | Anything that is about, or came from, a specific practitioner | Intake responses, blueprints written for them, audit findings naming their site, call notes and transcripts, baseline numbers, photographs, testimonials, hours logs tied to a name, consent register | The **practitioner** is the data controller; HAMAL acts at most as processor under a DPA (blueprint §4) | **Never** |
| **C. Configuration** | Parameters that make a generic component work for one engagement | Where an enquiry form should send data, which booking tool is in use, copy strings, brand tokens | Practitioner-owned values, HAMAL-managed | **Never** the values. The *schema* of the configuration (names and types of fields, no values) may be Class A |
| **D. Deployments** | Running systems and the credentials that operate them | A practitioner's website, their CRM, their form, API keys, domain and DNS access | The practitioner owns the accounts; HAMAL holds delegated access only for the engagement | **Never**. Credentials never appear in any repository, public or private |

Two further rules cut across all four:

- **No health data, anywhere, at any stage** (CLAUDE.md rule 5; GDPR Art. 9).
  Free-text intake fields invite it; see §4.
- **No client-of-client personal data.** Stage 1 handles none; Stage 2 touches
  it only inside the practitioner's own systems.

## 2. Classification test

Ask in order. The first "yes" decides.

1. Could a stranger identify a person, their business, their site, or their
   audience from it? → **Class B**.
2. Is it a credential, token, key, form URL, spreadsheet link, domain access, or
   any link that grants access to something? → **Class D**.
3. Is it a value that only makes sense for one engagement? → **Class C**.
4. Is it knowledge or code that would be identical for the next practitioner? →
   **Class A**.
5. Not sure → treat as **Class B** until the owner says otherwise.

## 3. How material moves between classes — the deposit gate

The compounding rule (D-005) requires every engagement to *deposit* something
reusable. Deposits flow **only from B to A**, and only through this gate:

```
Class B (private)  ──►  sanitise  ──►  review  ──►  Class A (this repo)
 engagement record      remove identity    owner     taxonomy entry / intake
                        and specifics      checks    question / component / test
```

A deposit may enter this repository only if **all** of these hold:

- [ ] No name, business name, handle, URL, email, phone, photograph, or
      distinctive phrasing from the source.
- [ ] Stated as a pattern ("an enquiry form routed to a personal inbox"), not as
      an anecdote about a recognisable situation.
- [ ] Carries an **evidence label and sample size** (see
      [taxonomy](../../taxonomy/README.md)) — never an implied frequency or outcome.
- [ ] The practitioner has not objected, and for anything derived from their
      own words, has reviewed the framing (consent-before-extraction is proposed
      doctrine, D-019, not yet adopted).
- [ ] `python3 scripts/check-docs.py` prints `OK`.

Nothing flows from A back into B automatically. A practitioner's records are
never edited by pulling updates from the product repository.

## 4. Consequences for intake

- **Question wording is Class A. Answers are Class B.** The template is public;
  every filled-in copy is private.
- Open narrative fields are the main route by which health or third-party
  personal data enters. Intake design must prefer structured, business-fact
  fields, and any narrative field must say what *not* to write.
- Data that is not needed to produce the diagnostic is not collected (data
  minimisation). The reconciliation of existing intakes lists candidates that
  fail this test.

## 5. Consequences for code

- A reusable component takes its client-specific values as **injected
  configuration** (Class C) and ships with none. The reference build's intake
  router is an example of a component that must be generalised before reuse
  because it hard-codes one practitioner's form.
- Multi-tenant templating is deliberately deferred until the third
  practitioner (CLAUDE.md rule 6). Until then, a second site is built by copying
  and editing, and the copy lives in the practitioner's own repository.
- Tests that guard a defect class (for example "no untracked submission path")
  are Class A and reusable.

## 6. Consequences for deployments

- Each practitioner's live system sits in **their** accounts. HAMAL's access is
  delegated, scoped, time-boxed, and revocable at handover.
- Credentials live in a secrets manager, never in a repository, and never in
  chat transcripts or documents.
- A deployment is not "done" until the practitioner's own test enquiry reaches
  their own CRM, witnessed by them (blueprint §3 and §6.4).

## 7. What is not decided here

| Question | Where it is tracked |
|---|---|
| Which private store holds Class B records | D-017 (proposal) |
| Which existing intake is the base schema | D-018 |
| Whether consent-before-extraction becomes binding doctrine | D-019 |
| Whether this repository itself should become private | Owner's call under D-010; not proposed |
| DPA wording and the refund policy | D-022 |

This document records boundaries. It does not authorise building storage,
automation, or a platform.
