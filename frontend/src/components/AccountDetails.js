import React, { useState, useEffect } from 'react';

function AccountDetails() {
  const [accounts, setAccounts] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5002/accounts')
      .then(response => response.json())
      .then(data => setAccounts(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Accounts</h2>
      <ul>
        {accounts.map(account => (
          <li key={account.id}>
            {account.name} - ${account.balance}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default AccountDetails;

