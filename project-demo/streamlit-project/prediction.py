import streamlit as st
import pandas as pd
import joblib

############ Const & Config ############
# MODEL_PATH = './model/model.joblib'
MODEL_PATH = './model/best_gb_params_rs.joblib'
# DATA_PATH = './data/default_input.csv'
DATA_PATH = './data/default_input_opt.csv'
NBR = ('Adams', 'Alki', 'Arbor Heights', 'Atlantic', 'Belltown', 'Bitter Lake', 'Briarcliff', 'Brighton', 'Broadview', 'Broadway', 'Bryant', 'Cedar Park', 'Central Business District', 'Columbia City', 'Crown Hill', 'Dunlap', 'East Queen Anne', 'Eastlake', 'Fairmount Park', 'Fauntleroy', 'First Hill', 'Fremont', 'Gatewood', 'Genesee', 'Georgetown', 'Green Lake', 'Greenwood', 'Haller Lake', 'Harbor Island', 'Harrison/Denny-Blaine', 'High Point', 'Highland Park', 'Holly Park', 'Industrial District', 'Interbay', 'International District', 'Laurelhurst', 'Lawton Park', 'Leschi', 'Lower Queen Anne', 'Loyal Heights', 'Madison Park', 'Madrona', 'Mann', 'Maple Leaf', 'Matthews Beach', 'Meadowbrook', 'Mid-Beacon Hill', 'Minor', 'Montlake', 'Mount Baker', 'North Admiral', 'North Beach/Blue Ridge', 'North Beacon Hill', 'North College Park', 'North Delridge', 'North Queen Anne', 'Olympic Hills', 'Phinney Ridge', 'Pike-Market', 'Pinehurst', 'Pioneer Square', 'Portage Bay', 'Rainier Beach', 'Rainier View', 'Ravenna', 'Riverview', 'Roosevelt', 'Roxhill', 'Seaview', 'Seward Park', 'South Beacon Hill', 'South Delridge', 'South Lake Union', 'South Park', 'Southeast Magnolia', 'Stevens', 'Sunset Hill', 'University District', 'Victory Heights', 'View Ridge', 'Wallingford', 'Wedgwood', 'West Queen Anne', 'West Woodland', 'Westlake', 'Whittier Heights', 'Windermere', 'Yesler Terrace')
P_TYPE = ('Entire guesthouse', 'Private room in rental unit', 'Entire home', 'Entire guest suite', 'Entire rental unit', 'Private room in home', 'Entire bungalow', 'Private room in cottage', 'Entire condo', 'Private room', 'Private room in bungalow', 'Entire townhouse', 'Private room in condo', 'Entire cottage', 'Private room in townhouse', 'Private room in guest suite', 'Boat', 'Private room in boat', 'Entire loft', 'Shared room', 'Entire vacation home', 'Private room in treehouse', 'Entire villa', 'Entire cabin', 'Entire place', 'Tent', 'Camper/RV', 'Tiny home', 'Houseboat', 'Entire serviced apartment', 'Shared room in rental unit', 'Private room in hostel', 'Room in boutique hotel', 'Shared room in home', 'Private room in loft', 'Shared room in loft', 'Room in hotel', 'Private room in villa', 'Shared room in townhouse', 'Private room in tiny home', 'Shared room in hostel', 'Private room in bed and breakfast', 'Casa particular', 'Room in aparthotel', 'Shared room in bed and breakfast', 'Farm stay', 'Shared room in condo', 'Bus', 'Private room in casa particular', 'Private room in guesthouse', 'Private room in serviced apartment'),
RT_PRE = 'room_type_'
# BT_PRE = 'bath_type_'
BT_PRE = 'bathroom_type_'
PT_PRE = 'property_type_'
# NBR_PRE = 'neighbourhood_'
NBR_PRE = 'neighbourhood_cleansed_'


############ Setup ############
# page info
st.markdown("# Predict Your Airbnb Price 🏡")
st.divider()

st.sidebar.markdown("# Prediction 🏡")
st.sidebar.markdown("Predict you ideal Airbnb rental price using our regression model trained with real world data!")

# load the trained model
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

# load default user input (as a DataFrame)
@st.cache_data
def default_input():
    return pd.read_csv(DATA_PATH)


############ Basic information ############
basic_col1, basic_col2 = st.columns(2)

# selectbox for neighbourhood
with basic_col1:
    nbr_input = st.selectbox('Neighbourhood', NBR)

# accommodates
with basic_col2:
    acm_input = st.slider('Accommadates', 1, 15, 1)


############ Bedroom information ############
bedroom_col1, bedroom_col2, bedroom_col3 = st.columns(3)

# room type
with bedroom_col1:
    rt_input = st.radio('Room Type', ['Entire home/apt', 'Private room', 'Shared room'])

# bedroom number
with bedroom_col2:
    bedroom_input = st.slider('Bedrooms', 0, 12, 1)

# bed number
with bedroom_col3:
    bed_input = st.slider('Beds', 1, 15, 1)


############ Bathroom information ############
bathroom_col1, bathroom_col2, bathroom_col3 = st.columns(3)

# bath type
with bathroom_col1:
    bt_input = st.radio('Bath Type', ['Standard', 'Shared', 'Private'])

# bathroom number
with bathroom_col2:
    bathroom_input = st.slider('Bathrooms', 0, 15, 1)


############ Property type ############
pt_input = st.selectbox("Poperty Type", P_TYPE, key="selectbox_poperty")


############ Review rating information ############
# rating_input = st.slider('Rating Score', 0.0, 5.0, 0.1)


############ Wrap the input data and Predict price with the model ############
# def rt_map(rt_input: str) -> str:
#     rt = 'shared'
#     if rt_input == 'Entire home/apt':
#         rt = 'entire'
#     elif rt_input == 'Private room':
#         rt = 'private'
#     return RT_PRE+rt

if st.button("Predict", type='primary'):
    model = load_model()
    df_input = default_input()

    st.divider()

    # try:
    # categorical cols
    # df_input.at[0, rt_map(rt_input)] = True
    df_input.at[0, RT_PRE+rt_input] = True
    df_input.at[0, BT_PRE+(bt_input.lower())] = True
    df_input.at[0, NBR_PRE+nbr_input] = True
    df_input.at[0, PT_PRE+pt_input] = True

    # numerical cols
    df_input.at[0, 'accommodates'] = acm_input
    df_input.at[0, 'bedrooms'] = bedroom_input
    df_input.at[0, 'beds'] = bed_input
    df_input.at[0, 'bathroom_count'] = bathroom_input
    # df_input.at[0, 'rating'] = rating_input

    result = model.predict(df_input)[0]

    st.success(f'Your ideal price will be ${round(result, 2)}, room details:', icon="✅")

    res_col11, res_col12, res_col13 = st.columns(3)
    res_col11.metric('Person(s)', f'{acm_input}')
    res_col12.metric(f'{rt_input}', f'{bedroom_input}')
    res_col13.metric(f'{bt_input} Bathroom', f'{bathroom_input}')

    res_col21, res_col22, res_col23 = st.columns(3)
    res_col21.metric('Area', f'{nbr_input}')
    res_col22.metric('Bed', f'{bed_input}')
    res_col23.metric('Price', f'${round(result, 2)}')
    
    # except Exception as e:
    #     st.error('Something went wrong, try again please', icon="🚨")
