import streamlit as st
from PIL import Image

st.title("BANANA ROTATE")

st.header("RETURN TO MONKEY")
st.write("Donkey kong")
image = Image.open("banana.gif")
st.image(image, caption= "Banana") 
