# AI Image Classifier

## Overview

This repository contains a simple yet powerful AI Image Classifier built using Streamlit for the user interface and TensorFlow/Keras with the MobileNetV2 model for image classification. It allows users to upload an image and receive instant predictions about its content.

## Features

*   **User-Friendly Interface**: Built with Streamlit for an intuitive and interactive web experience.
*   **Deep Learning Powered**: Leverages the pre-trained MobileNetV2 model from TensorFlow/Keras, known for its efficiency and accuracy in image recognition tasks.
*   **Real-time Classification**: Upload an image and get classification results almost instantly.
*   **Top 3 Predictions**: Displays the top 3 most likely classifications along with their confidence scores.

## How it Works

1.  **Image Upload**: Users upload an image file (JPG or PNG) through the Streamlit interface.
2.  **Preprocessing**: The uploaded image is resized to 224x224 pixels and preprocessed according to MobileNetV2's requirements.
3.  **Inference**: The pre-trained MobileNetV2 model predicts the classes present in the image.
4.  **Display Results**: The application decodes the predictions and displays the top 3 labels with their corresponding confidence percentages.

## Getting Started

### Prerequisites

*   Python 3.7+
*   [`uv`](https://uv.astral.sh/): A fast Python package installer and virtual environment manager.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone git@github.com:Fidelek84/agentic_ai.git
    cd ai-image-classifier
    ```

2.  **Create a virtual environment and install dependencies with `uv`:**

    ```bash
    uv venv # Creates a .venv virtual environment
    source .venv/bin/activate # Activate the environment (macOS/Linux)
    # Or for Windows PowerShell: .\.venv\Scripts\activate
    
    uv pip install "opencv-python" "numpy" "streamlit" "tensorflow" "Pillow"
    ```
    *Note: TensorFlow can be complex. Refer to the official TensorFlow documentation if you encounter specific GPU/system setup issues that `uv` can't resolve automatically.*

### Running the Application

1.  **Ensure your virtual environment is active:**

    ```bash
    source .venv/bin/activate # macOS/Linux
    # Or for Windows PowerShell: .\.venv\Scripts\activate
    ```

2.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

3.  Your web browser will automatically open to the Streamlit app (usually `http://localhost:8501`).

## Usage

1.  Once the application is running, you will see "AI Image Classifier" in your browser.
2.  Click the "Choose an image..." button to upload a `.jpg` or `.png` file from your computer.
3.  After the image is displayed, click the "Classify Image" button.
4.  The application will process the image, and the top 3 predictions with their confidence scores will appear under the "Predictions" section.

## Model Details

The application uses `MobileNetV2` from `tensorflow.keras.applications`. This model is pre-trained on the ImageNet dataset, which contains millions of images across 1000 categories.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.