# Complete Physics, Engineering, and Mathematics Keyword Register for the ASU MSE Thesis

**Official V3 title:** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Date:** 2026-11-13  
**Scientific status:** Derivative study and terminology reference. **Not a new scope amendment, established causal link or frozen final mathematical model.**

## Scientific identity

**Frozen General Objective (verbatim):**

> To characterize and model thermal interdependencies between the Power System and the Electrified Transportation System under extreme heat, and to quantify how their consequences evolve through physical state and time.

**Frozen SO1 (verbatim):**

> Identify and qualify the thermally sensitive physical states and directional thermal interdependency mechanisms connecting the Power System and the Electrified Transportation System.

**Frozen SO2 (verbatim):**

> Develop a physics-based state-time model of the qualified thermal interdependencies and their propagation under extreme heat.

**Frozen SO3 (verbatim):**

> Quantify critical transition times, interdependency propagation delays, and the resulting electricity and mobility service consequences.

### Governing causal/evidential chain

```text
Extreme heat forcing
→ Thermally sensitive physical states
→ Thermally conditioned capability and constraints
→ Qualified directional thermal interdependency
→ State-time transitions and propagation
→ Required electricity/mobility service consequences
→ Service-level resilience interpretation
```

The Power System and Electrified Transportation System remain distinct; EVSE belongs to Electrified Transportation. The eight selected research subjects are a working **component roster**, not eight independent ODEs. Shared ambient heat or an electrical connection alone is not proof of thermal causation.

This is a **glossary of 313 defined terms**, including scientific foundations, conditional candidate mechanisms, numerical methods, and evidence needs. Inclusion in the glossary does not mean a state, coefficient, threshold, interface, or service metric has passed model-admission and validation gates.

## Full keyword glossary (313 entries)

### A. Fundamental systems and research concepts

1. **Physical infrastructure:** Engineered equipment and networks providing electricity, transportation, and associated services.
2. **Power System (P):** The physical electrical infrastructure supplying and distributing electricity.
3. **Electrified Transportation System (T_e):** The complete technical system comprising electrically propelled road vehicles, energy storage, propulsion, electrical auxiliaries, power-supply circuits, EVSE, charging connections, and required power-transfer communication/control.
4. **Coupled systems:** Two distinct systems whose states, constraints or operation can influence each other through qualified relationships.
5. **System of Systems (SoS):** An architectural perspective on interacting systems that retain distinct identities.
6. **Complex system:** A system whose interactions and dynamics may produce nontrivial collective behavior.
7. **System boundary:** The definition of which physical components belong to each system.
8. **Active model boundary:** The subset of physical phenomena and variables represented in the selected mathematical model.
9. **Physical interface:** A location or mechanism through which systems exchange physical quantities.
10. **Electrical interface:** A connection enabling electrical power, current or energy transfer.
11. **Thermal interdependency:** A qualified directional dependency through which thermal state or thermally conditioned capability influences the other system or its service.
12. **Directional relationship:** A source-to-receiver effect whose direction must be justified.
13. **Power-to-Transportation (P→T_e):** A candidate effect originating in Power-system thermal conditions and influencing electrified transportation.
14. **Transportation-to-Power (T_e→P):** A candidate effect originating in transportation-side thermal behavior and influencing the Power System.
15. **Bidirectional interaction:** Two separately established directional relationships, not simply a two-headed arrow.
16. **Physical connection:** An actual electrical or mechanical connection, which alone does not prove thermal causation.
17. **Functional dependency:** Reliance of one function or capability on another system's operation.
18. **Thermal exposure:** The influence of external temperature or heat on equipment.
19. **Common-cause forcing:** The same external heat event affecting both systems without necessarily creating intersystem causation.
20. **Minimum sufficient physics:** Modeling only those physical states and mechanisms necessary to answer the defined research questions.
21. **Component-level behavior:** The physical behavior of an individual piece of equipment.
22. **System-level consequence:** The outcome of component interactions on electricity or mobility delivery.
23. **Service-level resilience:** Maintaining or recovering required services as thermal states and dependencies evolve.
24. **Engineering feasibility:** Whether a model, mechanism or engineering response is physically and operationally admissible.
25. **Scientific qualification:** Establishing enough physical, mathematical and observational evidence to admit a mechanism into the research model.

### B. Extreme heat and environmental physics

26. **Extreme heat:** The external thermal stressor investigated by the thesis.
27. **Ambient temperature (T_a):** Temperature of the surrounding environment.
28. **Heat-event onset (t_0):** Declared beginning of the extreme-heat event.
29. **Heat-exposure duration:** Time over which the system experiences the declared thermal conditions.
30. **External forcing (H(t)):** Time-dependent environmental input influencing system dynamics.
31. **Temperature trajectory:** Temperature evolving over time.
32. **Diurnal temperature variation:** Daily pattern in ambient thermal conditions.
33. **Heatwave duration:** Length of the extreme-heat episode.
34. **Initial thermal condition:** Equipment temperature at the beginning of the analysis.
35. **Thermal history:** Previous temperature and loading conditions influencing the present state.
36. **Heat accumulation:** Energy stored when heat generation exceeds heat rejection.
37. **Thermal inertia:** Resistance to rapid temperature changes due to thermal storage.
38. **Thermal lag:** Delayed thermal response following a change in forcing.
39. **Transient thermal response:** Time-dependent temperature behavior before equilibrium.
40. **Thermal equilibrium:** Condition in which net heat storage is zero.
41. **Thermal boundary condition:** Prescribed temperature, heat flux or other condition at a model boundary.
42. **Ambient convection:** Heat exchange between equipment surfaces and surrounding fluid.
43. **Solar thermal gain:** Heat input from solar radiation, when relevant to the equipment.
44. **Soil thermal conditions:** Underground thermal environment potentially affecting buried cables.
45. **Wind-dependent cooling:** Influence of airflow on convective heat rejection.
46. **Environmental heat rejection:** Transfer of heat from equipment to its surroundings.
47. **Operating temperature range:** Range over which equipment or the adopted model is applicable.
48. **Extreme-heat scenario:** A declared environmental forcing sequence used for analysis.
49. **Climate-data uncertainty:** Uncertainty in measured or prescribed temperature forcing.
50. **Thermal exposure versus interdependency:** Simultaneous heating of two components does not prove a causal relationship between them.

### C. Fundamental thermodynamics and heat transfer

51. **First law of thermodynamics:** Conservation of energy.
52. **Thermal energy balance:** Accounting for heat generation, input, output and storage.
53. **Internal energy:** Energy associated with a system's physical condition.
54. **Thermal capacitance (C_th):** Effective heat storage per unit temperature change.
55. **Heat capacity:** Heat required to change a material or body's temperature.
56. **Specific heat capacity (c_p):** Heat capacity per unit mass.
57. **Thermal resistance (R_th):** Resistance to heat transfer.
58. **Thermal conductivity (k):** Material property governing conductive heat transport.
59. **Heat conduction:** Transfer of thermal energy through a temperature gradient.
60. **Heat convection:** Heat transfer involving fluid and surface interaction.
61. **Thermal radiation:** Electromagnetic heat exchange associated with temperature.
62. **Heat flux (q''):** Heat-transfer rate per unit area.
63. **Heat-generation rate (Qdot_gen):** Thermal power generated internally.
64. **Heat-rejection rate (Qdot_out):** Rate at which equipment transfers heat to its surroundings.
65. **Temperature gradient:** Spatial temperature variation.
66. **Lumped thermal model:** Reduced representation using one or a few temperatures.
67. **Distributed thermal model:** Representation with temperature varying across physical space.
68. **Heat-transfer coefficient (h):** Effective parameter describing convective heat exchange.
69. **Thermal time constant (tau_th):** Characteristic response time under a specified model.
70. **Steady-state temperature:** Equilibrium temperature under specified, unchanging conditions.
71. **Heat-transfer nonlinearity:** Temperature-dependent or otherwise nonlinear heat exchange.
72. **Temperature-dependent material property:** Resistance, viscosity or conductivity varying with temperature.
73. **Control volume:** Explicit physical region over which conservation equations are applied.
74. **Thermal constitutive law:** Relationship connecting heat flux, temperature and relevant properties.
75. **Conservation residual:** Difference between the two sides of a governing energy balance.

### D. Power-system equipment and electrical physics

76. **P1, Distribution Transformer:** Equipment transferring electrical power between voltage levels.
77. **P2, Distribution Feeder:** Electrical conductors and associated network elements transferring power to downstream loads.
78. **P3, Transformer Protection/Load-Management Hardware:** Real installed equipment that may restrict or manage loading under declared conditions.
79. **P4, Transformer Cooling Equipment:** Equipment responsible for transformer heat rejection.
80. **Transformer core:** Magnetic structure supporting electrical energy transformation.
81. **Transformer winding:** Conductors carrying current and generating load-related heat.
82. **Core losses:** Electrical power dissipated through magnetic processes.
83. **Copper or winding losses:** Load-dependent resistive losses in transformer conductors.
84. **No-load losses:** Losses present during energized operation even at little or no load.
85. **Load losses:** Losses dependent on load and equipment condition.
86. **Joule heating:** Resistive conversion of electrical energy into heat.
87. **Top-oil temperature (theta_TO):** Oil temperature used in transformer thermal modeling.
88. **Winding hottest-spot temperature (theta_HS):** Temperature associated with the relevant winding hot region.
89. **Hot-spot temperature rise:** Difference between the hot-spot temperature and a reference temperature.
90. **Oil thermal inertia:** Thermal storage associated with transformer oil and surrounding structures.
91. **Winding thermal inertia:** Thermal storage governing winding-temperature evolution.
92. **Oil viscosity (mu):** Fluid property affecting circulation and heat transfer.
93. **Natural oil circulation:** Oil movement driven by temperature-dependent density differences.
94. **Natural-air cooling:** Heat rejection to air without forced airflow.
95. **Forced cooling:** Fan- or pump-assisted heat rejection when applicable to the actual equipment.
96. **ONAN transformer:** Oil Natural Air Natural cooling classification.
97. **Transformer rated apparent power:** Equipment rating typically expressed in kVA or MVA.
98. **Transformer loading:** Actual electrical burden relative to the equipment's applicable operating limits.
99. **Temperature-dependent loading capability:** Potential change in permissible loading resulting from thermal conditions.
100. **Transformer thermal protection:** Hardware or operating logic responding to measured or estimated thermal conditions.
101. **Protection setpoint:** Documented threshold used by an installed control or protection function.
102. **Trip action:** Actual protective disconnection when supported by installed equipment and settings.
103. **Load curtailment:** Reduction in supplied or permitted electrical demand.
104. **Feeder conductor resistance:** Resistance of the selected electrical conductor.
105. **Feeder electrical losses:** Energy dissipated along distribution conductors.
106. **Conductor ampacity:** Permissible current under defined thermal conditions.
107. **Overhead conductor cooling:** Heat exchange between exposed conductors and their surroundings.
108. **Underground cable heating:** Heat production and transport involving buried conductors and surrounding material.
109. **Power-flow equations:** Network relationships governing voltages, currents and power exchange.
110. **Transformer thermal capability map:** A relation connecting thermal state to permissible electrical operation, which remains equipment- and evidence-dependent.

### E. Electrified transportation equipment and physical behavior

111. **T1, DC EV Charger:** Charging equipment delivering regulated DC electrical power to an electric vehicle.
112. **T2, Vehicle Battery Pack:** Rechargeable electrical energy-storage equipment.
113. **T3, EVSE Cooling Equipment:** Equipment removing heat from charging-system components.
114. **T4, Vehicle HVAC Equipment:** Vehicle heating, ventilation and air-conditioning equipment.
115. **Electric vehicle supply equipment (EVSE):** Equipment enabling controlled energy transfer to a vehicle.
116. **Physical charging connection:** The actual electrical interface between charging equipment and vehicle.
117. **Charging connector:** Hardware forming the relevant electrical connection.
118. **AC input power:** Electrical power drawn from the distribution system by charging equipment.
119. **DC output power:** Electrical power delivered by the charger to the vehicle.
120. **AC/DC conversion:** Conversion of alternating-current electrical input into direct-current output.
121. **Power electronic rectifier:** Converter hardware performing the AC/DC conversion.
122. **Power conversion losses:** Electrical power dissipated during conversion.
123. **Charging efficiency:** Relationship between relevant AC energy input and DC energy output.
124. **Charger internal temperature:** Temperature of a relevant EVSE component.
125. **Rectifier temperature:** Thermal state of a charging-system power-conversion component.
126. **EVSE thermal derating:** Reduction in permissible or achieved charging power caused by thermal conditions.
127. **Charger cooling mode:** Cooling-system operating condition affecting EVSE temperature.
128. **Charging power request:** Requested charging power from the applicable control process.
129. **Actual charging power:** Power actually transferred and measured.
130. **Charging power limit:** Bound imposed by EVSE, vehicle, infrastructure or operating conditions.
131. **Battery state of charge (SOC):** Battery energy state expressed relative to a defined usable capacity.
132. **Battery charging acceptance:** Power a battery system can accept under its current conditions.
133. **Battery management system (BMS):** Vehicle system controlling and monitoring battery operation.
134. **Battery thermal state:** Battery temperature required by an adopted physical model.
135. **Battery thermal management:** Regulation of battery temperature.
136. **Vehicle auxiliary electrical load:** Electrical consumption unrelated to propulsion, including relevant thermal management.
137. **HVAC energy demand:** Energy consumed to heat or cool the vehicle environment.
138. **Charging session:** Interval during which charging equipment serves a vehicle.
139. **Arrival time:** Time a vehicle becomes available for charging.
140. **Departure deadline:** Time by which an identified mobility energy requirement must be satisfied.
141. **Required departure energy:** Battery energy necessary to meet a declared readiness condition.
142. **Charging duration:** Time over which charging occurs.
143. **Charging energy deficit:** Difference between required and achieved energy at the relevant deadline.
144. **Vehicle readiness:** Whether the selected vehicle or fleet satisfies its declared departure requirement.
145. **Mobility service:** Required transportation function, distinct from the technical vehicle system itself.
146. **Charging demand profile:** Charging power as a function of time.
147. **Fleet charging aggregation:** Combination of demand from multiple charging sessions.
148. **Trip energy consumption:** Energy consumed during a vehicle trip.
149. **Energy consumption per distance:** Vehicle energy use normalized by measured distance.
150. **Vehicle-to-Grid (V2G):** Bidirectional electrical transfer where supported, not automatically an established thermal interdependency.

### F. Directional thermal interdependencies and physical interfaces

151. **I1, ordinary electricity supply:** The established electrical transfer pathway from Power infrastructure to EVSE; not by itself a thermal interdependency.
152. **I2, candidate thermal-conditioned T_e→P:** Charging-system temperature and cooling behavior affecting measured grid-side AC demand, followed by changes in transformer loading and thermal state.
153. **I3, candidate thermal-conditioned P→T_e:** Transformer temperature influencing an actually implemented protection or load-management action that changes charging capability.
154. **I4, charger internal thermal mechanism:** EVSE heat generation, cooling and possible thermal derating.
155. **I5, charging-to-battery energy pathway:** Transfer of DC charging energy into the vehicle energy-storage system.
156. **I6, heat-conditioned vehicle demand pathway:** HVAC energy use influencing later charging requirements and potentially transformer thermal loading.
157. **I7, supporting price-informed charging decision:** A conditional economic or informational influence on charging, not itself a thermal interdependency.
158. **Source component:** Equipment where the proposed causal mechanism originates.
159. **Receiver component:** Equipment affected by the source-side mechanism.
160. **Electrical input port:** The defined location where electric power enters equipment.
161. **Electrical output port:** The defined location where electrical power leaves equipment.
162. **Active power (P_AC):** Grid-side real power associated with charging demand.
163. **Reactive power (Q_AC):** AC reactive power relevant to apparent power and current.
164. **Apparent power (S):** Combined magnitude of active and reactive power under compatible definitions.
165. **Interface current (I):** Electrical current connecting charging demand to conductor and transformer loading.
166. **Thermal-conditioned coupling:** A coupling relationship whose behavior depends on thermal states or thermal operating limits.
167. **Coupling variable (Z_PT^th):** Mathematical representation of qualified cross-system thermal-related exchanges or constraints.
168. **Interface topology:** Identification of which actual components and ports are connected.
169. **Directional mechanism qualification:** Establishing the physical and evidential support for a proposed source-to-receiver effect.
170. **Electrical coupling versus thermal coupling:** Distinguishing ordinary power exchange from an effect caused by thermal conditions.
171. **Thermal causality:** A physically supported temperature-dependent influence between the systems.
172. **Implemented protective action:** Real equipment behavior that changes permissible operation.
173. **Control-command evidence:** Recorded commands or actions establishing how equipment responded.
174. **Common-cause confounding:** Apparent coupling explained by external heat acting independently on both systems.
175. **Non-EV base load:** Other electrical demand that must be separated from EV-induced loading.
176. **Time synchronization:** Alignment of measurements from different equipment using comparable timestamps.
177. **Matched measurement:** Observations from the same or demonstrably connected operating installation.
178. **Counterfactual comparison:** Comparison of outcomes under defined alternative thermal or operating conditions.
179. **Cross-system propagation pathway:** The physical sequence connecting source changes to receiver consequences.
180. **Independent bidirectional evidence:** Separate qualification of the P→T_e and T_e→P mechanisms.

### G. Mathematical state-space modeling and time-dependent dynamics

181. **State variable:** A variable whose current value is needed to predict the model's subsequent evolution.
182. **State vector (X):** Collection of admitted variables describing the modeled system condition.
183. **Full physical state space:** All physical states that could legitimately exist in the system.
184. **Reduced state vector:** Smaller set sufficient for the specific research question.
185. **Power thermal state (X_P^th):** Thermal states admitted for the Power System.
186. **Transportation thermal state (X_T_e^th):** Thermal states admitted for the Electrified Transportation System.
187. **Fast thermal state:** Temperature-related variable evolving over the relevant operational thermal horizon.
188. **Operational state:** State describing equipment operation, mode or another necessary operating condition.
189. **Energy state:** Stored-energy-related variable, such as battery SOC.
190. **Slow degradation state:** Health or aging variable evolving on an appropriate longer time horizon.
191. **Initial condition (X_0):** State at the start of a model trajectory.
192. **State trajectory (X(t)):** Evolution of the modeled state over time.
193. **Governing differential equation:** Mathematical law describing state evolution.
194. **Ordinary differential equation (ODE):** Equation involving time derivatives of state variables.
195. **Algebraic equation:** Relationship defining a variable without assigning it independent dynamics.
196. **Differential-algebraic equation (DAE):** Model combining evolving states with simultaneous algebraic constraints.
197. **Hybrid dynamical system:** Model combining continuous evolution with discrete operating modes or switching events.
198. **Operating mode:** Discrete condition influencing the applicable physical dynamics.
199. **Transition condition:** Defined boundary triggering a physical or operational change.
200. **Event detection:** Numerical identification of a threshold-crossing or switching event.
201. **Critical transition time (tau_i^C):** Time at which a physically meaningful limiting condition is first reached.
202. **Propagation delay (delta_ij^th):** Time between a qualified source transition and the relevant receiver response.
203. **Service-disruption onset (t_Q):** Time at which a required electricity or mobility service first becomes unsatisfied.
204. **Departure deadline (t_d):** Operational time by which required vehicle energy or readiness must be achieved.
205. **Recovery time (t_R):** Time associated with returning a degraded service to its requirement, where recovery is modeled.
206. **Degradation horizon (t_deg):** Time period relevant to a slow equipment-health process.
207. **Thermal-response timescale:** Characteristic duration of temperature evolution.
208. **Timescale separation:** Distinguishing processes that evolve at materially different rates.
209. **State-dependent constraint:** Operating limit that changes with the current physical state.
210. **Memory effect:** Dependence of future behavior on information carried by the current state and its past evolution.

### H. Mathematical methods, computation and parameter identification

211. **Analytical solution:** Solution obtained in mathematical form under specified assumptions.
212. **Numerical integration:** Approximation of a differential equation's time evolution.
213. **Explicit Euler method:** First-order numerical time-integration method.
214. **Runge–Kutta method (RK4):** Fourth-order numerical time-integration method.
215. **Exact zero-order-hold solution:** Exact integration over an interval with appropriately constant model inputs.
216. **Numerical timestep (Delta t):** Discrete time interval used in a computation.
217. **Temporal discretization:** Replacement of continuous-time equations by discrete computational steps.
218. **Truncation error:** Approximation error introduced by the numerical method.
219. **Numerical convergence:** Tendency of computed solutions toward a limiting result as numerical resolution improves.
220. **Timestep refinement:** Repeating a computation with smaller time steps to assess numerical accuracy.
221. **Stability analysis:** Examination of whether errors or perturbations grow under a mathematical or numerical scheme.
222. **Well-posedness:** Whether an adopted mathematical problem has suitably defined solution existence, uniqueness and stability properties.
223. **Parameter vector (theta):** Collection of model coefficients requiring physical justification or estimation.
224. **Parameter calibration:** Adjustment of parameters to fit selected observations.
225. **Parameter estimation:** Determination of parameter values from available evidence.
226. **Inverse problem:** Inferring unknown parameters or states from measured outputs.
227. **State estimation:** Reconstructing unobserved system states from available observations and a model.
228. **Observability:** Whether available measurements contain sufficient information to distinguish relevant states.
229. **Structural identifiability:** Whether model parameters are theoretically distinguishable under idealized information.
230. **Practical identifiability:** Whether finite and noisy data can distinguish parameters adequately.
231. **Sensitivity matrix (J):** Matrix of output changes with respect to model parameters.
232. **Singular-value decomposition (SVD):** Matrix factorization used to examine sensitivity and numerical conditioning.
233. **Condition number:** Measure of sensitivity of a numerical problem to perturbations.
234. **Optimization problem:** Selection of decision variables to minimize or maximize a defined objective under constraints.
235. **Linear programming (LP):** Optimization with linear objectives and constraints.
236. **Constrained charging scheduling:** Allocation of charging power subject to energy, time and power requirements.
237. **Feasible solution:** Solution satisfying all adopted mathematical constraints.
238. **Objective function:** Mathematical expression representing the target of optimization.
239. **Numerical residual:** Difference between the computed result and the condition it should satisfy.
240. **Dimensional consistency:** Requirement that both sides of a physical equation have compatible units.

### I. Electricity service, mobility service and resilience

241. **Electricity service (Q_P):** Defined electricity delivery or performance output.
242. **Mobility service (Q_T):** Defined transportation service output.
243. **Service requirement (Q_k^req):** Minimum acceptable service under the declared assessment.
244. **Service trajectory:** Service performance changing over time.
245. **Service deficit:** Amount by which actual service falls below its requirement.
246. **Service continuity:** Maintenance of required service during changing conditions.
247. **Service degradation:** Reduction in service performance.
248. **Service disruption:** Failure to meet a defined service requirement.
249. **Minimum achieved service:** Lowest service level over a declared interval.
250. **Disruption duration:** Time over which service remains below the requirement.
251. **Accumulated service deficit:** Integrated shortage over a declared interval.
252. **Mobility readiness:** Whether a vehicle or fleet meets the necessary energy condition by a specified deadline.
253. **Vehicle availability:** Operational availability, which may differ from energy readiness.
254. **Fleet readiness percentage:** Fraction of a declared fleet meeting its readiness requirement.
255. **Electricity-service shortfall:** Difference between required and delivered electrical service.
256. **Thermal resilience consequence:** Service impact caused by a qualified thermal interdependency.
257. **Maintain:** Preserve required service during thermal stress.
258. **Improve:** Increase thermal capability or reduce vulnerability before disruption.
259. **Adapt:** Modify operating actions while thermal conditions evolve.
260. **Restore:** Return disrupted services to acceptable levels.
261. **Recovery trajectory:** Time-dependent progression of service toward the requirement.
262. **Robustness:** Ability to withstand an imposed disturbance under a declared performance criterion.
263. **Reliability:** Consistency or probability of acceptable performance within a defined operating domain.
264. **Resilience:** Ability to maintain or recover required electricity and mobility services as thermal states and interdependencies evolve.
265. **Component survival versus service resilience:** Equipment remaining operational does not establish that required service is being delivered.

### J. Sustainability, energy accounting and engineering consequences

266. **Electricity loss energy:** Energy dissipated in transformers, feeders or charging equipment within clearly separated boundaries.
267. **Energy efficiency:** Ratio between useful energy output and the relevant energy input.
268. **EVSE energy efficiency:** DC charging output energy divided by relevant grid-side AC input energy.
269. **Nonoverlapping energy accounting:** Avoiding double counting of losses across equipment boundaries.
270. **Mobility energy intensity:** Vehicle trip energy consumed per measured distance.
271. **Energy consumption:** Amount of energy required by the declared system or activity.
272. **Environmental consequence:** Relevant changes in energy, emissions, material use or resource demand.
273. **Economic consequence:** Relevant changes in operating, maintenance, replacement, intervention or disruption costs.
274. **Social consequence:** Relevant changes in service continuity, access, affordability, equity or safety.
275. **Direct consequence pathway:** Thermal interdependency leading to service effects and bounded sustainability outcomes.
276. **Engineering-response consequence pathway:** Changes resulting from actions used to improve, adapt or restore service.
277. **Reference scenario:** Defined baseline against which other cases are evaluated.
278. **Heat-without-response scenario:** Extreme-heat case without the selected engineering action.
279. **Heat-with-response scenario:** Comparable extreme-heat case including the engineering action.
280. **Functional unit:** Common reference basis for comparing outputs and impacts.
281. **Assessment boundary:** Components, processes and activities included in the sustainability accounting.
282. **Assessment horizon:** Time interval over which consequences are measured.
283. **GHG emissions:** Greenhouse-gas consequences, where suitable activity and emission-factor evidence exists.
284. **Service-disruption cost:** Economic impact of unmet electricity or mobility service, when measurable.
285. **Resilience–sustainability trade-off:** Possibility that improving service resilience increases another environmental, economic or social burden.

### K. Scientific evidence, validation and uncertainty

286. **Physical mechanism evidence:** Observations or established principles supporting a proposed mechanism.
287. **Mathematical-form evidence:** Source support for the structure of an adopted equation.
288. **Parameter evidence:** Support for numerical coefficients and their applicability.
289. **Equipment-specific evidence:** Measurements or technical documentation for the actual component being studied.
290. **Evidence provenance:** Traceable origin of every scientific claim, equation, parameter or result.
291. **Source-domain applicability:** Conditions under which external evidence is valid.
292. **Parameter transferability:** Whether a parameter can legitimately be used in another system.
293. **Code verification:** Checking that computational software correctly implements the intended equations.
294. **Solution verification:** Estimating numerical solution error for the chosen model.
295. **Model validation:** Comparing mathematical predictions with suitable independent physical evidence.
296. **Uncertainty quantification (UQ):** Characterizing uncertainty in model inputs, parameters and predictions.
297. **Measurement uncertainty:** Uncertainty associated with observations.
298. **Parameter uncertainty:** Uncertainty in estimated physical or mathematical coefficients.
299. **Model-form uncertainty:** Error arising from assumptions or missing physical mechanisms.
300. **Numerical uncertainty:** Uncertainty caused by computational approximation.
301. **Sensitivity analysis:** Quantifying how changes in inputs or parameters affect outcomes.
302. **Falsifiable hypothesis:** A scientific prediction that a credible observation could contradict.
303. **Counter-hypothesis:** Alternative explanation against which a proposed mechanism can be tested.
304. **Full-text evidence extraction:** Retrieving actual equations, assumptions, domains, validation and limitations from original research.
305. **Systematic literature screening:** Applying documented inclusion, exclusion and evidence-classification decisions to research records.

### L. Real data and experimental evidence

306. **TU Wien low-voltage grid:** A candidate electrical-network benchmark for separately evaluating distribution-network behavior.
307. **Qatar CPC50 charger experiment:** Published charging and thermal evidence relevant to possible charger derating, with synchronized underlying data still requiring qualification.
308. **Measured AC/DC charging profiles:** Candidate evidence for identifying actual charging input/output relationships.
309. **SINTEF monitored transformer data:** Equipment-specific observations of loading and thermal response, used in the working temperature-model experiments.
310. **EPFL charging-session data:** Observations used to examine charging sessions, achieved energy and hypothetical scheduling.
311. **STREAM transformer-station monitoring:** Candidate station measurements requiring unit, topology and equipment verification before thermal interpretation.
312. **Linked transformer–charger measurement requirement:** Synchronized, physically connected observations needed to evaluate a genuine intersystem thermal mechanism.
313. **Extreme-heat validation requirement:** Measurements in the relevant high-temperature domain needed before claiming validation under extreme-heat conditions.

## Further scientific references

- [Mathematical formulas, scientific-status ledger, working evidence and limitations](THESIS_MATHEMATICAL_FORMULAS_AND_RESEARCH_CONTEXT.md)
- [Frozen thesis objectives](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md)
- [Current title authority](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_THESIS_TITLE_V3.md)

### Primary source files supporting this compiled reference

- [`project/CANONICAL_THESIS_TITLE_V3.md`](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_THESIS_TITLE_V3.md)
- [`project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md)
- [`project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md)
- [`project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md)
- [`project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md)
- [`project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md`](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md)
- [`project/CANONICAL_RESILIENCE_DEFINITION_V1.md`](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_RESILIENCE_DEFINITION_V1.md)
- [`project/CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md`](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md)
- [`project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md)
- [`project/PHYSICS_MATHEMATICS_FIRST_HYPOTHESIS_TESTING_SCOPE_DIRECTIVE_V1.md`](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/PHYSICS_MATHEMATICS_FIRST_HYPOTHESIS_TESTING_SCOPE_DIRECTIVE_V1.md)
- [`project/thermal_sos_functional_architecture/SELECTED_EIGHT_COMPONENTS_WORKING_RESEARCH_BASELINE_V1.md`](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/thermal_sos_functional_architecture/SELECTED_EIGHT_COMPONENTS_WORKING_RESEARCH_BASELINE_V1.md)
- [`project/thermal_sos_functional_architecture/EIGHT_COMPONENT_PHYSICS_AND_DIRECTIONAL_INTERFACE_RESEARCH_DOSSIER_V1.md`](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/thermal_sos_functional_architecture/EIGHT_COMPONENT_PHYSICS_AND_DIRECTIONAL_INTERFACE_RESEARCH_DOSSIER_V1.md)
- [`research/working/2026-11-11_advanced_thermal_stochastic_v2/02_EQUATIONS_AND_HYPOTHESES.md`](https://github.com/Dossiya-SE/MSE-thesis/blob/main/research/working/2026-11-11_advanced_thermal_stochastic_v2/02_EQUATIONS_AND_HYPOTHESES.md)
- [`research/working/2026-11-11_advanced_thermal_stochastic_v2/03_SINTEF_THERMAL_HOTSPOT_AND_AGING.md`](https://github.com/Dossiya-SE/MSE-thesis/blob/main/research/working/2026-11-11_advanced_thermal_stochastic_v2/03_SINTEF_THERMAL_HOTSPOT_AND_AGING.md)
- [`research/working/2026-11-11_advanced_thermal_stochastic_v2/07_VVUQ_IDENTIFIABILITY.md`](https://github.com/Dossiya-SE/MSE-thesis/blob/main/research/working/2026-11-11_advanced_thermal_stochastic_v2/07_VVUQ_IDENTIFIABILITY.md)

**Authority and non-invention:** The canonical files above control research scope, state/time, service interpretation and admissibility. Distinguish source-grounded laws, thesis-defined concepts, derived mathematical templates and hypotheses. Not-yet-qualified data or parameters remain **OPEN / UNKNOWN / NOT YET QUALIFIED**.

The separate PLE engineering agent may use the glossary as background domain knowledge, but **AI-agent and digital-twin development are outside the active MSE thesis scope**.
