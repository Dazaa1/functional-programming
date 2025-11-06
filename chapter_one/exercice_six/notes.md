# Exercise 6 notes:
- Ternaries are great to reduce series of statements, like an `if`/`else` statement into an expression.

```python
    result = 0
    if number % 2 == 0:
        result = number / 2
    else:
        result = (number * 3) + 1
```
- Ternary let's us do this.
```python
    result = number / 2 if number % 2 == 0 else (number * 3) + 1
```
- these are good to maintain immutablity.

## Syntax is:
```python
    value_a if condition else value_b
```