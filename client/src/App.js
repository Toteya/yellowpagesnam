import './App.css';
import { Route, Routes } from 'react-router-dom';
import Header from './Header';
import Nav from './Nav';
import Content from './Content';
import { useEffect, useState } from 'react';

function App() {
  const [listings, setListings] = useState([]);
  const [fetchError, setFetchError] = useState(null);

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
      <Routes>
        <Route path="/" element={
          <>
            {fetchError && <p style={{color: 'red'}}>{fetchError}</p>}
            {!fetchError && <Content listings={listings} />}
          </>
        }/>
      </Routes>
    </div>
  );
}

export default App;
