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
import pandas as pd
import ipywidgets as widgets
from IPython.display import display

# Load data
df = pd.read_csv("../data/Processed/merged_quarterly.csv")
# Extract year and filter
df['Year'] = df['YearQuarter'].str.extract(r'(\d{4})').astype(int)
df = df[(df['Year'] >= 2013) & (df['Year'] <= 2023)].copy()
df.drop(columns='Year', inplace=True)

# Rename columns
column_rename_map = {
    'gross_job_gains_thousand_persons': 'Gross Job Gains (Thousands)',
    'gross_job_losses_thousand_persons': 'Gross Job Losses (Thousands)',
    'num_private_establishment_count': 'Number of Private Establishments',
    'num_priv_estab_gross_job_gains_thousands': 'Establishments Gaining Jobs (Thousands)',
    'num_priv_estab_gross_job_losses_thousands': 'Establishments Losing Jobs (Thousands)',
    'labor_productivity_pct_qoq_change': 'Labor Productivity (% QoQ)',
    'labor_output_pct_qoq_change': 'Labor Output (% QoQ Change)',
    'working_hours_pct_qoq_change': 'Working Hours (% QoQ Change)',
    'unit_labor_cost_pct_qoq_change': 'Unit Labor Cost (% QoQ Change)',
    'priv_wage_salaries_cost_pct_change_Estimate Value': 'Wages (% Change, Estimate)',
    'priv_wage_salaries_cost_pct_change_Standard Error': 'Wages (% Change, Std. Error)',
    'priv_wage_salaries_cost_dollars_per_hour_Estimate Value': 'Wages ($/Hour, Estimate)',
    'priv_wage_salaries_cost_dollars_per_hour_Relative Standard Error': 'Wages ($/Hour, Rel. Std. Error)',
    'priv_total_compensation_cost_pct_change_Estimate Value': 'Compensation (% Change, Estimate)',
    'priv_total_compensation_cost_pct_change_Standard Error': 'Compensation (% Change, Std. Error)',
    'priv_total_compensation_cost_dollars_per_hour_Estimate Value': 'Compensation ($/Hour, Estimate)',
    'priv_total_compensation_cost_dollars_per_hour_Relative Standard Error': 'Compensation ($/Hour, Rel. Std. Error)'
}
df.rename(columns=column_rename_map, inplace=True)

# Format all numeric columns to 2 decimal places
styled = df.style.format(precision=2).set_caption(
    "Quarterly Labor Market and Productivity Indicators for the U.S. Private Sector (2013–2023)"
).set_table_attributes('style="width:100%; border-collapse:collapse"').set_properties(**{
    'border': '1px solid #ccc',
    'padding': '6px',
    'text-align': 'center',
    'font-size': '13px'
})

styled
#
#
#
#
#
