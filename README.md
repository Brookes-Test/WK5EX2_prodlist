## Instructions

Write a function `prodlist` that returns the product of a list of numbers, that is to say the result of multiplying all the numbers in a list together. For example, `prodlist([2,3,4,5])` would return `120`. If the list is empty, the function should return 1.

**Note:** The function should **not** be made conditional on  `if __name__ == "__main__":`  That is something we do for programs, not functions.

## Example of use (in Python console)
```
> prodlist([4.5,1,3,5])
67.5
```
## Explanation of automated tests

The arguments passed to the function during the tests, and the expected return values are shown below

| Test| Argument| Expected return value | 
| --- | ---  | --- |
| test_1 | []| 1 | 
| test_2 | [3.5] | 3.5 |
| test_3 | [3,-1.5,1]| -4.5 |
