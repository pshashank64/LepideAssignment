# Document Summarization Web Application

## Overview

This project provides a web application that allows users to upload text documents(.txt) and receive summarized versions using a locally deployed Language Model. The application consists of a backend implemented in .NET, a frontend built with React, and a Python script utilizing a pre-trained language model for summarization(GPT-2).

## Project Structure

- **Backend**: Implemented in .NET 8.0.
- **Frontend**: Implemented in React.
- **Python Script**: Uses GPT-2 for generating summaries.

## Getting Started

### Prerequisites

1. **Python 3.8+** with `transformers` and `torch` libraries.
2. **.NET 8.0 SDK** for backend development.
3. **Node.js 16+** for React frontend development.

### 1. Setting Up the Python Environment

1. **Create a Virtual Environment**:

    ```bash
    python -m venv venv
    ```

2. **Activate the Virtual Environment**:

    - **Windows**:

      ```bash
      venv\Scripts\activate
      ```

3. **Install Required Packages**:

    ```bash
    pip install transformers torch
    ```

4. **Download the Pre-trained Model**:

   Ensure you have the GPT-2 model stored in the directory specified in your Python script (`E:/lepide software/models/gpt-2`) if not then create the model using the models file in models directory.

### 2. Setting Up the .NET Backend

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/pshashank64/LepideAssignment.git
    cd backend
    ```

2. **Restore Dependencies**:

    ```bash
    dotnet restore
    ```

3. **Run the Application**:

    ```bash
    dotnet run
    make sure to run the server on http (not in https or IIS Server)
    ```

   The backend server will be available at `http://localhost:5043`.

### 3. Setting Up the React Frontend

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/pshashank64/LepideAssignment.git
    cd frontend
    ```

2. **Install Dependencies**:

    ```bash
    npm install
    ```

3. **Start the Development Server**:

    ```bash
    npm start
    ```

   The frontend application will be available at `http://localhost:3000`.

### 4. Running the Python Script

1. **Save the Python Script** to a file, e.g., `summarize.py`.

2. **Run the Script**:

    ```bash
    python summarize.py path/to/your/document.txt
    ```

   Ensure you provide the correct path to your document

    ```bash
    python summarize.py path/to/your/document.txt
    ```

## Usage

1. **Upload a Document**:
   - Open the React application in your browser (`http://localhost:3000`).
   - Use the file input to select and upload a document.

2. **Receive a Summary**:
   - After uploading, the React frontend will send the file to the .NET backend.
   - The backend will then call the Python script to generate a summary.
   - The summary will be displayed in the frontend.

## Troubleshooting

- **CORS Issues**:
  Ensure the backend is configured to allow requests from the frontend domain. Check CORS policies and headers in the backend configuration.

- **Python Dependencies**:
  Verify that all required Python packages are installed and compatible with your environment.

- **Model Loading Errors**:
  Ensure the GPT-2 model is correctly downloaded and accessible at the specified path.

- **File Upload Errors**:
  Ensure that the file you are uploading is in a supported format(.txt) and does not exceed size limits set by your server configuration.

## References

- **Transformers and Torch**:
  https://pytorch.org/hub/huggingface_pytorch-transformers/
  
- **OpenAI GPT-2 Model for Summarizer**:
  https://huggingface.co/docs/transformers/en/model_doc/gpt2

- **React-spinners for loading purpose till the time model generates the summary**:
  https://www.npmjs.com/package/react-spinners

## Contributing

Feel free to fork the repository and submit pull requests. For any issues or feature requests, open an issue in the GitHub repository.
