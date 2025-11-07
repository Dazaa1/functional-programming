# Exercise 3 notes:
## First Class and Higher Order Functions

- ``Fist Class functions``: are functions that are treated like any other value, they can be passed in functions, returned by functions, assigned to variables.
- ``Higher-order functions``: are functions that accept another function as an argument or return a function. 

-- Python accepts them both.

### First Class example:
```python
    def square(x):
        return x * x

    # Assign function to a variable
    f = square

    print(f(5))
    # 25
```

## Higher-order functions:
```python
    def square(x):
    return x * x

    def my_map(func, arg_list):
        result = []
        for i in arg_list:
            result.append(func(i))
        return result

    squares = my_map(square, [1, 2, 3, 4, 5])
    print(squares)
    # [1, 4, 9, 16, 25]
```