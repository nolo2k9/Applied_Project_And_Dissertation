import React, { useState } from 'react'
import { Button } from 'react-bootstrap'
import { MILLISECONDS_PYTHON } from '../config'
import Transaction from './Transactions'

function ToggleTransaction({ block }) {
  //initially set to false
  const [displayTransaction, setDisplayTransaction] = useState(false)
  //pull data from block
  const { data } = block;

  const toggleDisplay = () => {
      //get the opposite to whatever the current state is
      setDisplayTransaction(!displayTransaction);
  }

  if (displayTransaction) {
    return (
      <div>
        {data.map((transaction) => (
          <div key={transaction.id}>
            <hr />
            <Transaction transaction={transaction} />
          </div>
        ))}
        <br />
        <Button
        varient="danger"
        size="sm"
        onClick={toggleDisplay}>
        Hide Transactions
        </Button>
      </div>
    )
  }
  // Default behaviour
  return (
    <div>
      <br />
      <Button varient="danger"
       size="sm"
       onClick={toggleDisplay}>Show Transactions</Button>
    </div>
  )
}

function Block({ block }) {
  const { timestamp, hash} = block
  //Substring of current hash
  const hashDisplay = `${hash.substring(0, 15)}...`
  //Display current timestamp
  const timestampDisplay = new Date(
    timestamp / MILLISECONDS_PYTHON,
  ).toLocaleString()

  return (
    <div className="Block">
      <b>Block Stats</b>
      <div>Hash: {hashDisplay}</div>
      <div>Timestamp: {timestampDisplay}</div>
      <ToggleTransaction block={block}/>
    </div>
  )
}

export default Block
