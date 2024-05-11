import streamlit as st
st.title('MPG ML PROJECT')
displacement = st.number_input('enter a value for displacement',
value=300, placeholder='enter a value for displcement')
Horsepower = st.number_input('enter a value for horsepower',
value=130, placeholder='enter a value for horsepower')

weight = st.number_input('enter a value for weight',
value=3000, placeholder='enter a value for weight')
Acceleration = st.number_input('enter a value for Acceleration',
value=12, placeholder='enter a value for Acceleration')

import pickle

loaded_model = pickle.load(open('mpg_regression.sav','rb'))
prediction = loaded_model.predict([[displacement,Horsepower,weight,Acceleration]])
st.subheader(f'predicted mpg value for above parametre is {prediction[0]}')

st.write(prediction)
