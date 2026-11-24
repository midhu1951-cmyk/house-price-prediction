
import streamlit as st
import requests

st.title('House price prediction')
st.write('Enter the house details below')

income = st.number_input('Income', min_value=0.0)
age = st.number_input('Age', min_value=0.0)
rooms = st.number_input('Total rooms', min_value=1)
bedrooms = st.number_input('Total bedrooms', min_value=1)
population = st.number_input('Population', min_value=0)

if st.button('Predict House Price'):

    data = {
        'income': income,
        'age': age,
        'rooms': rooms,
        'bedrooms': bedrooms,
        'population': population
    }

    try:
        response = requests.post(
            'http://127.0.0.1:5000/predict',
            json=data
        )

        result = response.json()

        if response.status_code == 200:
            st.success(
                f"Predicted house price: {result['predicted_price']:.2f}"
            )
        else:
            st.error(result.get('error', 'Prediction failed'))

    except requests.exceptions.ConnectionError:
        st.error('Flask backend is not running.')

