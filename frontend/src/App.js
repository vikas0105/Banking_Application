import React, { useState } from 'react';
import Home from './components/Home';
import About from './components/About';

const App = () => {
  const [currentPage, setCurrentPage] = useState('home');

  const handleNavigation = (page) => {
    setCurrentPage(page);
  };

  return (
    <div>
      <nav>
        <button onClick={() => handleNavigation('home')}>Home</button>
        <button onClick={() => handleNavigation('about')}>About</button>
      </nav>

      <div>
        {currentPage === 'home' && <Home />}
        {currentPage === 'about' && <About />}
      </div>
    </div>
  );
};

export default App;

