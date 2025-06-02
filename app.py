import streamlit as st
import pandas as pd

st.set_page_config(page_title="Buscador de Tramos", layout="centered")
st.title('🔎 Buscador de RUT - Chile ABC Tramos 2023')

# Carga de datos
@st.cache_data
def cargar_datos():
    df = pd.read_csv('Chile_ABC_Tramos2023.txt', sep=';', header=0, dtype=str)
    df.columns = ['RUT', 'Tramo']
    return df

df = cargar_datos()

# Input de búsqueda
rut_input = st.text_input("Ingresa el RUT (sin puntos, con guión, ej: 12345678-9):")

if rut_input:
    resultado = df[df['RUT'] == rut_input.strip()]
    
    if not resultado.empty:
        st.success(f"🧾 Tramo para el RUT {rut_input}: {resultado.iloc[0]['Tramo']}")
    else:
        st.error("❌ RUT no encontrado en la base de datos.")
