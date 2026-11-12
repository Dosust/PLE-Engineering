# Programming Languages and Their Roles in Our PLE Engineering Agent

For our [PLE-Engineering project](https://github.com/Dossiya-SE/PLE-Engineering), we should establish a clear division of responsibilities between programming languages.

Our objective is to develop one autonomous agent capable of interpreting engineering problems, performing mathematical computations, using engineering software, checking physical constraints, and producing verifiable deliverables across the 29 public tasks.

We do not need to use every programming language. Each language should be introduced only when it solves a specific engineering or computational problem.

## 1. The role of each language

| Language | Role in our project | Priority |
| --- | --- | --- |
| **Python** | Main agent architecture, AI model communication, engineering algorithms, scientific computing, numerical solvers, verification, data processing and automation | **Essential** |
| **Bash** | Execute engineering programs, manage files, configure environments, run tests and automate evaluation commands | **Essential** |
| SQL | Organize engineering data, experimental results, task outcomes and performance records | Useful later |
| C++ | Implement computationally intensive algorithms when Python performance is insufficient | Optional |
| Julia | Develop advanced mathematical models, differential equations and scientific simulations | Optional |
| TypeScript / JavaScript | Develop interactive dashboards, web interfaces or alternative agent implementations | Optional |
| HTML / CSS | Present experiment dashboards, research results and visual documentation | Optional |

For the first working version, **Python + Bash are sufficient**. We can use SQLite through Python without needing a separate database server.

## 2. What exactly will Python do?

Python will be our central engineering language, divided into six responsibilities.

**Python: Main Engineering Agent**

Planning, orchestration and verification.

| Responsibility | Methods and tools |
| --- | --- |
| **1. AI control** | Model APIs, reasoning loops, task planning |
| **2. Mathematics** | NumPy, SciPy, SymPy, optimization |
| **3. Physics** | Conservation laws, numerical modeling, constraints |
| **4. Engineering files** | PDF, Excel, Word, CAD and IFC |
| **5. Verification** | Units, residuals, tolerances and tests |
| **6. Experiments** | Scores, failures, ablations and cost |

Python will coordinate the agent, but it will not necessarily implement every algorithm itself. For example, SciPy already provides tested numerical methods, and IfcOpenShell provides specialized IFC capabilities.

## 3. How the languages work together

Consider the public **low-voltage cable-sizing** task.

| Stage | Engineering activity | Technology |
| --- | --- | --- |
| **1. Read** | Extract cable requirements, loading conditions and constraints | Python |
| **2. Formulate** | Represent voltage-drop, ampacity, cost and design constraints mathematically | Python + NumPy |
| **3. Solve** | Identify feasible cable selections and evaluate cost | Python + optimization solver |
| **4. Verify** | Check units, numerical results and hard operating limits | Python + pytest |
| **5. Produce** | Generate the required engineering schedule and design documentation | Python + document libraries |
| **6. Evaluate** | Execute the PLE evaluator and record results | Bash + Docker + Python |
| **7. Analyze** | Compare agent performance across experiments | Python + CSV or SQLite |

C++ and Julia are not necessary for this example unless a specific computational requirement justifies them.

## 4. Important distinction: languages, libraries, formats and protocols

These technologies serve different purposes.

| Category | Examples | Meaning |
| --- | --- | --- |
| Programming languages | Python, C++, Julia, TypeScript | Specify computational operations |
| Scientific libraries | NumPy, SciPy, SymPy, CVXPY | Provide mathematical and engineering algorithms |
| Data/configuration formats | JSON, YAML, CSV | Represent information and configuration |
| Engineering formats | IFC4, PDF, XLSX, DOCX | Store engineering models, drawings and deliverables |
| Communication protocols | WebSockets, MCP | Connect the agent with the benchmark environment and tools |
| Execution infrastructure | Docker, Harbor, GitHub | Run, isolate, evaluate and version the system |

For example, **MCP is not a programming language**. We implement MCP interactions using Python.

Similarly, `submission.yaml` configures the harness. YAML does not perform the engineering computations.

## 5. Our mathematical and computational engineering principle

We should design the project around five independent layers.

$$
\boxed{
\text{Physical problem}
\rightarrow
\text{Mathematical formulation}
\rightarrow
\text{Numerical algorithm}
\rightarrow
\text{Software implementation}
\rightarrow
\text{Verification}
}
$$

Each layer must have a clearly defined responsibility.

- **Physics** determines what relationships must hold.
- **Mathematics** expresses those relationships through equations, variables, constraints and objectives.
- **Numerical analysis** determines how to approximate or optimize solutions reliably.
- **Programming** implements these methods and automates the engineering workflow.
- **Verification and validation** establish what the computation satisfies and whether the model represents the physical problem adequately.

The choice of Python or C++ does not determine whether an engineering model is scientifically correct.

## 6. Our final technology decision

### Primary engineering language

**Python**

Use for the agent, computational mathematics, engineering tools and validation.

### Supporting technologies

Bash, Git, Docker, Harbor, JSON, YAML, WebSockets and MCP.

### Scientific computing

NumPy, SciPy, SymPy, CVXPY and domain-specific engineering libraries.

### Introduce only when justified

C++ for measured performance bottlenecks, Julia for specialized numerical modeling, SQL for larger experiment datasets, and TypeScript for interactive interfaces.

Our final technology decision is a **Python-first architecture with independent mathematical and physical verification**.

## 7. Next architectural decision

Separate the following components so each can be developed, tested, and verified independently:

| Engine | Responsibility | Status |
| --- | --- | --- |
| **AI reasoning engine** | Interpret requirements, plan, select tools and coordinate steps | Baseline model loop exists; specialized separation planned |
| **Mathematical computation engine** | Solve equations, optimization problems and numerical models | Planned |
| **Engineering-file engine** | Read project sources and generate/inspect required engineering deliverables | Baseline file tools exist; specialized processing planned |
| **Verification engine** | Check units, physics, numerical validity, constraints, deliverables and evidence | Planned |

This separation will make the system easier to test, improve and generalize across the 29 tasks.

**Scope note:** This is the adopted design and learning plan, not a claim that the planned engines and libraries are already installed or implemented. The actual baseline and current implementation status are tracked in [Architecture and engineering quality gates](ARCHITECTURE_AND_GATES.md) and [Roadmap](ROADMAP.md).
