# Changelog

## v0.1.0 — 2026-10-08
- Initial release: `survey-computations` domain with 12 parameterized generators
  (inverse, forward, traverse-misclosure, bowditch, area-coordinates,
  horizontal-curve, vertical-curve, level-notes, stadia, volumes,
  error-propagation, angular-misclosure).
- Versioned Question schema (v1), generator registry, deterministic QuizEngine
  (generate / bank / export / import / grade), thin `fs-quiz` CLI.
- Duck-typed interop: `flutter_contract()` JSON contract for the Phase 2 app.
- 52 tests passing (schema, registry, per-topic independent recomputation,
  determinism, engine round-trip).
- Docs: ARCHITECTURE, QUESTION_SCHEMA, INTEROP, ADDING_A_DOMAIN.
