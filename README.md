# CS2-Sta.Cruz-Caleb

# Travel Fare Calculator

## Description
This program calculates the total travel fare for passengers based on the distance traveled and the number of passengers.

## Version 1
## Original code without input validation

## Input
- Accepts the passenger's name.
- Accepts the travel distance.
- Accepts the total number of passengers.

## Process
- Multiplies the travel distance by the fare rate of 14.
- Multiplies the result by the number of passengers to calculate the total travel fare.

## Output
- Displays the total travel fare.

## Limitation
- Does not include input validation.

## Formula
**Total Fare = Distance × Fare Rate × Number of Passengers**

**Fare Rate:** 14 per unit of distance

## Version 2 
## Updated code with input validation

## Input
- Accepts the passenger's name.
- Accepts the travel distance.
- Accepts the total number of passengers.

## Process
- Validates that the passenger's name is not empty.
- Validates that the travel distance is a number greater than zero.
- Validates that the number of passengers is a positive whole number.
- Multiplies the travel distance by the fare rate of 14.
- Multiplies the result by the number of passengers to calculate the total travel fare.

## Output
- Displays the passenger's name.
- Displays the total travel fare in Philippine pesos, rounded to two decimal places.
- Displays error messages for invalid inputs and prompts the user to enter valid values.

## Improvement
- Includes input validation to prevent empty names, non-numeric inputs, zero or negative distances, and invalid passenger counts.

## Formula
**Total Fare = Distance × Fare Rate × Number of Passengers**

**Fare Rate:** 14 per unit of distance
