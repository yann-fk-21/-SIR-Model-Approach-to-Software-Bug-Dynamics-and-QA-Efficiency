import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme(style="whitegrid")

plt.rcParams['figure.figsize'] = (16, 8)
plt.rcParams['figure.dpi'] = 150
plt.rcParams['font.size'] = 14
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['legend.fontsize'] = 14
plt.rcParams['legend.title_fontsize'] = 16

def prepare_data(days, infection_rates, recovery_rates):

    min_length = min(len(days), len(infection_rates), len(recovery_rates))
    days = days[:min_length]
    infection_rates = infection_rates[:min_length]
    recovery_rates = recovery_rates[:min_length]
    
    r0_values = []
    for beta, gamma in zip(infection_rates, recovery_rates):
        if np.isnan(beta) or np.isnan(gamma) or gamma == 0:
            r0_values.append(np.nan)
        else:
            r0_values.append(beta / gamma)
    

    df_metrics = pd.DataFrame({
        'Day': days,
        'Infection Rate (Beta)': infection_rates,
        'Recovery Rate (Gamma)': recovery_rates,
        'R0 (Reproduction Number)': r0_values
    })
    
    return df_metrics

def plot_infection_recovery_rates(days, infection_rates, recovery_rates):

    df_metrics = prepare_data(days, infection_rates, recovery_rates)
    
    fig, ax = plt.subplots(figsize=(16, 8))
    
    sns.lineplot(data=df_metrics, x='Day', y='Infection Rate (Beta)', ax=ax, 
                 label='Infection Rate (β)', color='red', marker='o', markersize=10, linewidth=3)
    sns.lineplot(data=df_metrics, x='Day', y='Recovery Rate (Gamma)', ax=ax, 
                 label='Recovery Rate (γ)', color='green', marker='s', markersize=10, linewidth=3)
    
    ax.set_title('Evolution of Software Quality Parameters (Infection vs Resolution)', 
                 fontsize=18, fontweight='bold', pad=20)
    ax.set_xlabel('Project Duration (Days)', fontweight='bold', fontsize=16)
    ax.set_ylabel('Rate Value', fontweight='bold', fontsize=16)
    ax.legend(frameon=True, shadow=True, fontsize=14)
    ax.grid(True, alpha=0.3, linewidth=1.5)
    
    plt.tight_layout()
    plt.savefig("./visualization/infections_recovery_plot.png")

def plot_r0_evolution(days, infection_rates, recovery_rates):
    
    df_metrics = prepare_data(days, infection_rates, recovery_rates)
    
    fig, ax = plt.subplots(figsize=(16, 8))
    
    sns.lineplot(data=df_metrics, x='Day', y='R0 (Reproduction Number)', ax=ax, 
                 color='purple', linewidth=3, markersize=10, label='R0')
    
    
    ax.axhline(1, ls='--', color='black', alpha=0.7, linewidth=2.5, label='Critical Threshold (R0 = 1)')
    
   
    ax.fill_between(df_metrics['Day'], df_metrics['R0 (Reproduction Number)'], 1, 
                     where=(df_metrics['R0 (Reproduction Number)'] > 1), 
                     color='red', alpha=0.15, label='Unstable (Bugs Spreading)')
    ax.fill_between(df_metrics['Day'], df_metrics['R0 (Reproduction Number)'], 1, 
                     where=(df_metrics['R0 (Reproduction Number)'] <= 1), 
                     color='blue', alpha=0.15, label='Stable (QA in Control)')
    
    ax.set_title('Evolution of Basic Reproduction Number (R0)', 
                 fontsize=18, fontweight='bold', pad=20)
    ax.set_xlabel('Project Duration (Days)', fontweight='bold', fontsize=16)
    ax.set_ylabel('R0 Value', fontweight='bold', fontsize=16)
    ax.legend(frameon=True, shadow=True, fontsize=14)
    ax.grid(True, alpha=0.3, linewidth=1.5)
    
    plt.tight_layout()
    plt.savefig("./visualization/r0_evolution_plot.png")

def plot_inverse_r0_and_susceptible_ratio(days, infection_rates, recovery_rates, data, N=990):
    
    min_length = min(len(days), len(infection_rates), len(recovery_rates), len(data))
    days = days[:min_length]
    infection_rates = infection_rates[:min_length]
    recovery_rates = recovery_rates[:min_length]
    data = data[:min_length]
    
    inverse_r0_values = []
    for beta, gamma in zip(infection_rates, recovery_rates):
        if np.isnan(beta) or np.isnan(gamma) or gamma == 0:
            inverse_r0_values.append(np.nan)
        else:
            r0 = beta / gamma
            if r0 > 0:
                inverse_r0_values.append(1 / r0)
            else:
                inverse_r0_values.append(np.nan)
    
    s_over_n_values = []
    for item in data:
        if N > 0:
            s_over_n_values.append(item["S"] / N)
        else:
            s_over_n_values.append(np.nan)
    
    df_plot = pd.DataFrame({
        'Day': days,
        '1/R0': inverse_r0_values,
        'S/N': s_over_n_values
    })
    
    
    fig, ax = plt.subplots(figsize=(16, 8))
    

    sns.lineplot(data=df_plot, x='Day', y='1/R0', ax=ax, 
                 label='1/R0 (Inverse Reproduction Number)', 
                 color='#E63946', linewidth=3, marker='o', markersize=10)
    
    
    sns.lineplot(data=df_plot, x='Day', y='S/N', ax=ax, 
                 label='S/N (Susceptible Ratio)', 
                 color='#457B9D', linewidth=3, marker='s', markersize=10)
    
    
    ax.axhline(1, ls='--', color='black', alpha=0.5, linewidth=2.5, 
               label='Critical Threshold (1/R0 = 1)')
    
    ax.set_title(r'Évolution de $\frac{1}{R_{0}}$ et de $\frac{S}{N}$ dans le temps', 
                 fontsize=18, fontweight='bold', pad=20)
    ax.set_xlabel('Project Duration (Days)', fontweight='bold', fontsize=16)
    ax.set_ylabel('Value', fontweight='bold', fontsize=16)
    ax.legend(frameon=True, shadow=True, loc='best', fontsize=14)
    ax.grid(True, alpha=0.3, linewidth=1.5)
    
    plt.savefig("./visualization/r0_susceptible_by_N.png")