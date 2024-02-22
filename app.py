import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image

st.title("Interfaces Multimodales.")
image = Image.open('mago.jpg')

st.image(image, width=200)

try:
  os.mkdir("temp")
except:
  pass

st.subheader("Texto a audio.")
st.write('Las interfaces de texto a audio son fundamentales en las interfaces multimodales ya que permite'
        'una comunicación más accesible y natural, facilitando la inclusión de personas con discapacidades')
