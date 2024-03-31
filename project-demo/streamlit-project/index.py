import streamlit as st
import numpy as np
import pandas as pd
import joblib

############ Cons & Configs ############
# neighbourhood list
NBR = ['Adams', 'Alki', 'Arbor Heights', 'Atlantic', 'Belltown', 'Bitter Lake', 'Briarcliff', 'Brighton', 'Broadview', 'Broadway', 'Bryant', 'Cedar Park', 'Central Business District', 'Columbia City', 'Crown Hill', 'Dunlap', 'East Queen Anne', 'Eastlake', 'Fairmount Park', 'Fauntleroy', 'First Hill', 'Fremont', 'Gatewood', 'Genesee', 'Georgetown', 'Green Lake', 'Greenwood', 'Haller Lake', 'Harbor Island', 'Harrison/Denny-Blaine', 'High Point', 'Highland Park', 'Holly Park', 'Industrial District', 'Interbay', 'International District', 'Laurelhurst', 'Lawton Park', 'Leschi', 'Lower Queen Anne', 'Loyal Heights', 'Madison Park', 'Madrona', 'Mann', 'Maple Leaf', 'Matthews Beach', 'Meadowbrook', 'Mid-Beacon Hill', 'Minor', 'Montlake', 'Mount Baker', 'North Admiral', 'North Beach/Blue Ridge', 'North Beacon Hill', 'North College Park', 'North Delridge', 'North Queen Anne', 'Olympic Hills', 'Phinney Ridge', 'Pike-Market', 'Pinehurst', 'Pioneer Square', 'Portage Bay', 'Rainier Beach', 'Rainier View', 'Ravenna', 'Riverview', 'Roosevelt', 'Roxhill', 'Seaview', 'Seward Park', 'South Beacon Hill', 'South Delridge', 'South Lake Union', 'South Park', 'Southeast Magnolia', 'Stevens', 'Sunset Hill', 'University District', 'Victory Heights', 'View Ridge', 'Wallingford', 'Wedgwood', 'West Queen Anne', 'West Woodland', 'Westlake', 'Whittier Heights', 'Windermere', 'Yesler Terrace']
RT_PRE = 'room_type_'
BT_PRE = 'bath_type_'
NBR_PRE = 'neighbourhood_'


############ Setup ############
# page info
st.markdown("# Predict Your Airbnb Price 🏡")
st.sidebar.markdown("# Prediction 🏡")

# load the trained model
rf_model = joblib.load('./model/rf_model.joblib')

# load default user input (as a DataFrame)
df_input = pd.read_csv('./data/default_input.csv')
# df_input


############ Basic information ############
basic_col1, basic_col2 = st.columns(2)

# selectbox for neighbourhood
with basic_col1:
    nbr_input = st.selectbox('Neighbourhood', NBR)
    st.write('You selected:', nbr_input)

# accommodates
with basic_col2:
    acm_input = st.slider('Accommadates', 1, 15, 1)
    st.write("I'm ", acm_input, 'years old')


############ Bedroom information ############
bedroom_col1, bedroom_col2, bedroom_col3 = st.columns(3)

# room type
with bedroom_col1:
    rt_input = st.radio('Room Type', ['Entire Home/Apt', 'Private Room', 'Shared Room'])
    if rt_input == 'Entire Home/Apt':
        st.write('room_type_entire')
    elif rt_input == 'Private Room':
        st.write('room_type_private')
    else:
        st.write('room_type_shared')

# bedroom number
with bedroom_col2:
    bedroom_input = st.slider('Bedrooms', 1, 12, 1)
    st.write("I'm ", bedroom_input, 'years old')

# bed number
with bedroom_col3:
    bed_input = st.slider('Beds', 1, 15, 1)
    st.write("I'm ", bed_input, 'years old')


############ Bathroom information ############
bathroom_col1, bathroom_col2, bathroom_col3 = st.columns(3)

# bath type
with bathroom_col1:
    bt_input = st.radio('Bath Type', ['Standard', 'Shared', 'Private'])
    if bt_input == 'Standard':
        st.write('bath_type_standard')
    elif bt_input == 'Shared':
        st.write('bath_type_shared')
    else:
        st.write('bath_type_private')

# bathroom number
with bathroom_col2:
    bathroom_input = st.slider('Bathrooms', 1, 15, 1)
    st.write("I'm ", bathroom_input, 'years old')


############ Review rating information ############
rating_input = st.slider('Accommadates', 0.0, 5.0, 0.1)
st.write("I'm ", rating_input, 'years old')


############ Wrap the input data ############
def rt_map(rt_input: str) -> str:
    rt = 'shared'
    if rt_input == 'Entire Home/Apt':
        rt = 'entire'
    elif rt_input == 'Private Room':
        rt = 'private'
    return RT_PRE+rt
    
def bt_map(bt_input: str) -> str:
    bt = 'private'
    if bt_input == 'Standard':
        bt = 'standard'
    elif bt_input == 'Shared':
        bt = 'shared'
    return BT_PRE+bt

if st.button("Predict", type='primary'):
    st.write(nbr_input, acm_input, rt_input, bedroom_input, bed_input, bt_input, bathroom_input, rating_input)
    rt = rt_map(rt_input)
    bt = bt_map(bt_input)

    df_input.at[0, rt] = True
    df_input.at[0, bt] = True
    df_input.at[0, NBR_PRE+nbr_input] = True
    df_input.at[0, 'accommodates'] = acm_input
    df_input.at[0, 'bedrooms'] = bedroom_input
    df_input.at[0, 'beds'] = bed_input
    df_input.at[0, 'bathrooms'] = bathroom_input
    df_input.at[0, 'rating'] = rating_input

    st.write(df_input)
    st.write(rf_model.predict(df_input))