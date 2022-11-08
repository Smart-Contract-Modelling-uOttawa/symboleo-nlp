meat_sale_deltas = [
    {
        "original": "The Seller shall deliver the Order in one delivery within <delDueDateDays> days to the Buyer at its warehouse",
        "general": "The Seller shall deliver the Order in one delivery [DELIVERY_TIMEFRAME] to the Buyer [DELIVERY_LOCATION]",
        "template": "delivery: O(seller, buyer, true, Happens(delivered))",
        "examples": [
            {
                "keys": {
                    "DELIVERY_TIMEFRAME": "within 10 days",
                    "DELIVERY_LOCATION": "at its warehouse"
                },
                "result": {
                    "sym": "delivery: O(seller, buyer, true, WhappensBefore(delivered, delivered.delDueDate))",
                    "notes": "sets the delivery due date as well (in the domain model); also the location (warehouse)"
                }
            }
        ]
    },
    {
        "original": "The Buyer shall pay <amt> (“amount”) in <curr> (“currency”) to the Seller before <payDueDate>.",
        "general": "[TRIGGER] The Buyer shall pay [PAYMENT_DETAILS] to the Seller [PAYMENT_TIMEFRAME].",
        "template": "payment: O(buyer, seller, true, Happens(paid))",
        "examples": [
            {
                "keys": {
                    "PAYMENT_DETAILS": "$1000 in USD",
                    "PAYMENT_TIMEFRAME": "before April 17, 2022"
                },
                "result": {
                    "sym": "payment: O(buyer, seller, true, WhappensBefore(paid, paid.payDueDate))",
                    "notes": "sets the pay due date as well; and also the paid amount and currency"
                }
            }
        ]
    },
    {
        "original": "In the event of late payment of the amount owed due, the Buyer shall pay interests equal to <intRate>% of the amount owed",
        "general": "[TRIGGER] The Buyer shall pay interests equal to [INTEREST_AMOUNT]",
        "template": "latePayment: O(buyer, seller, true, Happens(paidLate))",
        "examples": [
            {
                "keys": {
                    "TRIGGER": "In the event of late payment of the amount owed due",
                    "INTEREST_AMOUNT": "<intRate>% of the amount owed"
                },
                "result": {
                    "sym": "latePayment: Happens(Violated(obligations.payment)) -> O(buyer, seller, true, Happens(paidLate))",
                    "notes": "Need to add some event properties"
                }   
            }
        ]
    },
    {
        "original": "Both Seller and Buyer must keep the contents of this contract confidential during the execution of the contract and six months after the termination of the contract",
        "general": "Both Seller and Buyer must keep the contents of this contract confidential [CONFIDENTIALITY_TIMEFRAME]",
        "template": "O(seller, buyer, true, not Happens(disclosed))",
        "examples": [
            {
                "keys": {
                    "CONFIDENTIALITY_TIMEFRAME": "during the execution of the contract and six months after the termination of the contract"
                },
                "result": {
                    "sym": "O(seller, buyer, true, not WhappensBefore(disclosed, Date.add(Activated(self), 6, months)))"
                }
            }
        ]
    },
    {
        "original": "the Seller may suspend performance of all of its obligations under the agreement until payment of amounts due has been received in full.",
        "general": "the Seller may suspend performance of all of its obligations under the agreement [SUSPENSION_CONDITION]",
        "template": "suspendDelivery: Happens(Violated(obligations.payment)) -> P(seller, buyer, true, Suspended(obligations.delivery))",
        "examples": [
            {
                "keys": {
                    "SUSPENSION_CONDITION": "until payment of amounts due has been received in full"
                },
                "result": {
                    "sym": "suspendDelivery: Happens(Violated(obligations.payment)) -> P(seller, buyer, true, Suspended(obligations.delivery))"
                }
            }
        ]
    },
    {
        "original": "the Seller may suspend performance of all of its obligations under the agreement until payment of amounts due has been received in full.",
        "general": "the Seller may suspend performance of all of its obligations under the agreement [SUSPENSION_CONDITION]",
        "template": "resumeDelivery: P(buyer, seller, true, Resumed(obligations.delivery))",
        "examples": [
            {
                "keys": {
                    "SUSPENSION_CONDITION": "until payment of amounts due has been received in full"
                },
                "result": {
                    "sym": "resumeDelivery: HappensWithin(paidLate, Suspension(obligations.delivery)) -> P(buyer, seller, true, Resumed(obligations.delivery))"
                }
            }
        ]
    },
    {
        "original": "Any delay in delivery of the goods will not entitle the Buyer to terminate the Contract unless such delay exceeds 10 Days",
        "general": "Any delay in delivery of the goods will not entitle the Buyer to terminate the Contract [TERMINATION_CONDITION]",
        "template": "terminateContract: P(buyer, seller, true, Terminated(self))",
        "examples": [
            {
                "keys": {
                    "TERMINATION_CONDITION": "unless such delay exceeds 10 Days"
                },
                "result": {
                    "sym": "terminateContract: Happens(Violated(obligations.delivery)) -> P(buyer, seller, true, Terminated(self))",
                    "notes": "may need to keep the 'unless' part in there... Tough one, since its split up"
                }
            }
        ]
    }

]