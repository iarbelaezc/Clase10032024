import streamlit as st
from PIL import Image 

st.title(" Aplicación para ciudades inteligentes")

st.header( "En este espacio podrás obtener información de tu ciudad.")

image= Image.open ('1540.jpg')
st.image(image,caption= 'Inteligencia Urbana')
