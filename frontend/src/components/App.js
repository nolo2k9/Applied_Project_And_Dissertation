import React, {useState, useEffect} from 'react';
import logo from '../assets/df1.png';

function App() {
  const [walletInfo, setWalletInfo] = useState({});

  useEffect(() => {
    fetch('http://localhost:5000/wallet/info')
    .then( res => res.json())
    .then(json => setWalletInfo(json));

  },[]);

  const {address, balance} = walletInfo;
  return (
    <div className="App">
      
      <img className="logo" src = {logo} alt = "nan"/>
      <h3>Welcome to the Delta Coin Network</h3>
      <b/>
      <div className="WalletInfo">
        <div>Address: {address}</div>
        <div>Balance: {balance}</div>
      </div>
    </div>
  );
}

export default App;
