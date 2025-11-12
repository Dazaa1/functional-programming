# Exercise 5 notes:
## Map, Filter, and Reduce Review
- Higher order functions like ``map`` ``filter`` ``reduce``, allow us to reduce stateful iteration and mutation.
- Here is an imperative example.

```python
    def factorial(n):
    # a procedure that continuously multiplies
    # the current result by the next number
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

```python
    import functools

    def factorial(n):
        return functools.reduce(lambda x, y: x * y, range(1, n + 1))