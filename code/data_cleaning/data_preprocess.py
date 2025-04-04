from data_cleaning import Cleaner
from config_cleaning import configs
from functools import reduce
import pandas as pd
import os

# set output directory
output_dir = "data/Processed"
os.makedirs(output_dir, exist_ok=True)

# separate monthly and quarterly
monthly_dfs = []
quarterly_dfs = []

# clean
for config in configs:

    cleaner = Cleaner(
        file_path=config["file_path"],
        var_name=config["var_name"],
        unit=config["unit"],
        time_freq=config["time_freq"],
        skiprows=config.get("skiprows", 0),
        wide_format=config.get("wide_format", True),
        id_var=config.get("id_var", "Year")
    )

    df_clean = cleaner.clean()

    # append separately
    if config["time_freq"] == "monthly":
        monthly_dfs.append(df_clean)
    elif config["time_freq"] == "quarterly":
        quarterly_dfs.append(df_clean)

    filename = f"{config['var_name']}_{config['unit']}.csv"
    output_path = os.path.join(output_dir, filename)
    df_clean.to_csv(output_path, index=False)

    print(f"Saved cleaned file: {output_path}")

# merge（quarterly monthly）
if monthly_dfs:
    df_monthly = reduce(lambda left, right: pd.merge(left, right, on='YearMonth', how='outer'), monthly_dfs)
    df_monthly.to_csv(os.path.join(output_dir, "merged_monthly.csv"), index=False)
    print("Saved merged monthly data.")

if quarterly_dfs:
    df_quarterly = reduce(lambda left, right: pd.merge(left, right, on='YearQuarter', how='outer'), quarterly_dfs)
    df_quarterly.to_csv(os.path.join(output_dir, "merged_quarterly.csv"), index=False)
    print("Saved merged quarterly data.")
