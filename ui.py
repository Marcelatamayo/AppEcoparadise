import streamlit as st
from PIL import Image

def glamping_tres_elementos():
    st.title('GLAMPING TRES ELEMENTOS')
    st.write("Bienvenidos a Ecoparadise")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
        with image_column:
            image = Image.open("assets/gte.jpeg")
            st.image(image, use_column_width=True)
        with text_column:
            st.subheader("Glamping Tres Elementos")
            st.write('Aquí que incluye y en qué consiste el alojamiento')

def Alpes():
    st.title('GLAMPING LOS ALPES')
    st.write("Bienvenidos a Ecoparadise")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
        with image_column:
            image = Image.open("assets/alpes.jpeg")
            st.image(image, use_column_width=True)
        with text_column:
            st.subheader("Glamping Los Alpes")
            st.write('Aquí que incluye y en qué consiste el alojamiento')

def cabaña():
    st.title('CABAÑA COLORES')
    st.write("Bienvenidos a Ecoparadise")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
        with image_column:
            image = Image.open("assets/cabaña.jpeg")
            st.image(image, use_column_width=True)
        with text_column:
            st.subheader("Cabaña Colores")
            st.write('Aquí que incluye y en qué consiste el alojamiento')
def iniciar_sesion():
    st.title('INICIAR SESIÓN')
    usuario = st.text_input("Ingrese su nombre de usuario")
    contraseña = st.text_input("Ingrese su contraseña",type="password")
    '''if st.button ("INGRESAR"):
        if usuario == "marcela" and contraseña == "camilo":
            st.success(f"Bienvenido {usuario} ")
        else:
            st.error("Usuario o contraseña incorrectos")'''