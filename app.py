import streamlit as st
from PIL import Image

st.title("BANANA ROTATE")

st.header("RETURN TO MONKEY")
st.write("Donkey kong")
image = Image.open("banana.png")
st.image(image, caption= "Banana") 


texto = st.text_input("write name", "")
st.write("Your monkey name is ", texto)
