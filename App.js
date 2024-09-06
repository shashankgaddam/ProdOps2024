import React, { useState } from 'react';
import './App.css';
import FeatureDashboard from '../FeatureDashboard';
import TranscribeFeature from '../TranscribeFeature';

function TranscriptUploader() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleFileUpload = () => {
    if (selectedFile) {
      console.log('Uploading file:', selectedFile.name);
    } else {
      console.log('No file selected');
    }
  };

  return (
    <div id="upload-section" className="subsection">
      <h2>Upload Transcript</h2>
      <div className="upload-controls">
        <input type="file" id="fileInput" onChange={handleFileChange} hidden />
        <label htmlFor="fileInput" className="styled-button">Choose File</label>
        <button className="styled-button" onClick={handleFileUpload}>Upload</button>
      </div>
      {selectedFile && <p className="file-info">Selected File: {selectedFile.name}</p>}
      <div id="insights-box">
        <h3>Insights</h3>
        <textarea
          value="Your insights will appear here after the file is processed."
          readOnly
        />
      </div>
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <header className="app-header">
        <h1>ProdOps AI – Transcript Analysis</h1>
      </header>
      <div className="container">
        <main className="main-content">
          <div className="combined-box">
            <TranscriptUploader />
            <TranscribeFeature />
          </div>
          <FeatureDashboard />
        </main>
      </div>
      <footer className="app-footer">
        <p>© 2024 ProdOps AI</p>
      </footer>
    </div>
  );
}

export default App;
