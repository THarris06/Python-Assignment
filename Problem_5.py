# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:08:52 2023

@author: Tyson Harris
"""

print ("\nTable of Powers\n")

strt_num = int(input("Start number:\t"))
stop_num = int(input("Stop number:\t"))

if strt_num > stop_num:
    print ("\nError: Stating value exceeds Stoping value.")

else:
    print ("\nNumber\t\tSquared\t\t\tCubed")
    print ("------\t\t-------\t\t\t-----")
    for i in range (strt_num, stop_num + 1):
        print ("{}\t\t\t{}\t\t\t{}".format(i, i ** 2, i ** 3))