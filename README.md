# AI Image Captioning Web App (BLIP + Gradio)

This project implements an AI-powered image captioning system that generates meaningful, context-aware natural-language descriptions for images. It leverages the **BLIP (Bootstrapping Language-Image Pretraining)** vision–language transformer from Hugging Face and provides an interactive web interface using **Gradio** for real-time inference.

---

## 🔍 Project Overview

Image captioning is a multimodal deep learning task that combines **computer vision** and **natural language processing (NLP)**. In this project, a pretrained BLIP model encodes visual features from an input image and performs conditional text generation to produce human-like captions. The application is designed to be simple, interactive, and suitable for real-world use cases such as accessibility, media automation, and content management.

---

## 🚀 Features

- AI-based image-to-text caption generation
- Multimodal learning using vision–language transformers
- Real-time image upload and caption inference
- Interactive web interface built with Gradio
- Clean and modular Python implementation

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Deep Learning Framework:** PyTorch  
- **Model:** BLIP (Bootstrapping Language-Image Pretraining)  
- **Libraries:** Hugging Face Transformers, Gradio, Pillow, NumPy  

---

## 📂 Project Structure

ai-image-captioning-blip/
    ├── image_captioning_app.py   # Main Gradio-based web application
    ├── image_cap.py              # Standalone script for image caption generation
    ├── hello.py                  # Gradio quickstart demo
    ├── requirements.txt          # List of required dependencies
    ├── images.jpg                # Sample image for testing (optional)
    └── README.md                 # Project documentation

---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/VaibhavUNavalagi/ai-image-captioning-blip.git
   cd ai-image-captioning-blip

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Running the Application
   Launch the Gradio web app using:
   ```bash
   python image_captioning_app.py

👤 Author

Vaibhav U Navalagi
