import React from 'react';
import AccountDetails from './components/AccountDetails';
import Transactions from './components/Transactions';
import Analytics from './components/Analytics';

function App() {
  return (
    <div>
      <h1>Banking App</h1>
      <AccountDetails />
      <Transactions />
      <Analytics />
    </div>
  );
}

export default App;

