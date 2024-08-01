### ISLAND PERIMETER

This is a basic manipulation of a 2D matrix to find the perimeter of an island that meets the requirement.

## ALGORITHM
> Initialize a counter with 0 (default)
> Loop through grid (rows) (1)
> Loop through rows (column) to get each item (2)
> Check if value is 1
> if value is 1
    - add 4 to counter
    > Check if the value at the right is also 1
    > if value->right is 1
    - subtract 2 from counter
    > Check if the value at the bottom is also 1
    > if value->bottom is 1
    - subtract 2 from counter
    > Repeat for all values
> exit loop (2)
> exit loop (1)
> print perimeter to stdout or return perimeter for use
