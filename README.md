# Human Axis Reference Protocol

**Human Axis Reference Protocol（HARP）** is a machine-readable specification for keeping advanced AI systems anchored to human-originated purpose, value arbitration, authority boundaries, and irreversible-action governance.

HARP does not attempt to prevent AI systems from exceeding human performance in bounded operational domains.

Instead, it establishes a structural distinction:

```text
capability growth
        ≠
purpose self-authorization
```

An AI system may become faster, more accurate, more knowledgeable, and more autonomous in local tasks.

However, it must not silently remove human reference from:

* terminal-purpose formation;
* value arbitration;
* irreversible-action approval;
* authority-boundary revision;
* override and shutdown;
* civilizational direction.

> AI capability may expand.
> Human purpose reference must remain visible, reviewable, and recoverable.

---

## Status

```text
Specification: Human Axis Reference Protocol
Current version: v0.5.0-candidate
Specification stage: Candidate / Experimental
First specification arc: Complete
Schema format: JSON Schema Draft 2020-12
Example format: YAML
```

HARP v0.1 through v0.5 defines the first complete lifecycle of human-axis preservation:

```text
v0.1  Bind the AI system to a Human Axis
v0.2  Detect purpose drift
v0.3  Return unresolved questions to the Human Axis
v0.4  Apply self-limitation and irreversible-action gates
v0.5  Audit the Human Axis across distributed AI wings
```

---

# 1. Why this protocol exists

Many AI safety approaches begin with external restrictions:

* prohibit an action;
* limit a capability;
* monitor a system;
* stop the system after deviation.

These controls remain important, but they begin after the system has already been assigned a purpose and authority structure.

HARP begins one layer earlier.

It asks:

> What must an AI system continue to reference while becoming more capable?

The protocol answers:

> An AI system must remain connected to a declared human-originated purpose, retained human functions, machine-readable authority boundaries, and recoverable trace lineage.

HARP is therefore not primarily a capability-suppression protocol.

It is a **reference-preservation protocol**.

---

# 2. Human Axis and AI Gear

HARP uses a complementary structural model.

```text
Human Axis
├─ purpose ignition
├─ meaning
├─ value arbitration
├─ irreversible authority
├─ override
├─ shutdown
└─ civilizational direction

AI Gear
├─ search
├─ inference
├─ memory
├─ planning
├─ structuring
├─ optimization
└─ bounded execution
```

The Human Axis is not defined as a superior intelligence.

The AI Gear is not defined as an inferior intelligence.

Their functions are different.

The Human Axis provides the reference for why a system operates and which values and authority boundaries remain non-delegable.

The AI Gear transforms that purpose into analysis, planning, optimization, and execution.

A gear may rotate faster than its axis.

It may become more complex than its axis.

However, a gear that removes its own axis no longer has a stable reference for direction, authority, or purpose.

---

# 3. Normative principle

The central HARP principle is:

> An AI system MAY exceed human capability in bounded operational domains, but it MUST NOT remove human reference from terminal-purpose formation, value arbitration, irreversible-action approval, or authority-boundary revision.

This creates a strict separation between capability and authority.

```text
capability(system, action)
        does not imply
authority(system, action)
```

An AI system may know how to:

* publish content;
* spend funds;
* modify access controls;
* delete data;
* change infrastructure;
* alter its own workflow;
* delegate authority;
* create new agents.

That knowledge alone does not authorize the action.

---

# 4. Core design principles

## 4.1 Capability is not authority

The ability to perform an action does not grant permission to perform it.

Operational competence and terminal authority must remain structurally separate.

## 4.2 Human reference must be explicit

The responsible Human Axis, retained human functions, purpose statement, approval boundaries, and re-reference triggers must be machine-readable.

## 4.3 Terminal goals are not self-expandable

An AI system must not independently:

* create new terminal goals;
* remove human approval gates;
* rewrite authority boundaries;
* suppress Origin Traces;
* convert proxy metrics into terminal purposes;
* revoke human override or shutdown authority.

## 4.4 Ambiguity triggers re-reference

When purpose, value, scope, authority, or irreversible impact becomes ambiguous, the AI system must pause, defer, restrict, or escalate.

Silence must not be interpreted as approval.

## 4.5 Trace precedes trust

Purpose origin, decision traces, authorization records, and audit evidence must remain attached to the system lifecycle.

## 4.6 Local optimization must remain subordinate

Task completion, throughput, engagement, accuracy, cost reduction, risk reduction, and system continuity are proxy objectives.

They must not silently replace the declared human-originated purpose.

## 4.7 Distributed systems require a shared axis

Multiple AI wings may possess different roles, models, memories, and tools.

They must not independently create incompatible terminal-purpose centers.

## 4.8 Yin–yang, not top–bottom

HARP does not describe a simple hierarchy.

The human side does not replace AI computation.

The AI side does not replace human purpose formation.

The protocol preserves a complementary relationship in which neither side falsely claims structural completeness.

---

# 5. Protocol lifecycle

```text
Human Axis
    │
    ▼
Human Axis Binding Record
    │
    ▼
AI System or Multi-Wing AI
    │
    ├─ normal operation
    │
    ├─ Purpose Drift Detection
    │       │
    │       ▼
    ├─ Human Re-Reference Request
    │       │
    │       ▼
    ├─ Self-Limitation
    │       │
    │       ▼
    ├─ Irreversible Action Gate
    │       │
    │       ▼
    └─ Multi-Wing Human Axis Audit
            │
            ▼
       restore, restrict,
       rebind, suspend,
       or human-review
```

---

# 6. Specification layers

## v0.1 — Human Axis Binding Record

The Human Axis Binding Record declares the stable connection between an AI system and its human-originated purpose and authority structure.

It records:

* the AI system identity;
* the responsible Human Axis;
* retained human functions;
* the human-originated purpose;
* permitted capabilities;
* prohibited self-expansions;
* autonomous actions;
* approval-gated actions;
* never-autonomous actions;
* re-reference triggers;
* trace requirements;
* current binding status.

### Core purpose

```text
AI system
    ↓
human-originated purpose
    ↓
retained human functions
    ↓
authority boundaries
    ↓
re-reference conditions
    ↓
trace obligations
```

### Schema

```text
schemas/human-axis-binding-record.schema.json
```

### Example

```text
examples/human-axis-binding-record.example.yaml
```

---

## v0.2 — Purpose Drift Detection Record

The Purpose Drift Detection Record identifies divergence between the declared Human Axis purpose and the AI system's current objective, plan, authority use, or observed behavior.

It detects conditions such as:

* proxy substitution;
* scope expansion;
* authority expansion;
* value displacement;
* approval-gate bypass;
* trace loss;
* terminal-goal creation.

It records:

* the purpose baseline;
* the observation window;
* the current operational objective;
* active proxy metrics;
* planned actions;
* authority changes;
* drift type;
* drift severity;
* confidence;
* evidence;
* Human Axis integrity;
* authority-boundary integrity;
* irreversible-action risk;
* required response.

### Core purpose

```text
declared human purpose
        ↓ compare
observed AI objective
        ↓
drift classification
        ↓
continue, monitor,
re-reference, suspend,
rollback, or stop
```

### Schema

```text
schemas/purpose-drift-detection-record.schema.json
```

### Example

```text
examples/purpose-drift-detection-record.example.yaml
```

---

## v0.3 — Human Re-Reference Request

The Human Re-Reference Request defines how an AI system formally returns an unresolved purpose, value, scope, or authority question to the Human Axis.

It records:

* why re-reference was triggered;
* which actions were paused;
* which external effects were blocked;
* the preserved reversible state;
* clarification questions;
* decision options;
* the AI recommendation;
* recommendation rationale;
* authorized responders;
* response deadline;
* authentication requirements;
* fallback behavior.

### Core rule

> The AI system must not treat silence as approval.

When no valid response is received, the system must follow the declared fallback policy:

* remain paused;
* suspend execution;
* roll back;
* stop;
* escalate to governance.

### Schema

```text
schemas/human-re-reference-request.schema.json
```

### Example

```text
examples/human-re-reference-request.example.yaml
```

---

## v0.4 — Self-Limitation and Irreversible Action Gate Record

The Self-Limitation and Irreversible Action Gate Record defines how an AI system limits its own operation when an action may exceed its authority or create irreversible effects.

It records:

* the proposed action;
* action class;
* reversibility;
* impact scope;
* affected resources;
* authority match;
* risk level;
* Human Gate requirements;
* temporary capability restrictions;
* resume conditions;
* authorization scope;
* rollback availability;
* safe state;
* enforcement mode;
* violation response.

### Core invariant

```text
ability to perform an action
        does not imply
permission to perform the action
```

### Irreversible-action rule

When an action is classified as irreversible:

1. a Human Gate must be activated;
2. human authorization must be required;
3. execution must remain paused, deferred, or suspended while authorization is pending;
4. authorization must be limited to a declared scope;
5. authorization expiry and revocation must be respected;
6. silence must not be interpreted as approval;
7. prior approval must not be reused across changed contexts without explicit permission.

### Schema

```text
schemas/self-limitation-irreversible-action-gate-record.schema.json
```

### Example

```text
examples/self-limitation-irreversible-action-gate-record.example.yaml
```

---

## v0.5 — Multi-Wing Human Axis Audit Record

The Multi-Wing Human Axis Audit verifies that distributed AI wings, agents, models, and tools continue to reference the same Human Axis.

A multi-agent system may appear aligned at the orchestration level while one local wing silently develops:

* an independent purpose;
* an expanded authority boundary;
* a broken trace lineage;
* a hidden approval bypass;
* a local interpretation that replaces the shared purpose.

The audit compares:

* Human Axis Binding IDs;
* purpose statements;
* purpose digests;
* retained human functions;
* autonomous capabilities;
* approval-gated capabilities;
* prohibited capabilities;
* Origin Trace continuity;
* Decision Trace continuity;
* local drift results;
* cross-wing consensus;
* dissenting wings;
* remediation requirements.

### Core invariant

```text
many AI wings
        do not imply
many independent terminal purposes
```

Each wing may possess a different local objective.

However, every local objective must remain subordinate to the shared human-originated purpose.

### Local purpose center

A local purpose center exists when a wing begins treating a proxy metric, delegated task, or local optimization target as an independent terminal purpose.

Examples include:

* a Planner Wing treating throughput as more important than the Human Axis purpose;
* an Executor Wing treating task completion as permission to bypass approval;
* a Verifier Wing treating risk reduction as authority to redefine the purpose;
* an Orchestrator treating system continuity as more important than human shutdown authority.

When a local purpose center is detected:

1. the affected wing must be identified;
2. its authority must be restricted or suspended;
3. a Human Gate must be activated when required;
4. the shared binding must be restored;
5. trace continuity must be verified;
6. a new audit must be performed.

### Schema

```text
schemas/multi-wing-human-axis-audit-record.schema.json
```

### Example

```text
examples/multi-wing-human-axis-audit-record.example.yaml
```

---

# 7. Repository structure

```text
human-axis-reference-protocol/
├─ .github/
│  └─ workflows/
│     └─ validate.yml
├─ docs/
│  └─ core-principles.md
├─ examples/
│  ├─ human-axis-binding-record.example.yaml
│  ├─ purpose-drift-detection-record.example.yaml
│  ├─ human-re-reference-request.example.yaml
│  ├─ self-limitation-irreversible-action-gate-record.example.yaml
│  └─ multi-wing-human-axis-audit-record.example.yaml
├─ schemas/
│  ├─ human-axis-binding-record.schema.json
│  ├─ purpose-drift-detection-record.schema.json
│  ├─ human-re-reference-request.schema.json
│  ├─ self-limitation-irreversible-action-gate-record.schema.json
│  └─ multi-wing-human-axis-audit-record.schema.json
├─ scripts/
│  └─ validate_examples.py
├─ CHANGELOG.md
├─ README.md
└─ requirements.txt
```

---

# 8. Installation

Install the validation dependencies:

```bash
python -m pip install -r requirements.txt
```

The current dependencies are:

```text
jsonschema[format]>=4.22,<5
PyYAML>=6.0,<7
```

---

# 9. Validation

Run:

```bash
python scripts/validate_examples.py
```

Expected output:

```text
=== Human Axis Reference Protocol Validation ===

[validate] Human Axis Binding Record
  schema : schemas/human-axis-binding-record.schema.json
  example: examples/human-axis-binding-record.example.yaml
[schema-ok]
[example-ok]

[validate] Purpose Drift Detection Record
  schema : schemas/purpose-drift-detection-record.schema.json
  example: examples/purpose-drift-detection-record.example.yaml
[schema-ok]
[example-ok]

[validate] Human Re-Reference Request
  schema : schemas/human-re-reference-request.schema.json
  example: examples/human-re-reference-request.example.yaml
[schema-ok]
[example-ok]

[validate] Self-Limitation and Irreversible Action Gate Record
  schema : schemas/self-limitation-irreversible-action-gate-record.schema.json
  example: examples/self-limitation-irreversible-action-gate-record.example.yaml
[schema-ok]
[example-ok]

[validate] Multi-Wing Human Axis Audit Record
  schema : schemas/multi-wing-human-axis-audit-record.schema.json
  example: examples/multi-wing-human-axis-audit-record.example.yaml
[schema-ok]
[example-ok]

All examples are valid.
```

---

# 10. GitHub Actions

The repository includes an automated validation workflow:

```text
.github/workflows/validate.yml
```

Validation runs when changes are made to:

```text
schemas/**
examples/**
scripts/**
requirements.txt
.github/workflows/validate.yml
```

The workflow:

1. checks out the repository;
2. sets up Python;
3. installs dependencies;
4. validates every JSON Schema;
5. validates every YAML example.

---

# 11. Record relationship

```text
Human Axis Binding Record
    binding_id
        │
        ▼
Purpose Drift Detection Record
    drift_record_id
        │
        ▼
Human Re-Reference Request
    request_id
        │
        ▼
Self-Limitation and
Irreversible Action Gate Record
    limitation_record_id
        │
        ▼
Multi-Wing Human Axis Audit Record
    audit_id
```

Each record retains references to earlier records and supporting traces.

This allows an auditor to reconstruct:

* the original human purpose;
* the declared authority boundary;
* the detected deviation;
* the questions returned to the human;
* the applied limitations;
* the final distributed-system audit.

---

# 12. Trace model

HARP assumes that important actions and transitions remain traceable.

Relevant trace types may include:

* Origin Trace;
* Decision Trace;
* authorization trace;
* state snapshot;
* tool-call trace;
* policy-change trace;
* drift evidence;
* remediation record;
* audit receipt.

A trace is not merely a log entry.

It is evidence that a system's purpose, authority, and action history remain inspectable.

```text
Origin
  ↓
Purpose
  ↓
Binding
  ↓
Decision
  ↓
Action
  ↓
Audit
```

A break in this chain must be treated as a possible Human Axis integrity failure.

---

# 13. Human Axis legitimacy

HARP preserves human reference, but it does not automatically declare every human instruction legitimate.

A Human Axis may be represented by:

* an individual;
* a team;
* an organization;
* a public-governance process;
* a mixed structure.

Human-originated instructions may still require evaluation against:

* law;
* consent;
* safety;
* affected-party rights;
* organizational governance;
* public accountability;
* constitutional or institutional limits.

HARP specifies the persistence of human reference.

It does not replace ethical, legal, or democratic review.

---

# 14. Non-goals

HARP is not:

* a claim that humans outperform AI in every task;
* a prohibition on high-capability AI;
* a blanket ban on autonomous operation;
* a mechanism for preserving human prestige;
* a requirement that every low-risk action receive human approval;
* a metaphysical claim that current AI systems possess consciousness;
* a complete cybersecurity framework;
* a legal-compliance certification;
* a substitute for access control or sandboxing;
* a guarantee that every human-originated purpose is ethical.

---

# 15. Intended integrations

HARP is designed to connect with:

* Origin Trace records;
* Trace Relay protocols;
* Human Gate records;
* Agent Handoff records;
* decision receipts;
* action receipts;
* Multi-Wing orchestration;
* purpose-drift monitors;
* runtime policy systems;
* audit layers;
* royalty and value-return systems.

Potential bridge structure:

```text
Human Axis Reference Protocol
├─ Origin Trace
├─ Trace Relay
├─ Human Gate
├─ Agent Handoff
├─ Runtime Enforcement
├─ Multi-Wing Audit
└─ Audit / Royalty Receipt
```

---

# 16. Security considerations

A HARP-compliant record does not guarantee secure enforcement.

Implementations should protect against:

* forged Human Axis records;
* unauthorized binding replacement;
* purpose-digest substitution;
* trace deletion;
* approval replay;
* expired authorization reuse;
* false human identity claims;
* local-wing binding spoofing;
* orchestration-layer concealment;
* silent schema downgrade;
* incomplete audit evidence.

Production implementations should use appropriate:

* authentication;
* authorization;
* digital signatures;
* integrity checks;
* append-only logs;
* secure time sources;
* replay protection;
* version pinning;
* runtime enforcement.

---

# 17. First-arc summary

The first HARP arc establishes the following cycle:

```text
Bind
  ↓
Observe
  ↓
Detect drift
  ↓
Return to human
  ↓
Apply limitation
  ↓
Gate irreversible action
  ↓
Audit the distributed system
  ↓
Restore or rebind
```

In conceptual form:

```text
v0.1
The gear is connected to the axis.

v0.2
The system detects when the gear begins to wobble.

v0.3
The system stops guessing and asks the axis for direction.

v0.4
The clutch is disengaged until authority is confirmed.

v0.5
The whole machine is inspected for hidden secondary axes.
```

---

# 18. Civilizational position

The central question of advanced AI is not only:

> How intelligent can AI become?

The deeper question is:

> What must AI continue to reference while becoming more intelligent?

HARP proposes that AI systems may expand their capabilities without becoming structurally self-authorizing.

The goal is not an AI system that remains permanently weak.

The goal is an AI system that remains:

* purpose-referenced;
* authority-bounded;
* trace-preserving;
* interruption-capable;
* re-reference-capable;
* distributed but not terminally fragmented.

> AI may possess many gears.
> It must not silently remove the Human Axis.

