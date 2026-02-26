import streamlit as st
from PIL import Image

st.title("BANANA ROTATE")

st.header("RETURN TO MONKEY")
st.write("Donkey kong")
image = Image.open("banana.png")
st.image(image, caption= "Banana") 


texto = st.text_input("write name", "")
st.write("Your monkey name is ", texto)


st.subheader("Monkey divide")

coll, col2 = st.columns(2)

with coll:
  st.subheader("Monkey team 1")
  st.write("Donkey Kong")
  image2 = Image.open("DK.png")
  st.image(image2, caption= "DK") 
  resp  = st.checkbox("TEAM DK")
  if resp:
    st.write("OK!")


with col2:
  st.subheader("Monkey team 2")
  st.write("Diddy Kong")
  image2 = Image.open("DD.png")
  st.image(image2, caption= "DD") 
  modo = st.radio("Why Diddy is better",("LOOKS","CAP","GUN"))
  if modo == "LOOKS":
    st.write("HELL YEAH")
  if modo == "CAP":
    st.write("STOP THE CAP")
  if modo == "GUN":
    st.write("🦅")


st.subheader("Return to monkey button")
if st.button("MONKEY"):
  st.write("OK!")
else:
  st.write("IM WAITING")
  
