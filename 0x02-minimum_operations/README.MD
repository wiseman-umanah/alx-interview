### MINIMUM NUMBER OF OPERATIONS FOR H N TIMES

To solve the problem of calculating the minimum number of operations required to obtain exactly 𝑛
n H characters using only "Copy All" and "Paste" operations, we can use the concept of prime factorization.

The problem can be broken down into understanding the operations:

Copy All: Copies the entire content.
Paste: Pastes the copied content, effectively doubling the size if done consecutively after a copy.
Given a target 𝑛
n, our goal is to determine the minimum number of operations required.

n characters is to repeatedly use "Copy All" and then perform a series of "Paste" operations. The number of operations required can be deduced by factorizing 𝑛
n and summing up the factors. Each factor represents a set of operations: copying the current content and then pasting it multiple times to reach the factor's length.

# Example
```
For 𝑛 = 9

9 = 3×3

First, create 3 Hs: (1 Copy All + 2 Pastes) = 3 operations.
Then create 9 Hs from 3 Hs: (1 Copy All + 2 Pastes) = 3 operations.
Total = 3 + 3 = 6 operations.
```


## OPERATIONS
- Get factors of n
- Add the factors of n
- Return the results that is the number of operation needed to copy and paste H n time 