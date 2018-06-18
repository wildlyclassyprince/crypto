#!/usr/bin/bash --

# To initiate a transaction over the blockchain
curl "localhost:5000/txion" \
			-H "Content-Type: application/json" \
			-d '{"from": "Sender 1", "to":"Receiver 1", "amount": 5}'
