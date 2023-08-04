"""
Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
and tax percent (the percentage of the meal price being added as tax) for a meal, 
find and print the meal's total cost. Round the result to the nearest integer.
"""

def meal_cost(meal_cost, tip_percent, tax_percent):
    tip = tip_percent / 100 * meal_cost
    tax = tax_percent / 100 * meal_cost
    total_meal_cost = round(meal_cost + tip + tax)
    return print(total_meal_cost)

print(meal_cost(10.25, 17, 5))