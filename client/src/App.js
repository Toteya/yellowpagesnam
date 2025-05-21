import './App.css';
import { Route, Routes } from 'react-router-dom';
import Header from './Header';
import Nav from './Nav';
import Content from './Content';

function App() {
  return (
    <div className="App">
      <Header />
      <Nav />
      <Routes>
        <Route path="/" element={<Content />} />
      </Routes>
    </div>
  );
}

export default App;
