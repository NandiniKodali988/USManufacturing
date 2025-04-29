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
import plotly.express as px
df = pd.read_csv("../data/raw/manufacturing-value-added-to-gdp.csv")
# rename the GDP column for convenience
df = df.rename(columns={"Manufacturing, value added (% of GDP)": "ManufacturingGDP"})
df = df[(df['Year'] >= 2013) & (df['Year'] <= 2024)]
df = df.dropna(subset=['Code']).reset_index(drop=True)
df_filtered = df[(df["Year"] >= 2013) & (df["Year"] <= 2024)]
# Create animated choropleth map
fig = px.choropleth(
    df_filtered,
    locations="Entity",
    locationmode="country names",   # Use full country names
    color="ManufacturingGDP",
    hover_name="Entity",
    animation_frame="Year",
    color_continuous_scale="Blues",
    range_color=[0, 40],            # Adjust range if needed
    title="Manufacturing as % of GDP by Country (2013–2024)"
)
fig.update_layout(
    geo=dict(showframe=False, showcoastlines=False),
    coloraxis_colorbar=dict(title="% of GDP")
)
fig.show()
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
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.express as px
df = pd.read_csv("../data/Processed/GdpByInd.csv")
# Clean up column names just in case
df.columns = df.columns.str.strip()

# Identify actual year columns (assuming they are 4-digit years)
year_columns = [col for col in df.columns if col.isdigit() and len(col) == 4]

# Melt the data safely
df_long = df.melt(
    id_vars=["Group", "Subgroup"],
    value_vars=year_columns,
    var_name="Year",
    value_name="Value"
)

# Convert year to integer
df_long["Year"] = df_long["Year"].astype(int)

df_grouped = df_long.groupby(["Group", "Year"], as_index=False)["Value"].sum()

unique_groups = df_grouped["Group"].unique()
group_positions = {
    group: (np.cos(i * 2 * np.pi / len(unique_groups)) * 3,
            np.sin(i * 2 * np.pi / len(unique_groups)) * 3)
    for i, group in enumerate(unique_groups)
}

# Filter for 2013–2024
df_grouped_filtered = df_grouped[df_grouped["Year"].between(2013, 2024)].copy()

# Convert from millions to billions
df_grouped_filtered["Value_Trillions"] = df_grouped_filtered["Value"] / 1000000

# Step 2: Add a column for custom coloring
df_grouped_filtered["Color"] = df_grouped_filtered["Group"].apply(
    lambda g: "Manufacturing" if g == "Manufacturing" else "Other"
)

# Step 3: Define color map (blue for Manufacturing, gray for others)
color_map = {
    "Manufacturing": "steelblue",
    "Other": "lightgray"
}

fig = px.bar(
    df_grouped_filtered,
    x="Value_Trillions",
    y="Group",
    color="Color",
    animation_frame="Year",
    orientation='h',
    color_discrete_map=color_map,
    title="Group-Level Output Race Over Time (2013–2024)",
    hover_data={"Color": False}  # hide 'Color' in tooltip
)

# Set custom tooltip on static traces (initial frame)
for trace in fig.data:
    trace.hovertemplate = "<b>%{y}</b><br>Value (Trillion USD): %{x:.2f}<extra></extra>"

# Set custom tooltip on animated frames
for frame in fig.frames:
    for trace in frame.data:
        trace.hovertemplate = "<b>%{y}</b><br>Value (Trillion USD): %{x:.2f}<extra></extra>"

# Layout settings
fig.update_layout(
    showlegend=False,
    xaxis=dict(
        title="Output (Trillions USD)",
        tickformat=".2f",
        range=[0, 12.5]
    ),
    margin=dict(t=40, l=100, r=40, b=40)
)

fig.show()

#
#
#
import pandas as pd
import altair as alt
import ipywidgets as widgets
from IPython.display import display
from ipywidgets import VBox

# Read data
df_clean = pd.read_csv("../data/Processed/employment_rate.csv")
df_clean['Month'] = pd.to_datetime(df_clean['Month'], errors='coerce')

# Original industries to plot
industries_to_plot = [
    'Manufacturing',
    'Construction',
    'Retail trade',
    'Transportation and warehousing',
    'Leisure and hospitality',
    'Financial activities'
]

# Mapping of original industry names to new legend labels
legend_labels = {
    'Manufacturing': 'Manufacturing',
    'Construction': 'Utilities & Construction',
    'Retail trade': 'Retail trade',
    'Transportation and warehousing': 'Transportation and warehousing',
    'Leisure and hospitality': 'Health, Education & Leisure',
    'Financial activities': 'Information & Finance'
}

# Melt data to long format
df_long = df_clean.melt(
    id_vars=['Month'],
    value_vars=industries_to_plot,
    var_name='Industry',
    value_name='Employment'
)

# Add custom legend labels based on the mapping
df_long['Industry_legend'] = df_long['Industry'].map(legend_labels)

# Create the selection widgets for start and end months
start_picker = widgets.SelectionSlider(
    options=list(df_clean['Month'].dt.to_period('M').astype(str)),
    description='Start Month',
    layout=widgets.Layout(width='800px')
)

end_picker = widgets.SelectionSlider(
    options=list(df_clean['Month'].dt.to_period('M').astype(str)),
    description='End Month',
    layout=widgets.Layout(width='800px')
)

# Explicitly define the desired order of industries for the legend
ordered_industries = [
    'Manufacturing',
    'Utilities & Construction',
    'Retail trade',
    'Transportation and warehousing',
    'Health, Education & Leisure',
    'Information & Finance'
]

# Create the stacked area chart using original Employment values (stacking them)
area_stack_chart = alt.Chart(df_long).mark_area(opacity=0.8).encode(
    x=alt.X('Month:T', title='Year'),
    y=alt.Y('Employment:Q', stack='zero', title='Employment (Thousands)'),  # stack='zero' for stacked area chart
    color=alt.Color('Industry_legend:N', scale=alt.Scale(domain=ordered_industries, range=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'])),
    tooltip=['Month:T', 'Industry_legend:N', 'Employment:Q']
).properties(
    width='container',  # Makes the width responsive
    height=400,  # Constrained height for better aspect ratio
    title='Stacked Employment Trend by Industry (2013–2023)'
)

# Adjust the legend position to be outside the plot and order it
area_stack_chart = area_stack_chart.configure_legend(
    orient='top',  # Legend at the top of the plot
    direction='horizontal',  # Horizontal legend
    title=None,  # No title for the legend
    offset=40,  # Increased spacing between chart and legend
    padding=20,  # Added padding inside the legend box
    labelFontSize=12,  # Set the font size of the legend labels
)

# Display the chart and the widgets
display(area_stack_chart)

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
