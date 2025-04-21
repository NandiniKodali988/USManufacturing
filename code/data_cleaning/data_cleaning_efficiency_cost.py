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




