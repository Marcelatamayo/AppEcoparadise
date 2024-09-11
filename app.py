import streamlit as st
from home_page import pagina_principal, nosotros
from ui import glamping_tres_elementos, Alpes, cabaña , iniciar_sesion
from utils import css_load

def sidebar():
    st.sidebar.title('Menu de navegación')
    pagina = st.sidebar.selectbox('Selecciona una página', ['pagina principal',
                                                            'glamping tres elementos', 
                                                            'glamping los alpes', 
                                                            'cabaña colores'])
    print(pagina)
    boton =st.sidebar.button("login")
    print(boton)
    if boton:
        pagina = 'login'
        iniciar_sesion()
      #  boton = False
    elif pagina == 'pagina principal' and boton == False:
        pagina_principal()
        nosotros()
    elif pagina == 'glamping tres elementos':
        glamping_tres_elementos()
    elif pagina == 'glamping los alpes':
        Alpes()
    elif pagina == 'cabaña colores':
        cabaña()
  
css_load("style/main.css")
sidebar()
