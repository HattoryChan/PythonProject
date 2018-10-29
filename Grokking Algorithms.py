# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 13:47:24 2018

@author: Admin
"""
def main():
    arr = [2, 4, 6]
    print(simpleSum(arr))
    print(arr[len(arr)- 1])   
    print(arr[-1])
    print(recSum([2, 4, 6]))

def recSum(arrList):   
    if len(arrList) == 1:        
        return arrList[0]    
    else:        #Return all elements without last
        return arrList[0] + recSum(arrList[1:])
    

def simpleSum(arr):
    total = 0
    for x in arr:
        total += x
    return total


"""
        Start Function!
"""
main()


    