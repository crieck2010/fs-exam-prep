# Changelog

## v0.3.0 — 2026-10-08
- All 7 FS domains shipped (48 generators total): `surveying-processes-and-methods`
  (7), `mapping-processes-and-methods` (6), `surveying-principles-geodesy` (5),
  `business-concepts-ethics` (5), `applied-math-statistics` (6).
- Mixed-domain bank generation across the full blueprint
  (`fs-quiz generate --all`).
- 164 tests passing; every new answer independently re-derived in tests
  (caught 3 more generator bugs pre-release: duplicate distractors,
  identical distractor pair).

## v0.2.0 — 2026-10-08
- New domain: `boundary-law-and-real-property` with 7 scenario generators
  (hierarchy-of-calls, senior-junior-rights, plss, water-boundaries, easements,
  adverse-possession, deeds-recording).
- Scenario templates with randomized names/dates/measurements; answers
  re-derivable from question parameters (tests re-derive every answer
  independently, including an independent PLSS boustrophedon implementation).
- 75 tests passing (52 from v0.1.0 + 23 new).

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
