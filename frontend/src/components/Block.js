import React from 'react'
import { MILLISECONDS_PYTHON } from '../config'
import Transaction from './Transactions'

function Block({ block }) {
  const { timestamp, hash, data } = block
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
      <div>
        {data.map((transaction) => (
          <div key={transaction.id}>
            <hr />
            <Transaction transaction={transaction} />
          </div>
        ))}
      </div>
    </div>
  )
}

export default Block
