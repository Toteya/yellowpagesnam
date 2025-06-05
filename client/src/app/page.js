"use client";

import './components/App.module.css';
import Header from './components/Header';
import Nav from './components/Nav';
import Content from './components/Content';
import { useEffect, useState } from 'react';
import { ImSpinner } from 'react-icons/im';

export default function Home() {
  const [listings, setListings] = useState([]);
  const [fetchError, setFetchError] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [currentListing, setCurrentListing] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    const fetchListings = async () => {
      setIsLoading(true);
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
      } finally {
        setIsLoading(false);
      }
    }

    fetchListings();
    
  }, []);

  const filteredListings = listings.filter((listing) =>
    listing.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    listing.category.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div className="App">
      <Header />
      <Nav setSearchQuery={setSearchQuery}/>
      <main>
        {isLoading && (
          <div className='flex items-center justify-center h-screen'>
            <p className='flex items-center text-gray-600'>
              <ImSpinner className="animate-spin text-3xl" />
            </p>
          </div>
        )}
        {!isLoading && fetchError && <p style={{color: 'red'}}>{fetchError}</p>}
        {!isLoading && !fetchError && (
          <Content
            listings={filteredListings}
            currentListing={currentListing}
            setCurrentListing={setCurrentListing}
          />
        )}
      </main>
    </div>
  );
}
