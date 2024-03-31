import streamlit as st
import numpy as np
import pandas as pd
import joblib

# neighbourhood list
NBR = ['Wallingford', 'Georgetown', 'Fairmount Park', 'Whittier Heights',
'Sunset Hill', 'Eastlake', 'Fremont', 'Green Lake', 'Portage Bay',
'Phinney Ridge', 'Crown Hill', 'Columbia City', 'Lawton Park',
'North Queen Anne', 'West Queen Anne', 'First Hill', 'Broadway',
'Stevens', 'North Admiral', 'International District',
'North Beacon Hill', 'West Woodland', 'Greenwood', 'Cedar Park',
'Mount Baker', 'Mann', 'Ravenna', 'Belltown',
'University District', 'Harrison/Denny-Blaine', 'South Delridge',
'Atlantic', 'Broadview', 'Maple Leaf', 'East Queen Anne',
'Pioneer Square', 'Highland Park', 'Laurelhurst', 'Haller Lake',
'Madison Park', 'Fauntleroy', 'Madrona', 'Loyal Heights',
'Gatewood', 'Leschi', 'Westlake', 'Adams',
'North Beach/Blue Ridge', 'North Delridge', 'Bryant',
'Seward Park', 'View Ridge', 'Central Business District',
'Pike-Market', 'High Point', 'Yesler Terrace', 'Alki',
'Bitter Lake', 'Lower Queen Anne', 'Harbor Island', 'Windermere',
'Minor', 'Rainier Beach', 'Victory Heights', 'Seaview',
'Roosevelt', 'Dunlap', 'Matthews Beach', 'Southeast Magnolia',
'Genesee', 'Olympic Hills', 'Mid-Beacon Hill', 'Brighton',
'Interbay', 'Briarcliff', 'Montlake', 'North College Park',
'Riverview', 'Pinehurst', 'Wedgwood', 'Meadowbrook',
'Rainier View', 'South Beacon Hill', 'Industrial District',
'South Park', 'South Lake Union', 'Roxhill', 'Arbor Heights',
'Holly Park']

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

# load the trained model
rf_model = joblib.load('./model/rf_model.joblib')

# load default user input (as a DataFrame)
df_input = pd.read_csv('./data/default_input.csv')

# df_input

# selectbox for neighbourhood
option = st.selectbox('Neighbourhood', NBR)
st.write('You selected:', option)

st.write(sorted(NBR))