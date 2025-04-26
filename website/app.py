import streamlit as st
import streamlit.components.v1 as components

# Set page config first
st.set_page_config(
    page_title="Global Manufacturing Trends",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom CSS for blue background
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e6f0ff;  /* Light blue */
        background-attachment: fixed;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --- Title & Subheading ---
st.markdown("<h1>🏭 US Manufacturing Trend</h1>", unsafe_allow_html=True)
st.markdown("<h4>Explore the transformation of the American manufacturing sector from a national overview into buyers and producers perspective</h4>", unsafe_allow_html=True)

# --- Intro Paragraph ---

st.markdown("""
# Introduction
This project aims to analyze the **recent trends in U.S. manufacturing**, identify the factors influencing its trajectory, and provide insights into the industry's future direction.

**Why this matters:**  
Manufacturing plays a critical role in employment, exports, innovation, and economic stability. But its form is evolving.

This app is divided into two parts:

- 🔍 **Big Picture** — Understand how manufacturing contributes to GDP, employment. 
- 🧩 **Two Perspectives** — Dive into Buyers and Producers
---
""")

# --- Big Picture ---
st.markdown("""
# 🌍 Global Manufacturing Share of GDP (2013–2024)

- Displays manufacturing output as % of GDP across countries
- Darker blue indicates higher manufacturing contribution
- Key observations:
  - **Asia** (China, Vietnam) leads in manufacturing share
  - **U.S. manufacturing share** remains comparatively lower
  - **Emerging economies** show steady industrial growth
- Reveals shifting patterns in global industrial competitiveness
""")
with open("img/manufacturing_gdp_map.html", "r") as f:
    html_content = f.read()

components.html(html_content, height=500, scrolling=True)

# --- Employment rate  ---
st.markdown("""
---
# Employment Rate 
- The **U.S. has experienced a long-term decline in manufacturing’s share of GDP**, contrasting with Asia-Pacific industrial giants.
- **Employment has decreased**, but this does not necessarily reflect a failing sector—it reflects increasing automation, outsourcing, and a shift toward high-value manufacturing.
- A new form of industrial economy is emerging—one that may not be labor-intensive but still strategically essential.

This raises a natural next question:  
**How are specific manufacturing subsectors performing—and who is driving this transformation?**
""")


# --- Annual Worker Metrics ---
st.markdown("""
# Annual Worker

This plot visualizes the annual trends of several key labor metrics from **2013 to 2024**.

Each line represents a different year, tracking across four dimensions:
- **Hourly Earnings**
- **Total Compensation per Hour**
- **Wage Cost per Hour**
- **Weekly Hours**

The color gradient from light blue to dark blue represents the timeline:  
lighter colors are earlier years, darker colors are more recent years.

## 🔍 Why This Plot Matters

- **Compare multiple metrics simultaneously**, showing relationships across time.
- **Overall wage increase** observed after 2020.
- **Significant dip around 2020**, likely caused by the COVID-19 pandemic.
- Highlights evolving **labor cost and productivity** trends across a decade.
""")

with open("img/Annual_worker.html", "r") as f:
    html_content = f.read()

components.html(html_content, height=500, scrolling=True)


# --- Producer ---
st.markdown("""
# Producer
Our parallel coordinates plot reveals:
- **Steady increases in hourly earnings and total compensation** over the past decade
- **Relatively flat or slightly declining weekly hours**, suggesting efficiency gains

These labor dynamics reflect **rising costs per hour** but not necessarily falling competitiveness.

In addition, the connected scatterplot links **labor productivity** with **unit labor costs**, across policy shifts (A, B, C). We observe how policy environments correspond with changes in both efficiency and cost burdens, highlighting the **trade-offs of regulatory and economic decisions**.

Lastly, we examine **GDP contribution growth rates** across subsectors to see where the momentum lies—and which industries are driving the modern manufacturing engine.
""")

st.markdown("""
---
### Producer
- **Worker compensation is rising**, but not at the expense of weekly hours—pointing to increased wage pressure and potential productivity trade-offs.
- **Policy shifts are tightly linked** to changes in cost-productivity dynamics, and visualizing them helps contextualize what drives these transitions.
- Certain manufacturing subsectors are **outpacing others in GDP growth**, suggesting that the decline narrative is not universal—**some producers are thriving**.

This producer-centered perspective helps us understand not just the “what” of the trend, but the **“who” and “why”** behind the change.
""")
with open("img/Connected_chart.html", "r") as f:
    html_content = f.read()

components.html(html_content, height=800, scrolling=True)

# --- Conclusion ---
st.header("🔍 Conclusion")
st.markdown("Let’s zoom into individual sectors...")
