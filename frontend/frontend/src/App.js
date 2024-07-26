import React, { useRef, useState } from 'react';
import { ClipLoader } from 'react-spinners';
import axios from 'axios';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState('');
  const [content, setContent] = useState('');
  const [loading, setLoading] = useState(false);
  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile);

    const reader = new FileReader();
    reader.onload = (event) => {
      setContent(event.target.result);
    };
    reader.readAsText(selectedFile);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);
    setLoading(true);

    try {
      const response = await axios.post('http://localhost:5043/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });      
      setSummary(response.data.summary);
    } catch (error) {
      console.error('Error uploading file:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleClear = async (e) => {
    e.preventDefault();
    setFile(null);
    setContent('');
    setSummary('');
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
          <ClipLoader color="#ffffff" loading={loading} size={150} />
        ) : (
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