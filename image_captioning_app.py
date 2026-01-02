import gradio as gr
import numpy as np
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
model.eval()

def caption_image(input_image: np.ndarray):
    # Convert numpy array to PIL Image and RGB
    raw_image = Image.fromarray(input_image).convert("RGB")

    # Process image
    inputs = processor(images=raw_image, return_tensors="pt")

    # Generate caption
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=50)

    # Decode caption
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption

# Create Gradio interface
iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(),
    outputs="text",
    title="Image Captioning",
    description="Turn images into words — an AI-driven web app that describes visual content using advanced vision–language intelligence."
)

# Launch app
iface.launch(share=True)
