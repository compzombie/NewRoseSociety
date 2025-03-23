import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../styles/Home.css';
import Header from '../components/Header';

function Home() {
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch data from the backend API
    axios.get('/api')
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
    <Header /> 
  );
}

export default Home;
