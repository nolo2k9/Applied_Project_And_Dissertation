import React from 'react';
import { MILLISECONDS_PYTHON } from '../config';

function Block({block}){
    const {timestamp, hash, data} = block;
    //Substring of current hash
    const hashDisplay = `${hash.substring(0, 15)}...`;
    //Display current timestamp
    const timestampDisplay = new Date(timestamp / MILLISECONDS_PYTHON).toLocaleString();


    return(
        <div className='Block'>
        <div>Hash: {hashDisplay}</div>
        <div>Timestamp: {timestampDisplay}</div>
        <div>{JSON.stringify(data)}</div>
        </div>
    )

}

export default Block;