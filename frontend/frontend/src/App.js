import React, { useRef, useState } from 'react';
import { ClipLoader } from 'react-spinners';
import axios from 'axios';
import './App.css';

function App() {
  // State variables to manage file, summary, content, and loading status
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState('');
  const [content, setContent] = useState('');
  const [loading, setLoading] = useState(false);
  const fileInputRef = useRef(null);

  // Handle file change event
  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile);

    // Read the file content and update the state
    const reader = new FileReader();
    reader.onload = (event) => {
      setContent(event.target.result);
    };
    reader.readAsText(selectedFile);
  };

  // Handle form submission to upload the file and get the summary
  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);
    setLoading(true);

    try {
      // Send a POST request to the server with the uploaded file
      const response = await axios.post('http://localhost:5043/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });      
      // Update the summary state with the response data
      setSummary(response.data.summary);
    } catch (error) {
      console.error('Error uploading file:', error);
    } finally {
      // Stop the loading spinner
      setLoading(false);
    }
  };

  // Handle clear button click to reset the state
  const handleClear = async (e) => {
    e.preventDefault();
    setFile(null);
    setContent('');
    setSummary('');
    // Reset the file input field
    if (fileInputRef.current) {
      fileInputRef.current.value = null;
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Document Summarizer</h1>
        <form onSubmit={handleSubmit}>
          <label className="custom-file-input">
            Choose File
            <input type="file" ref={fileInputRef} onChange={handleFileChange} />
          </label>
          <button type="submit">Upload and Summarize</button>
          <button type="button" onClick={handleClear}>Clear</button>
        </form>
        {content && (
          <div className="file-content">
            <h2>Uploaded File Content:</h2>
            <pre>{content}</pre>
          </div>
        )}
        {loading ? (
          // Display loading spinner while waiting for the summary
          <ClipLoader color="#ffffff" loading={loading} size={150} />
        ) : (
          // Display the summary once it is available
          summary && (
            <div className="summary">
              <h2>Summary:</h2>
              <p>{summary}</p>
            </div>
          )
        )}
      </header>
    </div>
  );
}

export default App;
