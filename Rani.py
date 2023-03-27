import streamlit as st
import numpy as np
from PIL import Image
st.title("Electromagnetic Waves")
st.image("electromagnetic-spectrum-diagram (1).jpg")
option = st.selectbox('selection of Rays',
('Radio','Microwaves','Infrard','Visible light','Ultraviolet','X-rays','Gamma'))
if option=="Radio":
    print('Uses=Radioastronomy')
elif option=="Microwaves":
    print("Uses=Cooking")
Image=Image.open('spectrum.PNG')
st.image('spectrum.PNG',caption ='Spectrum of light ')
st.title('The visible light spectrum')
color = st.color_picker('Pick A Color', '#00f900')
option = st.selectbox('selection of light',
('Red','Orange','Yellow','Green','Blue','Indigo','Violet'))
if option=="Red":
    Wavelength = 650
    st.write('wavelength of selected option is :',Wavelength)
    frequency = (3 * 10**8) / int(Wavelength )
    st.write('frequency of selected option is:',frequency)
elif option== 'Orange' :
    Wavelength =590
    st.write('wavelength of selected option is :',Wavelength)
    frequency = (3 * 10**8) / int(Wavelength )
    st.write('frequency of selected option is:',frequency)
elif option== 'Yellow' :
    Wavelength = 570
    st.write('wavelength of selected option is :',Wavelength)
    frequency = (3 * 10**8) / int(Wavelength )
    st.write('frequency of selected option is:',frequency)
elif option== 'Green' :
    Wavelength = 510
    st.write('wavelength of selected option is :',Wavelength)
    frequency = (3 * 10**8) / int(Wavelength )
    st.write('frequency of selected option is:',frequency)
elif option== 'Blue' :
    Wavelength = 475
    st.write('wavelength of selected option is :',Wavelength)
    frequency = (3 * 10**8) / int(Wavelength )
    st.write('frequency of selected option is:',frequency)
elif option== 'Indigo' :
    Wavelength = 445
    st.write('wavelength of selected option is :',Wavelength)
    frequency = (3 * 10**8) / int(Wavelength )
    st.write('frequency of selected option is:',frequency)
elif option== 'Violet' :
    Wavelength = 400
    st.write('wavelength of selected option is :',Wavelength )
    frequency = (3 * 10**8) / int(Wavelength )
    st.write('frequency of selected option is:',frequency )
















9





