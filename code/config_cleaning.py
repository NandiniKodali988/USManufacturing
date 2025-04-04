configs = [
    # formal
    #
    {
        "file_path": "data/raw/Workforce/All_Employees.xlsx",
        "var_name": "all_employees",
        "unit": "thousands",
        "time_freq": "monthly",
        "skiprows": 12
    },
    {
        "file_path": "data/raw/Workforce/Unemployment_Rate.xlsx",
        "var_name": "unemployment",
        "unit": "rate",
        "time_freq": "monthly",
        "skiprows": 14
    },
    {
        "file_path": "data/raw/Workforce/Job_Opennings.xlsx",
        "var_name": "job_opennings",
        "unit": "thousands",
        "time_freq": "monthly",
        "skiprows": 13
    },
    #
    {
        "file_path": "data/raw/Workforce/Average_Hourly_Earnings.xlsx",
        "var_name": "avg_hourly_earnings",
        "unit": "dollars",
        "time_freq": "monthly",
        "skiprows": 12
    },
    {
        "file_path": "data/raw/Workforce/Average_Weekly_Hoursxlsx.xlsx",
        "var_name": "avg_weekly_work",
        "unit": "hours",
        "time_freq": "monthly",
        "skiprows": 12
    },
    # 
    {
        "file_path": "data/raw/Workforce/Gross_Job_Gains.xlsx",
        "var_name": "gross_job_gains",
        "unit": "thousand_persons",
        "time_freq": "quarterly",
        "skiprows": 15
    },
    {
        "file_path": "data/raw/Workforce/Gross_Job_Losses.xlsx",
        "var_name": "gross_job_losses",
        "unit": "thousand_persons",
        "time_freq": "quarterly",
        "skiprows": 15
    },
    #
    {
        "file_path": "data/raw/Workforce/PPI.xlsx",
        "var_name": "producer_price",
        "unit": "index",
        "time_freq": "monthly",
        "skiprows": 10
    },
    {
        "file_path": "data/raw/Workforce/Import_Price_Index.xlsx",
        "var_name": "import_price",
        "unit": "index",
        "time_freq": "monthly",
        "skiprows": 10
    },
     {
        "file_path": "data/raw/Workforce/Export_Price_Index.xlsx",
        "var_name": "export_price",
        "unit": "index",
        "time_freq": "monthly",
        "skiprows": 10
    },
    #
    {
        "file_path": "data/raw/Workforce/Number_of_Establishments(private).xlsx",
        "var_name": "num_private_establishment",
        "unit": "count",
        "time_freq": "quarterly",
        "skiprows": 13
    },
    {
        "file_path": "data/raw/Workforce/NOE_Job_Gains.xlsx",
        "var_name": "num_priv_estab_gross_job_gains",
        "unit": "thousands",
        "time_freq": "quarterly",
        "skiprows": 15
    },
    {
        "file_path": "data/raw/Workforce/NOE_Job_Losses.xlsx",
        "var_name": "num_priv_estab_gross_job_losses",
        "unit": "thousands",
        "time_freq": "quarterly",
        "skiprows": 15
    },
    {
        "file_path": "data/raw/Workforce/Labor_Productivity.xlsx",
        "var_name": "labor_productivity",
        "unit": "pct_qoq_change",
        "time_freq": "quarterly",
        "skiprows": 10
    },
    {
        "file_path": "data/raw/Workforce/Output.xlsx",
        "var_name": "labor_output",
        "unit": "pct_qoq_change",
        "time_freq": "quarterly",
        "skiprows": 10
    },
    {
        "file_path": "data/raw/Workforce/Hours_Worked.xlsx",
        "var_name": "working_hours",
        "unit": "pct_qoq_change",
        "time_freq": "quarterly",
        "skiprows": 10
    },
    {
        "file_path": "data/raw/Workforce/Unit_Labor_Costs.xlsx",
        "var_name": "unit_labor_cost",
        "unit": "pct_qoq_change",
        "time_freq": "quarterly",
        "skiprows": 10
    },
    #
    {
        "file_path": "data/raw/Workforce/Wage_Salary(12mon_percentchange).xlsx",
        "var_name": "priv_wage_salaries_cost",
        "unit": "pct_change",
        "time_freq": "quarterly",
        "skiprows": 15,
        "wide_format": False,  
        "id_var": None  
    },
    {
        "file_path": "data/raw/Workforce/Wages_Salaries(perhour).xlsx",
        "var_name": "priv_wage_salaries_cost",
        "unit": "dollars_per_hour",
        "time_freq": "quarterly",
        "skiprows": 14,
        "wide_format": False,  
        "id_var": None  
    },
    {
        "file_path": "data/raw/Workforce/Total_Compensation(12mon_percentchange).xlsx",
        "var_name": "priv_total_compensation_cost",
        "unit": "pct_change",
        "time_freq": "quarterly",
        "skiprows": 15,
        "wide_format": False,  
        "id_var": None  
    },
    {
        "file_path": "data/raw/Workforce/Total_Compensation(perhour).xlsx",
        "var_name": "priv_total_compensation_cost",
        "unit": "dollars_per_hour",
        "time_freq": "quarterly",
        "skiprows": 14,
        "wide_format": False,  
        "id_var": None  
    }
]

