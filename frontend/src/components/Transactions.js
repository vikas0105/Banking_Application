import React, { useState, useEffect } from 'react';

function Transactions() {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5003/transactions')
      .then(response => response.json())
      .then(data => setTransactions(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Transactions</h2>
      <ul>
        {transactions.map(txn => (
          <li key={txn.id}>
            {txn.account}: {txn.type} ${txn.amount}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Transactions;

