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

<p align="center">
   <img width="700" height="400" alt="Image" src="https://github.com/user-attachments/assets/186e7fb8-4c5d-42d2-95ba-777a6aa3f64b" />
</p>

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Deep Learning Framework:** PyTorch  
- **Model:** BLIP (Bootstrapping Language-Image Pretraining)  
- **Libraries:** Hugging Face Transformers, Gradio, Pillow, NumPy  

---

## 📂 Project Structure

```text
ai-image-captioning-blip/
├── image_captioning_app.py   # Main Gradio-based web application
├── image_cap.py              # Standalone script for image caption generation
├── hello.py                  # Gradio quickstart demo
├── requirements.txt          # List of required dependencies
├── images.jpg                # Sample image for testing (optional)
└── README.md                 # Project documentation
```

---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/VaibhavUNavalagi/ai-image-captioning-blip.git
   cd ai-image-captioning-blip

2. Set up your virtual environment:
   ```bash
   pip3 install virtualenv
   virtualenv my_env 
   source my_env/bin/activate 

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Running the Application
   Launch the Gradio web app using:
   ```bash
   python image_captioning_app.py
   
---

## ⚙️ Results & Demonstration

The following examples showcase the performance of the AI-powered image captioning system. The BLIP vision–language model successfully interprets visual content and generates meaningful, context-aware natural-language descriptions in real time through the Gradio web interface.

---

### 🖼️ Example 1: Text-based Visual Understanding

This example demonstrates the model’s ability to recognize objects and read visible text within an image. The system correctly identifies the scene and generates a descriptive caption capturing both the object type and the textual content.

<img width="1919" height="1014" alt="Image Captioning Output - Example 1" src="https://github.com/user-attachments/assets/d6660623-798d-4dc2-84ca-af15592817b9" />

---

### 🖼️ Example 2: Complex Scene Interpretation

In this example, the model analyzes a dynamic and visually complex scene. It extracts key entities, actions, and contextual details to generate a concise natural-language description, highlighting the model’s capability in real-world visual understanding scenarios.

<img width="1919" height="1018" alt="Image" src="https://github.com/user-attachments/assets/20382263-643b-48ab-aaf9-7e479e098f11" />

---

📌 *These results demonstrate the effectiveness of multimodal deep learning by combining computer vision and natural language processing to generate human-like image descriptions.*

---



👤 Author

Vaibhav U Navalagi
