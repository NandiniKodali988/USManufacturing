import pandas as pd

# deal with imports data
df = pd.read_excel("data/raw/domestic_output_vs_import/Imports.xlsx", sheet_name="General Customs Value")

df = df[pd.to_numeric(df["Year"], errors="coerce").notna()]
df = df[pd.to_numeric(df["Month"], errors="coerce").notna()]

df["Year"] = df["Year"].astype(int)
df["Month"] = df["Month"].astype(int)

df["Date"] = pd.to_datetime(df["Year"].astype(str) + "-" + df["Month"].astype(str))

df["Quarter"] = df["Date"].dt.to_period("Q")
df_quarterly = df.groupby("Quarter")["General Customs Value"].sum().reset_index()

df_quarterly["Value (Billion $)"] = df_quarterly["General Customs Value"] / 1e9

df_quarterly = df_quarterly.sort_values("Quarter")
df_quarterly = df_quarterly.drop(columns="General Customs Value")

df_quarterly.to_csv("data/Processed/import_domestic/import.csv", index = False)


# deal with gross output data
with open("data/raw/domestic_output_vs_import/Domestic_Production.csv", "r") as f:
    lines = f.readlines()

line = lines[5]  

parts = line.strip().split(",")
quarter_values = parts[2:] 

quarters = []
years = list(range(2013, 2025))
for year in years:
    for q in range(1, 5):
        quarters.append(f"{year}Q{q}")
quarters = quarters[:len(quarter_values)]  

df_gross_output = pd.DataFrame({
    "Quarter": pd.PeriodIndex(quarters, freq="Q"),
    "Gross Output (Billion $)": pd.to_numeric(quarter_values, errors="coerce")
})

df_gross_output.to_csv("data/Processed/import_domestic/domestic_gross_output.csv", index = False)