import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="EU Renewable Energy Dashboard", layout="wide")

# 2. Load Data
@st.cache_data
def load_data():
    df = pd.read_csv(r'C:\Users\Bishownath Raut\cleaned_renewable_data.csv')
    return df

df = load_data()

# Identify aggregates vs countries
aggregates = ['European Union - 27 countries', 'Euro area – 20 countries']
df_countries = df[~df['Country'].isin(aggregates)]

# --- SIDEBAR FILTERS ---
st.sidebar.header("Dashboard Filters")

# Country Multi-select
selected_countries = st.sidebar.multiselect(
    "Select Countries to Compare:",
    options=df_countries['Country'].unique(),
    default=["Germany", "France", "Sweden"]
)

# Year Range Slider
min_year, max_year = int(df['Year'].min()), int(df['Year'].max())
year_range = st.sidebar.slider("Select Year Range:", min_year, max_year, (min_year, max_year))

# Filter dataframe based on selections
mask = (df_countries['Country'].isin(selected_countries)) & \
       (df_countries['Year'].between(year_range[0], year_range[1]))
df_filtered = df_countries[mask]

# --- MAIN PAGE ---
st.title("🇪🇺 Renewable Energy Transition in Europe")
st.markdown("Interactive analysis of Eurostat renewable energy shares.")

# --- KPI CARDS ---
col1, col2, col3 = st.columns(3)

# Latest EU Average
latest_eu_val = df[(df['Country'] == 'European Union - 27 countries') & 
                   (df['Year'] == max_year)]['Renewable_Share'].values[0]

# Top Performing Country
top_country_row = df_countries[df_countries['Year'] == max_year].sort_values('Renewable_Share', ascending=False).iloc[0]

with col1:
    st.metric("EU Average (Latest)", f"{latest_eu_val:.2f}%")
with col2:
    st.metric(f"Top Performer: {top_country_row['Country']}", f"{top_country_row['Renewable_Share']:.2f}%")
with col3:
    st.metric("Reporting Countries", len(df_countries['Country'].unique()))

# --- INTERACTIVE PLOTS ---
st.divider()

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("Historical Growth Comparison")
    fig_line = px.line(df_filtered, x='Year', y='Renewable_Share', color='Country',
                       markers=True, title="Renewable Share % Over Time")
    st.plotly_chart(fig_line, use_container_width=True)

with row2_col2:
    st.subheader(f"Top 10 Leaders in {year_range[1]}")
    top_10_filtered = df_countries[df_countries['Year'] == year_range[1]].sort_values('Renewable_Share', ascending=False).head(10)
    fig_bar = px.bar(top_10_filtered, x='Renewable_Share', y='Country', orientation='h',
                     color='Renewable_Share', color_continuous_scale='Greens')
    st.plotly_chart(fig_bar, use_container_width=True)

# --- MAP INTEGRATION ---
st.divider()
st.subheader("Geographical Distribution")
fig_map = px.choropleth(
    df_countries[df_countries['Year'] == year_range[1]],
    locations="Country",
    locationmode='country names',
    color="Renewable_Share",
    hover_name="Country",
    title=f"Renewable Energy Share Across Europe ({year_range[1]})",
    color_continuous_scale='YlGn'
)
st.plotly_chart(fig_map, use_container_width=True)

st.sidebar.info("Data Source: Eurostat (sdg_07_40)")