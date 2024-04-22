import streamlit as st
from PIL import Image
from rembg import remove as rembg_remove
import numpy as np
import io

def remove_background(input_image):
    img = Image.open(input_image)
    img = rembg_remove(img)
    img_np = np.array(img)
    return img_np
st.sidebar.image("example.png", use_column_width=True)
st.sidebar.title("Developer Contact")
st.sidebar.info(
        """
        
        **Email:** mustafaansari@mail.com  
    **LinkedIn:** [LinkedIn/mustafaansaari/](https://www.linkedin.com/in/mustafaansaari/)  
    **GitHub:** [github/mustafaansaari/](https://github.com/mustafaansarii)  
        """
    )



st.title("Background Removal")
st.write("Remove background from an image.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the original image
    original_image = Image.open(uploaded_file)

    # Display input and output images side by side
    col1, col2 = st.columns(2)
    with col1:
        st.image(original_image, caption='Original Image', use_column_width=True)
    with col2:
        processed_image = remove_background(uploaded_file)
        st.image(processed_image, caption='Processed Image', use_column_width=True)

    # Convert processed image to bytes
    processed_image_bytes = io.BytesIO()
    Image.fromarray(processed_image).save(processed_image_bytes, format='PNG')
    processed_image_bytes = processed_image_bytes.getvalue()

    # Provide download button
    st.download_button(
        label="Download Processed Image",
        data=processed_image_bytes,
        file_name='processed_image.png',
        mime='image/png'
    )
