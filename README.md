# Navigating Change: Analyzing the Evolution of U.S. Manufacturing

## Team Member - group 13 in section 02
- Li-Wen Hu
- Nandini Kodali
- Ruijie Xu
- Jiahui Liu

## Overview

This project presents an interactive data-driven story exploring the evolution of U.S. manufacturing over the past decade. Through global comparisons, economic indicators, and stakeholder perspectives, the narrative highlights the forces reshaping the manufacturing sector — including globalization, labor trends, and policy interventions.


## Project structure.

```bash 
dsan5200-spring2025-project-group-13/
│
├── website/                       # Main website directory
├── ├──_site/                      # auto-generated HTML output folder
│      ├── index.html
│      ├── slides.html
│      └── data.html
│   ├── index.qmd                  # Main narrative
│   ├── data.qmd                   # Data format
│   ├── slides.qmd                 # Presentation
│   └── news.png                   # Image asset
│
├── code/                          # Jupyter notebooks for visualizations
│   ├── data_cleaning/             # Data cleaning scripts 
│   ├── cost_efficiency_producer.ipynb     # Producer perspective: bubble chart
│   ├── employment_rate_2.ipynb            # Updated employment rate plot
│   ├── employment_rate.ipynb              # Sectoral employment analysis
│   ├── gdp_bubble.ipynb                   # GDP + employment bubble test
│   ├── import_domestic_buyer.ipynb        # Buyer: IPI vs PPI + import share
│   ├── stacked_area.ipynb                 # Stacked industry employment plot
│   ├── wage_hour_job_worker.ipynb         # Worker: wages + job conditions
│   ├── workforce_timeseries.ipynb         # Employment by sector over time
│   ├── producer_real_output.ipynb         # Producer: pointing to productivity gains.
│   ├── Import_export.ipynb                # Import and Export trade for us manufacture
│   └── worldmap.ipynb                     # Choropleth map of GDP share
│
│
├── data/                          # Raw and processed data
│   ├── raw/
│   └── Processed/
│
├── img/                           # HTML image exports
│
├── README.md
├── _quarto.yml
└── requirement.txt
```
### Data Source

All raw datasets were preprocessed using scripts located in `code/data_cleaning/`.  
The cleaned datasets were saved into the `data/Processed/` directory and served as the input for all visualization notebooks.

- `data/raw/` – Contains original, unmodified datasets
- `code/data_cleaning/` – Contains Python scripts for cleaning, transforming, and organizing data
- `data/Processed/` – Contains cleaned and analysis-ready CSVs used throughout the project


### Core Capabilities

| Code File | Visualization Output(s) | Role in Narrative |
|---|---|---|
| `worldmap.ipynb` | Global choropleth map showing manufacturing % of GDP | **Part 1 – Big Picture:** Global manufacturing comparison |
| `gdp_bubble.ipynb` | Bar chart of sectoral output across years | **Part 1 – Big Picture:** U.S. industry-level comparison |
| `stacked_area.ipynb` | Stacked area chart of industry employment trends | **Part 1 – Big Picture:** Workforce structural shift |
| `import_domestic_buyer.ipynb` | IPI vs PPI line chart, import share trend, import vs domestic bar chart | **Part 2 – Buyer Perspective:** Market dynamics and cost decisions |
| `cost_efficiency_producer.ipynb` | Bubble chart of labor cost vs productivity over time | **Part 2 – Producer/Policy Perspective:** Impact of policy on efficiency and firm behavior |
| `wage_hour_job_worker.ipynb` | Wage and compensation trends, net job creation, unemployment rate | **Part 2 – Worker Perspective:** Job security, wage changes, and recovery trajectory |

### Website

The `website/` folder contains all Quarto source files and rendered HTML outputs for the final presentation.

- `index.qmd` – The main source file for the full **visual narrative report**
- `slides.qmd` – A condensed version of the content, formatted as a **presentation deck**
- `data.qmd` –  A formatted data table that presents part of our data

The corresponding rendered files in `_site`are:

- `index.html` – Opens the interactive **report-style website**
- `slides.html` – Opens the **slideshow presentation**
- `data.html` – Opens the **formatted data table**

You can view either HTML file directly in a browser. 


### Plot Views

1. **Global Manufacturing Comparison**
   - Choropleth map of manufacturing as a % of GDP by country  
      `worldmap.ipynb`

2. **Domestic Sectoral Trends**
   - Grouped bar chart: Output by industry sector across time  
      `employment_rate.ipynb`
   - Stacked area chart: Employment share by sector  
      `stacked_area.ipynb`

3. **Market Dynamics – Linked Views**
   - Line chart: IPI - PPI gap over time  
   - Line chart: Import share trend  
   - Bar chart: Import value vs domestic output  
      `import_domestic_buyer.ipynb`  
   > These plots are **linked by time selection** and provide coordinated insights from a buyer's decision-making lens.

4. **Producer Cost vs Productivity**
   - Bubble chart: Labor cost vs productivity (bubble size = number of establishments)  
   - Line chart: Annual growth rate of private firms  
      `cost_efficiency_producer.ipynb`

5. **Worker Experience**
   - Parallel line plot: Hourly wage, compensation, and weekly hours  
   - Bar chart: Net job creation/loss by year  
   - Line chart: Manufacturing unemployment rate  
      `wage_hour_job_worker.ipynb`

| Plot Type         | Count | Description |
|-------------------|-------|-------------|
| Choropleth Map    | 1     | Global GDP share map |
| Grouped Bar Chart | 1     | Sectoral output comparison |
| Stacked Area Chart| 1     | Workforce structure shift |
| Line Charts       | 5     | Used in Market Dynamics and Worker view |
| Bar Charts        | 2     | Import comparison, job net change |
| Bubble Chart      | 1     | Producer cost vs productivity |
| Parallel Line Plot| 1     | Wages, benefits, and hours |


## Installation

To run the notebooks or generate the website locally, follow these steps:

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # or .\env\Scripts\activate on Windows

2.Install all required dependencies from requirements.txt:
   ```bash
   pip install -r requirement.txt
   ```

## Findings&Conclusion

The U.S. manufacturing sector is navigating a period of complex adjustment. From a global perspective, it faces growing competition from more cost-efficient production centers in Asia, even as domestic output and employment continue to rise modestly. Internally, manufacturers contend with rising labor costs, slow productivity gains, and shifting policy frameworks designed to support reshoring and innovation. For buyers, importing has become increasingly attractive due to sustained price advantages. For firms, federal initiatives have sparked growth spurts but have not resolved underlying cost pressures. For workers, the post-pandemic recovery brought better wages but also renewed concerns about long-term job security. These dynamics underscore a key insight: the future of U.S. manufacturing will depend not just on policy or production volume, but on its ability to adapt structurally—investing in advanced technologies, fostering a skilled workforce, and redefining competitiveness in an interconnected, fast-changing global economy. Ultimately, the future of U.S. manufacturing will be shaped not only by national policy and international pressures, but by the day-to-day choices of firms, workers, and buyers alike. Their experiences—navigating cost tradeoffs, job uncertainty, and competitive pressure—underscore that revitalizing manufacturing is as much a human story as an economic one.

   

