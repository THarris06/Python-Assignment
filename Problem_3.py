# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 17:11:29 2023

@author: Tyson Harris
"""

def coin_calculator(num_cents):
    """
    

    Parameters
    ----------
    num_cents : int
        The amount in cents.

    Returns
    -------
    None.

    """
    num_quarters = num_cents // 25
    num_cents -= num_quarters * 25
    
    num_dimes = num_cents // 10
    num_cents -= num_dimes * 10
    
    num_nickels = num_cents // 5
    num_cents -= num_nickels * 5
    
    num_pennies = num_cents
    
    print (f"\nQuarters: {num_quarters}")
    print (f"Dimes: {num_dimes}")
    print (f"Nickels: {num_nickels}")
    print (f"Pennies: {num_pennies}")
    
if __name__ == '__main__':
    
    loop = 'y'
    
    print ("\nChange Calculator")
    
    while loop == 'y':
        
        cents = int(input("\nEnter Amount of Cents (0-99):"))
        
        if cents > 99 or cents < 0:
            print ("\nError, Cents must be between 0-99")
            
        else:
            coin_calculator(cents)    
    
            loop = input("\nContinue? (y/n): ")
            
            if loop.lower() == 'n':
                print ("\nBye!")
            
            elif loop != 'y':
                print ("\nUnkown Entery, Exiting Program")
            
        