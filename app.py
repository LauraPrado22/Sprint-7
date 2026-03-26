

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Mi Análisis de Datos con Streamlit y Plotly")

# Crear un dataframe de ejemplo
df = pd.DataFrame({
    "Categoría": ["A", "B", "C", "D"],
    "Valores": [10, 20, 30, 40]
})

# Mostrar la tabla
st.write("Tabla de datos:")
st.dataframe(df)

# Crear un gráfico de barras
fig = px.bar(df, x="Categoría", y="Valores", title="Gráfico de ejemplo")
st.plotly_chart(fig)

print(df)