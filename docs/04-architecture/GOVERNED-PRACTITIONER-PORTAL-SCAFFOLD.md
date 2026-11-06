# Governed Practitioner Portal — Technical Scaffold and Pat Handoff

**Status:** Proposed future platform pattern; documentation only  
**Canonical product:** STB Practitioner Business OS  
**Owner for approval:** Major Dream Williams  
**Implementation lead:** Pat / HAMAL engineering  
**Date:** 6 November 2026

## 1. Decision boundary

This document translates the SPARK LAB concept demonstration into technical scaffolding for the STB Practitioner Business OS.

It does **not** change the approved product direction:

- done-for-you service first;
- platform later;
- Stage 1 diagnostic is the only cold offer;
- Stage 2 is scoped from the diagnostic;
- no Stage 3 until three measured Stage 2 engagements exist;
- no outcome claims without measured evidence;
- no multi-tenant platform before real delivery variation is known.

The dashboard and agent engine shown in the concept screens are proposed future infrastructure, not current product capability.

## 2. Core operating pattern

Practitioner requests → HAMAL prepares → practitioner approves → authorized work executes → result is verified → evidence returns to practitioner.

The pattern must preserve four truths:

1. The practitioner remains in control.
2. Consequential work requires recorded approval.
3. Provider success is not the same as a verified business result.
4. Every engagement deposits a reusable rule, component, test, or taxonomy entry.

## 3. Current versus future

### What exists today

- canonical commercial blueprint;
- approved three-stage structure;
- scope and claims discipline;
- provenance and reuse constraints;
- selected reusable enquiry and honesty-state components;
- manually delivered HAMAL work supported by bounded assistant skills;
- no validated demand;
- no paid practitioner evidence;
- no multi-tenant portal;
- no live automated agent engine.

### Proposed future platform

- practitioner dashboard;
- request and preparation workspace;
- approval gate;
- authorized connector execution;
- verification receipts;
- exception queue;
- evidence tracker;
- reusable defect taxonomy;
- school-partner view;
- engineering observability.

Every screen must visibly label live, manual, proposed, blocked, and retired capabilities.

## 4. Product surfaces

### 4.1 Practitioner dashboard

Recommended modules:

| Module | Purpose |
|---|---|
| Enquiries & Bookings | Current journey state and verified exceptions |
| Clients | Relationship state without ingesting health data |
| Offer & Pathway | Approved offer, page and booking flow |
| Needs Attention | Decisions, failures and owner actions |
| Evidence | Baseline, observed results and confidence |
| Requests | New work requested in the practitioner's own words |
| Approval Queue | Exact artifacts awaiting a decision |
| Delivery History | Verified work and operational receipts |

The dashboard should lead with exceptions and decisions, not vanity metrics.

### 4.2 HAMAL delivery view

Internal view for:

- diagnostic preparation;
- scope;
- creative and systems work;
- approval status;
- connector permissions;
- execution;
- verification;
- evidence capture;
- learning deposit.

### 4.3 School-partner view

Future scope only.

A school may eventually support graduates without accessing client records. A school view may see:

- graduate participation;
- implementation milestones;
- support status;
- aggregate completion;
- consented evidence.

It must not expose:

- practitioner client records;
- health data;
- private intake;
- practitioner credentials;
- unrestricted workspace content.

No school-partner feature should be marketed or built before the practitioner delivery model has paid evidence.

## 5. Shared workflow state machine

Canonical happy path:

1. REQUESTED
2. ARCHITECTED
3. PREPARED
4. AWAITING_APPROVAL
5. APPROVED
6. EXECUTING
7. VERIFYING
8. RETURNED
9. LEARNING_DEPOSITED
10. CLOSED

Exception states:

- REJECTED
- CHANGES_REQUESTED
- BLOCKED
- FAILED
- CANCELLED
- EXPIRED

Rules:

1. A draft is not approval.
2. Approval binds an exact artifact hash, action scope and destination.
3. Material changes invalidate approval.
4. Execution requires a registered capability and idempotency strategy.
5. Return requires domain verification, not only an API response.
6. Close requires a reusable deposit under the approved compounding rule.
7. Failures create a visible owner, next action and due date.

## 6. Minimum platform entities

### PractitionerInstance

- id;
- owner identity;
- business identity;
- plan/stage;
- approved connectors;
- data region;
- retention policy;
- workspace status.

### WorkRequest

- id;
- practitioner instance;
- request in the practitioner's words;
- category;
- sensitivity;
- stage and scope reference;
- owner;
- status;
- timestamps.

### PreparedArtifact

- exact content;
- source references;
- assumptions;
- unresolved decisions;
- content hash;
- status and version.

### ApprovalReceipt

- approver;
- artifact hash;
- decision;
- allowed actions;
- destinations;
- expiry;
- timestamp.

### ExecutionReceipt

- capability;
- connector;
- idempotency key;
- result;
- external reference;
- redacted log;
- timing.

### VerificationReceipt

- expected result;
- observed result;
- test type;
- evidence reference;
- witness;
- confidence.

### ExceptionRecord

- severity;
- owner;
- next action;
- due date;
- retry eligibility;
- resolution evidence.

### EvidenceBaseline

- metric definition;
- measurement window;
- source;
- baseline count;
- consent status;
- known limitations.

### LearningDeposit

- engagement reference;
- type: question, defect, component, test, playbook rule;
- taxonomy category;
- reusable artifact reference;
- privacy review;
- accepted by;
- version.

## 7. Capability registry

Each capability requires:

- purpose;
- allowed roles;
- stage eligibility;
- required approval;
- allowed data classifications;
- connector and permission scopes;
- idempotency strategy;
- verification method;
- failure owner;
- rollback or compensating action;
- audit retention.

Initial read-only capabilities:

- inspect approved site and booking configuration;
- read business-level inquiry and booking counts;
- list operational exceptions;
- inventory approved business assets;
- summarize request status.

Initial prepare-only capabilities:

- draft diagnostic;
- prepare severity-ranked defect list;
- draft offer/page;
- draft booking flow;
- prepare CRM configuration plan;
- prepare test journey;
- prepare operating instructions.

Initial executable capability should be low-risk and reversible, such as creating a draft page or draft calendar/booking configuration.

Explicitly prohibited in V1:

- financial transactions;
- refunds;
- autonomous client communication;
- health or therapy intake ingestion;
- client-of-client PII storage;
- fabricated bookings or scarcity;
- outcome promises;
- publishing without exact approval;
- unrestricted practitioner account access;
- cross-practitioner data sharing.

## 8. Delivery mapping

| Platform stage | Approved STB delivery stage |
|---|---|
| Request | Practitioner request or diagnostic input |
| Architect | Diagnostic and scope definition |
| Prepare | Draft page, booking flow, CRM plan and instructions |
| Approve | Practitioner reviews exact artifacts |
| Execute | HAMAL performs scoped work in practitioner-owned accounts |
| Verify | Practitioner's own test enquiry reaches the intended system |
| Return | Result and receipts appear in dashboard |
| Learn | Reusable artifact enters reviewed taxonomy |

The platform must not imply that all components are included. Stage 2 remains a menu selected by the diagnostic, with out-of-scope items named in writing.

## 9. Privacy architecture

The canonical privacy rule remains binding:

- no health data;
- no client-of-client PII in Stage 1;
- practitioner remains controller of their systems;
- a DPA is required before Stage 2 work that makes HAMAL a processor;
- client records stay in practitioner-owned systems;
- school partners see participation, not records.

Technical requirements:

- tenant isolation;
- least-privilege OAuth;
- named accounts;
- secret-store integration;
- separate dev/test/prod;
- redacted logs;
- configurable retention;
- export and deletion;
- access revocation;
- auditable approval and execution;
- no production data in fixtures or screenshots.

## 10. Honest-state UI requirements

The UI must never claim:

- a booking exists when it is only a preference;
- an email was sent when a provider call was skipped or failed;
- a page is live when it is a draft;
- scarcity or capacity without source data;
- a conversion or revenue result without a measured baseline and after-state;
- a platform feature exists because a concept screen exists.

Required badges:

- Live
- Manual
- Proposed
- Blocked
- Not built
- Verified
- Needs evidence

## 11. Architecture boundaries

Suggested bounded components:

1. Portal UI
2. Identity and role service
3. Work orchestration service
4. Artifact/version service
5. Approval service
6. Capability registry
7. Connector adapters
8. Verification service
9. Exception service
10. Evidence and learning service
11. Audit log

Do not begin by building a generalized autonomous agent platform.

Implementation sequence:

- document manual workflow;
- model state and receipts;
- build read-only visibility;
- build preparation and approval;
- add one low-risk execution;
- verify;
- only generalize after repeated paid delivery.

## 12. Pilot sequence

### Phase 0 — product blockers

- owner confirms monthly revenue floor;
- pricing decision recorded;
- refund policy drafted;
- DPA drafted if Stage 2 touches practitioner systems;
- one legally reusable sample exists.

### Phase 1 — manual delivery with receipts

Deliver paid diagnostics manually while recording:

- request;
- prepared artifact;
- approval;
- time spent;
- defect taxonomy;
- outcome limitations.

### Phase 2 — read-only practitioner portal

Show:

- work status;
- decisions required;
- current artifacts;
- exceptions;
- evidence;
- delivery history.

### Phase 3 — preparation and approval

Allow:

- exact artifact review;
- comments;
- approve/reject/changes requested;
- version locking;
- scope-bound receipts.

### Phase 4 — one authorized execution

Choose a reversible action. Do not start with payments, outbound client email, CRM bulk writes, or health-adjacent intake.

### Phase 5 — compounding measurement

Measure:

- human hours per engagement;
- repeated defects;
- reusable components;
- tests added;
- time saved;
- evidence completeness.

If engagement six is not materially easier than engagement two, the system is not compounding.

## 13. Pat handoff

Pat should return:

1. a current/manual/proposed/blocked architecture map;
2. a data-flow diagram;
3. a role and permission matrix;
4. entity schemas and state transitions;
5. a capability registry format;
6. a tenant-isolation and secret-management plan;
7. the first reversible execution candidate;
8. verification and exception rules;
9. estimates by phase;
10. explicit non-goals;
11. a path from manual service receipts to future platform;
12. a decision list for Major, without converting recommendations into approvals.

## 14. Acceptance criteria

The scaffold is ready for implementation review when:

- it does not contradict the canonical blueprint or decision log;
- platform language remains internal until approved;
- every consequential action has an approval and verification rule;
- no health data is required;
- school-partner access excludes client records;
- honest-state labels are implemented;
- failures have owners;
- evidence and learning deposits are first-class;
- the first build remains a service-enablement layer, not speculative SaaS.

## 15. Final principle

The system is not valuable because it looks autonomous.

It is valuable when it lets a practitioner request work in plain language, stay in control, receive a verified result, and own a system they can operate—while every delivery makes the next delivery safer and more efficient.