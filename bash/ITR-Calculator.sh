#!/bin/bash

# Function to calculate tax
calculate_tax() {
    local CTC=$1
    local tax=0

    if (( CTC <= 300000 )); then
        tax=0
    elif (( CTC > 300000 && CTC <= 700000 )); then
        tax=$(( (CTC - 300000) * 5 / 100 ))
        tax=$(( tax + (tax * 4 / 100) ))
    elif (( CTC > 700000 && CTC <= 1000000 )); then
        tax=$(( 20000 + (CTC - 700000) * 10 / 100 ))
        tax=$(( tax + (tax * 4 / 100) ))
    elif (( CTC > 1000000 && CTC <= 1200000 )); then
        tax=$(( 20000 + 30000 + (CTC - 1000000) * 15 / 100 ))
        tax=$(( tax + (tax * 4 / 100) ))
    elif (( CTC > 1200000 && CTC <= 1500000 )); then
        tax=$(( 20000 + 30000 + 30000 + (CTC - 1200000) * 20 / 100 ))
        tax=$(( tax + (tax * 4 / 100) ))
    else
        tax=$(( 20000 + 30000 + 30000 + 20000 + (CTC - 1500000) * 30 / 100 ))
        tax=$(( tax + (tax * 4 / 100) ))
    fi
    
    echo "Income Tax Payable: Rs. $tax"
}

# Read input from user
echo -n "Enter your CTC (in Rs.): "
read CTC

# Validate input
if ! [[ "$CTC" =~ ^[0-9]+$ ]]; then
    echo "Invalid input! Please enter a valid numeric CTC."
    exit 1
fi

# Call function to calculate tax
calculate_tax $CTC
