# Exercise 1 notes:
- In python functions are just like integers, strings and object we can for example asigne a function to a variable

```python
    def add(x, y):
    return x + y

    # assign the function to a new variable
    # called "addition". It behaves the same
    # as the original "add" function
    addition = add
    print(addition(2, 5))
    # 7
```