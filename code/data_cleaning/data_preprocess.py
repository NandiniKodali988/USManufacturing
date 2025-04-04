from data_cleaning import Cleaner
from config_cleaning import configs
import os

output_dir = "Dataset/Processed"
os.makedirs(output_dir, exist_ok=True)

for config in configs:
    cleaner = Cleaner(
        file_path=config["file_path"],
        var_name=config["var_name"],
        unit=config["unit"],
        time_freq=config["time_freq"],
        skiprows=config.get("skiprows", 0),
    )
    
    df_clean = cleaner.clean()

    filename = f"{config['var_name']}_{config['unit']}.csv"
    output_path = os.path.join(output_dir, filename)
    df_clean.to_csv(output_path, index=False)

    print(f"Saved cleaned file: {output_path}")
