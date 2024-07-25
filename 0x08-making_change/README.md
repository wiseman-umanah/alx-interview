### COIN CHANGE
This is a popular problem to exercise the strength of dynamic programming and tracking of solutions to a problem. 
In this task, we find the fewest minimum number of coins needed to meet an amount. This can be useful in a banking system where the machine needs to find out the number of coins that will be out of the system.

## Process
- Optionally check that val is greater than 0
- Create dummy list for tracking, initalized with 'nth' infinity
- initialize first item with 0; default val
- Loop from 1 to n+1
- within loop, loop each coin
- while looping change value of each item to the minimum value between the current value of item and iterator (i) - current coin, sum result with 1
- opt out of loops
- check if the value at nth position has changed from infinity, if true return what the value else return your error code for impossible solution.


```
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

```