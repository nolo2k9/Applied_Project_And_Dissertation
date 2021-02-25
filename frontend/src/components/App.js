import React, {useState, useEffect} from 'react';
import logo from '../assets/df1.png';
import {BASE_URL} from '../config';
import Blockchain from './Blockchain';

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
      <b/>
      <div className="WalletInfo">
        <div>Your Wallet Address: {address}</div>
        <div>Your currenct Balance: {balance}</div>
      </div>
      <br/>
      <Blockchain />
    </div>
  );
}

export default App;
