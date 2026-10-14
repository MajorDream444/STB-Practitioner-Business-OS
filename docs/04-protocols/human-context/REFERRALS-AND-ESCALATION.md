# Human Context — Referrals and Escalation Protocol

> **DRAFT — INACTIVE.** Not approved for use. See [the index](README.md) and
> D-035. **The referral directory is EMPTY and must stay empty until entries pass
> the verification checklist (D-033).** Do not fill it from memory, from an AI
> system, or from a web search. **The safety procedure in section 4 must be
> reviewed and completed by a qualified mental-health professional before
> activation.** No emergency numbers appear here on purpose: they must be copied
> from official sources for each jurisdiction and verified.

## 1. Two pathways

| Pathway | Who qualifies |
|---|---|
| **Bali-based** | Verified, appropriately licensed or credentialed mental-health professionals able to support clients locally, including English-speaking international clients where available |
| **Online** | Verified, qualified professionals **authorised to serve clients in the jurisdiction where the client is physically located** (not merely where they live) |

## 2. Directory structure (schema only — no entries)

| Field | Notes |
|---|---|
| `entry_id` | |
| `status` | `proposed`, `verified`, `suspended`, `retired`. Only `verified` entries may be offered |
| `pathway` | `bali`, `online` |
| `name` | Held only once verified and listed with consent |
| `credential_type` / `issuing_body` / `licence_reference` | As shown on the official register |
| `register_checked` / `register_checked_on` | Which official register, and when |
| `jurisdictions_served` | For `online`: the jurisdictions they are authorised to serve |
| `delivery` | `in_person`, `online`, `both` |
| `languages` | |
| `support_areas` | In the professional's own words |
| `fee_range` / `availability` | Optional; may go stale |
| `conflict_declaration` | Confirms **no referral fee, commission or other benefit** to HAMAL or the facilitator |
| `listing_consent` | The professional agreed to be listed |
| `verified_by` / `verified_on` | |
| `reverify_due` | Interval set by the owner |

## 3. Verification checklist (per entry; all must pass)

- [ ] Identity matches an entry on the **official register** of the issuing body,
      and the check is recorded (register, date).
- [ ] Licence or registration is **current**, with no restriction that conflicts
      with the support offered.
- [ ] Scope of practice covers the kind of support a practitioner might ask for.
- [ ] **Authorised** to serve clients in each jurisdiction stated (essential for
      the online pathway).
- [ ] Languages and delivery mode stated and confirmed with the professional.
- [ ] Contact route verified by a **test contact**, not assumed.
- [ ] `conflict_declaration` signed: no referral fees or benefits.
- [ ] `listing_consent` obtained.
- [ ] Complaints or disciplinary status checked where the register provides it.
- [ ] A second person reviewed the entry where possible.
- [ ] `reverify_due` set; entries not re-verified on time become `suspended`.
- [ ] A removal route exists (the professional or the owner can withdraw the entry
      at once).

## 4. Safety escalation (skeleton — requires qualified professional review)

Principle: when the practitioner may be at risk, **the business conversation
stops**. A human facilitator handles this; **AI agents never do** (D-027).

| Level | Situation | Facilitator action |
|---|---|---|
| 1 | Ordinary strong emotion (for example shame, overwhelm) | Acknowledge, offer a choice (pause, continue business work, or stop for today), do not probe, record only what is approved |
| 2 | The practitioner wants to work on the emotional material itself | Offer referral information from `verified` entries only. They choose. HAMAL continues the business work within their boundaries. No pressure, no follow-up probing |
| 3 | Any indication of risk to the practitioner's safety or someone else's | Stop the business conversation. Follow the steps approved by the reviewing professional (below) |

**Level 3 steps — to be written and approved by a qualified mental-health
professional, and checked against the law of each jurisdiction:**

1. Stop the business conversation and stay engaged with the person.
2. Use the location and contact route confirmed at the start of the conversation.
3. Direct the person to the **official emergency service or crisis support for
   their location** (table below).
4. Whether and when the facilitator may contact emergency services on the
   person's behalf is **a jurisdiction-specific question for the reviewing
   professional and counsel**. It is not decided here.
5. Record minimally: that it happened, when, and what was done. No content.
6. Follow up with the person at a time they agree, then debrief with the owner.
7. Review the protocol afterwards.

### Emergency contacts by jurisdiction (to be filled from official sources)

| Jurisdiction | Emergency number | Crisis support | Official source | Verified on | Verified by |
|---|---|---|---|---|---|
| *(empty)* | | | | | |

A jurisdiction row is added only when its source is recorded and verified. If a
practitioner is in a jurisdiction with no verified row, the facilitator **does not
proceed with Human Context** for that conversation.

## 5. Non-urgent referral conduct

Offer information, not instructions. Never suggest the practitioner needs help.
Never receive anything in return for a referral. Never follow up to ask whether
they went.
