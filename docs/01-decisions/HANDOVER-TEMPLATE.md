# Synchronisation Handover Template

Use this to hand a decision from strategy discussion into implementation. One
per major decision. It exists so an implementing session does not have to
reinterpret a whole conversation, and cannot mistake discussion for direction.

Keep it short. If it exceeds a page, the decision is not yet made.

```markdown
## Handover — <short title> · <date>

### Decision
<One or two sentences. What was decided, in the imperative.>

### Status
APPROVED | RECOMMENDED | EXPLORATORY

### Supersedes
<Prior decision IDs this changes or overrides, or "nothing">

### Scope — do
- <specific, bounded item>

### Scope — do NOT
- <explicit out-of-scope items; this section prevents more rework than any other>

### Constraints
- <money, legal, privacy, consent, naming, deployment limits>

### Where it lands
Repository: <repo> · Path: <path> · Branch: <branch> · Merge: yes/no

### Evidence this rests on
- <links or paths; mark anything unverified as unverified>

### Open questions I am NOT asking you to resolve
- <so they are not silently answered by assumption>

### Done looks like
- <observable, checkable condition>
```
