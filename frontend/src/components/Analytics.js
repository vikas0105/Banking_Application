import React, { useState, useEffect } from 'react';

function Analytics() {
  const [report, setReport] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5006/analytics/report')
      .then(response => response.json())
      .then(data => setReport(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Analytics</h2>
      {report ? (
        <div>
          <p>Total Transactions: {report.total_transactions}</p>
          <p>Total Credits: ${report.total_credits}</p>
          <p>Total Debits: ${report.total_debits}</p>
          <p>Net Balance: ${report.net_balance}</p>
        </div>
      ) : (
        <p>Loading analytics...</p>
      )}
    </div>
  );
}

export default Analytics;

