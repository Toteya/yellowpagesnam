import './App.css';
import Header from './Header';
import Nav from './Nav';
import { Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Header />
      <Nav />
      <Routes>
        <Route path="/" element={<h2>Welcome to the Business Directory Namibia</h2>} />
      </Routes>
    </div>
  );
}

export default App;
