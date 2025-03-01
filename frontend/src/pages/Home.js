import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../styles/Home.css';

function Home() {
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch data from the backend API
    axios.get('http://localhost:8000/')
      .then(response => {
        setMessage(response.data.message);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        setMessage('Failed to connect to the server');
        setLoading(false);
      });
  }, []);

  return (
    <div className="home">
      <div className="hero">
        <h1>Welcome to New Rose Society</h1>
        <p className="subtitle">Celebrating beauty and innovation</p>
      </div>
      
      <div className="content-section">
        <h2>Our Mission</h2>
        <p>The New Rose Society is dedicated to exploring new ideas and fostering creativity across disciplines.</p>
        
        <div className="api-message">
          {loading ? (
            <p>Loading message from API...</p>
          ) : (
            <p>Message from API: {message}</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default Home;
