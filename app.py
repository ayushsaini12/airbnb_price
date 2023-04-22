import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('reg.pkl', 'rb'))

st.title('price? :blossom:')

host_identity_verified_option = [0,1]
instant_bookable_option= [0,1]
cancellation_policy_options = [0,1,2]
room_type_options = [0,1,2,3]
neighbourhood_group_option = [0,1,2,3,4]

host_identity_verified = st.selectbox(options= host_identity_verified_option, label="Host Verification (Verified: 1, Non-Verified: 0)")
instant_bookable = st.selectbox(label= "Instantly Book(False --> 0 , True --> 1)", options= instant_bookable_option )
cancellation_policy = st.selectbox(label= "Cancellation Policy (moderate --> 1 , strict --> 2 , flexible --> 0  )", options= cancellation_policy_options)
room_type = st.selectbox(label= "Room Type (Hotel room --> 1 , Private room --> 2 , Entire home/apt --> 0 , Shared room --> 3)", options=room_type_options)
neighbourhood_group = st.selectbox(options= neighbourhood_group_option, label= "Neighbourhood Group (Brooklyn --> 1 , Manhattan --> 2 , Bronx --> 0 , Queens --> 3 , Staten Island --> 4 )")
Construction_year = st.slider(min_value=2003.000000, max_value= 2022.000000, label="Construction year")
minimum_nights = st.slider(min_value=1.000000, max_value=150.000000, label= "Minimum nights")
service_fee = st.slider(min_value= 0.000000, max_value= 250.000000, label= "Service fee")
number_of_reviews = st.slider(min_value= 1.000000, max_value= 1024.000000, label= "calculated host listings count")
availability= st.slider(min_value=0.000000, max_value= 365.000000, label= "availability 365")


def predict():
    final_features= [np.array([host_identity_verified,neighbourhood_group,instant_bookable,cancellation_policy,room_type,Construction_year,service_fee,minimum_nights,number_of_reviews,availability])]
    prediction = model.predict(final_features)
    label = prediction[0]
    print(type(label))
    print(label)
    st.success('The Price is : ' + str(label) + ' :thumbsup:')
    
trigger = st.button('Predict', on_click=predict)