## A SIR Model Approach to Software Bug Dynamics and QA Efficiency

This research project explores the application of epidemiological compartmental models (SIR) to the field of software engineering, specifically to analyze bug propagation and the effectiveness of Quality Assurance (QA) teams.

📄 **Full Research Paper**: [Download PDF](paper.pdf)

For a comprehensive analysis of the methodology, results, and theoretical framework, please refer to the complete research paper.

### 📊 Project Overview

As modern software systems grow in complexity, defect management has become critical. This work transposes the mathematical framework of Kermack and McKendrick to:

Model the "contagion" of defects between modules in a software architecture.

Mathematically evaluate the performance of maintenance teams through the resolution rate ($\gamma$).

Identify systemic instability phases using the basic reproduction number ($R_0$).

### 🧮 Methodology

The software system is modeled through three mutually exclusive states:

S (Susceptible): Healthy modules that are vulnerable to bug coupling.

I (Infected): Modules with active anomalies.

R (Recovered): Modules that have been fixed, tested, and validated by QA.

Model Differential Equations

$$\frac{dS}{dt} = -\beta S \frac{I}{N}$$

$$\frac{dI}{dt} = \beta S \frac{I}{N} - \gamma I$$

$$\frac{dR}{dt} = \gamma I$$

Where $\beta$ represents the transmission rate (software complexity) and $\gamma$ represents the resolution rate (team efficiency).

### 📈 Key Results

Simulations conducted on a synthetic dataset reveal:

Critical Imbalance: A maximum infection rate exceeding 30%, while the resolution capacity plateaus at 15%.

Systemic Instability: An $R_0$ indicator consistently above the critical threshold of 1, confirming an active "bug epidemic" phase.

Stability Threshold: Propagation only ceases when the density of susceptible modules falls below $1/R_0$ (approximately 42%).

### Visualization of Results

**Figure 1: Evolution of Infection and Recovery Rates**

![Infection and Recovery Rates](visualization/infections_recovery_plot.png)

This figure illustrates the temporal evolution of the infection rate ($\beta$) and recovery rate ($\gamma$) throughout the software development lifecycle. The analysis reveals the critical imbalance between bug propagation and resolution capabilities.

**Figure 2: Basic Reproduction Number (R0) Evolution**

![R0 Evolution](visualization/r0_evolution_plot.png)

The basic reproduction number $R_0 = \beta / \gamma$ tracks the stability of the software system. Values above 1 indicate an unstable system where bugs are spreading faster than they can be resolved, while values below 1 indicate a stable state where QA teams maintain control.

**Figure 3: Relationship between 1/R0 and S/N**

![1/R0 and S/N Evolution](visualization/r0_susceptible_by_N.png)

This figure demonstrates the critical relationship between the inverse reproduction number ($1/R_0$) and the susceptible ratio ($S/N$). The stability threshold condition $S/N < 1/R_0$ defines when bug propagation can be controlled by the QA team.

### 🛠️ Technologies & Tools

Language: Python

Simulation: Pandas, NumPy

Visualization: Matplotlib

### 📚 References

J.O. Kephart and S.R. White. "Directed-graph epidemiological models of computer viruses". IEEE, 1991.

W. O. Kermack and A. G. McKendrick. "Contributions to the Mathematical Theory of Epidemics". 1927.