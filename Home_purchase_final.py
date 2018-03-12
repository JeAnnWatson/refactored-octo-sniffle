# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 00:06:56 2018

@author: Mrs Watson
"""

def char_to_float (user_input):
    char_input = ""
    for char in user_input: 
        if char in "1234567890.":
            char_input += char
    float_input = float(char_input)
    return float_input   
def decimal_percentage (user_input):
    num_only = char_to_float (user_input)
    decimal_percent = float()
    if num_only > 1:
        decimal_percent = num_only/100
    else:
        decimal_percent = num_only
    return decimal_percent           
annual_salary_input = input("Please enter your annual salary: ")
portion_saved_input = input("Please enter the portion of your salary that you will be saving: ")
total_cost_input = input("Please enter the total cost of your dream home: ")
annual_salary = char_to_float (annual_salary_input)
portion_saved = decimal_percentage (portion_saved_input)
total_cost = char_to_float (total_cost_input)
if annual_salary <= 0 or portion_saved <= 0 or total_cost <= 0: #this is to avoid an infinite loop
    print ("Invalid entry") 
else:
    portion_down_payment = 0.25
    down_payment = portion_down_payment * total_cost
    current_savings = 0
    monthly_salary = annual_salary/12
    mthly_return = (1 + (0.04/12))
    num_months = 0
    while current_savings < down_payment:
        num_months += 1
        current_savings += monthly_salary * portion_saved
        current_savings *= (1 + (0.04/12))
        print (current_savings)
        
    print (num_months)    

   
   
        