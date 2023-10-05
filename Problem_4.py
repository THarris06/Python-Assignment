# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 00:03:31 2023

@author: Tyson Harris
"""

loop = 'y'

print ("=" * 30)
print ("Shipping Calculator")


while loop == 'y':
    
    print ("=" * 30)
    cost = float(input("Cost of items ordered:\t"))

    if cost < 0:
        print ("ERROR")

    while cost >= 0:
    
        if cost <= 29.99 and cost >= 0:
            ship_cost = 5.95
    
        elif cost <= 49.99 and cost >= 30.00:
            ship_cost = 7.95
    
        elif cost <= 74.99 and cost >= 50.00:
            ship_cost = 9.95
    
        elif cost >= 75.00:
            ship_cost = 0    


        total = cost + ship_cost    

        print (f"Shipping cost: {ship_cost}")
        print (f"Total cost: {total}")  
        
        cost = -1
        
        loop = input("\nContinue? (y/n): ")
        
        if loop == 'n':
            print ("=" * 30)
            print ("Bye!")
            
        elif loop != 'y':
            print ("Error")