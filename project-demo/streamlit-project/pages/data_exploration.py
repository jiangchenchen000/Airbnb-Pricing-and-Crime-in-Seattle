import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import plotly.express as px
import geopandas as gpd


############ Const & Config ############
DATA_PATH = './data/listing_primary.csv'
NBR = ['Adams', 'Alki', 'Arbor Heights', 'Atlantic', 'Belltown', 'Bitter Lake', 'Briarcliff', 'Brighton', 'Broadview', 'Broadway', 'Bryant', 'Cedar Park', 'Central Business District', 'Columbia City', 'Crown Hill', 'Dunlap', 'East Queen Anne', 'Eastlake', 'Fairmount Park', 'Fauntleroy', 'First Hill', 'Fremont', 'Gatewood', 'Genesee', 'Georgetown', 'Green Lake', 'Greenwood', 'Haller Lake', 'Harbor Island', 'Harrison/Denny-Blaine', 'High Point', 'Highland Park', 'Holly Park', 'Industrial District', 'Interbay', 'International District', 'Laurelhurst', 'Lawton Park', 'Leschi', 'Lower Queen Anne', 'Loyal Heights', 'Madison Park', 'Madrona', 'Mann', 'Maple Leaf', 'Matthews Beach', 'Meadowbrook', 'Mid-Beacon Hill', 'Minor', 'Montlake', 'Mount Baker', 'North Admiral', 'North Beach/Blue Ridge', 'North Beacon Hill', 'North College Park', 'North Delridge', 'North Queen Anne', 'Olympic Hills', 'Phinney Ridge', 'Pike-Market', 'Pinehurst', 'Pioneer Square', 'Portage Bay', 'Rainier Beach', 'Rainier View', 'Ravenna', 'Riverview', 'Roosevelt', 'Roxhill', 'Seaview', 'Seward Park', 'South Beacon Hill', 'South Delridge', 'South Lake Union', 'South Park', 'Southeast Magnolia', 'Stevens', 'Sunset Hill', 'University District', 'Victory Heights', 'View Ridge', 'Wallingford', 'Wedgwood', 'West Queen Anne', 'West Woodland', 'Westlake', 'Whittier Heights', 'Windermere', 'Yesler Terrace']

# format numeric number as %.2f
def num_formatter(num):
    return round(num, 2)


############ Setup ############
st.markdown("# Data Exploration 📊")
st.divider()

st.sidebar.markdown("# Data Exploration 📊")
st.sidebar.markdown(' 1️⃣ Data Overview')
st.sidebar.markdown(' 2️⃣ Data Distribution')
st.sidebar.markdown(' 3️⃣ Relation Exploration')


# load cleaned data
@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)

# stat by area
@st.cache_data
def area_stat(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('neighbourhood', as_index=False)['price'].agg([np.mean, np.median, np.size])

# data distribution stat
@st.cache_data
def data_dis(df: pd.DataFrame, target: str) -> pd.DataFrame:
    dis_df = df[target].value_counts().rename_axis(target).reset_index(name='count')
    dis_df[target] = dis_df[target].astype(int)
    return dis_df

# relation between single feature and price
@st.cache_data
def sinlge_rel(feature: str) -> pd.DataFrame:
    return df[[feature, 'price']]


############ Data overview ############
st.markdown("## Data Overview")

df = load_data()
price_area = area_stat(df)

# overview metrics
ov_col1, ov_col2, ov_col3, ov_col4 = st.columns(4)
ov_col1.metric('Total Records', f'{len(df)}')
ov_col2.metric('Neighbourhoods', f'{df["neighbourhood"].nunique()}')
ov_col3.metric('Lowest Price', f'${num_formatter(df["price"].min())}')
ov_col4.metric('Highest Price', f'${num_formatter(df["price"].max())}')

# dataframe toggler
if st.button("View DataFrame", type='primary', key='expd_df'):
    st.dataframe(df)
    if st.button("Collapse", type='secondary', key='clps_df'):
        # collapse the dataframe by rerender
        st.rerun()

# view price by neighborhood
st.markdown("### Price by Area")
st.markdown("Will rental price significantly varies between area? Explore the data in different neighbourhoods!")

area = st.selectbox("Neighbourhood:", NBR)

area_res = price_area.loc[price_area["neighbourhood"]==area].iloc[0]

area_col1, area_col2, area_col3 = st.columns(3)
area_col1.metric('Total Rentals', f'{area_res["size"]}')
area_col2.metric('Avg Price', f'${num_formatter(area_res["mean"])}')
area_col3.metric('Median Price', f'${num_formatter(area_res["median"])}')

st.divider()

st.markdown("Also, you can view the distribution of the numeric features in our dataset be selecting the feature in the box below!")

target = st.selectbox(
    "Select feature:",
    ("accommodates", "beds", "bedrooms", "bathrooms"),
)

if target:
    st.bar_chart(data_dis(df, target), x=target, y='count')

# st.divider()

############ Relations to price ############
st.markdown("## Correlation Exploration")
st.markdown("Want to explore the relation between single feature and price? You can try it by selecting the feature you want to explore!")

feature = st.selectbox(
    "Select feature:",
    ("accommodates", "beds", "bedrooms", "bathrooms", "rating"),
)

st.scatter_chart(sinlge_rel(feature), x=feature, y='price')

# st.divider()

############ Data distribution ############
st.markdown("## Data Distribution")
st.markdown("Interested in the data distribution? You can hover around the cursor to see the Average Price of Airbnb and Crime Situation in different neighborhoods!")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Average Airbnb Prices by Neighborhood in Seattle")

    # Load the Seattle GeoJSON into a GeoDataFrame 
    gdf = gpd.read_file('./data/listing_geo.geojson')
    # Convert the GeoDataFrame to a JSON format that Plotly can understand
    geojson = gdf.__geo_interface__
    
    # Create the choropleth map using Plotly Express
    fig = px.choropleth_mapbox(gdf, geojson=geojson, 
                           locations=gdf.index, color="price",
                           hover_name="neighborhood", 
                           hover_data={"price": True}, 
                           mapbox_style="carto-positron", 
                           center={"lat": gdf.geometry.centroid.y.mean(), "lon": gdf.geometry.centroid.x.mean()},
                           zoom=10,
                           labels={"price": "Average Price ($)"}
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, title="Average Airbnb Prices by Neighborhood in Seattle")
    # Display the figure in Streamlit
    st.plotly_chart(fig, use_container_width=True)

with col2: 
    st.subheader("Total Crime (2008-2024) by Neighborhood in Seattle")

    # Load the Seattle GeoJSON into a GeoDataFrame
    gdf_crime = gpd.read_file('./data/crime_geo.geojson')
    
    # Convert the GeoDataFrame to a JSON format that Plotly can understand
    geojson = gdf_crime.__geo_interface__
    # Create the choropleth map using Plotly Express
    fig = px.choropleth_mapbox(gdf_crime, geojson=geojson, 
                           locations=gdf.index, color="Total crime",
                           hover_name="neighborhood", 
                           hover_data={"Total crime": True}, 
                           mapbox_style="carto-positron", 
                           center={"lat": gdf_crime.geometry.centroid.y.mean(), "lon": gdf_crime.geometry.centroid.x.mean()},
                           zoom=10,
                           labels={"Total crime": "Total Crime Amount"}
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, title="Crime Amount (2008-2024) by Neighborhood in Seattle")
    
    # Display the figure in Streamlit
    st.plotly_chart(fig, use_container_width=True)
