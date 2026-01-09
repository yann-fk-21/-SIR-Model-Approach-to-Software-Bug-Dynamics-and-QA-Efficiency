A SIR Model Approach to Software Bug Dynamics and QA Efficiency

This research project explores the application of epidemiological compartmental models (SIR) to the field of software engineering, specifically to analyze bug propagation and the effectiveness of Quality Assurance (QA) teams.

📊 Project Overview

As modern software systems grow in complexity, defect management has become critical. This work transposes the mathematical framework of Kermack and McKendrick to:

Model the "contagion" of defects between modules in a software architecture.

Mathematically evaluate the performance of maintenance teams through the resolution rate ($\gamma$).

Identify systemic instability phases using the basic reproduction number ($R_0$).

🧮 Methodology

The software system is modeled through three mutually exclusive states:

S (Susceptible): Healthy modules that are vulnerable to bug coupling.

I (Infected): Modules with active anomalies.

R (Recovered): Modules that have been fixed, tested, and validated by QA.

Model Differential Equations

$$\frac{dS}{dt} = -\beta S \frac{I}{N}$$

$$\frac{dI}{dt} = \beta S \frac{I}{N} - \gamma I$$

$$\frac{dR}{dt} = \gamma I$$

Where $\beta$ represents the transmission rate (software complexity) and $\gamma$ represents the resolution rate (team efficiency).

📈 Key Results

Simulations conducted on a synthetic dataset reveal:

Critical Imbalance: A maximum infection rate exceeding 30%, while the resolution capacity plateaus at 15%.

Systemic Instability: An $R_0$ indicator consistently above the critical threshold of 1, confirming an active "bug epidemic" phase.

Stability Threshold: Propagation only ceases when the density of susceptible modules falls below $1/R_0$ (approximately 42%).

🛠️ Technologies & Tools

Language: Python

Simulation: Pandas, NumPy

Visualization: Matplotlib

📚 References

J.O. Kephart and S.R. White. "Directed-graph epidemiological models of computer viruses". IEEE, 1991.

W. O. Kermack and A. G. McKendrick. "Contributions to the Mathematical Theory of Epidemics". 1927.