import React, { useState, useEffect } from 'react'
import { BASE_URL } from '../config'
/*
    Fetch blockchain data
*/
function Blockchain() {
  const [blockchain, setBlockchain] = useState([])

  useEffect(() => {
    //Fetch Endpoint
    fetch(`${BASE_URL}/blockchain`)
      .then((res) => res.json())
      .then((json) => setBlockchain(json))
  }, [])

  return (
    <div className="Blockchain">
      <h3>Blockchain</h3>
      <div>
        {blockchain.map((block) => (
          <div key={block.hash}>{JSON.stringify(block)}</div>
        ))}
      </div>
    </div>
  )
}

export default Blockchain;
