import pandas as pd
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


email_contact = "marcelatamayo53@gmail.com"
def pagina_principal():

    #st.set_page_config(page_title="Eco", page_icon="🌿", layout="wide")
    st.write("Bienvenidos a Ecoparadise")
    st.write('usa el menú de la izquierda para navegar')
    


# Función para cargar el CSS en la página web
def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

css_load("style/main.css")  # Cargar el archivo CSS desde la ruta especificada

url = "https://lottie.host/54c476fd-523a-429c-bf77-4b2f1aac725a/xKdKPZxKGJ.json"

# Función para cargar la animación Lottie
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Cargar la animación Lottie en la página web
lottie = load_lottie(url)

def nosotros():
# Sección "Somos Ecoparadise"
    with st.container():
        st.header("Somos Ecoparadise 👋")
        st.title("¡Sueña, explora y descubre!")
        st.write(
        "Somos un hotel ecológico, apasionados por la naturaleza y rodeados de ambientes llenos de tranquilidad y paz. Ubicados en el corregimiento de La Marina, a 20 minutos de Tuluá, Valle del Cauca."
        )

# Sección "Sobre nosotros"
    with st.container():
        st.write("---")
        text_column, animation_column = st.columns(2)
        with text_column:
            st.header("Sobre nosotros 🔍")
            st.write(
            """
            Hola 👋 Encontraste el lugar que estabas buscando...
            Ecoparadise es un conjunto de emociones inolvidables.
            Permítenos hacer realidad la noche de tus sueños... Te estamos esperando ♥
            ¿En qué alojamiento deseas soñar? Tenemos varias opciones para ti. 💬📲
            """
        )
        with animation_column:
            st_lottie(lottie, height=400)
    contacto()

# contacto
def contacto():
    with st.container():
        st.write("---")
        st.header("Ponte en contacto con nosotros!")
        st.write("##")
        contact_form = f"""
        <form action="https://formsubmit.co/{email_contact}" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Tu nombre" required>
            <input type="email" name="email" placeholder="Tu email" required>
            <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
            <button type="submit">Enviar</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
        





def glamping_tres_elementos():

    st.title('GLAMPING TRES ELEMENTOS')
    st.write("Bienvenidos a Ecoparadise")
    st.write('usa el menú de la izquierda para navegar')

    with st.container():
        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            image = Image.open("assets/gte.jpeg")
            st.image(image, use_column_width=True)
        with text_column:
            st.subheader("Glamping Tres Elementos")
            st.write(
            'Aqui que incluye y en que consiste el alojamiento'
        )
            
def Alpes():

    st.title('GLAMPING LOS ALPES')
    st.write("Bienvenidos a Ecoparadise")
    st.write('usa el menú de la izquierda para navegar')

    with st.container():
        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            image = Image.open("assets/alpes.jpeg")
            st.image(image, use_column_width=True)
        with text_column:
            st.subheader("Glamping Los Alpes")

            st.write(

             'Aqui que incluye y en que consiste el alojamiento'
           
        )

def cabaña():

    st.title('CABAÑA COLORES')
    st.write("Bienvenidos a Ecoparadise")
    st.write('usa el menú de la izquierda para navegar')
    with st.container():
        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            image = Image.open("assets/cabaña.jpeg")
            st.image(image, use_column_width=True)
        with text_column:
            st.subheader("Cabaña Colores")
            st.write(
            'Aqui que incluye y en que consiste el alojamiento'
        )


def sidebar():
    st.sidebar.title('Menu de navegación')
    pagina = st.sidebar.selectbox('Selecciona una página', ['pagina principal',
                                                            'glamping tres elementos', 
                                                            'glamping los alpes', 
                                                            'cabaña colores'])

    if pagina == 'pagina principal':
        pagina_principal()
        nosotros()

    elif pagina =='glamping tres elementos':
        glamping_tres_elementos()
    elif pagina =='glamping los alpes':
        Alpes()
    elif pagina =='cabaña colores':
        cabaña()

sidebar()


