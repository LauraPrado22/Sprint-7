import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal
st.header('Análisis de Vehículos en Venta en EE.UU.')
st.write('Explora los datos de anuncios de venta de coches usando los gráficos interactivos a continuación.')


# histograma
build_histogram = st.checkbox('Construir un histograma del odómetro')

if build_histogram:
    st.write('Histograma de la distribución del odómetro')
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión (precio vs odómetro)')

if build_scatter:
    st.write('Gráfico de dispersión: Precio vs Odómetro')
    fig_scatter = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Precio vs Odómetro',
        labels={'odometer': 'Odómetro (millas)', 'price': 'Precio (USD)'},
        opacity=0.5
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
