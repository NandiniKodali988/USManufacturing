import pandas as pd
import re

df = pd.read_excel("data/raw/efficiency_cost/labor-productivity-major-sectors.xlsx", sheet_name='Quarterly', header=2)

# select the needed 
df = df[df['Sector'].str.contains('manufacturing', case=False, na=False)].copy()
first_sector = df['Sector'].unique()[0]
df = df[df['Sector'] == first_sector] # row

pattern = re.compile(r'^(201[3-9]|202[0-4]) Q[1-4]$')
quarter_cols = [c for c in df.columns if pattern.match(c)]
keep = ['Sector','Basis','Measure','Units'] + quarter_cols 
df = df[keep] # column

# df.to_csv("data/Processed/efficiency_productivity/under_process.csv", index = False)

target_measures = ["Labor productivity", "Unit labor costs"]
df = df[df['Measure'].isin(target_measures) & (df['Units'] == "Index (2017=100)")]

quarter_cols = [c for c in df.columns if re.match(r'^\d{4}\sQ[1-4]$', c)]

df_long = df.melt(id_vars=['Measure'], value_vars=quarter_cols, var_name='Quarter', value_name='Value')
df_conn = df_long.pivot(index='Quarter', columns='Measure', values='Value').reset_index()

df_conn['Quarter_clean'] = df_conn['Quarter'].str.replace(r'\s+', '', regex=True)
df_conn['Date'] = pd.PeriodIndex(df_conn['Quarter_clean'], freq='Q').to_timestamp()
df_conn = df_conn[['Date', 'Labor productivity', 'Unit labor costs']].sort_values('Date').reset_index(drop=True)

df_conn.to_csv("data/Processed/efficiency_productivity/efficiency_productivity.csv")






