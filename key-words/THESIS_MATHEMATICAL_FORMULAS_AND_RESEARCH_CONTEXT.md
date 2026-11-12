# Thesis Mathematical Formulas, Working Evidence, and Engineering Reality

**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Role:** Supporting mathematical and experimental-context reference accompanying the [313-term glossary](THESIS_PHYSICS_ENGINEERING_MATHEMATICS_KEYWORDS.md).  
**Date:** 2026-11-13  
**Governance:** Compiled technical guide, **not a final model, new hypothesis freeze, established thermal interdependency, new empirical experiment, or a thesis-scope amendment**.

## 1. Thirty-four formula entries, grouped by their scientific roles

The previous glossary contained 34 numbered formula entries; the paired electricity/mobility service inequalities are retained in **one** entry. These formulas are a mixture of standard physical relations, canonical structural constructs, candidate device models, a specific evaluated regression/LP, and optional metrics. **Their statuses are not interchangeable**.

### A. State-space representation

**1. General dynamic system**

$$
\dot X(t)=F(X(t),H(t),u(t);\theta)
$$

*Scientific status:* Canonical general state-time equation; X is admitted state, H external heat forcing, u an operating action and theta parameters.

**2. Coupled thermal state vector**

$$
X_{\mathrm{th}}(t)=\begin{bmatrix}X_{P,\mathrm{th}}(t)\\X_{T_e,\mathrm{th}}(t)\end{bmatrix}
$$

*Scientific status:* Canonical structural representation. Exact state variables and couplings remain open.

**3. Candidate transformer thermal state**

$$
X_{P,\mathrm{th}}=\begin{bmatrix}\theta_{TO}\\\theta_{HS}\end{bmatrix}
$$

*Scientific status:* Evidence-supported top-oil/hot-spot candidate; not the frozen final device model.

**4. Candidate transportation thermal state**

$$
X_{T_e,\mathrm{th}}=\begin{bmatrix}T_{\mathrm{EVSE}}\\T_B\end{bmatrix}
$$

*Scientific status:* Conditional candidate; selected states must affect the qualified mechanism or service prediction.

### B. Fundamental electrical and thermal physics

**5. Conservation of thermal energy**

$$
C_{\mathrm{th}}\frac{dT}{dt}=\dot Q_{\mathrm{gen}}-\dot Q_{\mathrm{out}}
$$

*Scientific status:* General physical foundation. C_th in J/K; heat rates in W; time in s; device-specific terms need explicit control volumes.

**6. Electrical resistive heat generation**

$$
P_{\mathrm{loss}}=I^2R
$$

*Scientific status:* Standard resistive-loss relationship with appropriate current, conductor, and resistance definitions.

**7. Feeder resistive losses**

$$
P_{f,\mathrm{loss}}(t)=\sum_{\phi}I_\phi^2(t)R_\phi(T)
$$

*Scientific status:* Candidate feeder relationship; phase and line-segment topology and conductor properties must be established.

**8. Transformer winding heat balance**

$$
C_w\frac{dT_w}{dt}=P_{w,\mathrm{loss}}-\dot Q_{w\to o}
$$

*Scientific status:* Conditional lumped heat balance, not a manufacturer-specific validated law.

**9. Transformer oil heat balance**

$$
C_o\frac{dT_o}{dt}=P_{\mathrm{core,loss}}+\dot Q_{w\to o}-\dot Q_{\mathrm{cool}}
$$

*Scientific status:* Conditional reduced balance. Heat and core-loss allocation must be adjusted for the adopted control volumes; do not count cooling twice.

**10. Temperature-dependent electrical resistance**

$$
R=R(T)
$$

*Scientific status:* General constitutive dependence. Exact functional form requires conductor/device evidence.

**11. Convective heat transfer**

$$
\dot Q_{\mathrm{conv}}=hA(T_s-T_a)
$$

*Scientific status:* Standard surface convection template; h and boundary conditions require physical justification.

**12. Simple linear thermal time constant**

$$
\tau_{\mathrm{th}}=\frac{C_{\mathrm{th}}}{hA}
$$

*Scientific status:* Valid only for the relevant linear one-state constant-parameter model, not universally for transformers.

**13. Compatible AC apparent-power quantities**

$$
S=\sqrt{P^2+Q^2}
$$

*Scientific status:* Standard relationship for compatible AC real/reactive power; dataset names/units must be confirmed before using it as rated loading.

### C. Working transformer thermal model

**14. Reduced oil-temperature ODE**

$$
C_{\mathrm{eff}}\frac{dT_o}{dt}=P_{\mathrm{loss,eff}}(I,T_o)-H_{\mathrm{eff}}(T_o-T_a)
$$

*Scientific status:* Working conditional equation used in the November 11 thesis analysis; not universally validated.

**15. One-hour reduced thermal recurrence**

$$
T_{o,t+1}=aT_{o,t}+(1-a)\left[T_{a,t}+d+g\left(\frac{I_t}{I_{\mathrm{ref}}}\right)^2\right],\quad a=\exp(-\Delta t/\tau),\quad\Delta t=1\ \mathrm{hour}
$$

*Scientific status:* Effective SINTEF reduced model; d and g are effective coefficients, I_ref is a training reference, and tau is not an equipment-general constant.

**16. Sensitivity matrix**

$$
J_{ik}=\frac{\partial\widehat T_{i+1}}{\partial\theta_k}
$$

*Scientific status:* Used for local inverse-problem conditioning; not a global uniqueness proof.

### D. Power–Transportation coupling

**17. General thermal-conditioned coupling**

$$
Z_{PT}(t)=Z_{PT}\left(X_{P,\mathrm{th}},X_{T_e,\mathrm{th}},D,u;\theta\right)
$$

*Scientific status:* Canonical structural map; does not establish directional thermal causality.

**18. State-conditioned capability**

$$
P_{\mathrm{available}}(t)=\mathcal C_P(X_{P,\mathrm{th}}(t))
$$

*Scientific status:* Candidate relationship; equipment-specific limits and real implemented restriction remain open.

**19. Power-to-Transportation candidate pathway**

$$
\theta_{P1}(t)\longrightarrow u_{P3}(t)\longrightarrow P_{\mathrm{AC,available}}(t)\longrightarrow E_{\mathrm{charge}}(t)
$$

*Scientific status:* Only a candidate chain. P3 must have a verified real protective/load-management rule.

**20. Transportation-to-Power candidate pathway**

$$
T_{\mathrm{EVSE}}(t)\longrightarrow(P_{\mathrm{AC}}(t),Q_{\mathrm{AC}}(t))\longrightarrow I_{P2}(t)\longrightarrow\theta_{P1}(t)
$$

*Scientific status:* Only a candidate chain. Requires synchronized grid-side demand, component temperature, power-system topology, and matched measurement.

### E. Time, transitions and propagation

**21. Critical thermal transition time**

$$
\tau_i^C=\inf\left\{t:g_i(X_i(t),H(t),t)=0\right\}
$$

*Scientific status:* Canonical conditional form: a physically meaningful, evidence-supported limiting boundary is required.

**22. Directional thermal propagation delay**

$$
\delta_{ij}^{\mathrm{th}}=t_j^{\mathrm{response}}-\tau_i^C
$$

*Scientific status:* Canonical conditional form, meaningful only for independently qualified source-to-receiver response.

**23. Electricity and mobility service adequacy**

$$
Q_P(t)\ge Q_P^{\mathrm{req}}(t),\qquad Q_T(t)\ge Q_T^{\mathrm{req}}(t)
$$

*Scientific status:* Two frozen service adequacy conditions counted together as one formula-register item, matching the previous 34-item register.

**24. Candidate service-deficit measure**

$$
D_k(t)=\max\left\{0,Q_k^{\mathrm{req}}(t)-Q_k(t)\right\}
$$

*Scientific status:* Optional thesis-derived metric; must be unit-compatible and separately adopted.

**25. Candidate accumulated service deficit**

$$
A_k=\int_{t_0}^{t_f}D_k(t)\,dt
$$

*Scientific status:* Optional integral metric; not a frozen resilience index.

### F. Charging, energy and optimization

**26. EVSE energy efficiency**

$$
\eta_{\mathrm{EVSE}}=\frac{E_{\mathrm{DC,out}}}{E_{\mathrm{AC,in}}}
$$

*Scientific status:* Conservation/accounting ratio over identical windows and documented AC/DC meter boundaries.

**27. Charging energy**

$$
E_{\mathrm{charge}}=\int_{t_a}^{t_b}P_{\mathrm{charge}}(t)\,dt
$$

*Scientific status:* General energy integration; define the charging port and battery/charger loss accounting.

**28. Battery energy-state balance**

$$
\frac{dE_B}{dt}=P_{B,\mathrm{in}}-P_{B,\mathrm{out}}
$$

*Scientific status:* Conditional storage relation; device losses and efficiencies must be represented when material.

**29. Offline charging-session optimization**

$$
\min z,\quad 0\le p_{it}\le P_i^{\max},\quad\sum_{t\in[a_i,b_i)}p_{it}\Delta t\ge E_i,\quad\sum_i p_{it}\le z
$$

*Scientific status:* Hypothetical EPFL offline LP; E_i is reported achieved energy, not independently verified requested energy; not observed operation.

**30. Proposed thermal-constrained scheduling**

$$
\min_{\{p_{it}\}}\max_t T_{\mathrm{transformer}}(t)
$$

*Scientific status:* Research proposal blocked from numerical implementation because the full qualified charging-to-transformer transfer relation is absent.

### G. Scientific validation equations

**31. Mean absolute error**

$$
\mathrm{MAE}=\frac{1}{n}\sum_{i=1}^n|y_i-\hat y_i|
$$

*Scientific status:* Standard discrepancy measure; does not independently prove physical adequacy.

**32. Root mean squared error**

$$
\mathrm{RMSE}=\sqrt{\frac{1}{n}\sum_{i=1}^n(y_i-\hat y_i)^2}
$$

*Scientific status:* Standard discrepancy measure; measured-domain limitations apply.

**33. Dimensional verification**

$$
[\mathrm{LHS}]=[\mathrm{RHS}]
$$

*Scientific status:* Mandatory physical dimensional-consistency check.

**34. Measurement-model residual**

$$
r(t)=y_{\mathrm{measured}}(t)-y_{\mathrm{model}}(t)
$$

*Scientific status:* Interpret using measurement, model and numerical uncertainty.

## 2. Reported working results and their exact limitations

The following observations are transcribed from the project's existing November 11 research reports, **not newly rerun or verified here**.

| Research activity | Reported result | Scope or limitation |
| --- | --- | --- |
| SINTEF transformer oil fit | Holdout RMSE **0.216529 °C**; MAE **0.149854 °C** | Specific reduced fitted oil model and observed equipment/forcing domain |
| Comparison with persistence | Model improves holdout RMSE relative to persistence (0.251699 °C) but worsens MAE relative to persistence (0.144981 °C) | Not a uniformly superior predictor |
| Heat-history perturbation | **106** distinct uninterrupted 24-hour holdout windows; median absolute final oil-temperature difference **0.354859 °C** under current-order permutations | Equal sum of normalized current-square values is not proof of equal electrical energy or causal EV intervention |
| Calendar fitting | Effective time constants **15.9818 h**, **8.2944 h**, and **13.5708 h** across three 2024 periods in a separate analysis | Regime dependence is not a proven structural nonidentifiability result |
| Local inverse conditioning | Standardized local condition number **2.4247** | Does not prove global uniqueness or correct model form |
| Numerical solver | Euler and RK4 errors decreased under refinement against an exact fixed-forcing solution | Numerical verification of the selected ODE, not model validation |
| EPFL charging | Offline peak-reduction LP and charging-session observations | No actual operational control action or measured transformer heat effect |
| Missing thermal-causal linkage | Full P→T_e and T_e→P physical evidence remains OPEN | Separate SINTEF and EPFL sites cannot validate a joint physical installation |
| Extreme heat | Maximum recorded SINTEF ambient **25.97 °C** | No measured 30 °C+ validation in this experiment |
| Insulation and hard thresholds | No qualified equipment-specific life-loss law or operating threshold admitted | Cannot infer genuine aging rate, critical transition timing or thermal P3 trip |

**Never describe measured fitting performance as proof of extreme-heat resilience, full bidirectional thermal dependency, safe equipment operation, or transformer life remaining.**

## 3. Twelve most important scientific keys and objective alignment

| Priority | Key | Scientific role | Objective |
| ---: | --- | --- | --- |
| 1 | Qualified directional thermal interdependency | Establish physically supported source-to-receiver mechanism | SO1 |
| 2 | Thermal physical state | Admit only necessary states | SO1, SO2 |
| 3 | Conservation laws and constitutive physics | Derive physical governing equations | SO2 |
| 4 | Thermal inertia and transient dynamics | Characterize heat memory and delayed responses | SO2 |
| 5 | State-conditioned capability | Demonstrate an actual thermally dependent operating restriction | SO1, SO2 |
| 6 | Coupled differential/algebraic dynamics | Model justified intersystem propagation | SO2 |
| 7 | Critical transition time | Quantify first meaningful boundary crossing | SO3 |
| 8 | Propagation delay | Quantify source-to-receiver response time | SO3 |
| 9 | Electricity and mobility service | Quantify real service outcomes and unmet requirements | SO3 |
| 10 | Service-level resilience | Interpret maintenance and recovery of required services | SO3 |
| 11 | Identification and observability | Check whether selected parameters/states are inferable | SO2 |
| 12 | Verification, validation and uncertainty | Assess numerical and physical credibility | SO2, SO3 |

## 4. Essential conceptual distinctions

| Must not conflate | With |
| --- | --- |
| System boundary | Mathematical boundary condition |
| Entire Electrified Transportation System | Selected reduced active model |
| Environmental heat forcing | Internal thermal state |
| Thermal state | Thermally conditioned capability |
| Capability | Delivered electricity/mobility service |
| Physical/electrical connection | Demonstrated thermal interdependency |
| Shared extreme-heat exposure | Direct intersystem causation |
| Charging request | Measured grid-side AC demand |
| Battery SOC | Battery temperature |
| Predicted thermal limit | Actual installed protection/load-management rule |
| Thermal transition time | Propagation delay |
| Propagation delay | Service-disruption onset |
| Thermal time constant | Aging/degradation horizon |
| Solver convergence | Model validation |
| Calibration | Independent validation |
| Transferred parameter | Measured equipment-specific parameter |
| Equipment surviving | Required service maintained |
| Resilience improvement | Sustainability improvement |

## 5. Thesis research principle

```text
Actual physical equipment and operating conditions
→ Conservation laws and admissible constitutive relations
→ Minimum-sufficient state-time formulation
→ Mechanism qualification and falsifiable hypotheses
→ Numerical solution and verification
→ Matched physical evidence, validation and uncertainty
→ Critical timing and electricity/mobility service consequences
→ Resilience and bounded sustainability interpretation
```

An equation without a physical system, source status, assumptions, units, domain, initial/boundary conditions and a credibility test is not a verified engineering model.

## 6. Source authorities and working research

- [Current title V3](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_THESIS_TITLE_V3.md)
- [Frozen General Objective and SO1–SO3](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md)
- [Canonical thermal research scope](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md)
- [Canonical state-time definitions](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md)
- [Canonical service resilience](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_RESILIENCE_DEFINITION_V1.md)
- [Evidence non-invention standard](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md)
- [Eight-component physical/interface dossier](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/thermal_sos_functional_architecture/EIGHT_COMPONENT_PHYSICS_AND_DIRECTIONAL_INTERFACE_RESEARCH_DOSSIER_V1.md)
- [Working mathematics and hypotheses, 2026-11-11](https://github.com/Dossiya-SE/MSE-thesis/blob/main/research/working/2026-11-11_advanced_thermal_stochastic_v2/02_EQUATIONS_AND_HYPOTHESES.md)
- [Thermal history, observed hot spots and aging gate, 2026-11-11](https://github.com/Dossiya-SE/MSE-thesis/blob/main/research/working/2026-11-11_advanced_thermal_stochastic_v2/03_SINTEF_THERMAL_HOTSPOT_AND_AGING.md)
- [VVUQ and identifiability, 2026-11-11](https://github.com/Dossiya-SE/MSE-thesis/blob/main/research/working/2026-11-11_advanced_thermal_stochastic_v2/07_VVUQ_IDENTIFIABILITY.md)

**This reference does not replace the linked authorities or change the scope.** It may also be included as a scientific background resource in [PLE-Engineering](https://github.com/Dossiya-SE/PLE-Engineering), but AI-agent development remains outside this thesis's current scientific objectives.
