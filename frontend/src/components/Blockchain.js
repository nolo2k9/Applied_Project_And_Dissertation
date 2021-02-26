import React, { useState, useEffect } from 'react'
import { Button } from 'react-bootstrap'
import { BASE_URL } from '../config'
import Block from './Block'

//Amount of blocks shown on 1 page
const RANGE = 3

//Fetch blockchain data
function Blockchain() {
  const [blockchain, setBlockchain] = useState([])
  const [blockchainLength, setBlockchainLength] = useState(0)

  const getBlockchainPage = ({ start, end }) => {
    fetch(`${BASE_URL}/blockchain/range?start=${start}&end=${end}`)
      .then(res => res.json())
      .then(json => setBlockchain(json));
  }
  useEffect(() => {
    //Fetch Endpoint
    getBlockchainPage({ start: 0, end: RANGE })

    fetch(`${BASE_URL}/blockchain/length`)
      .then(res => res.json())
      .then(json => setBlockchainLength(json))
  }, [])

  const buttonNumbers = []
  //loop until i is greater than the page range
  for (let i = 0; i < blockchainLength / RANGE; i++) {
    // add to array
    buttonNumbers.push(i)
  }

  return (
    <div className="Blockchain">
      <h3>Blockchain</h3>
      <div>
        {blockchain.map((block) => (
          <Block key={block.hash} block={block} />
        ))}
      </div>
      <div>
        {
        buttonNumbers.map(number => {
          const start = number * RANGE
          const end = (number + 1) * RANGE
          return (
            <span
              key={number}
              onClick={() => getBlockchainPage({ start, end })}>
              <Button size="sm" varient="danger">
                {number + 1}
              </Button>{' '}
            </span>
          )
        })}
      </div>
    </div>
  )
}

export default Blockchain
