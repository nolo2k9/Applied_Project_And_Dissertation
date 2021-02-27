import React, {useState} from 'react';
import {Link} from 'react-router-dom';
import {FormGroup, FormControl, Button} from 'react-bootstrap';
import {BASE_URL} from '../config';

function ConductTransaction()
{
    const[amount, setAmount] = useState(0);
    const[recipient, setRecipient] = useState('');

    const updateRecipient = event => {
        setRecipient(event.target.value);
    }

    const updateAmount = event => {
        setAmount(Number(event.target.value)); //cast to a number
    }

    const submitTransaction = () => {
        fetch(`${BASE_URL}/wallet/transact`, 
            {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({recipient, amount})
            }
        ).then(response => response.json())
         .then(json => {
            console.log('submitTransaction json', json);
            alert('Success!')
        });
    }

    return(
        <div className="ConductTransaction">
            <Link to="/">Home</Link>
            <hr/>
            <h3>Conduct a Transaction</h3>
            <br></br>
            <FormGroup>
                <FormControl 
                    input="text"
                    placeholder="recipient"
                    value={recipient}
                    onChange={updateRecipient}
                />
            </FormGroup>

            <FormGroup>
                <FormControl 
                    input="number"
                    placeholder="amount"
                    value={amount}
                    onChange={updateAmount}
                />
            </FormGroup>

            <div>
                <Button varient="danger" onClick={submitTransaction}>
                    Submit
                </Button>
            </div>
        </div>
    )
}

export default ConductTransaction;