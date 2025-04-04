import pandas as pd

class Cleaner:
    def __init__(self,file_path,var_name,unit,time_freq,skiprows=0,wide_format=True,id_var="Year"):
        self.file_path = file_path
        self.var_name = var_name
        self.unit = unit
        self.time_freq = time_freq  
        self.skiprows = skiprows
        self.wide_format = wide_format
        self.id_var = id_var
        self.df = None

    def load(self):
        self.df = pd.read_excel(self.file_path, skiprows=self.skiprows)
        return self

    def reshape(self):
        if self.wide_format:
            if self.id_var and self.id_var in self.df.columns:
                id_col = self.id_var
            else:
                id_col = self.df.columns[0]
                print("No detection of 'Year', using the first column's name")
                if id_col is None:
                    raise ValueError("No Detection of Time")
            self.df = self.df.melt(id_vars=id_col, var_name='Period', value_name='Value')
        else:
            expected_cols = ['Year', 'Period']
            for col in expected_cols:
                if col not in self.df.columns:
                    raise ValueError(f"Missing required column: {col}")
        return self

    def convert_date(self):
        if self.time_freq == "monthly":
            month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                         'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
            self.df['Month'] = self.df['Period'].map(month_map)
            self.df['YearMonth'] = self.df.apply(lambda row: pd.Period(f"{int(row['Year'])}-{int(row['Month'])}", freq='M'), axis=1)

        elif self.time_freq == "quarterly":
            self.df['Period'] = self.df['Period'].str.replace("Qtr", "Q").str.extract(r'(\d)').astype(int)
            self.df['YearQuarter'] = self.df.apply(lambda r: f"{int(r['Year'])} Q{int(r['Period'])}", axis=1)
        return self

    def finalize(self):
    
        if self.time_freq == "monthly":
            sort_col = 'YearMonth'
        elif self.time_freq == "quarterly":
            sort_col = 'YearQuarter'
        else:
            raise ValueError("Unsupported time frequency")
    
        if sort_col not in self.df.columns:
            raise ValueError(f"Expected time column '{sort_col}' not found.")
        
        exclude_cols = ['Year', 'Period', 'Month', sort_col]
        value_cols = [col for col in self.df.columns if col not in exclude_cols]

        self.df = self.df.dropna(subset=value_cols, how='all')

        rename_dict = {}
        for col in value_cols:
            if col == "Value":
                new_col = f"{self.var_name}_{self.unit}".strip('_')
            else:
                new_col = f"{self.var_name}_{self.unit}_{col}".strip('_')
            rename_dict[col] = new_col
        
        self.df = self.df[[sort_col] + value_cols].sort_values(sort_col).reset_index(drop=True)
        self.df = self.df.rename(columns=rename_dict)
        return self.df

    def clean(self):
        return self.load().reshape().convert_date().finalize()
