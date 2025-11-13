# Exercise 1 notes:

## Pure function:
- Return the same value given the same argument.
- Runing them causes no side effects.

### Example of a pure function:
```python
    def find_max(nums):
        max_val = float("-inf")
        for num in nums:
            if max_val < num:
                max_val = num
        return max_val
```

### Example of impure function:
```python
    # instead of returning a value
    # this function modifies a global variable
    global_max = float("-inf")

    def find_max(nums):
        global global_max
        for num in nums:
            if global_max < num:
                global_max = num
```