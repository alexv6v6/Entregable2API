import streamlit as st 
import pandas as pd
import requests

import pickle
def solicitud_API(muestra:list):
    
    # URL de la API
    url = 'https://miapistreamlit.azurewebsites.net/predict'

    # Datos de entrada
    data = {
        "data": [muestra]
    }

    # Realizar la solicitud POST a la API
    response = requests.post(url, json=data)

    # Verificar el código de estado de la respuesta
    if response.status_code == 200:
        # Obtener la respuesta en formato JSON
        result = response.json()
        
        # Obtener la predicción
        prediction = result["prediction"]
        
        # Imprimir la predicción
        print("Predicciónes:", prediction)
        return prediction
    else:
        print("Error en la solicitud:", response.status_code)
        return None



with open('models/modelo.pkl','rb') as gb:
    modelo = pickle.load(gb)


st.subheader("Machine Learning modelo seleccionado") 

st.subheader("Algoritmo de Machine Learning")
st.write("Definición del algoritmo implementado para predecir los patrones de flujo.")

st.subheader("Características de entrada")
features = ['Velocidad superficial del líquido (Vsl)', 'Velocidad superficial del gas (Vsg)', 'Viscosidad del líquido (VisL)', 'Viscosidad del gas (VisG)', 'Densidad del líquido (DenL)', 'Densidad del gas (DenG)', 'Tensión superficial (ST)', 'Ángulo de inclinación tubería (Ang)', 'Diámetro de la tubería (ID)']
st.write("A continuación, ingrese los valores de las características que serán utilizadas para la clasificación de patrones de flujo en los modelos de Machine Learning:")        

def user_input_parameters():
    inputs = {}
    for i, feature in enumerate(features):
        row, col = i // 3, i % 3
        with st.container():
            if i % 3 == 0:
                cols = st.columns(3)
            inputs[feature] = cols[col].text_input(feature)
    data_features = {
        'Vsl' : inputs[features[0]],
        'Vsg' : inputs[features[1]],
        'VisL' : inputs[features[2]],
        'VisG' : inputs[features[3]],
        'DenL': inputs[features[4]],
        'DenG' : inputs[features[5]],
        'ST' : inputs[features[6]],
        'Ang' : inputs[features[7]],
        'ID' : inputs[features[8]]
        }
    features_df = pd.DataFrame(data_features, index = [0])
    return features_df


df = user_input_parameters()
###########################################################
###########################################################
st.subheader("Modelo RF ")

# Crear un nuevo DataFrame con una fila adicional 'Valor'
df = df.T.reset_index()
df.columns = ['Característica', 'Valor']
df = df.set_index('Característica').T

st.table(df)

# Crear dos botones 'PREDECIR'
predict_button, clear_button = st.columns(2)
predict_clicked = predict_button.button('PREDECIR')
prediction = ''
if predict_clicked:
# Validar que todos los campos contengan valores numéricos
    for value in df.values.flatten():
        if not value or not value.isdigit():
            st.warning("Por favor, complete todos los datos con valores numéricos antes de hacer la predicción.")
            break
        else:
            #prediction = modelo.predict(df)
            prediction = solicitud_API(df.values.flatten().tolist())

    # Crear un diccionario para asociar las predicciones con sus descripciones
    prediction_descriptions = {
        'DB': 'Flujo de burbujas dispersas (DB)',
        'SS': 'Flujo estratificado uniforme (SS)',
        'SW': 'Flujo estratificado ondulado (SW)',
        'A': 'Flujo anular (A)',
        'I': 'Flujo intermitente (I)',
        'B': 'Flujo de burbujas (B)',

    }

    # Mostrar la descripción completa de la predicción
    st.success(prediction_descriptions[prediction[0]])

    if prediction[0] in ["I", "A"]:
        st.warning("Alerta: Presta atención a posibles fallos en la tubería.")