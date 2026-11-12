# All 29 public PLE development tasks

This catalog reproduces the *short descriptions* from Google's [official evaluation README](https://github.com/google-research/ple/blob/main/eval/README.md). The original task prompts, exact numeric inputs, required acceptance thresholds and private files were not inspected. For detailed execution, access the [gated dataset](https://huggingface.co/datasets/google/physical-engineerings-last-exam).

**Public set:** 29 tasks: Mechanical 7; Civil 9; Electrical 9; Structural 4. Grading: 12 `checks`, 14 `rubric`, 3 `checks-judge`.

| Task | Discipline | Graded by | What it asks for |
|---|---|---|---|
| `data-hall-mep-routing` | Mechanical engineering | `checks` | Reconstruct a data hall from seven drawing sheets and generate a clash-free IFC4 model routing cable tray, busway, and chilled-water piping |
| `fire-test-validation-memo` | Mechanical engineering | `rubric` | Evaluate a fire-resistance simulation against furnace test data and write an engineering validation memo in Word |
| `data-hall-mep-routing-offset` | Mechanical engineering | `checks` | Route MEP systems in a data hall where the structural grid is offset from the floor tiles, navigating a cross-aisle and 104 sprinkler heads |
| `eor-review-corrections` | Structural engineering | `checks-judge` | Turn engineer-of-record review markups into an issued drawing revision across two bid packages, including comment dispositions, a sheet index, and change documentation |
| `foundation-strategy` | Civil engineering | `checks-judge` | Choose between spread footings and aggregate piers for six building pads using geotechnical records, and deliver a design basis, schedule, and constraint register |
| `landscape-sheet-revision` | Civil engineering | `rubric` | Incorporate a street-tree comment into a landscape drawing set and verify the package for agency resubmittal |
| `data-center-site-model` | Civil engineering | `checks` | Lay out a two-phase data-center campus that meets every binding requirement in its approval document, as an IFC model |
| `engineers-estimate-check` | Civil engineering | `rubric` | Audit a section of an engineer's estimate against the project plans before it goes to the surety broker |
| `footing-settlement-verification` | Civil engineering | `rubric` | Verify the long-term settlement of a building block's spread footings on clay and issue the verification memo |
| `solar-supplemental-review` | Electrical engineering | `rubric` | Write the supplemental interconnection review memo for a solar application on a distribution feeder |
| `solar-witness-test-package` | Electrical engineering | `rubric` | Prepare the witness-test scope and schedule for municipal solar arrays that require testing, and list those that do not |
| `frame-extension-method` | Civil engineering | `checks` | Prepare a construction method package for a steel frame extension over an occupied floor, verified against safety regulations |
| `fire-solve-convergence` | Mechanical engineering | `rubric` | Provide a signed engineering disposition on a non-converging steady-state fire simulation before a fourth run is attempted |
| `les-mesh-resolution` | Mechanical engineering | `rubric` | Document the mesh-resolution basis of a large-eddy fire simulation to close a peer-review item |
| `mv-conveyance-study` | Electrical engineering | `checks` | Produce a conveyance study and cost workbook for seven 13.8 kV medium-voltage distribution circuits |
| `data-hall-device-takeoff` | Electrical engineering | `checks` | Complete an electrical device takeoff from a data hall drawing set and price the bill of materials |
| `division-26-specifications` | Electrical engineering | `checks` | Write Division 26 electrical specifications for an Army facility from its coordinated design package |
| `heat-rejection-life-cycle-cost` | Mechanical engineering | `checks` | Design a condenser-water heat rejection replacement for a federal campus and justify it with a life-cycle cost analysis |
| `cooling-water-flush-plan` | Mechanical engineering | `checks` | Create a cleaning, flushing, and passivation plan for a data hall's process cooling-water system prior to turnover |
| `wind-diaphragm-shear` | Structural engineering | `checks` | Calculate wind roof-diaphragm shears and shear-wall loads for a single-story data hall |
| `seismic-diaphragm-shear` | Structural engineering | `checks` | Calculate seismic diaphragm shears and shear-wall loads along a data-center building's lateral load path |
| `roof-deck-design` | Structural engineering | `checks` | Design a data center's steel roof deck for gravity and lateral loads, specifying gage, fastener pattern, and diaphragm capacity |
| `fill-compaction-acceptance` | Civil engineering | `rubric` | Decide whether slab-on-grade fill compaction testing and its records meet the earthwork specification, as a materials acceptance record |
| `shoring-design-verification` | Civil engineering | `rubric` | Verify a revised excavation shoring design against the logged groundwater and subsurface conditions before the excavation starts |
| `emergency-spillway-check` | Civil engineering | `rubric` | Check whether a stormwater basin's emergency spillway as drawn can answer a plan-check comment, and set out the revisions in a memo |
| `pre-application-capacity-response` | Electrical engineering | `rubric` | Write a utility's response to a pre-application request for a feeder's available capacity, and close the case in its tracking |
| `permission-to-operate-memo` | Electrical engineering | `rubric` | Advise whether permission to operate can issue for a PV site on the requested date, and open a work package for what stands in the way |
| `backfeed-energization-reply` | Electrical engineering | `rubric` | Reply to a community solar developer on whether its site can be energized for backfeed on the requested date, and open a work package |
| `lv-cable-sizing` | Electrical engineering | `checks-judge` | Size a building's low-voltage cable schedule for voltage drop, duct-bank ampacity, and cost, with a constraint register and design basis |

## Reading the catalog responsibly

- Descriptions here summarize official *assignments* and expected categories of deliverable, not verified results.
- Different tasks require drawings, CAD/IFC, spreadsheets, technical memoranda, calculations and application-specific systems.
- A physically plausible output is not automatically compliant with the exact engineering task; use task-specific requirements and mandatory acceptance gates.
- The task set may change in Google's gated dataset; pin its exact revision for every evaluation.

## Four representative development diagnostics

1. `lv-cable-sizing`: electrical constraints, unit checking, ampacity, voltage drop and cost.
2. `data-hall-mep-routing`: geometry, IFC parsing and clash detection.
3. `foundation-strategy`: geotechnical design tradeoffs and documentation.
4. `fire-test-validation-memo`: experiment-vs-simulation reasoning and document generation.

These are diagnostic *categories*, not task-specific shortcuts. The submitted harness must generalize rather than hard-code decisions by task identifier.