import gradio as gr
from PIL import Image
from rembg import remove as rembg_remove
import io
import numpy as np

def remove_background(input_image):
    img = Image.fromarray(input_image.astype('uint8'), 'RGB')
    img = rembg_remove(img)
    img_np = np.array(img)
    return img_np

iface = gr.Interface(
    fn=remove_background,
    inputs="image",
    outputs="image",
    title="Background Removal",
    description="Remove background from an image."
)

iface.launch(share=True)
