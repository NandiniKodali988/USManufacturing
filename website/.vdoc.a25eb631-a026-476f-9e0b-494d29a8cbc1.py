# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import pandas as pd

# Load and filter
df = pd.read_csv("../data/Processed/merged_quarterly.csv")
df['Year'] = df['YearQuarter'].str.extract(r'(\d{4})').astype(int)
df = df[(df['Year'] >= 2013) & (df['Year'] <= 2023)].copy()

# Rename relevant columns
column_rename_map = {
    'gross_job_gains_thousand_persons': 'Gross Job Gains (Thousands)',
    'gross_job_losses_thousand_persons': 'Gross Job Losses (Thousands)',
    'labor_productivity_pct_qoq_change': 'Labor Productivity (% QoQ)',
    'unit_labor_cost_pct_qoq_change': 'Unit Labor Cost (% QoQ Change)'
}
df = df[['YearQuarter'] + list(column_rename_map.keys())]
df.rename(columns=column_rename_map, inplace=True)
df = df.round(2)

# Apply parameter selection
selected_cols = ['YearQuarter'] + params["columns"]
df[selected_cols].head(params["nrows"]).style.set_caption(
    "Quarterly Labor Market Indicators (Filtered)"
).set_table_attributes('style="width:100%"').set_properties(**{
    'border': '1px solid #ccc',
    'padding': '6px',
    'text-align': 'center',
    'font-size': '13px'
})
#
#
#
