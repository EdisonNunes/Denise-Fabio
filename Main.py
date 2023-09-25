import streamlit as st

from PIL import Image

st.set_page_config(page_title='Denise e Fábio)')
st.title('Aqui pode colocar um texto')
st.subheader('Escreve mais alguma coisa aqui.....')

#opening the image
image = Image.open('FabioDeniseArthur.jpg')

#displaying the image on streamlit app
st.image(image, caption='Texto para colocar a foto')
