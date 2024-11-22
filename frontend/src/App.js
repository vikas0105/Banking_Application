import React, { useState } from 'react';
import Home from './components/Home';
import About from './components/About';
import AccountDetails from './components/AccountDetails';
import Analytics from './components/Analytics';

const App = () => {
  const [currentPage, setCurrentPage] = useState('home'); // Track current page for navigation

  // Function to handle navigation between pages
  const handleNavigation = (page) => {
    setCurrentPage(page);
  };

  return (
    <div>
      <nav>
        <button onClick={() => handleNavigation('home')}>Home</button>
        <button onClick={() => handleNavigation('about')}>About</button>
        <button onClick={() => handleNavigation('account')}>Account Details</button>
        <button onClick={() => handleNavigation('analytics')}>Analytics</button>
      </nav>

      <div>
        {/* Conditional rendering based on the currentPage */}
        {currentPage === 'home' && <Home />}
        {currentPage === 'about' && <About />}
        {currentPage === 'account' && <AccountDetails />}
        {currentPage === 'analytics' && <Analytics />}
      </div>
    </div>
  );
};

export default App;

