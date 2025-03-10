#!/bin/bash

# Loop indefinitely
while true; do
    # Generate a random four-digit number
    number=$(( RANDOM % 10000 ))

    # Print the number to STDOUT
    echo "OUT: $number"

    # Check if the number is odd
    if (( number % 2 == 1 )); then
        # Print the message to STDERR
        echo "ERR: Odd! $number" >&2
    fi

    # Check for input from STDIN for a second
    read -t 1 input
    if [[ $? -eq 0 ]]; then
        # There was some input, echo it
        echo "IN:  $input"
    fi

    sleep 1
done
