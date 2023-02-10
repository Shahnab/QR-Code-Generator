import numpy as np
import streamlit as st
import PIL
from PIL import Image
import qrcode

# st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Dentsu-logo_black.svg/2560px-Dentsu-logo_black.svg.png', width=250)
st.title("QR code Generator")
st.caption ("Upload link | text to be encoded in image to generate QR-Code")
text = st.text_input('Enter the Text | Links')


click = st.button("Generate")


if click:

    # st.write(text)

    img = qrcode.make(text)
    image = img.save("QR.png")
    output = Image.open("QR.png")
    st.image(output)
