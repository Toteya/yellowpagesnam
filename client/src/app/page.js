"use client";

import './components/App.module.css';
import Header from './components/Header';
import Nav from './components/Nav';
import Content from './components/Content';
import { useEffect, useState } from 'react';

export default function Home() {
  const [listings, setListings] = useState([]);
  const [fetchError, setFetchError] = useState(null);
  const [viewContent, setViewContent] = useState('Select a business to see more information about it.');

  useEffect(() => {
    const fetchListings = async () => {
      try {
        const response = await fetch('http://localhost:5001/api/v1/listings');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setListings(data);
        setFetchError(null);
      } catch (error) {
        setFetchError('Failed to fetch data. Please try again later.');
        console.error('Error fetching listings:', error);
      }
    }

    fetchListings();
    
  }, []);

  return (
    <div className="App">
      <Header />
      <Nav />
      <main>
        {fetchError && <p style={{color: 'red'}}>{fetchError}</p>}
        {!fetchError && (
          <Content
            listings={listings}
            viewContent={viewContent}
            setViewContent={setViewContent}
          />
        )}
      </main>
    </div>
  );
}
