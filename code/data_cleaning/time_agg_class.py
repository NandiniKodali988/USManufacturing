import pandas as pd

class month_quarter_year_transformation:

    def __init__(self):
        pass

    @staticmethod
    def month_to_quarter(self, df: pd.DataFrame) -> pd.DataFrame:

        df2 = df.copy()
        
        time_col, value_col = df2.iloc[:2]

        df2[time_col] = pd.to_datetime(df2[time_col], format="%Y-%m")
        df2["YearQuarter"] = df2[time_col].dt.to_period("Q").astype(str)

        df_q = (df.groupby("YearQuarter", as_index=False)[value_col].mean())

        return df_q
    
    @staticmethod
    def to_annual(self, df: pd.DataFrame) -> pd.DataFrame:

        df2 = df.copy()

        time_col, value_col = df2.columns[:2]

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
