import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear un histograma utilizando plotly.graph_objects
fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

# Añadir título al gráfico
fig.update_layout(title_text='Distribución del Odómetro')

# ✅ Mostrar el gráfico en Streamlit (NO usar fig.show())
st.plotly_chart(fig)
