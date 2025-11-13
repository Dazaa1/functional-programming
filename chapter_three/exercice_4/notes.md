# Exercice 4 notes:
## NO-OP:
- It is an operation that does nothing.
- If a function doesn t return anything, it is probably impure.

### Example of no-op function
```python
    def square(x):
        x * x
```

### Example of side effects
```python
    y = 5
    def add_to_y(x):
        global y
        y += x

    add_to_y(3)
    # y = 8
```