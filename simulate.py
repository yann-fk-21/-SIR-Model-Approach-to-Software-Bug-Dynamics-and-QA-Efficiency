import pandas as pd
from utils.model import SIRModel
from utils.plot import plot_infection_recovery_rates, plot_inverse_r0_and_susceptible_ratio, plot_r0_evolution


def create_data():
    print("Data preparing ...")
    data_df = pd.read_csv("./data/dynamic_software_quality_data.csv")
    data = []
    for i in range(0, len(data_df)):
        item = {"D": data_df["Day"].iloc[i], "S":data_df["S"].iloc[i],
        "I": data_df["I"].iloc[i], "R": data_df["R"].iloc[i], "dS": data_df["dS_dt"].iloc[i],
        "dI": data_df["dI_dt"].iloc[i], "dR": data_df["dR_dt"].iloc[i]}
        data.append(item)

    return data

def main():
    data = create_data()
    sir_model = SIRModel()
    days = []
    
    for i in range(0, len(data)):
        sir_model.compute_beta(S=data[i]["S"], I=data[i]["I"], N=990, dS_dt=data[i]["dS"])
        sir_model.compute_gamma(I=data[i]["I"], dR_dt=data[i]["dR"])
        days.append(data[i]["D"])
    
    print("Creating plots ....")
    plot_infection_recovery_rates(days, sir_model.infection_rates, sir_model.recovery_rates)
    print("infection_vs_resolution plot is created!")
    plot_r0_evolution(days, sir_model.infection_rates, sir_model.recovery_rates)
    print("R_0 evolution plot is created!")
    plot_inverse_r0_and_susceptible_ratio(days, sir_model.infection_rates, sir_model.recovery_rates, data, N=990)
    print("1/R_0_vs_S/N plot is created!")


if __name__ == "__main__":
    main()
