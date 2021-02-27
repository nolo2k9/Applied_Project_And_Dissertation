import React, {useState, useEffect} from 'react';
import {Link} from 'react-router-dom';
import logo from '../assets/df1.png';
import {BASE_URL} from '../config';

function App() {
  const [walletInfo, setWalletInfo] = useState({});

  useEffect(() => {
    fetch(`${BASE_URL}/wallet/info`)
    .then( res => res.json())
    .then(json => setWalletInfo(json));

  },[]);

  const {address, balance} = walletInfo;
  return (
    <div className="App">
      
      <img className="logo" src = {logo} alt = "nan"/>
      <h3>Welcome to the Delta Coin Network</h3>
      <br/>
      <Link to="/blockchain">Blockchain</Link>
      <Link to="/conduct-transaction">Make a Transaction</Link>
      <br/>
      <div className="WalletInfo">
        <div>Your Wallet Address: {address}</div>
        <div>Your Current Balance: {balance}</div>
      </div>
    </div>
  );
}

export default App;
