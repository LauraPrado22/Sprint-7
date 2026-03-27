

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Leer los datos del archivo CSV (ruta completa corregida)
car_data = pd.read_csv(r"C:\Users\laurap10\OneDrive - kochind.com\Documents\Laura's Folder\Project\Python\vehicles_us.csv")

# Crear un histograma utilizando plotly.graph_objects
fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

# Añadir título al gráfico
fig.update_layout(title_text='Distribución del Odómetro')

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)
