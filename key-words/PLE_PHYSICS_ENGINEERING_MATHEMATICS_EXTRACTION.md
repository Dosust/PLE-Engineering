# Complete Physics, Engineering, and Mathematics Extraction from PLE: Physical-Engineering's Last Exam

Source: PLE: Physical-Engineering's Last Exam, Rujun Han et al., arXiv:2610.30537v2, October 30, 2026.\
Document examined: 20 pages, including the abstract, figures, tables, mathematical equations, results, references, and appendices.

I am organizing the extraction in the same order as the paper, from page 1 to page 20. Each entry identifies the terminology, its engineering or mathematical meaning, and the practical reality discussed by the authors.

An important distinction: This is primarily a scientific paper about evaluating AI agents performing professional engineering work, not a textbook deriving electrical, mechanical, civil, or structural engineering equations. It explicitly presents two numbered mathematical equations for engineering-design scoring. It also names many physical laws, design constraints, numerical methods, and engineering standards without deriving their governing formulas. I will not invent missing equations and attribute them to the paper.

## Page 1. Abstract and Introduction

Research motivation, professional engineering, physical laws and infrastructure

1. Physical engineering: The engineering of real systems and infrastructure whose behavior is governed by physical principles, material properties, safety requirements, and technical standards.
2. Professional engineering work: Engineering calculations, design, analysis, documentation, and deliverables intended for actual projects rather than isolated classroom questions.
3. Physical modeling: Mathematical representation of the behavior and constraints of real engineering systems.
4. Legal code requirements: Binding requirements that an engineering design must satisfy in addition to physical feasibility.
5. Material cost optimization: Selecting feasible materials while reducing their procurement or installed cost.
6. Installation cost optimization: Minimizing the cost of implementing an engineering design, rather than considering material price alone.
7. Two-dimensional engineering design (2D): Plans, sections, details, and other technical drawings.
8. Three-dimensional engineering design (3D): Spatial models representing physical geometry and the relationships among engineering components.
9. Engineering design packages: Coordinated collections of calculations, drawings, schedules, reports, and specifications.
10. Licensed engineering review: Professional verification and sign-off before engineering designs are used in real projects.
11. Electrical engineering: Power distribution, electrical feeders, and electrical infrastructure.
12. Mechanical engineering: Heating, cooling, ventilation, and associated equipment.
13. Civil engineering: Site development, earthworks, grading, drainage, and infrastructure.
14. Structural engineering: Structural frames, foundations, and load-resisting systems.
15. Interdisciplinary infrastructure engineering: Coordinating these four engineering disciplines within the same building or campus project.
16. Agentic engineering tasks: Multi-step engineering assignments requiring an AI agent to inspect project information, operate tools, calculate, and prepare deliverables.
17. Long-horizon work: Engineering processes extending over many computational steps rather than a single model response.
18. Infrastructure investment gap: The paper cites a projected US infrastructure funding gap of $3.7 trillion for 2024–2033 and global infrastructure investment needs of $94 trillion by 2040.
19. Physical and safety consequences: Engineering errors can produce substantial economic damage and potentially severe safety failures.

Practical context: Designing a university laboratory requires electrical engineers to size feeders, mechanical engineers to design HVAC equipment, structural engineers to design the frame and foundations, and civil engineers to develop grading and drainage. All these contributions must be compatible.

## Page 2. Four Physical Engineering Domains

Figure 1 and the four representative engineering problems

### A. Structural engineering

20. Steel roof decking: Structural steel deck supporting loads and participating in the roof system.
21. Open-web joists: Structural members carrying roof loads to their supports.
22. Lateral diaphragm framing: Structural components that transfer lateral forces through the roof.
23. Gravity loads: Forces acting through gravity, including relevant dead and imposed loads.
24. Snow-drift loads: Potentially nonuniform snow accumulation affecting structural loading.
25. Shear loads: Forces acting tangentially through structural components.
26. Member demand: The force or effect imposed on a structural member.
27. Code capacity: The permitted or design resistance of a structural component under the applicable requirements.

Design reality: The roof structure must carry its loads without exceeding required strength or capacity limits.

### B. Civil engineering

28. Site layout: Spatial arrangement of buildings, roads, utilities, and site infrastructure.
29. Phased campus development: Designing infrastructure to accommodate multiple project phases.
30. Access roads: Vehicle access within the project site.
31. Utility corridors: Reserved locations for water, electricity, drainage, and other infrastructure.
32. Wetland buffers: Spatial restrictions intended to protect delineated wetland areas.
33. IFC model: Industry Foundation Classes, a standard representation for exchanging building and infrastructure model data.

Design reality: A site must be physically feasible and satisfy its approval constraints, including environmentally restricted areas.

### C. Electrical engineering

34. Low-voltage switchboards: Equipment for distributing electrical power to downstream circuits.
35. Cable trays: Physical pathways supporting cables.
36. Electrical feeders: Circuits distributing power to downstream equipment or panels.
37. Branch circuits: Circuits supplying utilization equipment or other defined loads.
38. Ampacity: Permissible current-carrying capacity under specified operating conditions.
39. Voltage drop: Reduction in electrical voltage along a conductor under load.
40. Cable sizing: Selection of conductor sizes that satisfy applicable thermal, voltage, and equipment constraints.
41. Circuit schedules: Records of circuit loads, conductor selections, routing, and relevant design properties.

Design reality: The paper's electrical example requires designing 32 feeder and branch circuits, accounting for cable routes, allowable current, and voltage-drop limits.

### D. Mechanical engineering

42. Cooling towers: Equipment transferring heat from a cooling-water system to the environment.
43. Heat-rejection equipment: Components responsible for removing heat from a facility.
44. Pumps: Equipment providing the pressure or energy needed to circulate fluid.
45. Piping networks: Connected fluid-carrying components.
46. Thermal load: Heat that must be removed or transferred by the system.
47. Hydraulic flow limits: Restrictions on the allowable or achievable fluid flow through a system.
48. Life-cycle cost (LCC): Cost considered over an equipment or system's operating life.
49. 25-year life-cycle optimization: The paper's mechanical example seeks a compliant replacement design with minimum cost over a 25-year horizon.

Design reality: The least expensive equipment to purchase is not necessarily the least expensive design over 25 years.

### Cross-disciplinary principles

50. Physical feasibility: A proposed design must be physically realizable.
51. Code compliance: A physically feasible design must also satisfy applicable engineering requirements.
52. Design optimality: Among compliant designs, some may be economically or operationally better.
53. Engineering trade-offs: Performance, cost, geometry, physical constraints, and regulatory requirements interact.
54. Multimodal technical information: Relevant engineering evidence appears in different document and model formats.
55. Production deliverables: The final result must be a usable engineering file, not merely a written answer.

## Page 3. Engineering Project Environments and Performance

Figure 2, benchmark construction, and the performance-cost frontier

56. Engineering project corpus: A collection of drawings, calculations, correspondence, schedules, specifications, and supporting files.
57. Sandboxed engineering environment: An isolated computational workspace in which an agent reads files, uses tools, and produces outputs.
58. PDF engineering documents: Technical reports, drawings, and design criteria.
59. Spreadsheets: Tabulated engineering data, quantities, calculations, and costs.
60. CAD: Computer-aided design, including 2D and 3D drawing representations.
61. BIM: Building information modeling, combining model geometry with engineering information.
62. DXF / DWG / IFC: Engineering drawing and model formats.
63. Code execution: Running programs to calculate, transform, or verify engineering outputs.
64. Engineering memos: Formal records of technical evaluations and decisions.
65. Calculation workbooks: Traceable engineering calculations.
66. Equipment schedules: Structured records of equipment selections and technical characteristics.
67. Expert-authored tasks: Assignments constructed directly by practicing engineers.
68. Co-authored tasks: Assignments originating from engineering briefs and developed with AI-assisted task creation, followed by professional validation.
69. Executable grader: Software that evaluates the engineering outputs.
70. Reference deliverable: A validated engineering output against which results can be assessed.
71. Rubric-based verification: Evaluation against explicit criteria.
72. Constraint-based verification: Testing a proposed design against physical, regulatory, or operational requirements.
73. Objective-based evaluation: Assessing performance or cost in addition to basic compliance.
74. Performance-cost frontier: The set of evaluated systems representing the best achieved score at their respective cost levels.
75. Logarithmic cost scale: Figure 2 displays cost per task on a logarithmic horizontal axis.

Reported experimental result: The best configuration in this paper, Claude Opus 5.5 with Claude Code, achieved a mean score of 50.6% across the 85 tasks, at a reported cost of $17.18 per task. This is a published experimental observation, not a universal limit on AI engineering capability.

## Page 4. Engineering Benchmarks, Mathematical Objectives, and Scientific Evaluation

Table 1, contributions, and comparison with previous work

76. Engineering benchmark: A standardized collection of tasks for evaluating engineering capabilities.
77. Real-work engineering tasks: Assignments corresponding to professional workflows rather than simplified textbook exercises.
78. Expert curation: Development or validation of engineering tasks by qualified professionals.
79. Large input corpus: The many documents and files an engineer must interpret before beginning calculations.
80. Large output artifacts: Complete engineering products such as drawings, models, calculation files, and reports.
81. Objective function: A mathematical expression representing what a design seeks to maximize or minimize.
82. Expert evaluation rubric: Criteria used to assess engineering deliverable quality.
83. Finite-element analysis: A computational method mentioned in connection with earlier engineering-agent benchmarks, not mathematically developed here.
84. CAD generation: Computational generation of engineering geometry and technical drawings.
85. Circuit design: Designing electrical circuit configurations.
86. Drawing revision: Modifying technical drawings in response to specified requirements.
87. Engineering benchmark saturation: A condition in which existing evaluation tasks become too easy to distinguish stronger systems.
88. Computational reproducibility: The ability to repeat an evaluation under documented conditions.
89. Engineering cost efficiency: The difference between merely satisfying design constraints and producing an economically preferable solution.

Important distinction: The paper compares PLE against engineering and AI benchmarks including EngiBench, EngDesign, Frontier-Eng, DrafterBench, and ElecBench. It does not claim to derive the mathematical formulations of those other benchmarks.

## Page 5. Formal Structure of an Engineering Task

Related work and Section 3, Data Curation

90. Physical laws versus software correctness: A computational result may be executable while still violating physical requirements.
91. Engineering standards: Authoritative design requirements governing professional engineering decisions.
92. Multidocument reasoning: Combining evidence from several project files.
93. Engineering project workflow: Progression from a client request to a verified technical deliverable.
94. Instruction: The engineering assignment specifying what must be achieved.
95. Environment: The project workspace containing the engineering information and available applications.
96. Deliverable specification: Requirements identifying the final output files.
97. Grader: A mechanism for assessing whether those deliverables meet the relevant criteria.
98. Weighted expert rubric: A collection of evaluation criteria carrying different weights.
99. Executable verifier: A computational program checking measurable aspects of engineering output.
100. Reference-based verification: Comparing an output with independently developed or validated reference information.
101. Model Context Protocol (MCP): A mechanism for enabling agent interaction with task-local applications.
102. Filesystem operations: Reading, writing, locating, and organizing project files.
103. Code-execution sandbox: An isolated environment in which computations and file operations can be performed.
104. Agent-tool interaction: The iterative process through which an AI system selects and executes external operations.

Practical context: The paper treats engineering work as a combination of a task instruction, realistic source files, specified deliverables, and verification. These are four distinct requirements.

## Page 6. Multi-System Mechanical, Electrical, and Plumbing Coordination

Figure 3, equipment-hall example

105. MEP coordination: Integration of mechanical, electrical, and plumbing systems into a shared physical environment.
106. Equipment hall: A facility space containing technical equipment and its supporting distribution systems.
107. 128 equipment cabinets: The example contains 128 cabinets that must be served by the relevant systems.
108. Floor plans: Drawings establishing horizontal positions and layout.
109. Equipment schedules: Documents specifying equipment quantities, dimensions, or requirements.
110. Schematics: Simplified representations of system connectivity and relationships.
111. Riser topology: The arrangement and connectivity of vertically distributed services.
112. Section drawings: Drawings used to determine vertical elevations and spatial relationships.
113. Overhead cable trays: Cable-support systems located above equipment.
114. Power busways: Enclosed arrangements for distributing electrical power.
115. Chilled-water mains: Pipes carrying cooling water through the facility.
116. Fire-sprinkler distribution: Fire-protection components occupying the same physical space.
117. Three-dimensional routing: Determining feasible paths for mechanical and electrical systems.
118. Spatial interference: Physical overlap or conflict between components.
119. Clash detection: Computational identification of unacceptable geometric interference.
120. Code clearances: Minimum separations or spaces required by relevant engineering regulations.
121. Connectivity constraints: Requirements ensuring equipment is connected to its intended services.
122. Route-length optimization: Seeking shorter feasible routes to reduce materials or installation effort.
123. Coordinated 3D model: A final digital representation containing the integrated systems.

Real engineering situation: The agent must reconcile eight input files, determine component locations and sizes, connect all required equipment, maintain clearances, and avoid collisions.

The underlying mathematical problem involves geometry, network connectivity, constrained routing, and optimization. The paper describes these requirements but does not provide a formal path-planning equation.

## Page 7. Engineering Cost Estimation and Expert Evaluation

Section 3.1, Expert-Authored Tasks

124. Construction cost estimation: Quantifying expected project costs.
125. Quantity takeoff: Extracting material or work quantities from engineering drawings.
126. Unit pricing: Associating a cost with a measured quantity.
127. Cost subtotal: Aggregating related project expenses.
128. Bond figure: A financial amount associated with construction surety arrangements.
129. Hydraulic-grade-line report: Engineering documentation relating to hydraulic energy or pressure conditions in a system.
130. Drainage drawings: Technical information defining stormwater or drainage infrastructure.
131. Cross-document consistency: Ensuring estimates and calculations agree with governing drawings.
132. Engineering change record: Documentation identifying what changed and its supporting evidence.
133. Source traceability: Linking a calculation or decision to its originating document.
134. Project correspondence: Formal communication of engineering decisions.
135. Document revisions: Different historical versions of engineering information.
136. Superseded documents: Older versions that may no longer govern the work.
137. Quality assurance: Processes intended to establish that engineering outputs meet defined requirements.
138. Binary verification criterion: A criterion evaluated as satisfied or not satisfied.
139. Numerical weighting: Assigning greater importance to more consequential criteria.
140. Weight-normalized scoring: Aggregating criterion outcomes while accounting for their relative weights.

Real example: A professional request requires checking an estimate against drawings, correcting quantities and unit prices, and preparing a documented decision memorandum. The paper gives an illustrative corrected subtotal of $1,303,717.70 as a high-weight rubric item.

Dataset information: The 44 expert-authored tasks contain 941 rubric criteria, averaging 21.4 per task.

## Page 8. Engineering Task Generation and Verification

Figure 4 and Section 3.2, Co-Authored Tasks

141. Expert seed problem: A realistic engineering assignment initially defined by a practicing engineer.
142. Task Creator agent: An AI agent responsible for constructing the task environment, instructions, and verification system.
143. Task Solver agent: A separate AI agent used to test the task's difficulty.
144. Creator–Solver loop: An iterative process of task creation, testing, inspection, and improvement.
145. Adversarial evaluation: Deliberately testing whether a solver can exploit weaknesses or shortcuts.
146. Ground-truth audit: Independent checking that the reference solution and evaluation are correct.
147. Task difficulty threshold: A target performance level used to decide whether a task requires further refinement.
148. Multiple independent attempts: Repeated solver trials used to examine difficulty.
149. Engineering properties: Numerical or physical characteristics supplied as problem inputs.
150. Physical constraints: Restrictions imposed by actual system behavior.
151. Regulatory constraints: Restrictions arising from applicable codes and standards.
152. Operational constraints: Limits associated with practical operation or procurement.
153. Hardware compatibility: Requirements ensuring components can function together.
154. Hard constraints: Mandatory safety or feasibility requirements.
155. Soft constraints: Requirements concerning documentation, conventions, or other noncritical preferences.
156. Independent constraints: Requirements based on distinct sources or engineering concerns.
157. Constraint provenance: Linking each requirement to the appropriate source.
158. Clause-level traceability: Identifying specific technical clauses and their values.
159. Deterministic simulation: Computational evaluation intended to produce reproducible results under fixed inputs.
160. Engineering optimization: Solving a problem to improve cost or performance while respecting constraints.
161. Reference-solution validation: Confirming that an intended answer is physically and mathematically defensible.
162. Document licensing: Ensuring engineering source materials can lawfully be used and distributed.

### Mathematical notation introduced

The task-calibration process uses repeated trials, typically:

\\[ N=3 \\]

with a difficulty target denoted by \\(\tau\\). A task is considered sufficiently difficult when the mean solver score falls below the chosen target.

Practical context: The task must be hard because the underlying engineering problem is complex, not because the instructions are ambiguous or intentionally misleading.

## Page 9. The Paper's Central Mathematical Formulas

Table 2, Figure 5, Equations (1) and (2)

This is the paper's most important mathematical section.

### Formula 1. Constraint compliance and design quality

The paper explicitly defines:

\\[ \boxed{s=0.4p+0.6GO'} \tag{1} \\]

where:

| Symbol    | Meaning                                        | Domain              |
| --------- | ---------------------------------------------- | ------------------- |
| \\(s\\)   | Engineering design score                       | \\(0\leq s\leq1\\)  |
| \\(p\\)   | Fraction of all constraints satisfied          | \\(p\in[0,1]\\)     |
| \\(G\\)   | Hard safety and feasibility gate               | \\(G\in\\{0,1\\}\\) |
| \\(O'\\)  | Normalized design-objective score              | \\(O'\in[0,1]\\)    |
| \\(0.4\\) | Weight assigned to constraint compliance       | Fixed coefficient   |
| \\(0.6\\) | Weight assigned to gated objective performance | Fixed coefficient   |

163. Constraint satisfaction fraction (\\(p\\)): Measures the proportion of requirements that the design satisfies.
164. Binary feasibility gate (\\(G\\)): Indicates whether every mandatory constraint passes.
165. Normalized objective score (\\(O'\\)): Evaluates how good the design is relative to a defined baseline and optimum bound.
166. Weighted objective: Combines compliance and optimization performance.
167. Safety-first optimization: Prevents an infeasible design from obtaining objective-performance credit.
168. Hard-constraint feasibility: The requirement that all mandatory limits hold simultaneously.
169. Design-objective performance: The quality of a compliant solution beyond minimum acceptability.

The hard gate operates as follows:

\\[ G= \begin{cases} 1,&\text{if all hard constraints are satisfied},\\\ 0,&\text{otherwise}. \end{cases} \\]

This piecewise expression is a clarification of the paper's definition, not a separate numbered equation in the article.

Critical consequence: When \\(G=0\\), the optimization term disappears, leaving \\(s=0.4p\\). This means an infeasible design cannot score above 0.4 through this scoring rule.

### Formula 2. Economic objective

For a minimum-cost design, the paper defines:

\\[ \boxed{O=\frac{c\_{\mathrm{bound}}}{c}} \\]

where:

- \\(c\\): Cost of the proposed design.
- \\(c\_{\mathrm{bound}}\\): Certified lower bound on the cost of any compliant design.
- \\(O\\): Raw objective-performance measure.

This is explicitly stated in the article, although not assigned its own equation number.

170. Certified lower bound: A mathematically justified cost bound that no compliant solution can improve upon.
171. Feasible design cost: Cost associated with a solution meeting the engineering constraints.
172. Cost minimization: The optimization objective of finding a compliant design with the lowest possible cost.
173. Optimality bound: A benchmark against which an engineering solution's quality can be assessed.

### Formula 3. Objective normalization

The paper's second numbered equation is:

\\[ \boxed{ O'= \operatorname{clip} \left( \frac{O-O\_{\mathrm{naive}}} {1-O\_{\mathrm{naive}}}, 0,1 \right) } \tag{2} \\]

where:

- \\(O\_{\mathrm{naive}}\\): Objective value for an unoptimized but compliant reference design.
- \\(\operatorname{clip}(x,0,1)\\): Restricts the output to the interval \\([0,1]\\).
- \\(O'\\): Improvement relative to the reference design, normalized to the certified bound.

174. Baseline normalization: Comparing an improved design with an ordinary compliant reference.
175. Clipping function: Restricting computed values to prescribed limits.
176. Relative objective improvement: Measuring the gain over the baseline design.
177. Design optimality: Achieving the best objective value allowed by the certified bound.
178. Feasibility versus optimality: Distinguishing whether a design satisfies requirements from how efficiently it does so.

Engineering interpretation: Two designs may satisfy the same constraints yet have different economic quality. The objective term is intended to distinguish them.

The paper applies this rule to applicable co-authored design tasks; it is not a universal formula for all 85 engineering assignments.

## Page 10. Engineering Data, Input Formats, and Deliverable Statistics

Figures 6 and 7, Section 4, Data Analysis

179. Dataset composition: How engineering information is distributed across tasks and file types.
180. Engineering-document diversity: Differences among PDF reports, spreadsheets, text files, engineering models, images, and code.
181. Native engineering formats: Source files stored in the formats used by practicing engineers.
182. Geometric data: Information about physical dimensions, locations, and spatial relationships.
183. Numerical data: Quantities, equipment values, calculated results, and engineering parameters.
184. Textual engineering evidence: Specifications, correspondence, design notes, and requirements.
185. Schematics and imagery: Visual representations of engineering systems.
186. Project-data volume: The storage and processing burden associated with realistic technical files.
187. Engineering-deliverable diversity: Production outputs ranging from documents and spreadsheets to executable code and 3D models.
188. Multifile engineering packages: Sets of outputs that must be mutually consistent.
189. Document-centric workflows: Tasks dominated by reading technical records and issuing reports.
190. Model-centric workflows: Tasks involving engineering geometry, calculations, and model production.

### Quantitative realities from the dataset

| Measurement              | Expert-authored | Co-authored |
| ------------------------ | --------------- | ----------- |
| Tasks                    | 44              | 41          |
| Mean environment files   | 62.8            | 58.7        |
| Largest environment      | 112 files       | 207 files   |
| Average environment size | 3.0 MB          | 38.1 MB     |
| Mean deliverables        | 1.1             | 4.9         |

The complete benchmark contains 5,170 environment files and requires 249 deliverable files.

Engineering implication: The agent needs strong document navigation, file interpretation, cross-document reasoning, and output-validation capabilities. A text-only reasoning system is insufficient for many tasks.

## Page 11. Computational Experiment Design

Section 5.1, Experimental Setup

191. Foundation model: A pretrained AI model used as the reasoning component of the engineering agent.
192. Agent harness: The software surrounding a model that manages tasks, tools, memory, execution, and outputs.
193. Model–harness pairing: A particular model operating within a particular agent architecture.
194. Experimental control: Holding evaluation conditions fixed when comparing models and harnesses.
195. Computational container: An isolated environment for executing the engineering work.
196. Model proxy: The controlled interface through which agents access their models.
197. Inference budget: Resources allocated to generating model responses.
198. Time budget: Maximum duration permitted for engineering work.
199. Reasoning effort: Model inference configuration affecting computation.
200. Independent grading: Evaluation performed outside the agent's execution environment.
201. Grader isolation: Preventing the agent from accessing answers or evaluation logic.
202. Repeated trials: Running the same configuration multiple times to measure variation.
203. Engineering task score: A numerical representation of assessed deliverable performance.
204. Zero-score outcome: A run with no credited engineering result or a complete failure under the applicable grading rules.

### Experiment configuration

- 14 AI models.
- Seven main publicly available agent harnesses, with a separate Grok-specific configuration.
- Three runs per task and model–harness configuration.
- Six-hour maximum agent execution time.
- Independent grading after execution.

### Special engineering constraints

The paper identifies stricter scoring for certain physical-design tasks.

For MEP coordination, a hard clash or an unserved equipment row can produce a zero score.

For site design, infeasibility restricts the achievable score.

These are examples of engineering-specific grading conditions, distinct from the general Equation (1).

## Page 12. Engineering Performance by Discipline

Table 3 and Section 5.2, Main Results

205. Mean task performance: Average benchmark score across engineering tasks.
206. Discipline-specific evaluation: Comparing performance separately for electrical, civil, mechanical, and structural tasks.
207. Experimental benchmarking: Measuring actual system performance under a common evaluation procedure.
208. Model capability gap: Difference in performance between AI models.
209. Harness effectiveness: Effect of the software architecture on model performance.
210. Computational cost: Financial cost incurred by model inference and execution.
211. Engineering generalization: Ability to solve diverse engineering assignments rather than one specific task.

### Representative published results

Claude Opus 5.5, scores in percent across all 85 tasks, averaged over three runs

| Harness     | Overall | Electrical | Civil | Mechanical | Structural |
| ----------- | ------- | ---------- | ----- | ---------- | ---------- |
| Pi          | 47.3    | 46.7       | 60.7  | 40.5       | 45.0       |
| OpenCode    | 47.4    | 47.9       | 62.1  | 39.2       | 44.4       |
| Antigravity | 48.4    | 49.5       | 62.1  | 41.4       | 41.6       |
| Hermes      | 48.6    | 51.9       | 65.1  | 38.4       | 40.8       |
| Codex       | 49.3    | 53.1       | 67.8  | 36.6       | 43.8       |
| OpenHands   | 49.9    | 50.6       | 67.0  | 40.2       | 46.6       |
| Claude Code | 50.6    | 50.7       | 69.9  | 40.5       | 46.6       |

Scientific observation: Performance depends on both model and harness. No single harness is automatically the strongest for every engineering discipline.

## Page 13. Statistical Analysis, Reliability, and Failure Mechanisms

Figure 8 and Section 5.3, Analysis

212. Performance distribution: Variation in scores across engineering tasks.
213. Inter-model variation: Differences in results produced by different AI models.
214. Inter-harness variation: Differences attributable to the agent implementation.
215. Within-configuration variability: Variation among repeated executions with the same model and harness.
216. Standard deviation: A measure of variation in repeated results.
217. Task-score range: Difference between the highest and lowest scores obtained for a task under repeated evaluation.
218. Evaluation robustness: Stability of results under repeated assessment.
219. LLM-as-a-judge: Using an AI model to evaluate technical deliverables against criteria.
220. Inter-rater agreement: Agreement between separate grading decisions.
221. Cohen's kappa (\\(\kappa\\)): Statistical measure of agreement adjusted for chance agreement.
222. Kendall's tau (\\(\tau\\)): Measure of agreement between rank orderings.
223. Judge dependence: Sensitivity of evaluation results to which model performs the grading.
224. Self-preference bias: Potential bias when a model evaluates outputs associated with its own model family.
225. Failure-rate analysis: Categorizing and quantifying unsuccessful attempts.
226. Constraint satisfaction rate: Proportion of engineering requirements successfully met.
227. Joint hard-constraint satisfaction: Requirement that all mandatory constraints pass together.
228. Numerical and execution failure: Problems such as context exhaustion, model errors, time limits, or missing output.
229. Engineering infeasibility: A delivered design that violates physical or mandatory design conditions.

### Statistical observations

The paper reports:

- A mean range of 15.4 percentage points across three runs for a task–harness combination.
- 105 of 595 such combinations spanning at least 30 points.
- Stronger stability in overall benchmark averages than in individual-task scores.
- Cohen's \\(\kappa=0.97\\) for two passes of the same principal judge, indicating high reported agreement.

### Major physical-engineering failure

The strongest configuration satisfied approximately 91% of constraints on average for co-authored deliverables, but only 41.3% of deliverable items satisfied every hard constraint.

This is one of the most important findings for our agent architecture.

A solution that satisfies many engineering requirements can still fail because one mandatory safety or feasibility condition remains unsatisfied.

## Page 14. Scientific Conclusions and Real-World Engineering Limits

Section 6, Conclusion and Ethical Discussion

230. Production-ready engineering: Output intended to match professional deliverable standards.
231. Physical-code reconciliation: Resolving both physical-system requirements and applicable technical rules.
232. Economic optimality: Achieving competitive cost or performance while preserving compliance.
233. Constraint completeness: Satisfying all necessary conditions, not merely the majority.
234. Engineering automation limitations: Boundaries between present AI capabilities and professional engineering judgment.
235. Human expert validation: Independent assessment of engineering realism and technical correctness.
236. Scientific reproducibility: Reporting model, harness, experiment configuration, and results sufficiently clearly to support verification.
237. Data licensing and provenance: Legal and documentary traceability of engineering source materials.
238. Professional accountability: Human responsibility for real engineering decisions and authorizations.
239. Safety-critical evaluation: Treating violations of fundamental safety conditions as especially consequential.

### Central finding

The paper identifies full hard-constraint satisfaction combined with cost optimization as a major unsolved challenge for current engineering agents.

This means that improving the language model alone is not enough. The software workflow must also detect engineering errors and enforce mandatory requirements.

## Pages 15–18. Technical Concepts Appearing in the References

Bibliography and related scientific literature

These pages consist primarily of references. The following are relevant research concepts appearing in the referenced titles or descriptions, not methods derived or experimentally tested by the PLE paper itself.

240. Multiphysics reasoning: Reasoning across physical systems or interacting physical phenomena.
241. Finite-element methods and simulation: Numerical discretization of physical engineering problems.
242. Analog circuit modeling: Mathematical and computational representation of electronic circuits.
243. SPICE netlists: Structured descriptions of electronic circuits for simulation.
244. Power-system dispatch: Allocation or scheduling of power-system resources.
245. Structural engineering workflow automation: AI-supported execution of structural engineering processes.
246. Building energy systems: Engineering systems governing building heating, cooling, and energy performance.
247. HVAC operations: Operation and control of heating, ventilation, and air-conditioning systems.
248. Generative engineering optimization: Using computational methods to construct and improve designs.
249. CAD program generation: Producing geometry or CAD instructions computationally.
250. Sequential CAD modeling: Building geometric designs through ordered modeling operations.
251. Engineering document understanding: Extracting and interpreting information from technical records.
252. Multimodal AI evaluation: Evaluating systems that process text, images, drawings, and structured information.
253. Scientific coding: Implementation of computational scientific reasoning.
254. Research reproducibility: Independent reproduction of computational research results.
255. Agent-based optimization: Systems using autonomous tools and reasoning to pursue computational goals.
256. Tool-assisted reasoning: Combining model-generated plans with external computational operations.
257. Engineering benchmark contamination: Evaluation problems being compromised by prior exposure to their answers.
258. Human–AI engineering collaboration: Interaction between professional expertise and computational agents.

Scientific caution: A paper cited in the bibliography is not evidence that PLE itself implements the methods described in that cited work.

## Page 19. Evaluation Parameters and Mathematical Comparison

Appendix A, Appendix B, Tables 4 and 5

259. Experimental configuration matrix: Combinations of AI models and agent harnesses.
260. Model comparison: Assessment of performance differences between foundation models.
261. Harness comparison: Assessment of the contribution of software execution architectures.
262. Reasoning configuration: Settings controlling model inference.
263. Network restriction: Preventing unrestricted external access during evaluation.
264. Repeated evaluation: Three runs for each task–configuration pairing.
265. Independent rubric judging: Scoring deliverables separately from their generation process.
266. Frozen executable grader: An evaluation program that remains fixed during experiments.
267. Computational budget: Six hours, equivalent to 21,600 seconds, per task.
268. Performance matrix: Table 5 reports the scores of model–harness combinations.
269. Ranking sensitivity: Results depend on both the AI model and its surrounding software architecture.

### Results worth retaining

| Model and harness             | Mean score over 85 tasks |
| ----------------------------- | ------------------------ |
| Claude Opus 5.5, Claude Code  | 50.6%                    |
| GPT 6 Astra, Codex            | 48.3%                    |
| Gemini 4 Argon, Claude Code   | 43.2%                    |
| Gemini 3.8 Flash, Claude Code | 28.2%                    |
| GLM 5.2, Codex                | 25.3%                    |

These are historical benchmark results within the paper's experimental design. They should not be treated as predicted scores for our repository.

## Page 20. Complete Realistic Engineering Problem Specification

Appendix C, Figure 9, Expert Seed Nomination Interface

The final page provides six essential fields for specifying realistic engineering problems.

### 1. Situation

270. Engineering problem context: Description of the actual system and the engineering assignment.
271. Engineering role: Identification of professional responsibility.
272. Operational environment: Conditions within which the solution must function.
273. Facility electrical distribution: The electrical infrastructure serving the facility.
274. 480 V and 208 V systems: Voltage levels mentioned in the illustrative electrical design task.
275. Underground duct banks: Underground arrangements containing electrical conduits or cables.
276. Indoor conduits: Protective pathways for electrical conductors.

### 2. Inputs

277. Single-line electrical diagrams: Simplified drawings describing electrical distribution topology.
278. Motor load schedules: Technical records of motor electrical requirements.
279. Panel schedules: Records identifying electrical circuits and loads.
280. Geotechnical thermal-resistivity data: Ground-property information relevant to underground cable thermal conditions.
281. Vendor equipment catalogues: Product specifications used to select physical components.
282. Cable price books: Material pricing used to evaluate design alternatives.
283. Revision control: Identification of which engineering documents govern.

### 3. Goal

284. Installed material cost: Total relevant conductor and conduit material expense.
285. Conductor selection: Choosing suitable cable sizes and types.
286. Conduit selection: Choosing suitable cable containment arrangements.
287. Multicircuit design optimization: Considering the requirements and costs of multiple circuits.
288. Feasible-cost minimization: Minimizing cost while preserving all mandatory engineering limits.

### 4. Constraints

289. National Electrical Code (NEC): Electrical installation code cited in the illustrative task.
290. Unified Facilities Criteria (UFC): Technical criteria used in relevant federal facility design.
291. UFC 3-501-01: The specific electrical-engineering criteria document named in the example.
292. Neher–McGrath thermal derating: A named approach for considering thermal effects on underground electrical conductor ampacity.
293. Mutual heating: Thermal interaction between cables carrying electrical current.
294. Cable thermal resistivity: Material or surrounding-medium properties influencing heat transfer.
295. Voltage-drop limit: Maximum permitted voltage loss along specified electrical paths.
296. Feeder voltage-drop criterion: The example specifies a limit of 3%.
297. Total voltage-drop criterion: The example specifies a combined limit of 5%.
298. Fire-pump locked-rotor voltage drop: Voltage-drop consideration associated with fire-pump motor starting conditions.
299. Equipment termination limits: Restrictions on conductor compatibility with electrical equipment terminals.
300. Standardized cable-size choices: The example restricts the number of distinct cable sizes above a specified AWG reference.

These are the example task's stated requirements. They are not universal limits applicable to every electrical installation.

### 5. Verification

301. Python engineering verifier: A program checking the completed engineering design.
302. Hard-constraint checks: Mandatory physical, safety, and feasibility evaluations.
303. Soft-constraint checks: Documentation or other nonmandatory criteria.
304. Per-circuit compliance: Checking the requirements associated with each electrical circuit.
305. Source-clause register: A structured record of the standards, values, and documents used.
306. Installed-package cost: Total cost of the selected engineering configuration.
307. Certified relaxation bound: The independently established benchmark against which optimized cost is compared.

The example describes checking 25 hard and 10 soft constraints per circuit.

### 6. Expected Output

308. Cable and conduit schedule (XLSX): Structured record of the selected conductors and conduits.
309. Updated electrical riser drawing (DXF): Revised technical drawing.
310. Code requirement register (JSON): Machine-readable list of applicable engineering requirements and their sources.
311. Production-format verification: Confirming that required files exist and use the correct formats.
312. Cross-file consistency: Ensuring that drawings, schedules, and requirement registers agree.
313. Traceable engineering decision: A final result supported by identifiable calculations, constraints, and source evidence.

This final example makes the mathematical and physical meaning of the competition especially clear: the agent must design a system that is compliant, physically feasible, economically competitive, and properly documented.

## Consolidated Mathematical Formula Register

The paper's directly stated mathematical relations and evaluation quantities can be summarized as follows.

| Mathematical expression                                                                          | Meaning                                                        | Location             |
| ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- | -------------------- |
| \\(s=0.4p+0.6GO'\\)                                                                              | Constraint and objective score                                 | Page 9, Equation (1) |
| \\(p\in[0,1]\\)                                                                                  | Constraint satisfaction fraction                               | Page 9               |
| \\(G\in\\{0,1\\}\\)                                                                              | Hard feasibility gate                                          | Page 9               |
| \\(O'\in[0,1]\\)                                                                                 | Normalized objective score                                     | Page 9               |
| \\(O=c\_{\mathrm{bound}}/c\\)                                                                    | Cost-based objective                                           | Page 9               |
| \\(O'=\operatorname{clip}\left(\frac{O-O\_{\mathrm{naive}}}{1-O\_{\mathrm{naive}}},0,1\right)\\) | Normalized improvement over baseline                           | Page 9, Equation (2) |
| \\(N=3\\)                                                                                        | Typical number of independent calibration attempts             | Page 8               |
| \\(\tau\\)                                                                                       | Target difficulty threshold                                    | Page 8               |
| \\(\kappa=0.97\\)                                                                                | Reported agreement between two principal-judge passes          | Page 13              |
| \\(\tau=1.0,\ 0.90\\)                                                                            | Reported Kendall rank-agreement results under alternate judges | Page 14              |

Important: The \\(\tau\\) used for the difficulty threshold and Kendall's \\(\tau\\) for rank correlation are different concepts that happen to use the same Greek letter.

### Physical equations the paper does not explicitly derive

Although it refers to these concepts, the paper does not provide their governing mathematical derivations:

- Electrical voltage-drop equations.
- Current-carrying-capacity and thermal-derating equations.
- Neher–McGrath underground cable thermal equations.
- Heat-transfer and cooling-tower performance equations.
- Pump hydraulic equations.
- Structural gravity, wind, snow, or seismic load equations.
- Roof-diaphragm shear equations.
- Geotechnical foundation-settlement equations.
- Hydraulic-grade-line equations.
- Mathematical formulations of 3D MEP collision-free routing.

We would need the actual task materials, applicable codes, and suitable engineering references to construct and verify those models.

## The Most Important Engineering Lessons for Our Agent

The extraction leads to five central requirements for our architecture:

1. Requirements must be traceable. The agent needs to identify governing documents, source clauses, numerical limits, and revisions before computing.
2. Mathematical computation must be independently checked. Correct-looking numbers are insufficient without units, assumptions, constraint checks, and numerical verification.
3. Physical feasibility must precede optimization. A lower-cost design is not acceptable when mandatory engineering limits fail.
4. Engineering deliverables must be mutually consistent. Calculations, schedules, 2D drawings, 3D models, and technical reports must describe the same design.
5. Performance must be demonstrated experimentally. Repeated runs, per-discipline results, failures, model comparisons, and costs are needed to justify improvements.

The paper's central scientific distinction is:

\\[ \boxed{ \text{Engineering compliance} \neq \text{Engineering optimality} } \\]

A design can satisfy basic engineering checks without being economically competitive. Conversely, an inexpensive design can be unacceptable because it violates a critical constraint.

For the PLE agent in our GitHub repository, the essential objective is to achieve both feasibility and quality while producing verifiable engineering artifacts.