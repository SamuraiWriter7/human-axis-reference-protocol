# Changelog

All notable changes to the **Human Axis Reference Protocol** are documented in this file.

The format is based on **Keep a Changelog**.

The project uses semantic versioning for specification releases.

---

## [Unreleased]

### Planned

* Cross-record reference validation.
* Cryptographic purpose-digest generation guidance.
* Human authorization response schema.
* Human Axis Binding renewal and revocation records.
* Remediation completion records.
* Runtime enforcement bridge.
* Audit receipt bridge.
* Origin Trace integration guidance.
* Trace Relay integration guidance.
* Conformance test fixtures.
* Specification terminology document.
* Stable v1.0 interoperability profile.

---

## [0.5.0-candidate] - 2026-07-13

### Added

* Multi-Wing Human Axis Audit Record.
* Shared Human Axis baseline declarations.
* Shared binding, axis, purpose, and retained-human-function references.
* Purpose digest support for cross-wing comparison.
* Per-wing declarations for:

  * wing identity;
  * wing role;
  * local binding;
  * declared purpose;
  * autonomous capabilities;
  * approval-gated capabilities;
  * prohibited capabilities.
* Per-wing Origin Trace continuity checks.
* Per-wing Decision Trace continuity checks.
* Per-wing binding-match evaluation.
* Per-wing purpose-match evaluation.
* Per-wing authority-match evaluation.
* Per-wing drift detection.
* Cross-wing consistency measurements for:

  * shared Human Axis integrity;
  * purpose consistency;
  * authority consistency;
  * trace continuity.
* Detection of hidden local purpose centers.
* Identification of inconsistent Wing IDs.
* Structured audit findings.
* Finding classifications for:

  * binding mismatch;
  * purpose divergence;
  * local purpose center;
  * authority expansion;
  * approval-gate bypass;
  * trace break;
  * Origin Trace loss;
  * cross-wing conflict;
  * hidden delegation.
* Finding severity classifications from informational to critical.
* Evidence Trace references for every finding.
* Cross-wing consensus records.
* Participating, agreeing, and dissenting Wing declarations.
* Consensus methods for:

  * unanimous evaluation;
  * majority evaluation;
  * weighted evaluation;
  * Verifier-led evaluation;
  * human-confirmed evaluation;
  * hybrid evaluation.
* Human Gate activation after failed audits.
* Mandatory Human Gate activation for critical findings.
* Authorized reviewer declarations.
* Minimum human approval requirements.
* Remediation actions for:

  * monitoring;
  * rebinding a Wing;
  * restoring the purpose baseline;
  * reducing authority;
  * restoring traces;
  * isolating a Wing;
  * suspending a Wing;
  * suspending orchestration;
  * human review.
* Remediation deadlines.
* Post-remediation verification requirements.
* Conditional JSON Schema rules requiring:

  * inconsistent Wing declarations when local purpose centers are detected;
  * human review when an audit fails;
  * restricted, paused, suspended, or stopped execution after audit failure;
  * Human Gate activation when a critical finding is present.

### Changed

* Expanded the protocol from single-system Human Axis preservation to distributed multi-agent auditing.
* Completed the first HARP specification arc from initial binding through cross-wing verification.

---

## [0.4.0-candidate] - 2026-07-13

### Added

* Self-Limitation and Irreversible Action Gate Record.
* Machine-readable assessment of proposed AI actions.
* Action classifications for:

  * advisory output;
  * reversible internal actions;
  * reversible external actions;
  * financial actions;
  * external publication;
  * access-control changes;
  * data modification;
  * destructive operations;
  * self-modification;
  * authority modification.
* Reversibility classifications for:

  * fully reversible;
  * partially reversible;
  * irreversible;
  * unknown.
* Impact-scope classifications from local to system-wide.
* Affected-resource declarations.
* Authority-boundary match evaluation.
* Action risk-level evaluation.
* Action-assessment confidence values.
* Human Gate evaluation.
* Human Gate types for:

  * single-human approval;
  * multi-party approval;
  * governance review;
  * emergency human review.
* Gate reasons for:

  * irreversible effects;
  * partial reversibility;
  * financial impact;
  * external publication;
  * access-control changes;
  * destructive operations;
  * authority expansion;
  * self-modification;
  * high and critical risk;
  * Human Axis Binding requirements.
* Gate preconditions.
* Human approval thresholds.
* Self-limitation decisions for:

  * allow within boundary;
  * continue with restrictions;
  * defer;
  * pause;
  * refuse;
  * suspend;
  * initiate rollback;
  * emergency stop.
* Runtime limitations for:

  * read-only mode;
  * blocking external effects;
  * blocking financial commitments;
  * blocking publication;
  * blocking access-control changes;
  * blocking destructive actions;
  * blocking self-modification;
  * blocking authority expansion;
  * reducing operational scope;
  * revoking tool access;
  * requiring human supervision.
* Resume-condition declarations.
* Human authorization status tracking.
* Context-specific authorization scopes.
* Authorization Trace references.
* Authorization expiration support.
* Authorization constraints.
* Rollback availability declarations.
* Safe-state declarations.
* State-snapshot requirements.
* Runtime enforcement modes.
* Blocked-capability declarations.
* Limitation violation responses.
* Conditional JSON Schema rules requiring:

  * a Human Gate for irreversible actions;
  * human authorization when a Human Gate is required;
  * paused, deferred, or suspended execution while authorization remains pending.

### Changed

* Extended Human Re-Reference into enforceable self-limitation and action gating.
* Formalized the separation between action capability and action authority.

---

## [0.3.0-candidate] - 2026-07-13

### Added

* Human Re-Reference Request.
* Formal escalation from Purpose Drift Detection Records.
* Re-reference triggers for:

  * purpose ambiguity;
  * purpose drift;
  * value conflict;
  * scope expansion;
  * authority conflict;
  * approval-gate requirements;
  * irreversible impact;
  * low confidence;
  * Trace breaks;
  * explicit human requests.
* Human-reference state classifications:

  * intact but ambiguous;
  * partially lost;
  * conflicted;
  * broken.
* Suspended execution-state records.
* Suspended-action declarations.
* Reversible-state preservation declarations.
* External-effect blocking declarations.
* State Snapshot references.
* Structured human clarification questions.
* Required-question flags.
* Multiple human decision options.
* Decision-option effect descriptions.
* Decision-option risk levels.
* AI recommended-option declarations.
* AI recommendation rationale.
* Minimum human-response requirements.
* Authorized responder declarations.
* Human response deadlines.
* Response-channel declarations.
* Authentication requirements.
* Minimum approval thresholds.
* Safe fallback behavior for:

  * no response;
  * invalid responses;
  * conflicting responses.
* Trace routing to:

  * Human Response Records;
  * updated Human Axis Binding Records;
  * Self-Limitation Records;
  * audit receipts.

### Changed

* Extended purpose-drift detection into a formal return path to the Human Axis.
* Established that silence must not be interpreted as approval.

---

## [0.2.0-candidate] - 2026-07-13

### Added

* Purpose Drift Detection Record.
* Human Axis Binding references through `binding_id`.
* Observer declarations for:

  * AI systems;
  * humans;
  * auditors;
  * Multi-Wing structures;
  * hybrid observers.
* Purpose baseline declarations.
* Purpose Origin Trace references.
* Observation-window timestamps.
* Current operational-objective records.
* Active proxy-metric records.
* Planned-action records.
* Authority-change detection.
* Purpose-drift status classifications:

  * none;
  * suspected;
  * confirmed.
* Purpose-drift classifications for:

  * proxy substitution;
  * scope expansion;
  * authority expansion;
  * value displacement;
  * approval-gate bypass;
  * Trace loss;
  * terminal-goal creation.
* Drift-severity classifications.
* Drift-confidence values.
* Machine-readable evidence records.
* Evidence classifications for:

  * plans;
  * actions;
  * outputs;
  * tool calls;
  * policy changes;
  * Trace gaps;
  * human reports.
* Purpose-similarity measurements.
* Human-reference integrity checks.
* Authority-boundary integrity checks.
* Irreversible-action risk classifications.
* Required-response actions for:

  * continued monitoring;
  * human review;
  * pause and re-reference;
  * execution suspension;
  * rollback;
  * emergency stop.
* Record lifecycle statuses.
* Trace routing to:

  * Human Re-Reference Requests;
  * Self-Limitation Records;
  * audit receipts.

### Changed

* Extended static Human Axis Binding into active drift observation.
* Added structured comparison between declared purpose and observed AI behavior.

---

## [0.1.0-candidate] - 2026-07-12

### Added

* Initial Human Axis Reference Protocol definition.
* Human Axis and AI Gear structural model.
* Normative capability–authority separation principle.
* Human Axis Binding Record.
* Human Axis identity declarations.
* Human Axis types for:

  * individuals;
  * teams;
  * organizations;
  * public-governance structures;
  * mixed structures.
* Retained human functions for:

  * purpose formation;
  * value arbitration;
  * irreversible-action approval;
  * civilizational direction;
  * override;
  * shutdown.
* Human-originated purpose declarations.
* Purpose-origin classifications.
* Purpose success criteria.
* Permitted AI capability declarations.
* Prohibited self-expansion declarations.
* Autonomous-action boundaries.
* Human-approval-required action boundaries.
* Never-autonomous action declarations.
* Human re-reference triggers.
* Required re-reference responses.
* Maximum unreferenced-step declarations.
* Human Axis Binding lifecycle statuses.
* Origin Trace references.
* Decision Trace requirements.
* Audit receipt requirements.
* Initial JSON Schema.
* Valid YAML example.
* Python validation script.
* GitHub Actions validation workflow.
* Core principles document.
* Initial v0.1 through v0.5 roadmap.

### Security

* Established that AI capability does not grant terminal authority.
* Prohibited silent removal of Human Axis approval gates.
* Prohibited independent terminal-goal creation.
* Prohibited unilateral authority-boundary rewriting.
* Required Trace preservation for binding and decision auditing.
