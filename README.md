# Invoice Reader using Gen AI

This project demonstrates an **Invoice Reader** application that uses **Generative AI** (Google Gemini) to extract and analyze information from invoices. The application is built with `Streamlit` and processes uploaded invoice images to provide intelligent insights based on the image contents.

## Features

- Upload invoice images in `jpg`, `jpeg`, or `png` formats.
- Generates content and answers questions about the uploaded invoice using Google Gemini's AI model.
- Interactive UI built with Streamlit for ease of use.

## How It Works

1. The app takes an invoice image as input via a file uploader.
2. It sends the image and a prompt to Google Gemini's generative model for processing.
3. The AI analyzes the invoice and provides intelligent responses based on user queries.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/invoice-reader-gen-ai.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd invoice-reader-gen-ai
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up environment variables:
   - Create a `.env` file in the root directory of the project.
   - Add your Google Generative AI API key:
     ```
     generative_api_key=YOUR_API_KEY
     ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open the app in your browser, upload an invoice image, and ask questions about the invoice to get responses from the AI model.

## Dependencies

- `langchain`
- `streamlit`
- `google-generativeai`
- `chromadb`
- `python-dotenv`
- `pyPDF2`

Ensure you have all dependencies installed by running `pip install -r requirements.txt`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
