# process worker perspective(wage_hour; employment)

# define function that transform monthly or quarterly data to yearly data
import pandas as pd
import glob
import os

def to_annual(df: pd.DataFrame) -> pd.DataFrame:

    time_col = df.columns[0]
    value_col = df.columns[1]
 
    df2 = df.copy()
    s = df2[time_col].astype(str)

    if df2[time_col].dtype == object:
     
        if df2[time_col].str.contains(r'Q[1-4]').all():

            quarters = s.str.replace(r'\s*([Qq])\s*([1-4])', r'\1\2', regex=True).str.upper()
          
            df2['Date'] = pd.PeriodIndex(quarters, freq='Q').to_timestamp()
        else:
          
            df2['Date'] = pd.to_datetime(df2[time_col])
    else:
      
        df2['Date'] = pd.to_datetime(df2[time_col])


    df2['Year'] = df2['Date'].dt.year

    annual_df = (
        df2
        .groupby('Year', as_index=False)[value_col]
        .mean()
        .rename(columns={value_col: f'{value_col}_annual_mean'})
    )
    return annual_df

# automatically process employment data
raw_folder = "../data/Processed/selected_data_for_worker/employment"          
pattern    = os.path.join(raw_folder, "*.csv")
files      = glob.glob(pattern)

annual_results = {}  

for path in files:
    name = os.path.splitext(os.path.basename(path))[0]
    df   = pd.read_csv(path)
    try:
        df_annual = to_annual(df)
    except Exception as e:
        print(f" Errors when processing {name}: {e}")
        continue

    annual_results[name] = df_annual

for name, df_ann in annual_results.items(): 
    df_ann.to_csv(f"../data/Processed/selected_data_for_worker/employment/{name}_annual.csv", index=False)

# automatically process wage_hour data
raw_folder = "../data/Processed/selected_data_for_worker/wage_hour"          
pattern    = os.path.join(raw_folder, "*.csv")
files      = glob.glob(pattern)

annual_results = {}  

for path in files:
    name = os.path.splitext(os.path.basename(path))[0]
    df   = pd.read_csv(path)
    try:
        df_annual = to_annual(df)
    except Exception as e:
        print(f" Errors when processing {name}: {e}")
        continue

    annual_results[name] = df_annual

for name, df_ann in annual_results.items(): 
    df_ann.to_csv(f"../data/Processed/selected_data_for_worker/wage_hour/{name}_annual.csv", index=False)