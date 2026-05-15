#!/bin/bash

calculate_sgpa() {
    read -p "Enter number of subjects: " n

    total_weighted=0
    total_credits=0

    for ((i=1; i<=n; i++))
    do
        read -p "Subject $i credits: " c
        read -p "Subject $i grade point: " g

        total_weighted=$(echo "$total_weighted + ($c * $g)" | bc)
        total_credits=$(echo "$total_credits + $c" | bc)
    done

    sgpa=$(echo "scale=2; $total_weighted / $total_credits" | bc)
    echo "SGPA = $sgpa"
}

calculate_cgpa() {
    read -p "Enter number of semesters: " n

    total_weighted=0
    total_credits=0

    for ((i=1; i<=n; i++))
    do
        read -p "Semester $i SGPA: " sgpa
        read -p "Semester $i total credits: " c

        total_weighted=$(echo "$total_weighted + ($sgpa * $c)" | bc)
        total_credits=$(echo "$total_credits + $c" | bc)
    done

    cgpa=$(echo "scale=2; $total_weighted / $total_credits" | bc)
    echo "CGPA = $cgpa"
}

while true
do
    echo ""
    echo "===== SGPA & CGPA Calculator ====="
    echo "1. Calculate SGPA"
    echo "2. Calculate CGPA"
    echo "3. Exit"
    read -p "Enter choice: " choice

    case $choice in
        1) calculate_sgpa ;;
        2) calculate_cgpa ;;
        3) echo "Exiting..."; exit 0 ;;
        *) echo "Invalid choice" ;;
    esac
done