# Agent architecture and engineering quality gates

## Status

**Implemented baseline:** Google's minimal single-model tool-calling loop with shell execution, file read/write, API retries, deadline-aware wrap-up and basic context overflow mitigation.

**Not implemented yet:** application MCP tool integration, independent verification layers, robust context summarization, specialized CAD/IFC processing, structured constraint ledger, generic artifact audit, and advanced timeout recovery. The following architecture is a **design target**.

## Proposed architecture

```text
Task instruction + project sources
        |
        v
1. Requirement discovery: required deliverables, inputs, units, standards
        |
        v
2. Evidence ledger: source -> claim -> uncertainty -> trace
        |
        v
3. Task planner: decomposition, runtime budget, dependencies, checklists
        |
        v
4. Tool executor: bash + files + permitted task-local MCP applications
        |
        v
5. Engineering computation: reliable numeric methods, units, constraints
        |
        v
6. Independent verification: constraints, engineering consistency, formats
        |                       |
        | failures              | passed
        +------> repair loop ----+----> output audit -> submit
```

No task-specific answer hard-coding. Candidate tools are activated according to requirements and tool availability, not benchmark identifiers.

## Quality gates

| Gate | What must be verified | Evidence to preserve |
| --- | --- | --- |
| G0: discover | Correct project files, instructions and workdir | Input inventory |
| G1: requirements | Deliverable filenames/formats, constraints and citations to source | Requirement/constraint ledger |
| G2: units | Consistent units and dimensions, correct sign conventions | Unit audit |
| G3: physics | Correct balance laws, constitutive relationships and justified assumptions | Calculation trace |
| G4: feasibility | All explicit hard constraints, safety margins and standards where stated | Constraint table |
| G5: numerics | Solver residuals, tolerances, convergence, geometry checks where applicable | Numerical validation log |
| G6: deliverables | Correct files exist, reopen successfully, cross-file consistency | File inventory and inspection |
| G7: provenance | No invented experimental validation, no untraceable assumptions | Evidence/limitations register |
| G8: deadline | Deliverables saved before timeout; recoverable errors handled | Timestamped logs |

## Domain-specific evaluation checks (planned)

- **Electrical:** voltage drop, ampacity/derating, power and energy conservation, feeder limits, protective constraints, equipment ratings and calculation units.
- **Mechanical:** thermal balances, boundary conditions, hydraulic/flow quantities, geometry clashes, fire-simulation convergence and fit to test evidence.
- **Civil:** geotechnical loading and settlement assumptions, approvals, geometry, construction constraints, cost traceability.
- **Structural:** applied loads, load combinations, equilibrium, transfer paths, capacity and consistent units.

Do not claim the harness checks any of these until an executable check has been implemented and tested.

## Uncertainty and model integrity

A simulation alone is not experiment validation. The agent must separate observed values, provided data, modeled estimates and unsupported assumptions, and it must stop or qualify conclusions if evidence is missing.

## Deadline recovery

The official benchmark gives at most six hours per task. Plan progress checkpoints, persistent intermediate outputs and a finalization buffer, but make these *generic* rather than task-name-dependent.