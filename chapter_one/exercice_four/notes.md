# Exercise 4 notes:
- Let's say we wanna get the average of a collection:

## The procedural way of doing it:
```python
    def get_average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)
```

## The declarative way of doing it:
```python
    def get_average(nums):
    return sum(nums) / len(nums)
```

- Here we don't care about the stete of sum variable we only care about the result.