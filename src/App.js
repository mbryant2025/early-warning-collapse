import React, { useState } from 'react';
import './App.css';

function App() {

  const[ledState, setLedState] = useState(0);

  const handleLEDToggle = () => {
    setLedState(!ledState ? 1 : 0);
    fetch('/led', { method: 'PUT', body: ledState ? '0' : '1' })
      .then(response => response.text())
      .then(console.log(ledState));
  }
 
  return (
    <div className="App">
      <button type="button" onClick={handleLEDToggle}>Toggle LED</button>
      <p>State of LED: {ledState}</p>
    </div>
  );
}

export default App;
